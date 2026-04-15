/**
 * Evidence triage: rule-based interpretation for project/month/activity selections.
 * Loaded after the matrix inline script so `data` and `provenanceData` exist.
 */
(function (global) {
  'use strict';

  var currentMode = 'resume';

  var BUCKET_TAGS = {
    'Documentation & specs': ['product', 'systems', 'delivery', 'documentation'],
    'Design systems & components': ['design systems', 'systems', 'scale', 'product'],
    'Prototyping & wireframes': ['prototyping', 'implementation', 'product'],
    'Prototyping & experiments': ['prototyping', 'implementation', 'product'],
    'Presentations & deck work': ['communication', 'influence', 'cross-functional'],
    'Presentations & critiques': ['communication', 'influence', 'cross-functional'],
    'Meetings & coordination': ['cross-functional', 'communication'],
    'Operations & runbooks': ['operations', 'delivery', 'cross-functional'],
    'Research & audits': ['research', 'product', 'systems'],
    'Research & discovery': ['research', 'product'],
    'Engineering handoff': ['delivery', 'implementation', 'cross-functional'],
    'Integrations & APIs': ['platform', 'systems', 'implementation'],
    'Store & monetization': ['monetization', 'platform', 'product'],
    'Marketing & player-facing web': ['product', 'platform', 'communication'],
    'Quest & journal systems': ['game', 'systems'],
    'HUD & objectives': ['game', 'systems'],
    'Inventory & equipment': ['game', 'systems'],
    'Map & world navigation': ['game', 'systems'],
    'Navigation & hubs': ['product', 'game', 'systems'],
    'Information architecture': ['product', 'systems'],
    'Visual design & wireframes': ['visual design', 'product'],
    'Visual design & theming': ['visual design', 'product'],
    'CMS & publishing': ['platform', 'delivery', 'product'],
    'Domains, hosting & deploy': ['platform', 'operations', 'delivery'],
    'Copywriting & messaging': ['communication', 'product'],
    'Accessibility': ['product', 'systems'],
    'Analytics & measurement': ['platform', 'product'],
    'Email & newsletters': ['communication', 'product'],
    'Workshops & talks': ['communication', 'influence', 'cross-functional'],
    'Infrastructure & scripts': ['systems', 'operations', 'implementation'],
    'General & planning': ['product'],
    'Immersive & installation': ['game', 'implementation'],
    'Generative & ML art': ['implementation', 'product'],
    'Site build & CMS': ['product', 'delivery'],
    'Community & social surfaces': ['product', 'communication'],
    'Recruiting & studio site': ['operations', 'communication'],
    'Audio & hardware studio': ['operations'],
    'Keyboard & desk hardware': ['operations'],
    'Rack & cabling': ['operations'],
    'Video & motion': ['visual design', 'communication'],
    'Branding & identity': ['visual design', 'product'],
    'Templates & page systems': ['systems', 'product', 'design systems'],
  };

  var GAME_TAGS = { game: 1, 'visual design': 0.3 };
  var PRODUCT_TAGS = { product: 1, platform: 1, documentation: 1, delivery: 0.8, systems: 0.8 };

  function clamp(n, lo, hi) {
    return Math.max(lo, Math.min(hi, n));
  }

  function toBand(score) {
    if (score >= 4) return 'High';
    if (score >= 2.5) return 'Medium';
    return 'Low';
  }

  function toStrength(score) {
    if (score >= 4) return 'Strong';
    if (score >= 2.5) return 'Moderate';
    return 'Weak';
  }

  function escapeHtml(s) {
    return String(s)
      .replace(/&/g, '&amp;')
      .replace(/</g, '&lt;')
      .replace(/"/g, '&quot;');
  }

  function summarySignals(monthMd) {
    if (!monthMd || typeof monthMd !== 'string') {
      return { score: 1, bullets: 0, hasDecisions: false, hasDeliverables: false, hasPeople: false };
    }
    var t = monthMd;
    var hasDecisions = /###\s*Key Decisions/i.test(t);
    var hasDeliverables = /###\s*Artifacts Delivered/i.test(t);
    var hasPeople = /###\s*People Involved/i.test(t);
    var hasConstraints = /constraint|risk|trade-?off|decision/i.test(t);
    var bullets = (t.match(/^\s*-\s+/gm) || []).length;
    var score = 1;
    if (hasDecisions) score += 1;
    if (hasDeliverables) score += 1;
    if (hasPeople) score += 0.5;
    if (hasConstraints) score += 0.5;
    if (bullets > 25) score += 1;
    else if (bullets > 12) score += 0.5;
    return {
      score: clamp(score, 1, 5),
      bullets: bullets,
      hasDecisions: hasDecisions,
      hasDeliverables: hasDeliverables,
      hasPeople: hasPeople,
    };
  }

  function peopleForMonthProject(prov, month, project) {
    if (!prov || !prov.peopleByProject) return [];
    var byM = prov.peopleByProject[month];
    if (!byM) return [];
    return byM[project] || [];
  }

  function countProjectsWithActivity(data, activityName) {
    if (!activityName || !data.projectActivities) return 0;
    var n = 0;
    data.rows.forEach(function (row) {
      var acts = data.projectActivities[row] || [];
      for (var i = 0; i < acts.length; i++) {
        if (acts[i].name === activityName && acts[i].total > 0) {
          n++;
          return;
        }
      }
    });
    return n;
  }

  function varietyAtMonth(data, project, monthIdx) {
    var acts = data.projectActivities[project] || [];
    var c = 0;
    acts.forEach(function (a) {
      if (a.monthly && a.monthly[monthIdx] > 0) c++;
    });
    return c;
  }

  function alignmentFromTags(tags) {
    var p = 0;
    var g = 0;
    tags.forEach(function (tag) {
      if (PRODUCT_TAGS[tag]) p += PRODUCT_TAGS[tag];
      if (GAME_TAGS[tag]) g += GAME_TAGS[tag];
    });
    return { product: clamp(p, 0, 5), game: clamp(g, 0, 5) };
  }

  function computeTriage(ctx) {
    var data = ctx.data;
    var prov = ctx.provenanceData;
    var month = ctx.month;
    var project = ctx.project;
    var activity = ctx.activity || '';
    var mode = ctx.mode || 'resume';

    var monthIdx = data.months.indexOf(month);
    var monthMd = prov && prov.monthSources ? prov.monthSources[month] : '';
    var sig = summarySignals(monthMd);
    var people = peopleForMonthProject(prov, month, project);
    var collabScore = clamp(people.length >= 4 ? 5 : people.length >= 2 ? 4 : people.length === 1 ? 2.5 : 1, 1, 5);

    var tags = BUCKET_TAGS[activity] || [];
    var align = alignmentFromTags(tags);
    var crossProject = activity ? countProjectsWithActivity(data, activity) : 0;
    var throughlineScore = clamp(crossProject >= 5 ? 5 : crossProject >= 3 ? 4 : crossProject >= 2 ? 3 : crossProject >= 1 ? 2 : 1, 1, 5);

    var densityScore = 1;
    var durationScore = 1;
    var varietyScore = 1;

    if (activity && monthIdx >= 0) {
      var acts = data.projectActivities[project] || [];
      var act = null;
      for (var i = 0; i < acts.length; i++) {
        if (acts[i].name === activity) {
          act = acts[i];
          break;
        }
      }
      if (act) {
        var cell = act.monthly[monthIdx] || 0;
        densityScore = clamp(cell >= 5 ? 5 : cell >= 3 ? 4 : cell >= 2 ? 3 : cell >= 1 ? 2 : 1, 1, 5);
        durationScore = clamp(
          act.activeMonths >= 18 ? 5 : act.activeMonths >= 12 ? 4 : act.activeMonths >= 6 ? 3 : act.activeMonths >= 3 ? 2 : 1,
          1,
          5
        );
        varietyScore = clamp(varietyAtMonth(data, project, monthIdx), 1, 5);
      }
    } else if (monthIdx >= 0) {
      var ps = data.projectScores && data.projectScores[project];
      var bullets = ps ? ps[monthIdx] || 0 : 0;
      densityScore = clamp(bullets >= 10 ? 5 : bullets >= 6 ? 4 : bullets >= 3 ? 3 : bullets >= 1 ? 2 : 1, 1, 5);
      varietyScore = clamp(varietyAtMonth(data, project, monthIdx), 1, 5);
      var activeMonths = 0;
      if (ps) {
        for (var j = 0; j < ps.length; j++) {
          if (ps[j] > 0) activeMonths++;
        }
      }
      durationScore = clamp(
        activeMonths >= 24 ? 5 : activeMonths >= 12 ? 4 : activeMonths >= 6 ? 3 : activeMonths >= 2 ? 2 : 1,
        1,
        5
      );
    }

    var resumeValue = clamp(
      0.35 * durationScore + 0.25 * varietyScore + 0.25 * sig.score + 0.15 * densityScore,
      1,
      5
    );
    var interviewValue = clamp(0.45 * collabScore + 0.35 * sig.score + 0.2 * varietyScore, 1, 5);
    var productRel = clamp((align.product + varietyScore * 0.2 + sig.score * 0.15) / 1.35, 1, 5);
    var gameRel = clamp((align.game + varietyScore * 0.15 + sig.score * 0.1) / 1.25, 1, 5);

    var mining = 0;
    if (mode === 'resume') {
      mining = 0.35 * resumeValue + 0.3 * Math.max(productRel, gameRel) + 0.25 * throughlineScore + 0.1 * densityScore;
    } else if (mode === 'interview') {
      mining = 0.4 * interviewValue + 0.35 * sig.score + 0.15 * collabScore + 0.1 * varietyScore;
    } else {
      mining = 0.45 * throughlineScore + 0.25 * crossProject + 0.2 * sig.score + 0.1 * varietyScore;
    }
    mining = clamp(mining, 1, 5);

    var priority = toBand(mining);

    var useProduct = productRel >= gameRel;
    var bestUse = [];
    var reasoning = [];
    var why = '';
    var priorityNote = '';
    var nextMove = '';

    function padSignals(arr, fallbackA, fallbackB) {
      var out = arr.filter(Boolean);
      while (out.length < 3) {
        if (out.indexOf(fallbackA) < 0) out.push(fallbackA);
        else if (out.indexOf(fallbackB) < 0) out.push(fallbackB);
        else out.push('archive-linked monthly summaries');
      }
      return out.slice(0, 3);
    }

    if (mode === 'resume') {
      if (resumeValue >= 2.5) bestUse.push('Resume bullets');
      if (useProduct && productRel >= 2.5) bestUse.push('Product-facing lines');
      else if (!useProduct && gameRel >= 2.5) bestUse.push('Game-facing lines');
      else if (productRel >= 2.5) bestUse.push('Product-facing lines');
      else if (gameRel >= 2.5) bestUse.push('Game-facing lines');
      if (throughlineScore >= 2.5 && crossProject >= 2) bestUse.push('Proof of repeated capability');
      if (bestUse.length === 0) bestUse.push('Thin for headline bullets—supporting detail only');

      priorityNote =
        priority === 'High'
          ? 'strong candidate to turn into resume bullets soon'
          : priority === 'Medium'
            ? 'usable bullets possible—expect some editing'
            : 'unlikely to carry a resume section on its own';

      if (activity) {
        reasoning.push('Resume lens: category "' + activity + '" with ' + toStrength(durationScore).toLowerCase() + ' run on this project');
      } else {
        reasoning.push('Resume lens: project snapshot for ' + month + '—map activity rows to outcomes');
      }
      reasoning.push(
        varietyScore >= 3
          ? varietyScore + ' work types this month → multiple bullet angles'
          : 'Narrow mix this month—one dominant story per bullet'
      );
      reasoning.push(
        (densityScore >= 3 ? 'Solid' : 'Light') +
          ' tagged volume here—' +
          (sig.hasDeliverables ? 'summary mentions deliverables' : 'mine raw lines for outcomes')
      );
      reasoning.push(
        useProduct
          ? 'Leans product/portfolio (' + toStrength(productRel).toLowerCase() + ' product signal)'
          : 'Leans game-facing (' + toStrength(gameRel).toLowerCase() + ' game signal)'
      );
      if (throughlineScore >= 3 && crossProject >= 2 && activity) {
        reasoning.push('Same category in ' + crossProject + ' projects—reuse one bullet with different examples');
      } else if (sig.hasDecisions) {
        reasoning.push('Decisions called out in summary—good for "impact" phrasing');
      }

      var rSig = padSignals(
        [
          activity ? '"' + activity + '" work with scope' : 'project-level activity',
          varietyScore >= 3 ? 'several transferable skills in one month' : null,
          sig.hasDeliverables ? 'deliverable-friendly summary sections' : null,
        ],
        'enough tagged work to anchor metrics',
        'monthly summary as source text'
      );
      why =
        'For resume mining, this selection is ' +
        (priority === 'High' ? 'strong' : priority === 'Medium' ? 'reasonable' : 'weak') +
        ' because it combines ' +
        rSig.join(', ') +
        '.';

      if (priority === 'Low') {
        nextMove = 'Skip for headline bullets; come back only if you need a small supporting line.';
      } else if (activity) {
        nextMove =
          'Write two bullets: one outcome-led, one scope/tooling-led, using this month’s matching summary lines.';
      } else {
        nextMove =
          'Expand the hottest activity row for this month, then draft one product-leaning and one game-leaning bullet.';
      }
    } else if (mode === 'interview') {
      if (interviewValue >= 2.5) bestUse.push('Interview stories');
      if (collabScore >= 3) bestUse.push('Cross-functional narrative');
      if (sig.hasDecisions || sig.score >= 3) bestUse.push('Decisions, constraints, or tradeoffs');
      if (bestUse.length < 2 && varietyScore >= 3) bestUse.push('Multiple threads to pick a single arc');
      if (bestUse.length === 0) bestUse.push('Low narrative depth—use as color, not centerpiece');

      priorityNote =
        priority === 'High'
          ? 'likely to yield a coherent STAR-style story'
          : priority === 'Medium'
            ? 'enough texture for a short anecdote with prep'
            : 'sparse story material—pair with another month';

      if (people.length >= 2) {
        reasoning.push('Interview lens: ' + people.length + ' named people—good for collaboration setup');
      } else if (people.length === 1) {
        reasoning.push('Interview lens: one named collaborator—pair with your role explicitly');
      } else {
        reasoning.push('Interview lens: few named collaborators—stress your ownership in the story');
      }
      if (sig.hasDecisions) {
        reasoning.push('Decisions in summary—use for conflict/choice in the narrative');
      } else {
        reasoning.push('Light explicit decisions—pull tension from tradeoffs in the raw month text');
      }
      reasoning.push(
        sig.hasDeliverables
          ? 'Deliverables noted—natural "result" beat for STAR'
          : 'Outcomes may need reconstruction from bullets'
      );
      if (activity) {
        reasoning.push('Focused category "' + activity + '"—one clear story beats a laundry list');
      } else {
        reasoning.push('Project-wide month—pick one activity row to be the spine of the story');
      }
      if (varietyScore >= 4) {
        reasoning.push('Many parallel work types—choose one thread or you will sound scattered');
      }

      var iSig = padSignals(
        [
          people.length >= 2 ? 'named collaborators' : null,
          sig.hasDecisions ? 'decision-shaped summary content' : null,
          sig.score >= 3 ? 'rich monthly narrative' : null,
        ],
        'enough context to rehearse aloud',
        'monthly summary as rehearsal script'
      );
      why =
        'For interview prep, this selection is ' +
        (priority === 'High' ? 'strong' : priority === 'Medium' ? 'workable' : 'thin') +
        ' because it combines ' +
        iSig.join(', ') +
        '.';

      if (priority === 'Low') {
        nextMove = 'Do not anchor a loop on this alone—bookmark and pair with a richer month.';
      } else {
        nextMove =
          'Draft a 4-beat outline: situation → constraint → what you did → measurable or qualitative outcome.';
      }
    } else {
      /* positioning */
      if (throughlineScore >= 2.5 || crossProject >= 2) bestUse.push('Throughline / repeated pattern');
      if (tags.length) bestUse.push('Tag-aligned narrative (' + tags.slice(0, 3).join(', ') + ')');
      if (useProduct && productRel >= 2.5) bestUse.push('Product positioning language');
      if (!useProduct && gameRel >= 2.5) bestUse.push('Game positioning language');
      if (bestUse.length === 0) bestUse.push('Weak pattern signal—avoid as career thesis');

      priorityNote =
        priority === 'High'
          ? 'strong repeatability—safe to reuse in positioning blurbs'
          : priority === 'Medium'
            ? 'partial pattern—pair with one more project before claiming it'
            : 'one-off signal—do not over-weight in positioning';

      reasoning.push(
        'Positioning lens: throughline strength ' +
          toStrength(throughlineScore).toLowerCase() +
          (activity && crossProject >= 2
            ? '; category appears across ' + crossProject + ' projects'
            : activity
              ? '; category mostly local to this project'
              : '; use activity rows to name the pattern')
      );
      if (tags.length) {
        reasoning.push('Strategic tags: ' + tags.slice(0, 5).join(', '));
      } else {
        reasoning.push('No strategic tag overlap—pattern is generic unless you name it yourself');
      }
      reasoning.push(
        durationScore >= 3
          ? toStrength(durationScore) + ' span—helps "over time" claims'
          : 'Short span—better as example than as pillar'
      );
      reasoning.push(
        varietyScore >= 3
          ? 'Several work types—pick one verb family for consistent positioning'
          : 'Single dominant type—clear wedge for your story'
      );
      if (activity) {
        reasoning.push('Category "' + activity + '" is the handle for this pattern');
      } else {
        reasoning.push('Project-month view—collapse to one pattern name after scanning categories');
      }

      var pSig = padSignals(
        [
          crossProject >= 3 && activity ? 'same work type across multiple projects' : null,
          tags.length ? 'aligned strategic tags' : null,
          throughlineScore >= 3 ? 'recurring archive signal' : null,
        ],
        'enough recurrence to cite without overstating',
        'monthly summaries as evidence anchors'
      );
      why =
        'For positioning and throughline, this selection is ' +
        (priority === 'High' ? 'strong' : priority === 'Medium' ? 'moderate' : 'weak') +
        ' because it combines ' +
        pSig.join(', ') +
        '.';

      if (priority === 'Low') {
        nextMove = 'Do not promote this as a career pillar; keep it as a footnote example.';
      } else if (activity && crossProject >= 2) {
        nextMove =
          'Write one sentence pattern claim, then attach one bullet from this month and one from a different project.';
      } else {
        nextMove =
          'Name the pattern in plain language, then find a second month (same project or not) that proves it.';
      }
    }

    var topActs = (data.projectActivities[project] || [])
      .filter(function (a) {
        return a.monthly && a.monthly[monthIdx] > 0;
      })
      .sort(function (a, b) {
        return (b.monthly[monthIdx] || 0) - (a.monthly[monthIdx] || 0);
      })
      .slice(0, 5)
      .map(function (a) {
        return a.name + ' (' + a.monthly[monthIdx] + ')';
      });

    var modeLabel = mode === 'resume' ? 'Resume' : mode === 'interview' ? 'Interview' : 'Positioning';

    return {
      modeLabel: modeLabel,
      why: why,
      bestUse: bestUse.slice(0, 3),
      priority: priority,
      priorityNote: priorityNote,
      reasoning: reasoning.slice(0, 5),
      nextMove: nextMove,
      supporting: {
        month: month,
        project: project,
        activity: activity,
        collaborators: people.slice(0, 8),
        topCategoriesThisMonth: topActs,
        tags: tags.slice(0, 8),
      },
      scores: {
        resumeValue: resumeValue,
        interviewValue: interviewValue,
        productRel: productRel,
        gameRel: gameRel,
        throughline: throughlineScore,
        mining: mining,
      },
    };
  }

  function renderTriage(root, result) {
    if (!root) return;
    var bu = result.bestUse.map(function (x) {
      return escapeHtml(x);
    }).join(', ');
    var reas = result.reasoning
      .map(function (r) {
        return '<li>' + escapeHtml(r) + '</li>';
      })
      .join('');
    var collab = result.supporting.collaborators
      .map(function (n) {
        return '<li>' + escapeHtml(n) + '</li>';
      })
      .join('');
    var cats = result.supporting.topCategoriesThisMonth
      .map(function (c) {
        return '<li>' + escapeHtml(c) + '</li>';
      })
      .join('');
    var tags = result.supporting.tags
      .map(function (t) {
        return '<span class="evidence-triage__chip">' + escapeHtml(t) + '</span>';
      })
      .join(' ');

    root.innerHTML =
      '<div class="evidence-triage__modes" role="group" aria-label="Triage mode">' +
      '<span class="evidence-triage__modes-label">Mode</span> ' +
      '<button type="button" class="evidence-triage__mode' +
      (currentMode === 'resume' ? ' is-active' : '') +
      '" data-mode="resume">Resume</button> ' +
      '<button type="button" class="evidence-triage__mode' +
      (currentMode === 'interview' ? ' is-active' : '') +
      '" data-mode="interview">Interview</button> ' +
      '<button type="button" class="evidence-triage__mode' +
      (currentMode === 'positioning' ? ' is-active' : '') +
      '" data-mode="positioning">Positioning</button>' +
      '</div>' +
      '<p class="evidence-triage__lens">Reading this selection as: <strong>' +
      escapeHtml(result.modeLabel || 'Resume') +
      '</strong> — all sections below follow this lens.</p>' +
      '<section class="evidence-triage__section"><h4 class="evidence-triage__h">Why this matters</h4>' +
      '<p class="evidence-triage__lead">' +
      escapeHtml(result.why) +
      '</p></section>' +
      '<section class="evidence-triage__section"><h4 class="evidence-triage__h">Best use</h4>' +
      '<p>' +
      bu +
      '</p></section>' +
      '<section class="evidence-triage__section"><h4 class="evidence-triage__h">Priority</h4>' +
      '<p><strong>' +
      escapeHtml(result.priority) +
      '</strong> — ' +
      escapeHtml(result.priorityNote) +
      '</p></section>' +
      '<section class="evidence-triage__section"><h4 class="evidence-triage__h">Reasoning</h4><ul class="evidence-triage__list">' +
      reas +
      '</ul></section>' +
      '<section class="evidence-triage__section"><h4 class="evidence-triage__h">Suggested next move</h4>' +
      '<p>' +
      escapeHtml(result.nextMove) +
      '</p></section>' +
      '<section class="evidence-triage__section"><h4 class="evidence-triage__h">Supporting records</h4>' +
      '<p class="evidence-triage__meta">' +
      escapeHtml(result.supporting.month) +
      ' · ' +
      escapeHtml(result.supporting.project) +
      (result.supporting.activity ? ' · ' + escapeHtml(result.supporting.activity) : '') +
      '</p>' +
      (tags ? '<div class="evidence-triage__tags">' + tags + '</div>' : '') +
      '<p class="evidence-triage__subh">Top categories this month</p><ul class="evidence-triage__list">' +
      (cats || '<li>—</li>') +
      '</ul>' +
      '<p class="evidence-triage__subh">Collaborators</p><ul class="evidence-triage__list">' +
      (collab || '<li>—</li>') +
      '</ul></section>';

    root.querySelectorAll('.evidence-triage__mode').forEach(function (btn) {
      btn.addEventListener('click', function () {
        var m = btn.getAttribute('data-mode');
        if (m && m !== currentMode) {
          currentMode = m;
          refresh();
        }
      });
    });
  }

  var lastCtx = null;

  function refresh() {
    if (!lastCtx) return;
    lastCtx.mode = currentMode;
    var result = computeTriage(lastCtx);
    var ins = document.getElementById('provenance-inspector');
    var ov = document.getElementById('provenance-overlay');
    var sidebar = ins && !ins.hidden;
    var overlay = ov && !ov.hidden;
    var sidebarRoot = document.getElementById('evidence-triage-root');
    var overlayRoot = document.getElementById('evidence-triage-overlay-root');
    if (overlay && overlayRoot) renderTriage(overlayRoot, result);
    if (sidebar && sidebarRoot) renderTriage(sidebarRoot, result);
    if (!sidebar && sidebarRoot && overlay) {
      sidebarRoot.innerHTML =
        '<p class="evidence-triage__placeholder">Triage for this selection is in the overview dialog (scroll the dialog).</p>';
    }
  }

  function afterInspectorOpen(month, project, activity, focusMeta) {
    var ins = document.getElementById('provenance-inspector');
    var ov = document.getElementById('provenance-overlay');
    var sidebar = ins && !ins.hidden;
    var overlay = ov && !ov.hidden;
    var sidebarRoot = document.getElementById('evidence-triage-root');
    if (!sidebarRoot) return;

    if (!sidebar && !overlay) {
      clearPanel();
      return;
    }

    if (typeof data === 'undefined') return;
    var prov = typeof provenanceData !== 'undefined' ? provenanceData : null;
    if (!prov) return;

    var act = activity == null ? '' : String(activity);
    lastCtx = {
      data: data,
      provenanceData: prov,
      month: String(month),
      project: String(project),
      activity: act,
      focusMeta: focusMeta,
      mode: currentMode,
    };
    var result = computeTriage(lastCtx);

    var overlayRoot = document.getElementById('evidence-triage-overlay-root');
    if (overlay && overlayRoot) {
      renderTriage(overlayRoot, result);
    } else if (overlayRoot) {
      overlayRoot.innerHTML = '';
    }

    if (sidebar) {
      renderTriage(sidebarRoot, result);
    } else {
      sidebarRoot.innerHTML =
        '<p class="evidence-triage__placeholder">Triage for this selection is in the overview dialog (scroll the dialog).</p>';
    }
  }

  function clearPanel() {
    var sidebarRoot = document.getElementById('evidence-triage-root');
    var overlayRoot = document.getElementById('evidence-triage-overlay-root');
    if (sidebarRoot) {
      sidebarRoot.innerHTML =
        '<p class="evidence-triage__placeholder">Use the selectors at the top, then Apply, to load triage.</p>';
    }
    if (overlayRoot) overlayRoot.innerHTML = '';
    lastCtx = null;
  }

  global.EvidenceTriage = {
    computeTriage: computeTriage,
    afterInspectorOpen: afterInspectorOpen,
    clearPanel: clearPanel,
    setMode: function (m) {
      if (m === 'resume' || m === 'interview' || m === 'positioning') {
        currentMode = m;
        refresh();
      }
    },
    getMode: function () {
      return currentMode;
    },
  };
})(typeof window !== 'undefined' ? window : this);
