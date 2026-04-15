/**
 * Evidence Triage: selection without the matrix/milestone charts.
 * Runs after the matrix inline script and openProvenanceInspector hook.
 */
(function () {
  'use strict';

  function init() {
    if (typeof data === 'undefined' || !data.rows || !data.months) return;

    var proj = document.getElementById('et-project');
    var month = document.getElementById('et-month');
    var act = document.getElementById('et-activity');
    var btn = document.getElementById('et-apply');
    if (!proj || !month || !act || !btn) return;

    data.rows.forEach(function (r) {
      var o = document.createElement('option');
      o.value = r;
      o.textContent = r;
      proj.appendChild(o);
    });

    data.months.forEach(function (m) {
      var o = document.createElement('option');
      o.value = m;
      o.textContent = m;
      month.appendChild(o);
    });

    if (data.defaultProject && data.rows.indexOf(data.defaultProject) >= 0) {
      proj.value = data.defaultProject;
    } else if (data.rows.length) {
      proj.value = data.rows[0];
    }
    if (data.months.length) {
      month.value = data.months[data.months.length - 1];
    }

    function refillActivities() {
      act.innerHTML = '';
      var o0 = document.createElement('option');
      o0.value = '';
      o0.textContent = 'Project overview (month snapshot)';
      act.appendChild(o0);
      var p = proj.value;
      var list = data.projectActivities && data.projectActivities[p] ? data.projectActivities[p] : [];
      list.forEach(function (a) {
        var o = document.createElement('option');
        o.value = a.name;
        o.textContent = a.name + ' (' + a.total + ')';
        act.appendChild(o);
      });
    }

    proj.addEventListener('change', refillActivities);
    refillActivities();

    function applySelection() {
      var p = proj.value;
      var m = month.value;
      var a = act.value;
      if (!p || !m) return;
      if (typeof openProvenanceInspector !== 'function') return;

      var rowIdx = data.rows.indexOf(p);
      if (a) {
        openProvenanceInspector(m, p, a, undefined);
      } else {
        var fm =
          rowIdx >= 0
            ? { projectOverview: true, rowIndex: rowIdx, rowKey: p }
            : { projectOverview: true };
        openProvenanceInspector(m, p, '', fm);
      }
    }

    btn.addEventListener('click', applySelection);
    applySelection();
  }

  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', function () {
      setTimeout(init, 0);
    });
  } else {
    setTimeout(init, 0);
  }
})();
