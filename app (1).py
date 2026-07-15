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
  background: #f1f4f9; height: 100vh;
  display: flex; flex-direction: column; overflow: hidden;
}

/* TOP BAR */
.top-bar {
  background: #fff; border-bottom: 1px solid #e2e8f0;
  padding: 10px 16px; display: flex; align-items: center;
  gap: 10px; flex-wrap: wrap; flex-shrink: 0; z-index: 100;
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

/* MAIN */
.main { display: flex; flex: 1; overflow: hidden; }

/* SIDEBAR */
.sidebar {
  width: 220px; background: #fff; border-right: 1px solid #e2e8f0;
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
.step-badge { color: #fff; border-radius: 4px; padding: 1px 5px; font-size: 10px; font-weight: 700; flex-shrink: 0; }
.badge-process  { background: #667eea; }
.badge-decision { background: #d69e2e; }
.badge-start    { background: #3182ce; }
.badge-end      { background: #38a169; }
.step-label { flex: 1; white-space: nowrap; overflow: hidden; text-overflow: ellipsis; }
.icon-btn { background: none; border: none; cursor: pointer; padding: 2px 4px; border-radius: 4px; color: #a0aec0; font-size: 13px; }
.icon-btn:hover { background: #e2e8f0; color: #2d3748; }
.icon-btn.red:hover { background: #fed7d7; color: #e53e3e; }
.branch-children { margin-left: 16px; border-left: 2px solid #e2e8f0; padding-left: 8px; margin-top: 4px; }

/* CANVAS */
.canvas-wrap { flex: 1; overflow: auto; padding: 40px; }

/* FLOW: horizontal main chain */
.flow-row { display: inline-flex; align-items: flex-start; }

/* Each block = node + optional decision tower below */
.flow-block { display: flex; flex-direction: column; align-items: center; }

/* node wrapper */
.flow-node { position: relative; display: flex; flex-direction: column; align-items: center; }

/* Arrow horizontal */
.arrow-h { display: flex; align-items: center; height: 48px; }
.arrow-h-line { height: 2px; width: 40px; background: #a0aec0; }
.arrow-h-head { width: 0; height: 0; border-top: 6px solid transparent; border-bottom: 6px solid transparent; border-left: 8px solid #a0aec0; }

/* Arrow vertical (down from decision) */
.arrow-v { display: flex; flex-direction: column; align-items: center; width: 2px; }
.arrow-v-line { width: 2px; height: 24px; background: #a0aec0; }
.arrow-v-head { width: 0; height: 0; border-left: 6px solid transparent; border-right: 6px solid transparent; border-top: 8px solid #a0aec0; }

/* NODES */
.node-box {
  background: #fff; border: 2px solid #667eea; border-radius: 10px;
  padding: 10px 18px; min-width: 130px; max-width: 200px;
  text-align: center; font-size: 13px; font-weight: 500; color: #2d3748;
  cursor: pointer; transition: all .15s; word-break: break-word; line-height: 1.4;
}
.node-box:hover { box-shadow: 0 2px 12px rgba(102,126,234,.25); }
.node-box.selected { border-color: #5a67d8; box-shadow: 0 0 0 3px rgba(102,126,234,.3); }
.node-box.start-box { background: #ebf8ff; border-color: #3182ce; border-radius: 999px; color: #1a365d; padding: 10px 24px; }
.node-box.end-box   { background: #f0fff4; border-color: #38a169; border-radius: 999px; color: #1c4532; padding: 10px 24px; }

/* DIAMOND via SVG canvas */
.diamond-wrap { position: relative; display: flex; align-items: center; justify-content: center; }
.diamond-wrap svg { display: block; }
.diamond-label {
  position: absolute; text-align: center; font-size: 12px; font-weight: 600;
  color: #744210; pointer-events: none; max-width: 100px;
  line-height: 1.3; word-break: break-word;
}

.node-type-badge { font-size: 9px; font-weight: 700; text-transform: uppercase; letter-spacing: .06em; color: #718096; margin-bottom: 3px; }
.start-box .node-type-badge { color: #2b6cb0; }
.end-box .node-type-badge   { color: #276749; }

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

/* DECISION LAYOUT */
/*
        [node before]
             |
          [diamond]
         /    |    \
       SIM   NAO  TALVEZ   (labels on branches)
        |     |     |
      [node][node][node]
*/
.decision-section {
  display: flex; flex-direction: column; align-items: center;
}
.decision-branches-row {
  display: flex; align-items: flex-start; position: relative;
}
.decision-branch-col {
  display: flex; flex-direction: column; align-items: center;
  padding: 0 12px;
}
.branch-label-pill {
  font-size: 11px; font-weight: 700; color: #744210;
  background: #fefcbf; border: 1px solid #d69e2e;
  border-radius: 999px; padding: 2px 10px; cursor: pointer;
  white-space: nowrap; transition: all .15s; margin-bottom: 4px;
}
.branch-label-pill:hover { background: #fef08a; }
.branch-label-edit-inp {
  font-size: 11px; font-weight: 700; border: 1px solid #d69e2e;
  border-radius: 999px; padding: 2px 10px; outline: none; color: #744210;
  background: #fefcbf; font-family: inherit; min-width: 50px; text-align: center;
}
.branch-v-line { width: 2px; background: #a0aec0; }
.add-branch-node-btn {
  width: 28px; height: 28px; border-radius: 50%;
  border: 1.5px dashed #a0aec0; background: #fff; cursor: pointer;
  font-size: 16px; color: #a0aec0; display: flex; align-items: center; justify-content: center;
  transition: all .15s; flex-shrink: 0;
}
.add-branch-node-btn:hover { border-color: #667eea; color: #667eea; background: #ebf4ff; }
.add-branch-btn-row {
  margin-top: 12px; display: flex; gap: 8px; justify-content: center;
}
.add-branch-pill {
  background: #fff; border: 1px dashed #a0aec0; border-radius: 999px;
  padding: 4px 14px; font-size: 12px; color: #718096; cursor: pointer; transition: all .15s;
}
.add-branch-pill:hover { border-color: #667eea; color: #667eea; background: #ebf4ff; }

/* horizontal connector line across branches */
.branch-h-connector {
  height: 2px; background: #a0aec0; position: absolute; top: 0; z-index: 0;
}

.empty-state { text-align: center; padding: 80px 40px; color: #a0aec0; }
.empty-icon { font-size: 48px; margin-bottom: 16px; }
.empty-state p { font-size: 14px; line-height: 1.8; }

/* MODAL */
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
  font-size: 14px; outline: none; margin-bottom: 6px; font-family: inherit;
}
.modal input:focus { border-color: #667eea; }
.modal-type-row { display: flex; gap: 6px; margin-bottom: 14px; flex-wrap: wrap; }
.modal-type-btn { padding: 4px 10px; border-radius: 6px; font-size: 12px; font-weight: 500; cursor: pointer; border: 1px solid #e2e8f0; background: #fff; color: #4a5568; }
.modal-type-btn.active { background: #667eea; color: #fff; border-color: #667eea; }
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

<!-- MODAL -->
<div class="modal-overlay" id="modal" style="display:none">
  <div class="modal">
    <h3 id="modal-title">Adicionar passo</h3>
    <input type="text" id="modal-input" placeholder="Nome do passo..." maxlength="80" />
    <div class="modal-type-row">
      <span style="font-size:11px;color:#718096;align-self:center">Tipo:</span>
      <button class="modal-type-btn active" id="mt-process"  onclick="setModalType('process')">Processo</button>
      <button class="modal-type-btn"        id="mt-decision" onclick="setModalType('decision')">Decisão</button>
      <button class="modal-type-btn"        id="mt-start"    onclick="setModalType('start')">Início</button>
      <button class="modal-type-btn"        id="mt-end"      onclick="setModalType('end')">Fim</button>
    </div>
    <div class="modal-actions">
      <button class="btn btn-secondary btn-sm" onclick="closeModal()">Cancelar</button>
      <button class="btn btn-primary btn-sm"   onclick="confirmModal()">Adicionar</button>
    </div>
  </div>
</div>

<script>
let root = [];
let selectedId = null;
let currentType = 'process';
let modalType = 'process';
let editingId = null;
let editingBranch = null; // {nodeId, branchId}
let modalCtx = null;
let _id = 1;
function uid() { return _id++; }

// ── helpers ──────────────────────────────────────────────────────────────────
function esc(s){ return String(s).replace(/&/g,'&amp;').replace(/</g,'&lt;').replace(/>/g,'&gt;').replace(/"/g,'&quot;'); }
function makeNode(text, type){
  const n = { id: uid(), text, type, branches: [] };
  if(type === 'decision') n.branches = [makeBranch('Sim'), makeBranch('Não')];
  return n;
}
function makeBranch(label){ return { id: uid(), label, nodes:[] }; }

function findNode(list, id){
  for(const n of list){
    if(n.id===id) return n;
    for(const b of n.branches){ const f=findNode(b.nodes,id); if(f) return f; }
  }
}
function deleteFromList(list, id){
  const i=list.findIndex(n=>n.id===id);
  if(i!==-1){ list.splice(i,1); return true; }
  for(const n of list){ for(const b of n.branches){ if(deleteFromList(b.nodes,id)) return true; } }
}

// ── type selector ─────────────────────────────────────────────────────────────
function setType(t){
  currentType=t;
  ['process','decision','start','end'].forEach(x=>document.getElementById('t-'+x).classList.toggle('active',x===t));
}
document.getElementById('stepInput').addEventListener('keydown',e=>{ if(e.key==='Enter') addRootStep(); });

// ── modal ─────────────────────────────────────────────────────────────────────
function setModalType(t){
  modalType=t;
  ['process','decision','start','end'].forEach(x=>document.getElementById('mt-'+x).classList.toggle('active',x===t));
}
function openModal(ctx,title){
  modalCtx=ctx; modalType='process';
  document.getElementById('modal-title').textContent=title||'Adicionar passo';
  document.getElementById('modal-input').value='';
  ['process','decision','start','end'].forEach(x=>document.getElementById('mt-'+x).classList.toggle('active',x==='process'));
  document.getElementById('modal').style.display='flex';
  setTimeout(()=>document.getElementById('modal-input').focus(),30);
}
function closeModal(){ document.getElementById('modal').style.display='none'; modalCtx=null; }
function confirmModal(){
  const text=document.getElementById('modal-input').value.trim();
  if(!text||!modalCtx) return;
  const node=findNode(root,modalCtx.nodeId);
  if(node){
    const br=node.branches.find(b=>b.id===modalCtx.branchId);
    if(br) br.nodes.push(makeNode(text,modalType));
  }
  closeModal(); render();
}
document.getElementById('modal-input').addEventListener('keydown',e=>{ if(e.key==='Enter') confirmModal(); if(e.key==='Escape') closeModal(); });
document.getElementById('modal').addEventListener('click',e=>{ if(e.target===document.getElementById('modal')) closeModal(); });

// ── actions ───────────────────────────────────────────────────────────────────
function addRootStep(){
  const inp=document.getElementById('stepInput');
  const t=inp.value.trim(); if(!t) return;
  root.push(makeNode(t,currentType)); inp.value=''; inp.focus(); render();
}
function deleteNode(id){ deleteFromList(root,id); if(selectedId===id) selectedId=null; render(); }
function addBranch(nodeId){
  const n=findNode(root,nodeId); if(!n) return;
  n.branches.push(makeBranch('Opção '+(n.branches.length+1))); render();
}
function deleteBranch(nodeId,branchId){
  const n=findNode(root,nodeId); if(!n) return;
  if(n.branches.length<=1) return;
  n.branches=n.branches.filter(b=>b.id!==branchId); render();
}
function startEdit(id,e){ e.stopPropagation(); editingId=id; render(); setTimeout(()=>{ const i=document.getElementById('edit-'+id); if(i){i.focus();i.select();} },20); }
function finishEdit(id){ const i=document.getElementById('edit-'+id); if(i){ const v=i.value.trim(); if(v){ const n=findNode(root,id); if(n) n.text=v; } } editingId=null; render(); }
function startEditBranch(nid,bid,e){ e.stopPropagation(); editingBranch={nodeId:nid,branchId:bid}; render(); setTimeout(()=>{ const i=document.getElementById('bedit-'+bid); if(i){i.focus();i.select();} },20); }
function finishEditBranch(nid,bid){ const i=document.getElementById('bedit-'+bid); if(i){ const v=i.value.trim(); if(v){ const n=findNode(root,nid); if(n){ const b=n.branches.find(b=>b.id===bid); if(b) b.label=v; } } } editingBranch=null; render(); }
function clearAll(){ if(!root.length) return; if(confirm('Limpar tudo?')){ root=[]; selectedId=null; render(); } }

// ── RENDER ────────────────────────────────────────────────────────────────────
function render(){ renderSidebar(); renderCanvas(); }

function renderSidebar(){
  const el=document.getElementById('stepList');
  if(!root.length){ el.innerHTML='<p style="font-size:12px;color:#a0aec0;text-align:center;padding:16px 0">Nenhum passo ainda</p>'; return; }
  el.innerHTML=root.map(n=>sbNode(n)).join('');
}
function sbNode(n){
  const bc='badge-'+n.type;
  const lbl=n.type==='process'?'P':n.type==='start'?'I':n.type==='end'?'F':'D';
  let h=`<div class="step-item ${selectedId===n.id?'selected':''}" onclick="selectedId=${n.id};render()">
    <span class="step-badge ${bc}">${lbl}</span>
    <span class="step-label" title="${esc(n.text)}">${esc(n.text)}</span>
    <button class="icon-btn red" onclick="event.stopPropagation();deleteNode(${n.id})">✕</button>
  </div>`;
  if(n.branches.length){
    h+='<div class="branch-children">';
    for(const br of n.branches){
      h+=`<div style="font-size:11px;color:#d69e2e;font-weight:700;margin:4px 0 2px">↳ ${esc(br.label)}</div>`;
      for(const c of br.nodes) h+=sbNode(c);
    }
    h+='</div>';
  }
  return h;
}

function renderCanvas(){
  const canvas=document.getElementById('canvas');
  if(!root.length){
    canvas.innerHTML=`<div class="empty-state"><div class="empty-icon">🔀</div><p>Adicione passos na barra superior<br>para construir seu fluxograma</p></div>`;
    return;
  }
  // render horizontal chain with vertical decision branches
  canvas.innerHTML = buildChain(root);
}

// build a horizontal flow-row from a list of nodes
function buildChain(nodes){
  let h = `<div class="flow-row">`;
  nodes.forEach((n,i)=>{
    h += buildBlock(n);
    if(i < nodes.length-1) h += arrowH();
  });
  h += `</div>`;
  return h;
}

function arrowH(){
  return `<div class="arrow-h" style="align-self:center"><div class="arrow-h-line"></div><div class="arrow-h-head"></div></div>`;
}
function arrowVDown(h){
  return `<div style="display:flex;flex-direction:column;align-items:center;"><div style="width:2px;height:${h}px;background:#a0aec0"></div><div style="width:0;height:0;border-left:6px solid transparent;border-right:6px solid transparent;border-top:8px solid #a0aec0"></div></div>`;
}

// one node block (node + optional decision branches below)
function buildBlock(node){
  let h = `<div class="flow-block">`;
  h += buildNodeBox(node);
  if(node.type==='decision' && node.branches.length){
    h += buildDecisionBranches(node);
  }
  h += `</div>`;
  return h;
}

function buildNodeBox(node){
  const isEditing = editingId===node.id;
  const isSel = selectedId===node.id;

  if(node.type==='decision'){
    // Diamond via SVG
    const W=160, H=90;
    const pts=`${W/2},4 ${W-4},${H/2} ${W/2},${H-4} 4,${H/2}`;
    const labelId='dlbl-'+node.id;
    let inner = isEditing
      ? `<foreignObject x="30" y="25" width="${W-60}" height="${H-50}"><div xmlns="http://www.w3.org/1999/xhtml"><input class="inline-edit" id="edit-${node.id}" value="${esc(node.text)}" onblur="finishEdit(${node.id})" onkeydown="if(event.key==='Enter'||event.key==='Escape')this.blur()" style="width:100%;font-size:12px" /></div></foreignObject>`
      : `<text x="${W/2}" y="${H/2+1}" text-anchor="middle" dominant-baseline="middle" font-size="12" font-weight="600" fill="#744210" style="pointer-events:none">${esc(node.text)}</text>`;

    return `<div class="flow-node" style="align-items:center">
      <svg width="${W}" height="${H}" style="cursor:pointer;overflow:visible" onclick="selectedId=${node.id};render()">
        <polygon points="${pts}" fill="#fefcbf" stroke="${isSel?'#5a67d8':'#d69e2e'}" stroke-width="${isSel?'3':'2'}" />
        ${inner}
      </svg>
      <div class="node-actions">
        <button class="node-act-btn" onclick="startEdit(${node.id},event)" title="Editar">✏️</button>
        <button class="node-act-btn del" onclick="event.stopPropagation();deleteNode(${node.id})" title="Excluir">🗑</button>
      </div>
    </div>`;
  }

  // regular box
  const nc = node.type==='start'?'start-box':node.type==='end'?'end-box':'';
  const lbl = node.type==='start'?'Início':node.type==='end'?'Fim':'';
  const inner = isEditing
    ? `<input class="inline-edit" id="edit-${node.id}" value="${esc(node.text)}" onblur="finishEdit(${node.id})" onkeydown="if(event.key==='Enter'||event.key==='Escape')this.blur()" onclick="event.stopPropagation()" />`
    : esc(node.text);

  return `<div class="flow-node" style="align-self:center">
    <div class="node-box ${nc} ${isSel?'selected':''}" onclick="selectedId=${node.id};render()">
      ${lbl?`<div class="node-type-badge">${lbl}</div>`:''}${inner}
    </div>
    <div class="node-actions">
      <button class="node-act-btn" onclick="startEdit(${node.id},event)" title="Editar">✏️</button>
      <button class="node-act-btn del" onclick="event.stopPropagation();deleteNode(${node.id})" title="Excluir">🗑</button>
    </div>
  </div>`;
}

// Decision branches: first branch goes RIGHT (horizontal), rest go DOWN (vertical)
function buildDecisionBranches(node){
  const branches = node.branches;
  let h = `<div style="display:flex;flex-direction:column;align-items:center;width:100%">`;

  // ── RIGHT branch (index 0 = "Sim") ────────────────────────────────────────
  // The horizontal arrow from diamond goes right into the first branch
  // This is rendered naturally by the parent flow-row's arrowH before next node
  // Instead, we render it as a special overlay row to the right of the diamond
  // We use a separate container that sits to the right

  // ── BOTTOM branches ────────────────────────────────────────────────────────
  // All branches rendered downward in columns side by side
  // With a horizontal line at top connecting them

  const colCount = branches.length;

  h += `<div style="display:flex;flex-direction:column;align-items:center;margin-top:0">`;

  // Top: vertical line down from diamond center
  h += `<div style="width:2px;height:20px;background:#a0aec0"></div>`;

  // horizontal bar connecting all branch tops
  // We'll render each branch col and use flexbox
  h += `<div style="display:flex;align-items:flex-start;position:relative">`;

  branches.forEach((br, bi)=>{
    const isEditingBr = editingBranch && editingBranch.nodeId===node.id && editingBranch.branchId===br.id;
    const isFirst = bi===0;
    const isLast  = bi===branches.length-1;

    let labelHtml = isEditingBr
      ? `<input class="branch-label-edit-inp" id="bedit-${br.id}" value="${esc(br.label)}" onblur="finishEditBranch(${node.id},${br.id})" onkeydown="if(event.key==='Enter'||event.key==='Escape')this.blur()" style="width:${Math.max(50,br.label.length*9)}px" />`
      : `<span class="branch-label-pill" onclick="startEditBranch(${node.id},${br.id},event)" title="Clique para editar">${esc(br.label)}</span>`;

    // top connector piece: left half-line, vertical tick, right half-line
    const lineLeft  = isFirst ? `<div style="width:50%;height:2px;background:transparent"></div>` : `<div style="flex:1;height:2px;background:#a0aec0"></div>`;
    const lineRight = isLast  ? `<div style="width:50%;height:2px;background:transparent"></div>` : `<div style="flex:1;height:2px;background:#a0aec0"></div>`;

    h += `<div class="decision-branch-col" style="min-width:140px">`;
    // horizontal connector row
    h += `<div style="display:flex;align-items:center;width:100%;height:2px">${lineLeft}<div style="width:2px;height:12px;background:#a0aec0;flex-shrink:0;margin-top:12px"></div>${lineRight}</div>`;
    // short vertical line down
    h += `<div style="width:2px;height:10px;background:#a0aec0;margin:0 auto"></div>`;
    // label
    h += `<div style="display:flex;justify-content:center;margin-bottom:6px">${labelHtml}</div>`;
    // arrow down
    h += `<div style="display:flex;flex-direction:column;align-items:center;margin-bottom:4px"><div style="width:2px;height:16px;background:#a0aec0"></div><div style="width:0;height:0;border-left:6px solid transparent;border-right:6px solid transparent;border-top:8px solid #a0aec0"></div></div>`;
    // branch nodes (vertical chain within this column)
    if(br.nodes.length){
      br.nodes.forEach((child,ci)=>{
        h += buildBlock(child);
        if(ci < br.nodes.length-1){
          h += `<div style="display:flex;flex-direction:column;align-items:center"><div style="width:2px;height:20px;background:#a0aec0"></div><div style="width:0;height:0;border-left:6px solid transparent;border-right:6px solid transparent;border-top:8px solid #a0aec0"></div></div>`;
        }
      });
      h += `<div style="width:2px;height:16px;background:#a0aec0;margin:4px auto 0"></div>`;
    }
    // add node button
    h += `<div style="display:flex;justify-content:center;margin:4px 0">
      <button class="add-branch-node-btn" onclick="openModal({target:'branch',nodeId:${node.id},branchId:${br.id}},'Adicionar em &quot;${esc(br.label)}&quot;')" title="Adicionar passo">+</button>
    </div>`;
    // delete branch (if more than 1)
    if(branches.length>1){
      h+=`<div style="display:flex;justify-content:center"><button class="icon-btn red" style="font-size:11px" onclick="deleteBranch(${node.id},${br.id})" title="Remover ramificação">✕ remover</button></div>`;
    }
    h += `</div>`; // end col
  });

  h += `</div>`; // end branches flex row

  // Add branch button
  h += `<div class="add-branch-btn-row"><button class="add-branch-pill" onclick="addBranch(${node.id})">+ Nova ramificação</button></div>`;
  h += `</div></div>`; // end decision section + flow-block inner
  return h;
}

render();
</script>
</body>
</html>
"""

components.html(html, height=820, scrolling=False)
