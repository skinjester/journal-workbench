/**
 * Shared cell provenance UI: monthly summary markdown → HTML with per-line highlights.
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

  function renderSummaryBody(bodyEl, source, hlSet) {
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
        if (sec.endIdx > i + 1 || sec.entries.length > 0) {
          var inner = renderPeopleEntriesHtml(sec.entries, hlSet);
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
      var inner = parseLineMarkdown(trimmed);
      var cls = hl ? 'summary-block summary-block--hl' : 'summary-block';
      parts.push('<div class="' + cls + '">' + inner + '</div>');
      i++;
    }
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

    if (!bodyEl) return { ok: false, error: 'Missing body element' };

    if (!month || !project || !activity) {
      if (kickerEl) kickerEl.textContent = '';
      if (titleEl) titleEl.textContent = 'Missing parameters';
      if (metaEl) {
        metaEl.innerHTML =
          '<span class="err">Use <code>?month=YYYY-MM&project=…&activity=…</code> (open from the matrix by clicking a subcategory cell).</span>';
      }
      bodyEl.textContent = '';
      return { ok: false, error: 'missing-params' };
    }

    const months = provenanceData.months || [];
    const mi = months.indexOf(month);
    const source = (provenanceData.monthSources && provenanceData.monthSources[month]) || '';
    const prov = provenanceData.activityProvenance && provenanceData.activityProvenance[project];
    const series = prov && prov[activity];
    const highlights = series && mi >= 0 && mi < series.length ? series[mi] : [];
    const hlSet = new Set((highlights || []).map(normLine));

    if (kickerEl) kickerEl.textContent = month;
    if (titleEl) titleEl.textContent = project;
    if (metaEl) metaEl.textContent = activity;

    if (!source) {
      bodyEl.innerHTML = '<span class="empty">No summary text found for this month.</span>';
      return { ok: true };
    }

    renderSummaryBody(bodyEl, source, hlSet);

    const first = bodyEl.querySelector('.summary-block--hl, .people-chip--hl');
    if (first && typeof first.scrollIntoView === 'function') {
      requestAnimationFrame(function () {
        first.scrollIntoView({ block: 'nearest', behavior: 'smooth' });
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
