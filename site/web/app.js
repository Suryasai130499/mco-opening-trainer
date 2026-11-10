/* MCO-15 Opening Trainer - one bundle shared by every page.
 *
 * Each page is a separate document: the hub lists the openings, an opening page
 * lists its lines, and a line page is the trainer for that one line. The page
 * says in <body data-*> which it is, where the site root is, and which data
 * file to fetch, and this script does the rest. Nothing here needs a chess
 * engine: positions and legal-move lists are precomputed by data/build.py.
 */
(function(){
"use strict";

var BODY = document.body;
var PAGE = BODY.getAttribute("data-page");
var ROOT = BODY.getAttribute("data-root") || "";
var SRC  = BODY.getAttribute("data-src");

var START = "rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq - 0 1";
var FILES = "abcdefgh";
var PIECE_DIR = ROOT + "pieces/";
var PIECE_NAME = { k:"king", q:"queen", r:"rook", b:"bishop", n:"knight", p:"pawn" };

/* ---------- small helpers ---------- */
function $(id){ return document.getElementById(id); }
function el(tag, cls, text){
  var n = document.createElement(tag);
  if(cls) n.className = cls;
  if(text != null) n.textContent = text;
  return n;
}
function esc(s){
  return String(s).replace(/[&<>"]/g, function(c){
    return { "&":"&amp;", "<":"&lt;", ">":"&gt;", '"':"&quot;" }[c];
  });
}
function colorName(c){ return c === "w" ? "White" : "Black"; }

/* ---------- what the learner has finished ---------- */
var LS_LEARNED = "mco15.learned.v1", LS_THEME = "mco15.theme.v1";
function lsGet(k){ try{ return localStorage.getItem(k); }catch(e){ return null; } }
function lsSet(k,v){ try{ localStorage.setItem(k,v); }catch(e){} }

var learned = {};
(function(){
  var raw = lsGet(LS_LEARNED);
  if(!raw) return;
  try{
    var a = JSON.parse(raw);
    if(Array.isArray(a)) a.forEach(function(id){ learned[id] = 1; });
  }catch(e){}
})();
function markLearned(id){
  if(learned[id]) return false;
  learned[id] = 1;
  lsSet(LS_LEARNED, JSON.stringify(Object.keys(learned)));
  return true;
}
function unmarkLearned(id){
  delete learned[id];
  lsSet(LS_LEARNED, JSON.stringify(Object.keys(learned)));
}

/* ---------- theme ---------- */
(function(){
  var t = lsGet(LS_THEME);
  if(t === "dark" || t === "light") document.documentElement.setAttribute("data-theme", t);
  var btn = $("themeBtn");
  if(!btn) return;
  btn.onclick = function(){
    var cur = document.documentElement.getAttribute("data-theme");
    if(!cur) cur = matchMedia("(prefers-color-scheme:dark)").matches ? "dark" : "light";
    var next = cur === "dark" ? "light" : "dark";
    document.documentElement.setAttribute("data-theme", next);
    lsSet(LS_THEME, next);
  };
})();

/* ---------- positions ---------- */
function fenToMap(fen){
  var rows = fen.split(" ")[0].split("/"), map = {};
  for(var r=0;r<8;r++){
    var f = 0, s = rows[r];
    for(var i=0;i<s.length;i++){
      var ch = s[i];
      if(ch >= "1" && ch <= "8"){ f += +ch; continue; }
      map[FILES[f] + (8-r)] = { p: ch.toLowerCase(), c: (ch === ch.toUpperCase() ? "w" : "b") };
      f++;
    }
  }
  return map;
}
function sideToMove(fen){ return fen.split(" ")[1] === "w" ? "w" : "b"; }
function posAt(plies, n){
  return { fen: n <= 0 ? START : plies[n-1].fen, last: n <= 0 ? null : plies[n-1] };
}

/* A move played on the board without a position to go with it.
 * The data has a FEN for every move in the book, but not for the wrong move
 * someone just played, and showing that move is the clearest way to say why it
 * was wrong - so this applies one to the piece map by hand. */
function applyVisual(map, from, to){
  var pc = map[from];
  if(!pc) return map;
  delete map[from];
  if(pc.p === "p" && from[0] !== to[0] && !map[to]){
    delete map[to[0] + from[1]];                      // en passant
  }
  if(pc.p === "k" && Math.abs(FILES.indexOf(to[0]) - FILES.indexOf(from[0])) === 2){
    var r = from[1];                                   // castling moves the rook too
    if(to[0] === "g"){ map["f"+r] = map["h"+r]; delete map["h"+r]; }
    else { map["d"+r] = map["a"+r]; delete map["a"+r]; }
  }
  if(pc.p === "p" && (to[1] === "8" || to[1] === "1")) pc = { p:"q", c:pc.c };
  map[to] = pc;
  return map;
}

/* ---------- a move, in words ---------- */
function moveWords(ply, lead){
  var san = ply.san, to = ply.to;
  if(/^O-O-O/.test(san)) return (lead || "Play") === "Play" ? "Castle queenside" : "castled queenside";
  if(/^O-O/.test(san))   return (lead || "Play") === "Play" ? "Castle kingside"  : "castled kingside";

  var letter = /^[KQRBN]/.test(san) ? san[0] : "P";
  var piece = { K:"king", Q:"queen", R:"rook", B:"bishop", N:"knight", P:"pawn" }[letter];
  var capture = san.indexOf("x") >= 0;
  var promo = /=([QRBN])/.exec(san);
  var check = san.indexOf("#") >= 0 ? ", checkmate" : (san.indexOf("+") >= 0 ? ", with check" : "");

  var body;
  if(promo){
    body = "push the " + piece + " to " + to + " and promote to a " +
           { Q:"queen", R:"rook", B:"bishop", N:"knight" }[promo[1]];
  } else if(capture){
    body = "take on " + to + " with the " + (letter === "P" ? san[0] + "-pawn" : piece);
  } else if(letter === "P"){
    body = "push the pawn to " + to;
  } else {
    body = "move the " + piece + " to " + to;
  }
  body += check;
  if(lead === "past") return body.replace(/^take/, "took").replace(/^push/, "pushed").replace(/^move/, "moved");
  return body[0].toUpperCase() + body.slice(1);
}
function pieceWord(ply){
  if(/^O-O/.test(ply.san)) return "king";
  var letter = /^[KQRBN]/.test(ply.san) ? ply.san[0] : "P";
  return { K:"king", Q:"queen", R:"rook", B:"bishop", N:"knight", P:"pawn" }[letter];
}
function moveNo(ply, idx){ return Math.floor(idx / 2) + 1; }
function numbered(idx, san){
  return (idx % 2 === 0) ? (idx/2 + 1) + "." + san : (Math.floor(idx/2) + 1) + "..." + san;
}
function pageTag(page){ return page ? "MCO-15, p." + page : "Modern theory"; }

/* ---------- board ---------- */
function makeBoard(opts){
  opts = opts || {};
  var b = el("div", "board");
  var cells = {};
  for(var r=8;r>=1;r--){
    for(var f=0;f<8;f++){
      var sq = FILES[f] + r;
      var c = el("div", "sq " + (((f + r) % 2) ? "d" : "l"));
      c.dataset.sq = sq;
      var pc = el("img", "pc");
      pc.alt = ""; pc.hidden = true; pc.draggable = false; pc.decoding = "async";
      c.appendChild(pc);
      var x = el("span", "x", "✕"); x.hidden = true; c.appendChild(x);
      if(r === 1) c.appendChild(el("span", "coord f", FILES[f]));
      if(f === 0) c.appendChild(el("span", "coord r", String(r)));
      b.appendChild(c); cells[sq] = c;
    }
  }
  b._cells = cells;
  b._flip = false;
  return b;
}
function orderBoard(b){
  Object.keys(b._cells).forEach(function(sq){
    var f = FILES.indexOf(sq[0]), r = +sq[1];
    b._cells[sq].style.order = b._flip ? ((r-1)*8 + (7-f)) : ((8-r)*8 + f);
  });
}
function paintMap(b, map, last){
  orderBoard(b);
  Object.keys(b._cells).forEach(function(sq){
    var cell = b._cells[sq], pc = cell.firstChild, piece = map[sq];
    if(piece){
      var src = PIECE_DIR + piece.c + piece.p + ".png";
      if(pc.getAttribute("src") !== src) pc.setAttribute("src", src);
      pc.alt = colorName(piece.c) + " " + PIECE_NAME[piece.p];
      pc.hidden = false;
    } else {
      pc.hidden = true; pc.alt = "";
    }
    cell.classList.remove("from","to","sel","hint","ok","no","dot","occ","cross","lift");
    cell.querySelector(".x").hidden = true;
    if(last && last.from === sq) cell.classList.add("from");
    if(last && last.to === sq) cell.classList.add("to");
  });
}
function paintFen(b, fen, last){
  paintMap(b, fenToMap(fen), last);
  // arrows belong to the position they were drawn on; once a move is played
  // they would be pointing at pieces that have moved, so they go
  if(b._marks && b._markFen && b._markFen !== fen) clearMarks(b);
  b._markFen = fen;
  renderMarks(b);
}
function flash(b, sq, cls, ms){
  var cell = b._cells[sq]; if(!cell) return;
  cell.classList.add(cls);
  setTimeout(function(){ cell.classList.remove(cls); }, ms || 480);
}
function shake(b){
  b.classList.add("shake");
  setTimeout(function(){ b.classList.remove("shake"); }, 260);
}

/* ---------- analysis arrows ----------
 * Drawn on an SVG laid over the squares, in board units: 10 per square, so a
 * square's centre is a round number and nothing depends on the pixel size.
 */
var SVGNS = "http://www.w3.org/2000/svg";
var COLOURS = { g:"g", y:"y", r:"r" };

function svgEl(name, attrs){
  var n = document.createElementNS(SVGNS, name);
  Object.keys(attrs || {}).forEach(function(k){ n.setAttribute(k, attrs[k]); });
  return n;
}
function makeMarks(b){
  var svg = svgEl("svg", { "class":"marks", viewBox:"0 0 80 80", "aria-hidden":"true" });
  var defs = svgEl("defs");
  Object.keys(COLOURS).forEach(function(c){
    var m = svgEl("marker", { id:"mco-head-" + c, viewBox:"0 0 6 6", refX:"4.6", refY:"3",
                              markerWidth:"3.4", markerHeight:"3.4", orient:"auto" });
    m.appendChild(svgEl("path", { d:"M0,0 L6,3 L0,6 Z", "class":"h-" + c }));
    defs.appendChild(m);
  });
  svg.appendChild(defs);
  b.appendChild(svg);
  b._marks = svg;
  b._arrows = [];
  b._circles = [];
  return svg;
}
function sqCentre(b, sq){
  var f = FILES.indexOf(sq[0]), r = +sq[1] - 1;
  var cx = b._flip ? 7 - f : f, cy = b._flip ? r : 7 - r;
  return [cx * 10 + 5, cy * 10 + 5];
}
/* A knight goes round the corner rather than through it: the long leg first,
 * then the turn - which is also the shape the move itself has. */
function arrowPath(b, from, to){
  var a = sqCentre(b, from), z = sqCentre(b, to);
  var df = Math.abs(FILES.indexOf(to[0]) - FILES.indexOf(from[0]));
  var dr = Math.abs(+to[1] - +from[1]);
  var pts = [a];
  if((df === 1 && dr === 2) || (df === 2 && dr === 1)){
    pts.push(df === 2 ? [z[0], a[1]] : [a[0], z[1]]);
  }
  pts.push(z);
  var n = pts.length, p = pts[n-2], q = pts[n-1];
  var dx = q[0] - p[0], dy = q[1] - p[1], len = Math.sqrt(dx*dx + dy*dy) || 1;
  pts[n-1] = [q[0] - dx/len * 3.2, q[1] - dy/len * 3.2];   // stop short of the centre
  return pts.map(function(pt, i){
    return (i ? "L" : "M") + pt[0].toFixed(2) + "," + pt[1].toFixed(2);
  }).join(" ");
}
function renderMarks(b){
  if(!b._marks) return;
  var svg = b._marks;
  while(svg.childNodes.length > 1) svg.removeChild(svg.lastChild);   // keep <defs>
  b._circles.forEach(function(c){
    var p = sqCentre(b, c.sq);
    svg.appendChild(svgEl("circle", { cx:p[0], cy:p[1], r:"4.2", "class":"c-" + c.col }));
  });
  b._arrows.concat(b._ghost ? [b._ghost] : []).forEach(function(a){
    svg.appendChild(svgEl("path", {
      d: arrowPath(b, a.from, a.to),
      "class": "c-" + a.col + (a.ghost ? " ghost" : ""),
      "marker-end": "url(#mco-head-" + a.col + ")"
    }));
  });
}
function clearMarks(b){
  if(!b._marks) return;
  b._arrows = []; b._circles = []; b._ghost = null;
  renderMarks(b);
}

/* Right-drag draws; the draw-mode button makes a plain drag do the same, so it
 * works on a touch screen. The arrow is only allowed where the piece could
 * actually go, which `opts.fen()` and the rules in chess.js decide together. */
function wireArrows(b, opts){
  makeMarks(b);
  var drag = null;

  function colourOf(ev){ return ev.shiftKey ? "y" : (ev.altKey || ev.ctrlKey ? "r" : "g"); }
  function markTargets(list){
    (list || []).forEach(function(t){
      var c = b._cells[t]; if(!c) return;
      c.classList.add("adot");
      if(!c.firstChild.hidden) c.classList.add("occ");
    });
  }
  function clearTargets(){
    Object.keys(b._cells).forEach(function(sq){
      b._cells[sq].classList.remove("adot", "occ");
    });
  }
  function squareAt(x, y){
    var node = document.elementFromPoint(x, y);
    var cell = node && node.closest ? node.closest(".sq") : null;
    return cell && b.contains(cell) ? cell.dataset.sq : null;
  }
  function same(a, x){ return a.from === x.from && a.to === x.to; }

  b.addEventListener("contextmenu", function(ev){ ev.preventDefault(); });

  b.addEventListener("pointerdown", function(ev){
    var drawing = ev.button === 2 || (b._draw && ev.button === 0);
    if(!drawing) return;
    var cell = ev.target.closest ? ev.target.closest(".sq") : null;
    if(!cell) return;
    ev.preventDefault();
    ev.stopPropagation();          // in draw mode a drag must not also move a piece
    var from = cell.dataset.sq;
    var legal = window.MCOChess ? window.MCOChess.movesFrom(opts.fen(), from) : [];
    drag = { from: from, legal: legal, col: colourOf(ev), id: ev.pointerId, to: null };
    markTargets(legal);
    try{ b.setPointerCapture(ev.pointerId); }catch(e){}
  }, true);

  b.addEventListener("pointermove", function(ev){
    if(!drag) return;
    var to = squareAt(ev.clientX, ev.clientY);
    var ok = to && to !== drag.from && drag.legal.indexOf(to) >= 0;
    drag.to = ok ? to : null;
    b._ghost = ok ? { from: drag.from, to: to, col: drag.col, ghost: true } : null;
    renderMarks(b);
  });

  function finish(ev){
    if(!drag) return;
    var d = drag; drag = null;
    b._ghost = null;
    clearTargets();
    try{ b.releasePointerCapture(d.id); }catch(e){}
    var to = squareAt(ev.clientX, ev.clientY);
    if(to === d.from || !to){                    // a click, not a drag: ring the square
      var i = -1;
      b._circles.forEach(function(c, n){ if(c.sq === d.from) i = n; });
      if(i >= 0 && b._circles[i].col === d.col) b._circles.splice(i, 1);
      else if(i >= 0) b._circles[i].col = d.col;
      else b._circles.push({ sq: d.from, col: d.col });
    } else if(d.legal.indexOf(to) >= 0){
      var a = { from: d.from, to: to, col: d.col }, j = -1;
      b._arrows.forEach(function(x, n){ if(same(x, a)) j = n; });
      if(j >= 0 && b._arrows[j].col === a.col) b._arrows.splice(j, 1);
      else if(j >= 0) b._arrows[j].col = a.col;
      else b._arrows.push(a);
    }
    renderMarks(b);
    if(opts.onchange) opts.onchange();
  }
  b.addEventListener("pointerup", finish);
  b.addEventListener("pointercancel", function(){
    if(!drag) return;
    drag = null; b._ghost = null; clearTargets(); renderMarks(b);
  });

  // a plain click puts the board back to a clean slate, as every board does
  b.addEventListener("pointerdown", function(ev){
    if(ev.button === 0 && !b._draw && (b._arrows.length || b._circles.length)){
      clearMarks(b);
      if(opts.onchange) opts.onchange();
    }
  });
}

/* Click-to-move and drag-to-move on one board. `handlers.pickable(sq)` says
 * whether a square may be picked up, and `handlers.move(from, to)` is told
 * about every attempt. */
function wireBoard(b, handlers){
  var sel = null, drag = null;

  function clearSel(){
    if(sel && b._cells[sel]) b._cells[sel].classList.remove("sel","lift");
    Object.keys(b._cells).forEach(function(sq){
      b._cells[sq].classList.remove("dot","occ");
    });
    sel = null;
  }
  function select(sq){
    clearSel();
    if(!handlers.pickable(sq)) return;
    sel = sq;
    b._cells[sq].classList.add("sel");
    (handlers.targets(sq) || []).forEach(function(t){
      var c = b._cells[t]; if(!c) return;
      c.classList.add("dot");
      if(!c.firstChild.hidden) c.classList.add("occ");
    });
  }
  function squareAt(x, y){
    var node = document.elementFromPoint(x, y);
    var cell = node && node.closest ? node.closest(".sq") : null;
    return cell && b.contains(cell) ? cell.dataset.sq : null;
  }

  b.addEventListener("pointerdown", function(ev){
    if(ev.button != null && ev.button !== 0) return;
    var cell = ev.target.closest ? ev.target.closest(".sq") : null;
    if(!cell) return;
    var sq = cell.dataset.sq;

    if(sel && sq !== sel && !handlers.pickable(sq)){   // finish a click-click move
      var from = sel; clearSel();
      handlers.move(from, sq);
      ev.preventDefault();
      return;
    }
    if(sel === sq){ clearSel(); ev.preventDefault(); return; }
    if(!handlers.pickable(sq)) return;

    select(sq);
    ev.preventDefault();

    // lift the piece so it can be dragged straight to its square
    var img = cell.firstChild;
    if(img.hidden) return;
    var rect = cell.getBoundingClientRect();
    var ghost = el("img", "dragpc");
    ghost.src = img.src; ghost.alt = "";
    ghost.style.width = rect.width + "px";
    ghost.style.height = rect.height + "px";
    ghost.style.left = ev.clientX + "px";
    ghost.style.top = ev.clientY + "px";
    document.body.appendChild(ghost);
    cell.classList.add("lift");
    drag = { from: sq, ghost: ghost, moved: false, id: ev.pointerId };
    try{ b.setPointerCapture(ev.pointerId); }catch(e){}
  });

  b.addEventListener("pointermove", function(ev){
    if(!drag) return;
    drag.moved = true;
    drag.ghost.style.left = ev.clientX + "px";
    drag.ghost.style.top = ev.clientY + "px";
  });

  function endDrag(ev){
    if(!drag) return;
    var d = drag; drag = null;
    d.ghost.remove();
    if(b._cells[d.from]) b._cells[d.from].classList.remove("lift");
    try{ b.releasePointerCapture(d.id); }catch(e){}
    if(!d.moved) return;                       // a tap: leave the square selected
    var to = squareAt(ev.clientX, ev.clientY);
    if(!to || to === d.from) return;
    clearSel();
    handlers.move(d.from, to);
  }
  b.addEventListener("pointerup", endDrag);
  b.addEventListener("pointercancel", function(){
    if(!drag) return;
    drag.ghost.remove();
    if(b._cells[drag.from]) b._cells[drag.from].classList.remove("lift");
    drag = null;
  });

  b._clearSel = clearSel;
  return b;
}

/* ---------- shared bits of furniture ---------- */
function sideBadge(side, big){
  var s = el("span", "sidebadge" + (big ? " lg" : ""));
  s.appendChild(el("i", side));
  s.appendChild(document.createTextNode("You play " + colorName(side)));
  return s;
}
function progressBar(done, total){
  var p = el("div", "prog" + (total && done >= total ? " done" : ""));
  var bar = el("div", "bar"), fill = el("i");
  fill.style.width = total ? Math.round(done / total * 100) + "%" : "0%";
  bar.appendChild(fill);
  p.appendChild(bar);
  p.appendChild(el("b", null, done + "/" + total));
  return p;
}
function getJSON(url){
  return fetch(url, { cache: "no-cache" }).then(function(r){
    if(!r.ok) throw new Error(url + " -> " + r.status);
    return r.json();
  });
}
function failed(where, err){
  var host = $(where);
  if(host) host.innerHTML = '<p class="empty">Could not load this page&rsquo;s data. ' +
    "Reload, or check that the whole site was copied.</p>";
  if(window.console) console.error(err);
}

/* ======================================================================
   HUB
   ====================================================================== */
function initHub(){
  getJSON(SRC).then(renderHub).catch(function(e){ failed("hubList", e); });

  function renderHub(d){
    var host = $("hubList");
    var q = "";
    var box = $("search");
    if(box){
      box.oninput = function(){ q = this.value.trim().toLowerCase(); draw(); };
      box.onkeydown = function(ev){ if(ev.key === "Escape"){ this.value = ""; q = ""; draw(); } };
    }

    var totalLines = 0, doneLines = 0;
    d.parts.forEach(function(p){ p.chapters.forEach(function(c){
      totalLines += c.n;
      c.done = c.vars.filter(function(v){ return learned[v]; }).length;
      doneLines += c.done;
    }); });

    var top = $("hubProgress");
    if(top){
      top.textContent = "";
      top.appendChild(progressBar(doneLines, totalLines));
      top.appendChild(el("span", "plycount",
        doneLines === totalLines ? "every line finished" : "lines finished"));
    }

    function draw(){
      host.textContent = "";
      var shown = 0;
      d.parts.forEach(function(p){
        var hits = p.chapters.filter(function(c){
          if(!q) return true;
          return (c.name + " " + (c.aka||"") + " " + c.eco + " " + c.line + " " +
                  (c.side === "w" ? "white" : "black")).toLowerCase().indexOf(q) >= 0;
        });
        if(!hits.length) return;
        shown += hits.length;

        var band = el("div", "partband");
        band.appendChild(el("em", null, "Part " + p.num));
        band.appendChild(el("h2", null, p.name));
        band.appendChild(el("span", null, p.line || ""));
        host.appendChild(band);

        var grid = el("div", "grid");
        hits.forEach(function(c){
          var a = el("a", "ocard");
          a.href = ROOT + "o/" + c.id + "/";
          var top = el("div", "top");
          top.appendChild(el("h3", null, c.name));
          top.appendChild(sideBadge(c.side));
          a.appendChild(top);
          if(c.aka) a.appendChild(el("div", "aka", "also called the " + c.aka));
          a.appendChild(el("div", "moves", c.linePgn || "1st move"));
          a.appendChild(progressBar(c.done, c.n));
          grid.appendChild(a);
        });
        host.appendChild(grid);
      });
      if(!shown) host.appendChild(el("p", "empty", "Nothing matches “" + q + "”."));
    }
    draw();
  }
}

/* ======================================================================
   OPENING PAGE
   ====================================================================== */
function initOpening(){
  getJSON(SRC).then(renderOpening).catch(function(e){ failed("lineList", e); });

  function renderOpening(d){
    var host = $("lineList");
    host.textContent = "";

    var done = d.vars.filter(function(v){ return learned[v.id]; }).length;
    var pr = $("chProgress");
    if(pr){
      pr.textContent = "";
      pr.appendChild(progressBar(done, d.vars.length));
      pr.appendChild(el("span", "plycount", "lines finished"));
    }

    var nextUp = d.vars.filter(function(v){ return !learned[v.id]; })[0] || d.vars[0];
    var start = $("startBtn");
    if(start){
      start.href = "./" + nextUp.slug + "/";
      start.textContent = done === 0 ? "Start training →"
        : (done >= d.vars.length ? "Train it again →" : "Continue: " + nextUp.name + " →");
    }

    d.vars.forEach(function(v){
      var a = el("a", "vrow" + (learned[v.id] ? " done" : ""));
      a.href = "./" + v.slug + "/";
      a.appendChild(el("span", "tick", "✓"));
      var mid = el("span");
      var nm = el("span", "vn", v.name);
      if(v.nsub) nm.appendChild(el("span", "sidecount", "+" + v.nsub));
      mid.appendChild(nm);
      mid.appendChild(el("span", "vm", v.pgn));
      a.appendChild(mid);
      a.appendChild(el("span", "vp", v.page ? "p." + v.page : "new"));
      host.appendChild(a);
    });

    // the chapter's own move order, played through on a small board
    var slot = $("boardSlot");
    if(slot && d.linePlies){
      var b = makeBoard();
      slot.appendChild(b);
      var n = 0;
      var caption = $("boardCaption");
      function show(){
        var pos = posAt(d.linePlies, n);
        paintFen(b, pos.fen, pos.last);
        if(caption){
          caption.textContent = n === 0 ? "The starting position"
            : d.linePlies.slice(0, n).map(function(p, i){ return numbered(i, p.san); }).join(" ");
        }
      }
      show();
      if(d.linePlies.length){
        var timer = setInterval(function(){
          n = (n + 1) % (d.linePlies.length + 1);
          if(n === 0) { clearInterval(timer); n = d.linePlies.length; }
          show();
        }, 900);
      }
    }
  }
}

/* ======================================================================
   LINE PAGE - the trainer
   ====================================================================== */
function initLine(){
  getJSON(SRC).then(start).catch(function(e){ failed("panel", e); });

  function start(d){
    var ch = d.ch, v = d.v;
    var side = ch.side;

    var S = {
      sub: null,         // the sideline being drilled, or null for the column
      plies: v.plies,
      ply: 0,
      wrong: 0, hints: 0, hintLevel: 0,
      locked: false,
      watching: false,
      mode: learned[v.id] ? "drill" : "learn",
      timer: null
    };

    var board = wireBoard(makeBoard(), {
      pickable: function(sq){
        if(S.locked || S.watching || S.ply >= S.plies.length) return false;
        if(mover() !== side) return false;
        var map = fenToMap(posAt(S.plies, S.ply).fen);
        return !!(map[sq] && map[sq].c === side);
      },
      targets: function(sq){
        if(S.ply >= S.plies.length) return [];
        return window.MCOChess.movesFrom(posAt(S.plies, S.ply).fen, sq);
      },
      move: attempt
    });
    board._flip = (side === "b");
    $("boardSlot").appendChild(board);
    wireArrows(board, {
      fen: function(){ return posAt(S.plies, S.ply).fen; },
      onchange: function(){ paintDrawBtn(); }
    });

    var drawBtn = $("drawBtn");
    drawBtn.onclick = function(){
      board._draw = !board._draw;
      board.classList.toggle("draw", board._draw);
      paintDrawBtn();
    };
    function paintDrawBtn(){
      var n = board._arrows.length + board._circles.length;
      drawBtn.setAttribute("aria-pressed", board._draw ? "true" : "false");
      drawBtn.textContent = board._draw ? "Drawing" : "Arrows";
      drawBtn.title = board._draw
        ? "Drag to draw an arrow; the pieces cannot be moved while this is on."
        : "Right-drag a piece to draw an arrow. Turn this on to draw by ordinary dragging.";
      $("markCount").textContent = n ? n + (n === 1 ? " mark" : " marks") : "";
    }

    /* ---- furniture ---- */
    var coach = el("div", "coach");
    var said = el("p", "said"), say = el("p", "say"), sub = el("p", "sub"), acts = el("div", "acts");
    coach.appendChild(said); coach.appendChild(say); coach.appendChild(sub); coach.appendChild(acts);
    var steps = el("div", "steps");

    var panel = $("panel");
    panel.insertBefore(coach, panel.firstChild);
    panel.insertBefore(steps, coach.nextSibling);

    var moveHost = $("moveTable"), subHost = $("subList");

    $("flipBtn").onclick = function(){ board._flip = !board._flip; paint(); };
    $("clearBtn").onclick = function(){ clearMarks(board); paintDrawBtn(); };
    $("restartBtn").onclick = function(){ reset(S.sub); };
    $("watchBtn").onclick = function(){ S.watching ? stopWatch() : watch(); };
    var modeBtn = $("modeBtn");
    modeBtn.onclick = function(){
      S.mode = S.mode === "learn" ? "drill" : "learn";
      S.hintLevel = 0;
      paint();
    };

    /* ---- the line being drilled ---- */
    function plies(){
      return S.sub ? v.plies.slice(0, S.sub.fromPly).concat(S.sub.plies) : v.plies;
    }
    function mover(){ return sideToMove(posAt(S.plies, S.ply).fen); }
    function atEnd(){ return S.ply >= S.plies.length; }

    function reset(toSub){
      clearTimeout(S.timer);
      S.sub = toSub || null;
      S.plies = plies();
      S.ply = 0; S.wrong = 0; S.hints = 0; S.hintLevel = 0;
      S.locked = false; S.watching = false;
      board._clearSel();
      paint();
      tick();
    }

    /* ---- the opponent answers by itself ---- */
    function tick(){
      clearTimeout(S.timer);
      if(atEnd() || S.watching) return;
      if(mover() === side) return;                 // your turn: wait for a move
      S.locked = true;
      paint();
      S.timer = setTimeout(function(){
        if(atEnd() || S.watching) { S.locked = false; return; }
        var p = S.plies[S.ply];
        S.ply++;
        S.locked = false;
        S.hintLevel = 0;
        paint();
        flash(board, p.to, "ok", 320);
        tick();
      }, 620);
    }

    function attempt(from, to){
      if(S.locked || S.watching || atEnd()) return;
      if(mover() !== side) return;
      var p = S.plies[S.ply];
      if(window.MCOChess.movesFrom(posAt(S.plies, S.ply).fen, from).indexOf(to) < 0){
        shake(board);                              // not a legal move at all
        return;
      }
      if(from === p.from && to === p.to){
        S.ply++;
        S.hintLevel = 0;
        board._clearSel();
        paint();
        flash(board, p.to, "ok");
        if(atEnd()) finish();
        else tick();
        return;
      }
      wrongMove(from, to);
    }

    function wrongMove(from, to){
      S.wrong++;
      S.locked = true;
      board._clearSel();
      var map = applyVisual(fenToMap(posAt(S.plies, S.ply).fen), from, to);
      paintMap(board, map, { from: from, to: to });
      var cell = board._cells[to];
      if(cell){ cell.classList.add("cross"); cell.querySelector(".x").hidden = false; }
      paintCoach(true);
      S.timer = setTimeout(takeBack, 1900);
    }
    function takeBack(){
      clearTimeout(S.timer);
      if(!S.locked) return;
      S.locked = false;
      paint();
      tick();
    }

    function finish(){
      // reaching the end of the column counts as having learned it; a sideline
      // is extra reading round the column, so it does not
      if(!S.sub) markLearned(v.id);
      paint();
    }

    /* ---- watch the line played through ---- */
    function watch(){
      clearTimeout(S.timer);
      S.watching = true; S.ply = 0; S.locked = false;
      board._clearSel();
      paint();
      (function step(){
        if(!S.watching) return;
        if(S.ply >= S.plies.length){ S.watching = false; paint(); return; }
        S.timer = setTimeout(function(){
          if(!S.watching) return;
          S.ply++;
          paint();
          step();
        }, 850);
      })();
    }
    function stopWatch(){
      clearTimeout(S.timer);
      S.watching = false;
      S.ply = 0;
      paint();
      tick();
    }

    function hint(){
      if(atEnd() || S.locked || S.watching || mover() !== side) return;
      S.hints++;
      S.hintLevel = Math.min(2, S.hintLevel + 1);
      paint();
      if(S.hintLevel >= 1){
        var cell = board._cells[S.plies[S.ply].from];
        if(cell) cell.classList.add("hint");
      }
    }
    function showMe(){
      if(atEnd() || S.watching) return;
      // only ever skips your own move: the opponent's replies play themselves,
      // and advancing one here would race the reply already on its way
      if(S.locked && mover() !== side) return;
      S.hints++;
      var p = S.plies[S.ply];
      S.ply++; S.hintLevel = 0;
      S.locked = false;
      paint();
      flash(board, p.to, "ok");
      if(atEnd()) finish(); else tick();
    }

    /* ---- drawing ---- */
    function paint(){
      var pos = posAt(S.plies, S.ply);
      paintFen(board, pos.fen, pos.last);
      if(S.hintLevel >= 1 && !atEnd() && !S.locked && mover() === side){
        var c = board._cells[S.plies[S.ply].from];
        if(c) c.classList.add("hint");
      }
      $("plyCount").textContent = S.ply + "/" + S.plies.length + " moves";
      var stm = sideToMove(pos.fen);
      $("toMove").innerHTML = '<i class="' + stm + '"></i>' + colorName(stm) + " to move";
      modeBtn.textContent = S.mode === "learn" ? "Mode: guided" : "Mode: from memory";
      modeBtn.title = S.mode === "learn"
        ? "The coach names each of your moves. Switch to play them from memory."
        : "You recall each move yourself. Switch back to being told.";
      $("watchBtn").textContent = S.watching ? "Stop" : "Watch";
      paintDrawBtn();
      paintCoach(false);
      paintSteps();
      paintMoves();
      paintSubs();
    }

    function paintSteps(){
      steps.textContent = "";
      for(var i=0;i<S.plies.length;i++){
        var dot = el("i");
        if(i < S.ply) dot.className = "on";
        if(sideToMove(posAt(S.plies, i).fen) === side) dot.className += " me";
        steps.appendChild(dot);
      }
    }

    function paintCoach(isWrong){
      coach.className = "coach";
      acts.textContent = "";
      said.textContent = "";
      sub.textContent = "";

      // what just happened
      if(S.ply > 0 && !isWrong){
        var prev = S.plies[S.ply-1];
        var who = sideToMove(posAt(S.plies, S.ply-1).fen);
        said.textContent = (who === side ? "You played " : colorName(who) + " played ") +
          numbered(S.ply-1, prev.san);
      }

      if(S.watching){
        coach.classList.add("good");
        say.innerHTML = "<b>Watching the line.</b>";
        sub.textContent = S.ply ? numbered(S.ply-1, S.plies[S.ply-1].san) + " — " +
          moveWords(S.plies[S.ply-1], "past").replace(/^./, function(c){ return c.toUpperCase(); })
          : "Follow the moves, then play it yourself.";
        act("Stop watching", stopWatch, true);
        return;
      }

      if(isWrong){
        coach.classList.add("bad");
        say.innerHTML = "<b>Not that move.</b>";
        sub.textContent = "It is legal, but this line plays something else here." +
          (S.mode === "learn" && !atEnd() ? " " + moveWords(S.plies[S.ply]) + "." : "");
        act("Try again", takeBack, true);
        act("Show me", function(){ S.locked = false; paint(); showMe(); });
        return;
      }

      if(atEnd()){
        coach.classList.add("good");
        var clean = S.wrong === 0 && S.hints === 0;
        say.innerHTML = "<b>" + (S.sub ? "Sideline complete." : "Line complete.") + "</b>";
        sub.textContent = clean ? "Straight through, no mistakes and no hints."
          : S.wrong + " wrong " + (S.wrong === 1 ? "move" : "moves") + ", " +
            S.hints + " " + (S.hints === 1 ? "hint" : "hints") + ".";
        act("Play it again", function(){ reset(S.sub); }, true);
        if(S.sub) act("Back to the main line", function(){ reset(null); });
        var nxt = $("nextLink");
        if(nxt && !S.sub){
          var go = el("a", "btn", "Next line →");
          go.href = nxt.href;
          acts.appendChild(go);
        }
        return;
      }

      if(S.locked && mover() !== side){
        say.innerHTML = "<b>" + colorName(mover()) + " is replying…</b>";
        sub.textContent = "You only play " + colorName(side) + " here.";
        return;
      }

      // your move
      var p = S.plies[S.ply];
      var num = moveNo(p, S.ply);
      if(S.mode === "learn" || S.hintLevel >= 2){
        say.innerHTML = "<b>" + esc(moveWords(p)) + ".</b>";
        sub.textContent = "Move " + num + " for " + colorName(side) +
          ". Drag the piece, or click it and then the square.";
      } else if(S.hintLevel === 1){
        say.innerHTML = "Move the <b>" + pieceWord(p) + "</b>.";
        sub.textContent = "Move " + num + " for " + colorName(side) + ". Its square is marked.";
      } else {
        say.innerHTML = "<b>Your move.</b> " + colorName(side) + " to play move " + num + ".";
        sub.textContent = "Play it from memory — or take a hint.";
      }
      if(S.mode === "drill") act(S.hintLevel >= 2 ? "Show me" : "Hint",
                                 S.hintLevel >= 2 ? showMe : hint, S.hintLevel === 0);
      else act("Show me", showMe);
    }
    function act(label, fn, primary){
      var b = el("button", "btn" + (primary ? " primary" : ""), label);
      b.onclick = fn;
      acts.appendChild(b);
      return b;
    }

    function paintMoves(){
      moveHost.textContent = "";
      var head = el("thead");
      head.innerHTML = "<tr><th></th><th>White</th><th>Black</th></tr>";
      moveHost.appendChild(head);
      var body = el("tbody");
      // a line can start on Black's move only after a branch, so pad by parity
      for(var i=0;i<S.plies.length;i+=2){
        var tr = el("tr");
        tr.appendChild(el("td", "n", String(i/2 + 1)));
        for(var k=0;k<2;k++){
          var td = el("td"), idx = i + k, p = S.plies[idx];
          if(p){
            var mine = sideToMove(posAt(S.plies, idx).fen) === side;
            var cls = "mv" + (mine ? " yours" : "");
            if(S.sub && idx >= S.sub.fromPly) cls += " side";
            if(idx < S.ply) td.appendChild(el("span", cls, p.san));
            else if(idx === S.ply && mine && !S.watching) td.appendChild(el("span", "mv now", "?"));
            else td.appendChild(el("span", cls + " todo", "···"));
          }
          tr.appendChild(td);
        }
        body.appendChild(tr);
      }
      moveHost.appendChild(body);
    }

    function paintSubs(){
      if(!subHost) return;
      subHost.textContent = "";
      var subs = v.subs || [];
      if(!subs.length) return;
      subs.forEach(function(s){
        var row = el("button", "subrow");
        row.setAttribute("aria-pressed", S.sub && S.sub.id === s.id ? "true" : "false");
        row.appendChild(el("span", "branch", "after " + numbered(s.fromPly - 1, v.plies[s.fromPly-1].san)));
        var mid = el("span");
        mid.appendChild(el("span", "sm", s.pgn));
        if(s.cite){
          var c = el("span", "sc");
          c.appendChild(el("b", null, "(" + s.key + ") "));
          c.appendChild(document.createTextNode(s.cite + " · " + pageTag(s.page)));
          mid.appendChild(c);
        }
        row.appendChild(mid);
        row.onclick = function(){
          reset(S.sub && S.sub.id === s.id ? null : s);
          document.querySelector(".boardwrap").scrollIntoView({ behavior:"smooth", block:"start" });
        };
        subHost.appendChild(row);
      });
    }

    /* ---- keyboard ---- */
    document.addEventListener("keydown", function(ev){
      if(ev.target && /^(INPUT|TEXTAREA)$/.test(ev.target.tagName)) return;
      var k = ev.key.toLowerCase();
      if(k === "h"){ hint(); ev.preventDefault(); }
      else if(k === "f"){ board._flip = !board._flip; paint(); ev.preventDefault(); }
      else if(k === "r"){ reset(S.sub); ev.preventDefault(); }
      else if(k === "w"){ S.watching ? stopWatch() : watch(); ev.preventDefault(); }
      else if(k === "s"){ showMe(); ev.preventDefault(); }
      else if(k === "a"){ drawBtn.onclick(); ev.preventDefault(); }
      else if(k === "escape"){ clearMarks(board); paintDrawBtn(); }
    });

    reset(null);
  }
}

/* ======================================================================
   QUIZ - which opening did this position come from?
   ====================================================================== */
function initQuiz(){
  getJSON(SRC).then(run).catch(function(e){ failed("panel", e); });

  function run(d){
    var board = makeBoard();
    $("boardSlot").appendChild(board);
    var panel = $("panel");
    var asked = 0, right = 0, item = null, answered = false;

    var coach = el("div", "coach");
    var say = el("p", "say"), sub = el("p", "sub"), acts = el("div", "acts");
    coach.appendChild(say); coach.appendChild(sub); coach.appendChild(acts);
    panel.appendChild(coach);
    var optCard = el("section", "card");
    optCard.appendChild(el("h2", null, "Which opening is this?"));
    var opts = el("div", "vlist");
    optCard.appendChild(opts);
    panel.appendChild(optCard);

    function pick(){
      answered = false;
      item = d.items[Math.floor(Math.random() * d.items.length)];
      board._flip = d.chapters[item.c].side === "b";
      paintFen(board, item.fen, null);
      $("quizMoves").textContent = "";
      say.innerHTML = "<b>Name the opening.</b>";
      var half = item.pgn.split(" ").length;      // pgn is one token per ply here
      sub.textContent = "Position " + Math.ceil(half / 2) + " moves into one of the lines.";
      coach.className = "coach";
      acts.textContent = "";

      // three plausible wrong answers, preferring openings of the same colour
      var chosen = [item.c], side = d.chapters[item.c].side;
      var pool = [];
      for(var i=0;i<d.chapters.length;i++) if(i !== item.c && d.chapters[i].side === side) pool.push(i);
      for(var j=0;j<d.chapters.length;j++) if(j !== item.c && d.chapters[j].side !== side) pool.push(j);
      while(chosen.length < 4 && pool.length){
        var k = Math.floor(Math.random() * Math.min(pool.length, 22));
        chosen.push(pool.splice(k, 1)[0]);
      }
      for(var m=chosen.length-1;m>0;m--){
        var n = Math.floor(Math.random() * (m + 1));
        var t = chosen[m]; chosen[m] = chosen[n]; chosen[n] = t;
      }

      opts.textContent = "";
      chosen.forEach(function(ci){
        var b = el("button", "vrow");
        b.appendChild(el("span", "tick", "✓"));
        var mid = el("span");
        mid.appendChild(el("span", "vn", d.chapters[ci].name));
        b.appendChild(mid);
        b.appendChild(el("span", "vp", d.chapters[ci].side === "w" ? "white" : "black"));
        b.dataset.ch = ci;
        b.onclick = function(){ answer(ci, b); };
        opts.appendChild(b);
      });
    }

    function answer(ci, btn){
      if(answered) return;
      answered = true;
      asked++;
      var ok = ci === item.c;
      if(ok) right++;
      if(!ok) btn.style.borderColor = "var(--bad)";
      Array.prototype.forEach.call(opts.children, function(b){
        b.disabled = true;
        if(+b.dataset.ch === item.c){        // mark the right one however they answered
          b.classList.add("done");
          b.style.borderColor = "var(--good)";
        }
      });
      coach.className = "coach " + (ok ? "good" : "bad");
      say.innerHTML = ok ? "<b>Yes.</b> " + esc(d.chapters[item.c].name)
                         : "<b>No — it is the " + esc(d.chapters[item.c].name) + ".</b>";
      sub.textContent = item.name + " · " + item.pgn;
      $("quizMoves").textContent = item.pgn;
      acts.textContent = "";
      var next = el("button", "btn primary", "Next position");
      next.onclick = pick;
      acts.appendChild(next);
      var open = el("a", "btn", "Train this line →");
      open.href = ROOT + item.url;
      acts.appendChild(open);
      acts.appendChild(el("span", "plycount", right + "/" + asked + " right"));
      next.focus();
    }

    document.addEventListener("keydown", function(ev){
      if(ev.key === "Enter" && answered){ pick(); ev.preventDefault(); }
    });
    pick();
  }
}

/* ---------- go ---------- */
if(PAGE === "hub") initHub();
else if(PAGE === "opening") initOpening();
else if(PAGE === "line") initLine();
else if(PAGE === "quiz") initQuiz();

})();
