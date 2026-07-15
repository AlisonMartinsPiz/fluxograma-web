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

html = r"""
<!DOCTYPE html>
<html lang="pt-BR">
<head>
<meta charset="UTF-8">
<style>
* { box-sizing: border-box; margin: 0; padding: 0; }
body {
  font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif;
  background: #f1f4f9;
  height: 100vh;
  display: flex;
  flex-direction: column;
  overflow: hidden;
}

/* ── TOP BAR ── */
.top-bar {
  background: #fff;
  border-bottom: 1px solid #e2e8f0;
  padding: 10px 16px;
  display: flex;
  align-items: center;
  gap: 10px;
  flex-wrap: wrap;
  flex-shrink: 0;
  z-index: 100;
}
.top-bar h1 { font-size: 15px; font-weight: 700; color: #1a202c; white-space: nowrap; }
.toolbar-divider { width: 1px; height: 26px; background: #e2e8f0; flex-shrink: 0; }
.type-selector { display: flex; gap: 4px; align-items: center; }
.type-lbl { font-size: 11px; color: #718096; font-weight: 600; white-space: nowrap; }
.type-btn {
  padding: 5px 11px; border-radius: 6px; font-size: 12px; font-weight: 500;
  cursor: pointer; border: 1px solid #e2e8f0; background: #fff; color: #4a5568; transition: all .15s;
}
.type-btn.active { background: #667eea; color: #fff; border-color: #667eea; }
.type-btn:hover:not(.active) { background: #f7fafc; }
.input-wrap { display: flex; flex: 1; min-width: 200px; gap: 6px; }
.input-wrap input {
  flex: 1; padding: 7px 12px; border: 1px solid #cbd5e0; border-radius: 8px;
  font-size: 13px; outline: none; transition: border-color .2s;
}
.input-wrap input:focus { border-color: #667eea; }
.btn { padding: 7px 14px; border-radius: 8px; font-size: 13px; font-weight: 500; cursor: pointer; border: none; transition: all .15s; white-space: nowrap; }
.btn-primary { background: #667eea; color: #fff; }
.btn-primary:hover { background: #5a67d8; }
.btn-secondary { background: #fff; color: #4a5568; border: 1px solid #e2e8f0; }
.btn-secondary:hover { background: #f7fafc; }
.btn-sm { padding: 4px 10px; font-size: 12px; border-radius: 6px; }

/* ── MAIN ── */
.main { display: flex; flex: 1; overflow: hidden; }

/* ── SIDEBAR ── */
.sidebar {
  width: 230px; background: #fff; border-right: 1px solid #e2e8f0;
  padding: 14px; overflow-y: auto; flex-shrink: 0;
}
.sidebar-title { font-size: 11px; font-weight: 700; color: #718096; text-transform: uppercase; letter-spacing: .05em; margin-bottom: 10px; }
.step-item {
  background: #f7fafc; border: 1px solid #e2e8f0; border-radius: 8px;
  padding: 7px 8px; margin-bottom: 5px; font-size: 12px; color: #2d3748;
  cursor: pointer; display: flex; align-items: center; gap: 5px; transition: background .15s;
}
.step-item:hover { background: #edf2f7; }
.step-item.selected { border-color: #667eea; background: #ebf4ff; }
.step-badge {
  color: #fff; border-radius: 4px; padding: 1px 5px;
  font-size: 10px; font-weight: 700; flex-shrink: 0; white-space: nowrap;
}
.badge-process  { background: #667eea; }
.badge-decision { background: #d69e2e; }
.badge-start    { background: #3182ce; }
.badge-end      { background: #38a169; }
.step-label { flex: 1; white-space: nowrap; overflow: hidden; text-overflow: ellipsis; }
.step-actions { display: flex; gap: 2px; }
.icon-btn { background: none; border: none; cursor: pointer; padding: 2px 4px; border-radius: 4px; color: #a0aec0; font-size: 13px; }
.icon-btn:hover { background: #e2e8f0; color: #2d3748; }
.icon-btn.red:hover { background: #fed7d7; color: #e53e3e; }

/* branch children in sidebar */
.branch-children { margin-left: 18px; border-left: 2px solid #e2e8f0; padding-left: 8px; margin-top: 4px; }

/* ── CANVAS ── */
.canvas-wrap { flex: 1; overflow: auto; padding: 40px; }
#canvas { display: inline-flex; align-items: flex-start; min-width: max-content; }

/* ── NODE ── */
.flow-row { display: flex; align-items: center; }
.flow-node { position: relative; display: flex; flex-direction: column; align-items: center; }

.node-box {
  background: #fff; border: 2px solid #667eea; border-radius: 10px;
  padding: 10px 18px; min-width: 140px; max-width: 200px;
  text-align: center; font-size: 13px; font-weight: 500; color: #2d3748;
  cursor: pointer; transition: all .15s; word-break: break-word; line-height: 1.4; position: relative;
}
.node-box:hover { box-shadow: 0 2px 12px rgba(102,126,234,.25); }
.node-box.selected { border-color: #5a67d8; box-shadow: 0 0 0 3px rgba(102,126,234,.3); }
.node-box.start-box { background: #ebf8ff; border-color: #3182ce; border-radius: 999px; color: #1a365d; padding: 10px 24px; }
.node-box.end-box   { background: #f0fff4; border-color: #38a169; border-radius: 999px; color: #1c4532; padding: 10px 24px; }
.node-box.decision-box {
  background: #fefcbf; border-color: #d69e2e; color: #744210;
  clip-path: polygon(50% 0%, 100% 50%, 50% 100%, 0% 50%);
  min-width: 160px; min-height: 80px; padding: 22px 36px; border-radius: 4px;
}

.node-type-badge { font-size: 9px; font-weight: 700; text-transform: uppercase; letter-spacing: .06em; color: #718096; margin-bottom: 3px; }
.start-box .node-type-badge { color: #2b6cb0; }
.end-box .node-type-badge   { color: #276749; }
.decision-box .node-type-badge { color: #975a16; }

.node-actions {
  display: none; position: absolute; top: -12px; right: -12px;
  flex-direction: row; gap: 3px; z-index: 20;
}
.flow-node:hover .node-actions { display: flex; }
.node-act-btn {
  width: 22px; height: 22px; border-radius: 50%;
  border: 1px solid #e2e8f0; background: #fff; cursor: pointer;
  font-size: 11px; display: flex; align-items: center; justify-content: center;
  box-shadow: 0 1px 4px rgba(0,0,0,.12); transition: all .15s;
}
.node-act-btn:hover { background: #f7fafc; }
.node-act-btn.del:hover { background: #fff5f5; border-color: #fed7d7; }

.inline-edit {
  background: none; border: none; border-bottom: 2px solid #667eea;
  font-size: 13px; font-weight: 500; color: inherit; text-align: center;
  outline: none; width: 100%; padding: 2px 0; font-family: inherit;
}

/* ── ARROWS ── */
.arrow-h { display: flex; align-items: center; width: 40px; flex-shrink: 0; }
.arrow-h-line { height: 2px; flex: 1; background: #a0aec0; }
.arrow-h-head { width: 0; height: 0; border-top: 6px solid transparent; border-bottom: 6px solid transparent; border-left: 8px solid #a0aec0; }

/* ── DECISION BRANCHES ── */
.decision-group { display: flex; flex-direction: column; align-items: flex-start; }

.branch-row { display: flex; align-items: flex-start; }

.branch-connector {
  display: flex; flex-direction: column; align-items: center;
  margin-right: 0; flex-shrink: 0;
}
.branch-vert-line { width: 2px; background: #a0aec0; }
.branch-horiz { display: flex; align-items: center; height: 2px; }
.branch-horiz-line { height: 2px; width: 28px; background: #a0aec0; }

.branch-label-wrap { display: flex; align-items: center; gap: 0; }
.branch-label {
  font-size: 11px; font-weight: 600; color: #667eea;
  background: #ebf4ff; border: 1px solid #c3dafe;
  border-radius: 999px; padding: 2px 8px; white-space: nowrap;
  cursor: pointer;
}
.branch-label:hover { background: #c3dafe; }

.branch-label-edit {
  font-size: 11px; font-weight: 600;
  border: 1px solid #667eea; border-radius: 999px;
  padding: 2px 8px; outline: none; color: #2b6cb0;
  background: #ebf4ff; min-width: 50px; font-family: inherit;
}

.branch-chain { display: flex; align-items: center; }

.add-branch-btn {
  background: #fff; border: 1px dashed #a0aec0; border-radius: 8px;
  padding: 6px 12px; font-size: 12px; color: #718096; cursor: pointer;
  white-space: nowrap; transition: all .15s; margin-top: 4px;
}
.add-branch-btn:hover { border-color: #667eea; color: #667eea; background: #ebf4ff; }

.add-to-branch-btn {
  width: 26px; height: 26px; border-radius: 50%;
  border: 1.5px dashed #a0aec0; background: #fff; cursor: pointer;
  font-size: 14px; color: #a0aec0; display: flex; align-items: center; justify-content: center;
  flex-shrink: 0; transition: all .15s;
}
.add-to-branch-btn:hover { border-color: #667eea; color: #667eea; background: #ebf4ff; }

.empty-state { text-align: center; padding: 80px 40px; color: #a0aec0; }
.empty-icon { font-size: 48px; margin-bottom: 16px; }
.empty-state p { font-size: 14px; line-height: 1.8; }

/* ── MODAL ── */
.modal-overlay {
  position: fixed; inset: 0; background: rgba(0,0,0,.35);
  display: flex; align-items: center; justify-content: center; z-index: 999;
}
.modal {
  background: #fff; border-radius: 14px; padding: 24px; width: 360px;
  box-shadow: 0 8px 32px rgba(0,0,0,.18);
}
.modal h3 { font-size: 15px; font-weight: 700; color: #1a202c; margin-bottom: 16px; }
.modal input {
  width: 100%; padding: 8px 12px; border: 1px solid #cbd5e0; border-radius: 8px;
  font-size: 14px; outline: none; margin-bottom: 14px; font-family: inherit;
}
.modal input:focus { border-color: #667eea; }
.modal-actions { display: flex; gap: 8px; justify-content: flex-end; }
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
    <input type="text" id="stepInput" placeholder="Nome do passo — Enter para adicionar..." maxlength="80" />
    <button class="btn btn-primary" onclick="addRootStep()">+ Adicionar</button>
  </div>

  <div class="toolbar-divider"></div>
  <button class="btn btn-secondary" onclick="clearAll()">🗑 Limpar</button>
</div>

<div class="main">
  <div class="sidebar">
    <div class="sidebar-title">Estrutura</div>
    <div id="stepList"></div>
  </div>
  <div class="canvas-wrap">
    <div id="canvas"></div>
  </div>
</div>

<!-- Modal para adicionar nó em branch -->
<div class="modal-overlay" id="modal" style="display:none">
  <div class="modal">
    <h3 id="modal-title">Adicionar passo</h3>
    <input type="text" id="modal-input" placeholder="Nome do passo..." maxlength="80" />
    <div class="modal-actions">
      <button class="btn btn-secondary btn-sm" onclick="closeModal()">Cancelar</button>
      <button class="btn btn-primary btn-sm" onclick="confirmModal()">Adicionar</button>
    </div>
  </div>
</div>

<script>
// ─── DATA MODEL ───────────────────────────────────────────────────────────────
// Each node: { id, text, type, branches: [{id, label, nodes:[...]}] }
// root is an array of nodes rendered left-to-right

let root = [];
let selectedId = null;
let currentType = 'process';
let editingId = null;
let editingBranchId = null; // {nodeId, branchId}
let modalCtx = null; // {target: 'root'|'branch', nodeId, branchId}

let _idCounter = 1;
function uid() { return _idCounter++; }

// ─── TYPE SELECTOR ────────────────────────────────────────────────────────────
function setType(type) {
  currentType = type;
  ['process','decision','start','end'].forEach(t =>
    document.getElementById('t-'+t).classList.toggle('active', t === type)
  );
}

document.getElementById('stepInput').addEventListener('keydown', e => {
  if (e.key === 'Enter') addRootStep();
});

// ─── ADD TO ROOT ──────────────────────────────────────────────────────────────
function addRootStep() {
  const input = document.getElementById('stepInput');
  const text = input.value.trim();
  if (!text) return;
  const node = makeNode(text, currentType);
  root.push(node);
  input.value = '';
  input.focus();
  render();
}

function makeNode(text, type) {
  return { id: uid(), text, type, branches: type === 'decision' ? [makeBranch('Sim'), makeBranch('Não')] : [] };
}

function makeBranch(label) {
  return { id: uid(), label, nodes: [] };
}

// ─── MODAL (add to branch) ────────────────────────────────────────────────────
function openModal(ctx, title) {
  modalCtx = ctx;
  document.getElementById('modal-title').textContent = title || 'Adicionar passo';
  document.getElementById('modal-input').value = '';
  document.getElementById('modal').style.display = 'flex';
  setTimeout(() => document.getElementById('modal-input').focus(), 30);
}
function closeModal() {
  document.getElementById('modal').style.display = 'none';
  modalCtx = null;
}
function confirmModal() {
  const text = document.getElementById('modal-input').value.trim();
  if (!text || !modalCtx) return;
  if (modalCtx.target === 'branch') {
    const node = findNode(root, modalCtx.nodeId);
    if (node) {
      const br = node.branches.find(b => b.id === modalCtx.branchId);
      if (br) br.nodes.push(makeNode(text, modalCtx.nodeType || 'process'));
    }
  }
  closeModal();
  render();
}
document.getElementById('modal-input').addEventListener('keydown', e => {
  if (e.key === 'Enter') confirmModal();
  if (e.key === 'Escape') closeModal();
});
document.getElementById('modal').addEventListener('click', e => {
  if (e.target === document.getElementById('modal')) closeModal();
});

// ─── FIND / DELETE ────────────────────────────────────────────────────────────
function findNode(list, id) {
  for (const n of list) {
    if (n.id === id) return n;
    for (const br of n.branches) {
      const f = findNode(br.nodes, id);
      if (f) return f;
    }
  }
  return null;
}

function deleteNodeFromList(list, id) {
  const i = list.findIndex(n => n.id === id);
  if (i !== -1) { list.splice(i, 1); return true; }
  for (const n of list) {
    for (const br of n.branches) {
      if (deleteNodeFromList(br.nodes, id)) return true;
    }
  }
  return false;
}

function deleteNode(id) {
  deleteNodeFromList(root, id);
  if (selectedId === id) selectedId = null;
  render();
}

function addBranch(nodeId) {
  const node = findNode(root, nodeId);
  if (!node) return;
  const label = 'Opção ' + (node.branches.length + 1);
  node.branches.push(makeBranch(label));
  render();
}

function deleteBranch(nodeId, branchId) {
  const node = findNode(root, nodeId);
  if (!node) return;
  node.branches = node.branches.filter(b => b.id !== branchId);
  render();
}

// ─── EDIT NODE TEXT ──────────────────────────────────────────────────────────
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
    if (val) { const n = findNode(root, id); if (n) n.text = val; }
  }
  editingId = null;
  render();
}

// ─── EDIT BRANCH LABEL ───────────────────────────────────────────────────────
function startEditBranch(nodeId, branchId, e) {
  e.stopPropagation();
  editingBranchId = { nodeId, branchId };
  render();
  setTimeout(() => {
    const inp = document.getElementById('bedit-' + branchId);
    if (inp) { inp.focus(); inp.select(); }
  }, 20);
}
function finishEditBranch(nodeId, branchId) {
  const inp = document.getElementById('bedit-' + branchId);
  if (inp) {
    const val = inp.value.trim();
    if (val) {
      const node = findNode(root, nodeId);
      if (node) { const br = node.branches.find(b => b.id === branchId); if (br) br.label = val; }
    }
  }
  editingBranchId = null;
  render();
}

function clearAll() {
  if (!root.length) return;
  if (confirm('Limpar todo o fluxograma?')) { root = []; selectedId = null; render(); }
}

function esc(str) {
  return String(str).replace(/&/g,'&amp;').replace(/</g,'&lt;').replace(/>/g,'&gt;').replace(/"/g,'&quot;');
}
function nodeBoxClass(type) {
  return type === 'start' ? 'start-box' : type === 'end' ? 'end-box' : type === 'decision' ? 'decision-box' : '';
}
function typeLabel(type) {
  return type === 'start' ? 'Início' : type === 'end' ? 'Fim' : type === 'decision' ? 'Decisão' : '';
}

// ─── RENDER ───────────────────────────────────────────────────────────────────
function render() {
  renderSidebar();
  renderCanvas();
}

// Sidebar: flat list with indentation for branches
function renderSidebar() {
  const list = document.getElementById('stepList');
  if (!root.length) {
    list.innerHTML = '<p style="font-size:12px;color:#a0aec0;text-align:center;padding:16px 0">Nenhum passo ainda</p>';
    return;
  }
  list.innerHTML = root.map(n => renderSidebarNode(n)).join('');
}

function renderSidebarNode(node) {
  const bc = 'badge-' + node.type;
  const lbl = node.type === 'process' ? 'P' : node.type === 'start' ? 'I' : node.type === 'end' ? 'F' : 'D';
  let html = `
    <div class="step-item ${selectedId===node.id?'selected':''}" onclick="selectedId=${node.id};render()">
      <span class="step-badge ${bc}">${lbl}</span>
      <span class="step-label" title="${esc(node.text)}">${esc(node.text)}</span>
      <span class="step-actions">
        <button class="icon-btn red" onclick="event.stopPropagation();deleteNode(${node.id})" title="Excluir">✕</button>
      </span>
    </div>`;
  if (node.branches.length) {
    html += '<div class="branch-children">';
    for (const br of node.branches) {
      html += `<div style="font-size:11px;color:#d69e2e;font-weight:700;margin:4px 0 2px">↳ ${esc(br.label)}</div>`;
      for (const child of br.nodes) {
        html += renderSidebarNode(child);
      }
    }
    html += '</div>';
  }
  return html;
}

// Canvas: horizontal chain
function renderCanvas() {
  const canvas = document.getElementById('canvas');
  if (!root.length) {
    canvas.innerHTML = `
      <div class="empty-state">
        <div class="empty-icon">🔀</div>
        <p>Adicione passos na barra superior<br>para construir seu fluxograma</p>
      </div>`;
    return;
  }
  canvas.innerHTML = renderChain(root, false);
}

// Render a horizontal chain of nodes
function renderChain(nodes, isSubChain) {
  if (!nodes.length) return '';
  let html = `<div class="flow-row" style="${isSubChain?'':''}">`;
  nodes.forEach((node, i) => {
    html += renderNodeBlock(node);
    if (i < nodes.length - 1) html += arrowH();
  });
  html += '</div>';
  return html;
}

function arrowH() {
  return `<div class="arrow-h"><div class="arrow-h-line"></div><div class="arrow-h-head"></div></div>`;
}

function renderNodeBlock(node) {
  const nc = nodeBoxClass(node.type);
  const lbl = typeLabel(node.type);
  const isEditing = editingId === node.id;

  let inner = '';
  if (isEditing) {
    inner = `<input class="inline-edit" id="edit-${node.id}" value="${esc(node.text)}"
      onblur="finishEdit(${node.id})"
      onkeydown="if(event.key==='Enter'||event.key==='Escape')this.blur()"
      onclick="event.stopPropagation()" />`;
  } else {
    inner = esc(node.text);
  }

  let html = `<div class="flow-node">
    <div class="node-box ${nc} ${selectedId===node.id?'selected':''}" onclick="selectedId=${node.id};render()">
      ${lbl ? `<div class="node-type-badge">${lbl}</div>` : ''}
      ${inner}
    </div>
    <div class="node-actions">
      <button class="node-act-btn" onclick="startEdit(${node.id},event)" title="Editar">✏️</button>
      <button class="node-act-btn del" onclick="event.stopPropagation();deleteNode(${node.id})" title="Excluir">🗑</button>
    </div>`;

  // Decision branches rendered below
  if (node.type === 'decision' && node.branches.length) {
    html += renderDecisionBranches(node);
  }

  html += '</div>';
  return html;
}

function renderDecisionBranches(node) {
  const totalBranches = node.branches.length;
  // We'll render branches stacked vertically, each going horizontally to the right
  let html = `<div style="display:flex;flex-direction:column;margin-top:16px;gap:12px;align-items:flex-start;">`;

  node.branches.forEach((br, bi) => {
    const isEditingBranch = editingBranchId && editingBranchId.nodeId === node.id && editingBranchId.branchId === br.id;
    let labelHtml = '';
    if (isEditingBranch) {
      labelHtml = `<input class="branch-label-edit" id="bedit-${br.id}" value="${esc(br.label)}"
        onblur="finishEditBranch(${node.id},${br.id})"
        onkeydown="if(event.key==='Enter'||event.key==='Escape')this.blur()"
        onclick="event.stopPropagation()" style="width:${Math.max(50,br.label.length*8+20)}px" />`;
    } else {
      labelHtml = `<span class="branch-label" onclick="startEditBranch(${node.id},${br.id},event)" title="Clique para editar">${esc(br.label)}</span>`;
    }

    html += `<div style="display:flex;align-items:center;gap:0;">`;
    // horiz line + label
    html += `<div style="display:flex;align-items:center;gap:6px;">
      <div style="width:28px;height:2px;background:#a0aec0;flex-shrink:0"></div>
      ${labelHtml}
      <div style="width:10px;height:2px;background:#a0aec0;flex-shrink:0"></div>
    </div>`;

    // nodes in this branch
    if (br.nodes.length) {
      html += `<div style="display:flex;align-items:center;gap:0;">`;
      br.nodes.forEach((child, ci) => {
        html += renderNodeBlock(child);
        if (ci < br.nodes.length - 1) html += arrowH();
        else html += `<div class="arrow-h"><div class="arrow-h-line"></div></div>`;
      });
      html += `</div>`;
    }

    // add node button
    html += `<button class="add-to-branch-btn" onclick="openModal({target:'branch',nodeId:${node.id},branchId:${br.id},nodeType:'process'},'Adicionar passo em &quot;${esc(br.label)}&quot;')" title="Adicionar passo nesta ramificação">+</button>`;

    // delete branch button (only if more than 1)
    if (totalBranches > 1) {
      html += `<button class="icon-btn red" style="margin-left:6px;font-size:14px" onclick="deleteBranch(${node.id},${br.id})" title="Remover ramificação">✕</button>`;
    }

    html += `</div>`; // end branch row
  });

  // add branch button
  html += `<button class="add-branch-btn" onclick="addBranch(${node.id})">+ Nova ramificação</button>`;
  html += `</div>`;
  return html;
}

render();
</script>
</body>
</html>
"""

components.html(html, height=820, scrolling=False)
