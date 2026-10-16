
(function(){
  // Newsletter / sponsor placeholders
  document.querySelectorAll('[data-newsletter]').forEach(function(form){
    form.addEventListener('submit', function(e){
      e.preventDefault();
      var email = form.querySelector('input[type=email]');
      var msg = form.querySelector('[data-msg]');
      if(!email || !email.value){ return; }
      if(msg){
        msg.textContent = '已记录意向（本地示意，尚未接邮箱服务）：' + email.value;
        msg.hidden = false;
      }
      form.reset();
    });
  });

  // Case filters
  var list = document.querySelector('[data-case-list]');
  var ind = document.querySelector('#filter-industry');
  var q = document.querySelector('#filter-q');
  function applyFilter(){
    if(!list) return;
    var iv = ind ? ind.value : '';
    var qv = (q && q.value || '').trim().toLowerCase();
    list.querySelectorAll('.case-card').forEach(function(card){
      var ok = true;
      if(iv && card.getAttribute('data-industry') !== iv) ok = false;
      if(qv){
        var t = card.textContent.toLowerCase();
        if(t.indexOf(qv) === -1) ok = false;
      }
      card.style.display = ok ? '' : 'none';
    });
  }
  if(ind) ind.addEventListener('change', applyFilter);
  if(q) q.addEventListener('input', applyFilter);

  // Feibiao demo
  var runBtn = document.querySelector('#run-sample');
  var out = document.querySelector('#demo-result');
  var fileInput = document.querySelector('#tender-file');
  var uploadHint = document.querySelector('#upload-hint');
  if(fileInput && uploadHint){
    fileInput.addEventListener('change', function(){
      if(fileInput.files && fileInput.files[0]){
        uploadHint.textContent = '已选择：' + fileInput.files[0].name + '（MVP 仅前端示意，请点「运行内置样例」查看结构化输出）';
      }
    });
  }
  if(runBtn && out){
    runBtn.addEventListener('click', function(){
      fetch('sample-tender.json').then(function(r){ return r.json(); }).then(function(data){
        out.hidden = false;
        out.innerHTML = renderFeibiao(data);
      }).catch(function(err){
        out.hidden = false;
        out.textContent = '加载样例失败：' + err;
      });
    });
  }
  function renderFeibiao(data){
    function rows(items, cols){
      return '<table class="table"><thead><tr>' + cols.map(function(c){return '<th>'+c+'</th>';}).join('') +
        '</tr></thead><tbody>' + items.map(function(it){
          return '<tr>' + cols.map(function(c){
            var key = ({'类型':'type','条款':'text','引用':'cite','类别':'category','要求':'text','分值/权重':'weight','说明':'note'})[c] || c;
            return '<td>' + (it[key] || '') + '</td>';
          }).join('') + '</tr>';
        }).join('') + '</tbody></table>';
    }
    return '<div class="ok-note">以下为<strong>内置样例招标文本</strong>的结构化抽取示意，非真实投标建议。必须人工复核。</div>' +
      '<p><strong>项目</strong>：' + data.project + '<br><strong>截止时间</strong>：' + data.deadline +
      ' <span class="muted">（引自 ' + data.deadline_cite + '）</span></p>' +
      '<h3>废标 / 否决项</h3>' + rows(data.disqualify, ['类型','条款','引用']) +
      '<h3>资格门槛</h3>' + rows(data.qualification, ['类别','要求','引用']) +
      '<h3>评分点</h3>' + rows(data.scoring, ['类别','说明','分值/权重','引用']) +
      '<p class="muted" style="margin-top:1rem">样例来源文件：' + data.sample_file + ' · 生成方式：规则+人工标注示意</p>';
  }
})();
