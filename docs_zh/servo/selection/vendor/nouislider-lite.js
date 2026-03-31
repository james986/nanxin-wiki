(function(){
  function create(el, opts){
    const root = document.createElement('div'); root.className='noui'; el.innerHTML=''; el.appendChild(root);
    const connect = document.createElement('div'); connect.className='noui-connect'; root.appendChild(connect);
    const h0 = document.createElement('div'); h0.className='noui-handle'; root.appendChild(h0);
    const h1 = document.createElement('div'); h1.className='noui-handle'; root.appendChild(h1);
    const min=opts.range.min, max=opts.range.max, step=opts.step||1;
    let v0=opts.start[0], v1=opts.start[1];
    const width=()=>root.clientWidth; const toPx=v=> (v-min)/(max-min)*width();
    const clamp=v=> Math.min(max, Math.max(min, Math.round(v/step)*step));
    function layout(){ const l=toPx(v0), r=toPx(v1); h0.style.left=(l-8)+'px'; h1.style.left=(r-8)+'px'; connect.style.left=l+'px'; connect.style.width=(r-l)+'px'; }
    function val(){ return [v0,v1]; }
    const listeners={ update:[], change:[] };
    function emit(type){ listeners[type].forEach(fn=>fn(val().map(x=>x.toFixed(2)))); }
    function onDrag(handle, setV){ let startX, startV; const mm=e=>{ const dx=e.clientX-startX; const dv=dx/width()*(max-min); setV(clamp(startV+dv)); layout(); emit('update'); }; const mu=()=>{ window.removeEventListener('mousemove',mm); window.removeEventListener('mouseup',mu); emit('change'); }; return e=>{ startX=e.clientX; startV=(handle===h0?v0:v1); window.addEventListener('mousemove',mm); window.addEventListener('mouseup',mu); e.preventDefault(); } }
    h0.addEventListener('mousedown', onDrag(h0, v=>{ v0=Math.min(v,v1); }));
    h1.addEventListener('mousedown', onDrag(h1, v=>{ v1=Math.max(v0,v); }));
    window.addEventListener('resize', layout);
    layout();
    const api={
      get:()=>[v0.toFixed(2), v1.toFixed(2)],
      on:(evt,fn)=>{ listeners[evt].push(fn); },
      destroy:()=>{ window.removeEventListener('resize', layout); },
    };
    el.noUiSlider=api; return api;
  }
  window.noUiSliderLite={ create };
  window.noUiSlider = { create: (el, opts)=> noUiSliderLite.create(el, opts) };
})();
