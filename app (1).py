import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(
    page_title="Criador de Fluxograma",
    page_icon="🔀",
    layout="wide"
)

st.markdown("""
    <style>
        #MainMenu {visibility: hidden;}
        footer {visibility: hidden !important;}
        header {visibility: hidden;}
        [data-testid="stToolbar"] {visibility: hidden;}
        [data-testid="manage-app-button"] {display: none !important;}
        .viewerBadge_container__r5tak {display: none !important;}
        ._profileContainer_pgrmq_53 {display: none !important;}
        .block-container {padding: 0 !important; max-width: 100% !important;}
        .stApp { overflow: hidden; }
    </style>
""", unsafe_allow_html=True)

html = """
<!DOCTYPE html>
<html lang="pt-BR">
<head>
<meta charset="UTF-8">
<style>
  * { box-sizing: border-box; margin: 0; padding: 0; }
  body { font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif; background: #f8f9fa; height: 100vh; display: flex; flex-direction: column; overflow: hidden; }

  .top-bar {
    background: #fff;
    border-bottom: 1px solid #e2e8f0;
    padding: 10px 16px;
    display: flex;
    align-items: center;
    gap: 10px;
    flex-wrap: wrap;
    flex-shrink: 0;
  }
  .top-bar h1 { font-size: 15px; font-weight: 600; color: #1a202c; }

  .input-wrap { display: flex; flex: 1; min-width: 220px; gap: 8px; }
  .input-wrap input {
    flex: 1;
    padding: 7px 12px;
    border: 1px solid #cbd5e0;
    border-radius: 8px;
    font-size: 13px;
    outline: none;
    transition: border-color .2s;
  }
  .input-wrap input:focus { border-color: #667eea; }

  .btn {
    padding: 7px 14px;
    border-radius: 8px;
    font-size: 13px;
    font-weight: 500;
    cursor: pointer;
    border: none;
    transition: all .15s;
    white-space: nowrap;
  }
  .btn-primary { background: #667eea; color: #fff; }
  .btn-primary:hover { background: #5a67d8; }
  .btn-secondary { background: #fff; color: #4a5568; border: 1px solid #e2e8f0; }
  .btn-secondary:hover { background: #f7fafc; }

  .toolbar-divider { width: 1px; height: 26px; background: #e2e8f0; flex-shrink: 0; }

  .type-selector { display: flex; gap: 4px; align-items: center; flex-wrap: wrap; }
  .type-lbl { font-size: 11px; color: #718096; font-weight: 600; white-space: nowrap; }
  .type-btn {
    padding: 5px 10px;
    border-radius: 6px;
    font-size: 12px;
    font-weight: 500;
    cursor: pointer;
    border: 1px solid #e2e8f0;
    background: #fff;
    color: #4a5568;
    transition: all .15s;
  }
  .type-btn.active { background: #667eea; color: #fff; border-color: #667eea; }
  .type-btn:hover:not(.active) { background: #f7fafc; }

  .main { display: flex; flex: 1; overflow: hidden; }

  .sidebar {
    width: 220px;
    background: #fff;
    border-right: 1px solid #e2e8f0;
    padding: 14px;
    overflow-y: auto;
    flex-shrink: 0;
  }
  .sidebar-title { font-size: 11px; font-weight: 600; color: #718096; text-transform: uppercase; letter-spacing: .05em; margin-bottom: 10px; }

  .step-item {
    background: #f7fafc;
    border: 1px solid #e2e8f0;
    border-radius: 8px;
    padding: 7px 8px;
    margin-bottom: 5px;
    font-size: 12px;
    color: #2d3748;
    cursor: pointer;
    display: flex;
    align-items: center;
    gap: 6px;
    transition: background .15s;
  }
  .step-item:hover { background: #edf2f7; }
  .step-item.selected { border-color: #667eea; background: #ebf4ff; }
  .step-num {
    background: #667eea;
    color: #fff;
    border-radius: 50%;
    width: 18px; height: 18px;
    display: flex; align-items: center; justify-content: center;
    font-size: 10px; font-weight: 600; flex-shrink: 0;
  }
  .step-num.start { background: #3182ce; }
  .step-num.end { background: #38a169; }
  .step-num.decision { background: #d69e2e; }
  .step-label { flex: 1; white-space: nowrap; overflow: hidden; text-overflow: ellipsis; }
  .step-actions { display: flex; gap: 2px; }
  .icon-btn {
    background: none; border: none; cursor: pointer;
    padding: 2px 4px; border-radius: 4px;
    color: #a0aec0; font-size: 13px; line-height: 1;
  }
  .icon-btn:hover { background: #e2e8f0; color: #2d3748; }
  .icon-btn.red:hover { background: #fed7d7; color: #e53e3e; }

  .canvas-wrap {
    flex: 1;
    overflow: auto;
    padding: 24px 32px;
    display: flex;
    align-items: flex-start;
    justify-content: center;
  }

  #canvas { min-width: 300px; }

  .flow-col { display: flex; flex-direction: column; align-items: center; }

  .flow-node { position: relative; display: flex; flex-direction: column; align-items: center; }

  .node-box {
    background: #fff;
    border: 2px solid #667eea;
    border-radius: 10px;
    padding: 11px 22px;
    min-width: 160px;
    max-width: 240px;
    text-align: center;
    font-size: 13px;
    font-weight: 500;
    color: #2d3748;
    cursor: pointer;
    transition: all .15s;
    word-break: break-word;
    line-height: 1.4;
  }
  .node-box:hover { box-shadow: 0 2px 10px rgba(102,126,234,.25); }
  .node-box.selected { border-color: #5a67d8; box-shadow: 0 0 0 3px rgba(102,126,234,.3); }

  .node-box.start-box { background: #ebf8ff; border-color: #3182ce; border-radius: 999px; color: #1a365d; padding: 11px 28px; }
  .node-box.end-box   { background: #f0fff4; border-color: #38a169; border-radius: 999px; color: #1c4532; padding: 11px 28px; }
  .node-box.decision-box {
    background: #fefcbf;
    border-color: #d69e2e;
    color: #744210;
    min-width: 170px;
    padding: 24px 36px;
    clip-path: polygon(50% 0%, 100% 50%, 50% 100%, 0% 50%);
    border-radius: 4px;
  }

  .node-type-badge {
    font-size: 9px; font-weight: 700; text-transform: uppercase;
    letter-spacing: .06em; color: #718096; margin-bottom: 3px;
  }
  .start-box .node-type-badge { color: #2b6cb0; }
  .end-box .node-type-badge { color: #276749; }
  .decision-box .node-type-badge { color: #975a16; }

  .node-actions {
    display: none;
    position: absolute;
    top: -12px; right: -12px;
    flex-direction: row;
    gap: 3px;
    z-index: 10;
  }
  .flow-node:hover .node-actions { display: flex; }
  .node-act-btn {
    width: 22px; height: 22px;
    border-radius: 50%;
    border: 1px solid #e2e8f0;
    background: #fff;
    cursor: pointer;
    font-size: 11px;
    display: flex; align-items: center; justify-content: center;
    box-shadow: 0 1px 4px rgba(0,0,0,.12);
    transition: all .15s;
  }
  .node-act-btn:hover { background: #f7fafc; }
  .node-act-btn.del:hover { background: #fff5f5; border-color: #fed7d7; }

  .arrow {
    display: flex; flex-direction: column; align-items: center;
    height: 36px;
  }
  .arrow-line { width: 2px; flex: 1; background: #a0aec0; }
  .arrow-head {
    width: 0; height: 0;
    border-left: 6px solid transparent;
    border-right: 6px solid transparent;
    border-top: 8px solid #a0aec0;
  }

  .inline-edit {
    background: none; border: none;
    border-bottom: 2px solid #667eea;
    font-size: 13px; font-weight: 500;
    color: inherit; text-align: center;
    outline: none; width: 100%; padding: 2px 0;
    font-family: inherit;
  }

  .empty-state {
    text-align: center; padding: 60px 20px; color: #a0aec0;
  }
  .empty-icon { font-size: 48px; margin-bottom: 12px; }
  .empty-state p { font-size: 13px; line-height: 1.6; }
</style>
</head>
<body>

<div class="top-bar">
  <h1>🔀 Fluxograma</h1>

  <div class="type-selector">
    <span class="type-lbl">Tipo:</span>
    <button class="type-btn active" id="t-process"  onclick="setType('process')">Processo</button>
    <button class="type-btn"        id="t-decision" onclick="setType('decision')">Decisão</button>
    <button class="type-btn"        id="t-start"    onclick="setType('start')">Início</button>
    <button class="type-btn"        id="t-end"      onclick="setType('end')">Fim</button>
  </div>

  <div class="toolbar-divider"></div>

  <div class="input-wrap">
    <input type="text" id="stepInput" placeholder="Digite o nome do passo e pressione Enter..." maxlength="80" />
    <button class="btn btn-primary" onclick="addStep()">+ Adicionar</button>
  </div>

  <div class="toolbar-divider"></div>
  <button class="btn btn-secondary" onclick="clearAll()">🗑 Limpar tudo</button>
</div>

<div class="main">
  <div class="sidebar">
    <div class="sidebar-title">Passos</div>
    <div id="stepList"></div>
  </div>
  <div class="canvas-wrap">
    <div id="canvas"></div>
  </div>
</div>

<script>
let steps = [];
let selectedId = null;
let currentType = 'process';
let editingId = null;

document.getElementById('stepInput').addEventListener('keydown', e => {
  if (e.key === 'Enter') addStep();
});

function setType(type) {
  currentType = type;
  ['process','decision','start','end'].forEach(t =>
    document.getElementById('t-'+t).classList.toggle('active', t === type)
  );
}

function addStep() {
  const input = document.getElementById('stepInput');
  const text = input.value.trim();
  if (!text) return;
  steps.push({ id: Date.now(), text, type: currentType });
  input.value = '';
  input.focus();
  render();
}

function deleteStep(id) {
  steps = steps.filter(s => s.id !== id);
  if (selectedId === id) selectedId = null;
  render();
}

function selectStep(id) {
  selectedId = selectedId === id ? null : id;
  render();
}

function startEdit(id, e) {
  e.stopPropagation();
  editingId = id;
  render();
  setTimeout(() => {
    const inp = document.getElementById('edit-' + id);
    if (inp) { inp.focus(); inp.select(); }
  }, 20);
}

function finishEdit(id) {
  const inp = document.getElementById('edit-' + id);
  if (inp) {
    const val = inp.value.trim();
    if (val) { const s = steps.find(s => s.id === id); if (s) s.text = val; }
  }
  editingId = null;
  render();
}

function moveStep(id, dir) {
  const i = steps.findIndex(s => s.id === id);
  const ni = i + dir;
  if (ni < 0 || ni >= steps.length) return;
  [steps[i], steps[ni]] = [steps[ni], steps[i]];
  render();
}

function clearAll() {
  if (!steps.length) return;
  if (confirm('Limpar todos os passos?')) { steps = []; selectedId = null; render(); }
}

function esc(str) {
  return String(str).replace(/&/g,'&amp;').replace(/</g,'&lt;').replace(/>/g,'&gt;').replace(/"/g,'&quot;');
}

function nodeClass(type) {
  return type === 'start' ? 'start-box' : type === 'end' ? 'end-box' : type === 'decision' ? 'decision-box' : '';
}

function typeLabel(type) {
  return type === 'start' ? 'Início' : type === 'end' ? 'Fim' : type === 'decision' ? 'Decisão' : '';
}

function numClass(type) {
  return type === 'start' ? 'start' : type === 'end' ? 'end' : type === 'decision' ? 'decision' : '';
}

function render() {
  renderSidebar();
  renderCanvas();
}

function renderSidebar() {
  const list = document.getElementById('stepList');
  if (!steps.length) {
    list.innerHTML = '<p style="font-size:12px;color:#a0aec0;text-align:center;padding:16px 0">Nenhum passo ainda</p>';
    return;
  }
  list.innerHTML = steps.map((s, i) => `
    <div class="step-item ${selectedId===s.id?'selected':''}" onclick="selectStep(${s.id})">
      <span class="step-num ${numClass(s.type)}">${i+1}</span>
      <span class="step-label" title="${esc(s.text)}">${esc(s.text)}</span>
      <span class="step-actions">
        <button class="icon-btn" onclick="event.stopPropagation();moveStep(${s.id},-1)" title="Subir">↑</button>
        <button class="icon-btn" onclick="event.stopPropagation();moveStep(${s.id},1)"  title="Descer">↓</button>
        <button class="icon-btn red" onclick="event.stopPropagation();deleteStep(${s.id})" title="Excluir">✕</button>
      </span>
    </div>
  `).join('');
}

function renderCanvas() {
  const canvas = document.getElementById('canvas');
  if (!steps.length) {
    canvas.innerHTML = `
      <div class="empty-state">
        <div class="empty-icon">📋</div>
        <p>Adicione passos na barra superior<br>para construir seu fluxograma</p>
      </div>`;
    return;
  }

  let html = '<div class="flow-col">';
  steps.forEach((s, i) => {
    const nc = nodeClass(s.type);
    const lbl = typeLabel(s.type);
    const isEditing = editingId === s.id;
    html += `
      <div class="flow-node">
        <div class="node-box ${nc} ${selectedId===s.id?'selected':''}" onclick="selectStep(${s.id})">
          ${lbl ? `<div class="node-type-badge">${lbl}</div>` : ''}
          ${isEditing
            ? `<input class="inline-edit" id="edit-${s.id}" value="${esc(s.text)}"
                onblur="finishEdit(${s.id})"
                onkeydown="if(event.key==='Enter'||event.key==='Escape')this.blur()"
                onclick="event.stopPropagation()" />`
            : esc(s.text)
          }
        </div>
        <div class="node-actions">
          <button class="node-act-btn" onclick="startEdit(${s.id},event)" title="Editar">✏️</button>
          <button class="node-act-btn del" onclick="event.stopPropagation();deleteStep(${s.id})" title="Excluir">🗑</button>
        </div>
      </div>
      ${i < steps.length-1 ? '<div class="arrow"><div class="arrow-line"></div><div class="arrow-head"></div></div>' : ''}
    `;
  });
  html += '</div>';
  canvas.innerHTML = html;
}

render();
</script>
</body>
</html>
"""

components.html(html, height=800, scrolling=False)
