/**
 * Shared cell provenance UI: monthly summary markdown → HTML with per-line highlights.
 * `hoverSummary`: hover tooltip only — kicker/title/meta plus a matching-line count (no full body).
 * Matrix overlay (`matchesOnly`): same ### sections as the month file, only lines relevant
 * to the selected activity (no highlight styling). Full page view keeps the whole summary.
 * Depends on global `marked` (https://marked.js.org) loaded before this script.
 */
(function (global) {
  'use strict';

  function escapeHtml(text) {
    return String(text)
      .replace(/&/g, '&amp;')
      .replace(/</g, '&lt;')
      .replace(/"/g, '&quot;');
  }

  function normLine(s) {
    return String(s).replace(/\s+/g, ' ').trim();
  }

  function parseLineMarkdown(trimmed) {
    const marked = global.marked;
    if (!marked || typeof marked.parse !== 'function') {
      return '<p>' + escapeHtml(trimmed) + '</p>';
    }
    try {
      const opts = { async: false };
      return marked.parse(trimmed + '\n', opts);
    } catch (e) {
      return '<p>' + escapeHtml(trimmed) + '</p>';
    }
  }

  var PEOPLE_H3 = /^###\s+People Involved\s*$/i;
  var BULLET = /^\s*-\s+(.*)$/;

  function stripBulletMd(text) {
    var m = String(text).match(BULLET);
    return m ? m[1].trim() : String(text).trim();
  }

  function displayNameFromBulletLine(raw) {
    return stripBulletMd(raw).replace(/\*\*/g, '').trim();
  }

  function initialsFromDisplayName(name) {
    var s = String(name).trim();
    if (!s) return '?';
    var parts = s.split(/\s+/).filter(Boolean);
    if (parts.length === 1) {
      return parts[0].charAt(0).toUpperCase();
    }
    var a = parts[0].charAt(0);
    var b = parts[parts.length - 1].charAt(0);
    return (a + b).toUpperCase();
  }

  /**
   * Lines after ### People Involved until ###, ---, or EOF (exclusive of terminator).
   */
  function parsePeopleSectionLines(lines, headingIdx) {
    var j = headingIdx + 1;
    var entries = [];
    while (j < lines.length) {
      var raw = lines[j];
      var t = raw.trim();
      if (t === '') {
        j++;
        continue;
      }
      if (/^###\s/.test(t)) break;
      if (/^---\s*$/.test(t)) break;
      if (BULLET.test(raw)) {
        var dn = displayNameFromBulletLine(raw);
        if (dn) entries.push({ kind: 'name', rawLine: raw, displayName: dn });
      } else if (/^none\s+identified\s*$/i.test(t)) {
        entries.push({ kind: 'none', rawLine: raw });
      } else {
        entries.push({ kind: 'plain', rawLine: raw, text: t });
      }
      j++;
    }
    return { endIdx: j, entries: entries };
  }

  function renderPeopleEntriesHtml(entries, hlSet) {
    var names = entries.filter(function (e) {
      return e.kind === 'name';
    });
    var nones = entries.filter(function (e) {
      return e.kind === 'none';
    });
    var plains = entries.filter(function (e) {
      return e.kind === 'plain';
    });
    var out = '';

    if (names.length === 0 && nones.length > 0 && plains.length === 0) {
      return '<p class="people-none">' + escapeHtml(nones[0].rawLine.trim()) + '</p>';
    }

    if (names.length > 0) {
      var chips = names
        .map(function (e) {
          var n = normLine(e.rawLine);
          var hl = Boolean(n && hlSet.has(n));
          var ini = initialsFromDisplayName(e.displayName);
          var cls = 'people-chip' + (hl ? ' people-chip--hl' : '');
          return (
            '<div class="' +
            cls +
            '" role="listitem">' +
            '<span class="people-avatar" aria-hidden="true">' +
            escapeHtml(ini) +
            '</span>' +
            '<span class="people-name">' +
            escapeHtml(e.displayName) +
            '</span>' +
            '</div>'
          );
        })
        .join('');
      out += '<div class="people-row" role="list">' + chips + '</div>';
    }

    for (var p = 0; p < plains.length; p++) {
      out +=
        '<div class="people-plain">' +
        parseLineMarkdown(plains[p].rawLine.trimEnd().trim()) +
        '</div>';
    }

    if (names.length === 0 && nones.length > 0 && plains.length > 0) {
      out = '<p class="people-none">' + escapeHtml(nones[0].rawLine.trim()) + '</p>' + out;
    }

    return out;
  }

  /**
   * Monthly files end with `---` then a short narrative paragraph; show that first in the overlay.
   * Uses the last `---` line only so an accidental rule earlier does not split the doc.
   */
  function splitClosingSummaryParagraph(source) {
    var lines = source.split('\n');
    var ruleIdx = -1;
    for (var k = lines.length - 1; k >= 0; k--) {
      if (/^---\s*$/.test(lines[k].trim())) {
        ruleIdx = k;
        break;
      }
    }
    if (ruleIdx < 0) {
      return { lead: '', detail: source };
    }
    var lead = lines.slice(ruleIdx + 1).join('\n').trim();
    var detail = lines.slice(0, ruleIdx).join('\n').trimEnd();
    if (lead) {
      return { lead: lead, detail: detail };
    }
    return { lead: '', detail: detail };
  }

  function filterPeopleSectionEntries(entries, peopleProjectFilter) {
    if (!peopleProjectFilter) return entries;
    var allow = peopleAllowSetForCell(
      peopleProjectFilter.provenanceData,
      peopleProjectFilter.month,
      peopleProjectFilter.project
    );
    if (allow == null) return entries;
    return entries.filter(function (e) {
      if (e.kind !== 'name') return false;
      return allow.has(normLine(e.displayName));
    });
  }

  function renderSummaryParts(source, hlSet, peopleProjectFilter) {
    var lines = source.split('\n');
    var parts = [];
    var i = 0;
    while (i < lines.length) {
      var line = lines[i];
      var trimmed = line.trimEnd();
      var t = trimmed.trim();
      if (PEOPLE_H3.test(t)) {
        var n0 = normLine(line);
        var hl0 = Boolean(n0 && hlSet.has(n0));
        var cls0 = hl0 ? 'summary-block summary-block--hl' : 'summary-block';
        parts.push('<div class="' + cls0 + '">' + parseLineMarkdown(trimmed) + '</div>');
        var sec = parsePeopleSectionLines(lines, i);
        var peEntries = filterPeopleSectionEntries(sec.entries, peopleProjectFilter);
        if (sec.endIdx > i + 1 || peEntries.length > 0) {
          var inner = renderPeopleEntriesHtml(peEntries, hlSet);
          if (inner) {
            parts.push('<div class="summary-block summary-block--people">' + inner + '</div>');
          }
        }
        i = sec.endIdx;
        continue;
      }
      var n = normLine(line);
      var hl = Boolean(n && hlSet.has(n));
      var isEmpty = !t;
      if (isEmpty) {
        parts.push('<div class="summary-block summary-block--empty"></div>');
        i++;
        continue;
      }
      var innerMd = parseLineMarkdown(trimmed);
      var cls = hl ? 'summary-block summary-block--hl' : 'summary-block';
      parts.push('<div class="' + cls + '">' + innerMd + '</div>');
      i++;
    }
    return parts;
  }

  function renderSummaryBody(bodyEl, source, hlSet, opts) {
    opts = opts || {};
    var peopleProjectFilter = opts.peopleProjectFilter || null;
    var split = splitClosingSummaryParagraph(source);
    var chunks = [];
    if (split.lead) {
      chunks = chunks.concat(renderSummaryParts(split.lead, hlSet, peopleProjectFilter));
      if (split.detail) {
        chunks.push('<hr class="summary-body-lead-divider" aria-hidden="true" />');
        chunks = chunks.concat(renderSummaryParts(split.detail, hlSet, peopleProjectFilter));
      }
    } else {
      chunks = renderSummaryParts(split.detail, hlSet, peopleProjectFilter);
    }
    bodyEl.innerHTML = chunks.join('');
  }

  /**
   * Flat list: file order, then highlight strings missing from file. Used as overlay fallback.
   */
  function orderedMatchingLines(source, hlSet, highlights) {
    var ordered = [];
    var seenNorm = new Set();
    var lines = source.split('\n');
    for (var i = 0; i < lines.length; i++) {
      var line = lines[i];
      var t = line.trim();
      if (!t || /^---\s*$/.test(t)) continue;
      var n = normLine(line);
      if (n && hlSet.has(n) && !seenNorm.has(n)) {
        seenNorm.add(n);
        ordered.push(t);
      }
    }
    for (var j = 0; j < highlights.length; j++) {
      var h = highlights[j];
      var nh = normLine(h);
      if (nh && !seenNorm.has(nh)) {
        seenNorm.add(nh);
        ordered.push(String(h).trim());
      }
    }
    return ordered;
  }

  function renderFlatMatchFallback(bodyEl, source, hlSet, highlights) {
    var rows = orderedMatchingLines(source, hlSet, highlights);
    if (rows.length === 0) {
      bodyEl.innerHTML =
        '<span class="empty">No matching lines found in the summary for this month.</span>';
      return;
    }
    var parts = rows.map(function (trimmed) {
      return '<div class="summary-block">' + parseLineMarkdown(trimmed) + '</div>';
    });
    bodyEl.innerHTML = parts.join('');
  }

  /**
   * When `peopleByProject` exists (from build_project_matrix), return a Set of normalized names
   * for this month+matrix row; otherwise null → show full People Involved (legacy HTML).
   */
  function peopleAllowSetForCell(provenanceData, month, project) {
    var root = provenanceData && provenanceData.peopleByProject;
    if (!root || !month || !project) return null;
    var pm = root[month];
    if (!pm || typeof pm !== 'object') return null;
    if (!Object.prototype.hasOwnProperty.call(pm, project)) return null;
    var arr = pm[project];
    if (!Array.isArray(arr)) return null;
    var s = new Set();
    for (var i = 0; i < arr.length; i++) {
      var n = normLine(String(arr[i] || '').trim());
      if (n) s.add(n);
    }
    return s;
  }

  /**
   * Matrix overlay: keep ### section headings from the month file, but only bullets that match
   * this cell’s provenance (everything else hidden). ### People Involved is appended after an
   * &lt;hr&gt;, filtered to names tied to this project when `peopleByProject` is present.
   */
  function renderFilteredOverlayBody(bodyEl, source, hlSet, highlights, cellCtx) {
    var lines = source.split('\n');
    var parts = [];
    var i = 0;
    var n = lines.length;
    var noHl = new Set();
    var peopleBlock = null;

    function flushSection(headingTrimmed, matchedTrimmedLines) {
      if (matchedTrimmedLines.length === 0) return;
      parts.push('<div class="summary-block">' + parseLineMarkdown(headingTrimmed) + '</div>');
      for (var k = 0; k < matchedTrimmedLines.length; k++) {
        parts.push('<div class="summary-block">' + parseLineMarkdown(matchedTrimmedLines[k]) + '</div>');
      }
    }

    function appendFullPeopleSection(chunks) {
      if (!peopleBlock || !peopleBlock.entries || peopleBlock.entries.length === 0) return;
      var allow =
        cellCtx && peopleAllowSetForCell(cellCtx.provenanceData, cellCtx.month, cellCtx.project);
      var pe = peopleBlock.entries;
      if (allow != null) {
        pe = pe.filter(function (e) {
          if (e.kind !== 'name') return false;
          return allow.has(normLine(e.displayName));
        });
        if (pe.length === 0) return;
      }
      var inner = renderPeopleEntriesHtml(pe, noHl);
      if (!inner) return;
      chunks.push('<hr class="summary-body-lead-divider" aria-hidden="true" />');
      chunks.push(
        '<div class="summary-block">' + parseLineMarkdown(peopleBlock.headingLine.trim()) + '</div>'
      );
      chunks.push('<div class="summary-block summary-block--people">' + inner + '</div>');
    }

    while (i < n) {
      var line = lines[i];
      var trimmed = line.trimEnd();
      var t = trimmed.trim();
      if (!t) {
        i++;
        continue;
      }
      if (/^---\s*$/.test(t)) {
        break;
      }
      if (PEOPLE_H3.test(t)) {
        var sec = parsePeopleSectionLines(lines, i);
        if (!peopleBlock && sec.entries.length > 0) {
          peopleBlock = { headingLine: trimmed, entries: sec.entries };
        }
        i = sec.endIdx;
        continue;
      }
      if (/^###\s/.test(t)) {
        var headingLine = trimmed;
        i++;
        var matchedLines = [];
        while (i < n) {
          var L = lines[i];
          var Te = L.trim();
          if (!Te) {
            i++;
            continue;
          }
          if (/^---\s*$/.test(Te)) {
            break;
          }
          if (/^###\s/.test(Te)) {
            break;
          }
          var nrm = normLine(L);
          if (nrm && hlSet.has(nrm)) {
            matchedLines.push(Te);
          }
          i++;
        }
        flushSection(headingLine, matchedLines);
        continue;
      }
      var nrm2 = normLine(line);
      if (nrm2 && hlSet.has(nrm2)) {
        parts.push('<div class="summary-block">' + parseLineMarkdown(t) + '</div>');
      }
      i++;
    }

    if (parts.length === 0 && highlights && highlights.length > 0) {
      var flat = orderedMatchingLines(source, hlSet, highlights);
      var flatParts = flat.map(function (trimmed) {
        return '<div class="summary-block">' + parseLineMarkdown(trimmed) + '</div>';
      });
      appendFullPeopleSection(flatParts);
      if (flatParts.length > 0) {
        bodyEl.innerHTML = flatParts.join('');
        return;
      }
      bodyEl.innerHTML =
        '<span class="empty">No matching lines found in the summary for this month.</span>';
      return;
    }
    if (parts.length === 0) {
      var onlyPeople = [];
      appendFullPeopleSection(onlyPeople);
      if (onlyPeople.length > 0) {
        bodyEl.innerHTML = onlyPeople.join('');
        return;
      }
      bodyEl.innerHTML =
        '<span class="empty">No matching lines found in the summary for this month.</span>';
      return;
    }
    appendFullPeopleSection(parts);
    bodyEl.innerHTML = parts.join('');
  }

  function render(options) {
    const month = options.month || '';
    const project = options.project || '';
    const activity = options.activity || '';
    const kickerEl = options.kickerEl;
    const titleEl = options.titleEl;
    const metaEl = options.metaEl;
    const bodyEl = options.bodyEl;
    const provenanceData = options.provenanceData || {};
    const matchesOnly = Boolean(options.matchesOnly);
    const projectOverview = Boolean(options.projectOverview);

    if (!bodyEl) return { ok: false, error: 'Missing body element' };

    if (!month || !project || (!projectOverview && !activity)) {
      if (kickerEl) kickerEl.textContent = '';
      if (titleEl) titleEl.textContent = 'Missing parameters';
      if (metaEl) {
        metaEl.innerHTML = projectOverview
          ? ''
          : '<span class="err">Use <code>?month=YYYY-MM&project=…&activity=…</code> (open from the matrix by clicking a subcategory cell).</span>';
      }
      bodyEl.textContent = '';
      return { ok: false, error: 'missing-params' };
    }

    const months = provenanceData.months || [];
    const mi = months.indexOf(month);
    const source = (provenanceData.monthSources && provenanceData.monthSources[month]) || '';

    if (projectOverview) {
      if (kickerEl) kickerEl.textContent = month;
      if (titleEl) titleEl.textContent = project;
      if (metaEl) metaEl.textContent = 'Project overview';
      if (!source) {
        bodyEl.innerHTML = '<span class="empty">No summary text found for this month.</span>';
        return { ok: true };
      }
      if (Boolean(options.hoverSummary)) {
        bodyEl.innerHTML = '<p class="prov-hover-count">Full month summary</p>';
        return { ok: true };
      }
      renderSummaryBody(bodyEl, source, new Set(), {
        peopleProjectFilter: { provenanceData: provenanceData, month: month, project: project }
      });
      const firstOv = bodyEl.querySelector('.summary-block--hl, .people-chip--hl');
      if (firstOv && typeof firstOv.scrollIntoView === 'function') {
        requestAnimationFrame(function () {
          firstOv.scrollIntoView({ block: 'nearest', behavior: 'smooth' });
        });
      }
      return { ok: true };
    }

    const prov = provenanceData.activityProvenance && provenanceData.activityProvenance[project];
    const series = prov && prov[activity];
    const rawHl = series && mi >= 0 && mi < series.length ? series[mi] : null;
    const highlights = Array.isArray(rawHl) ? rawHl : [];
    const hlSet = new Set(highlights.map(normLine));

    if (kickerEl) kickerEl.textContent = month;
    if (titleEl) titleEl.textContent = project;
    if (metaEl) metaEl.textContent = activity;

    if (!source) {
      bodyEl.innerHTML = '<span class="empty">No summary text found for this month.</span>';
      return { ok: true };
    }

    if (Boolean(options.hoverSummary)) {
      var hn = highlights.length;
      var hlabel =
        hn === 0 ? 'No matching items' : hn === 1 ? '1 matching item' : hn + ' matching items';
      bodyEl.innerHTML = '<p class="prov-hover-count">' + escapeHtml(hlabel) + '</p>';
      return { ok: true };
    }

    if (matchesOnly) {
      if (highlights.length === 0) {
        bodyEl.innerHTML =
          '<span class="empty">No matching lines for this activity in this month.</span>';
      } else {
        renderFilteredOverlayBody(bodyEl, source, hlSet, highlights, {
          provenanceData: provenanceData,
          month: month,
          project: project
        });
      }
    } else {
      renderSummaryBody(bodyEl, source, hlSet, {
        peopleProjectFilter: { provenanceData: provenanceData, month: month, project: project }
      });
    }

    const firstHl = bodyEl.querySelector('.summary-block--hl, .people-chip--hl');
    if (firstHl && typeof firstHl.scrollIntoView === 'function') {
      requestAnimationFrame(function () {
        firstHl.scrollIntoView({ block: 'nearest', behavior: 'smooth' });
      });
    }
    return { ok: true };
  }

  global.ProvenanceView = {
    escapeHtml: escapeHtml,
    normLine: normLine,
    render: render,
    renderSummaryBody: renderSummaryBody,
  };
})(typeof window !== 'undefined' ? window : globalThis);
