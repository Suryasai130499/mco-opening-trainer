/* The rules of chess, as far as a position needs them.
 *
 * The trainer itself needs no engine - every position in a line is precomputed.
 * Analysis arrows do: you point at any piece, on either side, and the board has
 * to say where that piece may go. That is a move generator, so here is one.
 *
 * window.MCOChess.movesFrom(fen, "g1")  ->  ["f3", "h3", "e2"]
 * window.MCOChess.legalMoves(fen, "w")  ->  "b1a3 b1c3 b2b3 ..."
 *
 * Moves are legal, not merely geometric: a pinned piece stays put, a king may
 * not walk into check, castling needs its rights, an empty path and squares
 * that are not attacked, and en passant is offered only to the side whose turn
 * the FEN says it is - the square it captures on belongs to that side alone.
 *
 * Asked for the side that is NOT to move, it answers as if it were their turn,
 * minus en passant. That is what an analysis arrow means when you point at the
 * other side's bishop: where could this go.
 *
 * Verified square by square against python-chess: data/check_rules.py replays
 * every position in the book through this file and demands the same list.
 */
(function(){
"use strict";

var FILES = "abcdefgh";

function idx(f, r){ return r * 8 + f; }           // r 0..7 = ranks 1..8
function name(i){ return FILES[i % 8] + (Math.floor(i / 8) + 1); }
function fileOf(i){ return i % 8; }
function rankOf(i){ return Math.floor(i / 8); }
function sqIndex(sq){ return idx(FILES.indexOf(sq[0]), +sq[1] - 1); }

/* ---------- reading a position ---------- */
function parse(fen){
  var parts = fen.split(" ");
  var sq = new Array(64);
  var rows = parts[0].split("/");
  for(var r = 0; r < 8; r++){
    var row = rows[7 - r], f = 0;
    for(var i = 0; i < row.length; i++){
      var ch = row[i];
      if(ch >= "1" && ch <= "8"){ f += +ch; continue; }
      sq[idx(f, r)] = { t: ch.toLowerCase(), c: ch === ch.toUpperCase() ? "w" : "b" };
      f++;
    }
  }
  return {
    sq: sq,
    turn: parts[1] === "b" ? "b" : "w",
    castle: parts[2] && parts[2] !== "-" ? parts[2] : "",
    ep: parts[3] && parts[3] !== "-" ? sqIndex(parts[3]) : -1
  };
}

var KNIGHT = [[1,2],[2,1],[2,-1],[1,-2],[-1,-2],[-2,-1],[-2,1],[-1,2]];
var DIAG   = [[1,1],[1,-1],[-1,-1],[-1,1]];
var ORTHO  = [[1,0],[0,1],[-1,0],[0,-1]];
var AROUND = DIAG.concat(ORTHO);

function onBoard(f, r){ return f >= 0 && f < 8 && r >= 0 && r < 8; }

/* Is `target` attacked by a piece of colour `by`? Pawns are asked backwards:
 * a square is attacked by a white pawn if a white pawn sits one rank below it,
 * diagonally. */
function attacked(sq, target, by){
  var tf = fileOf(target), tr = rankOf(target), i, f, r, p;

  var pdir = by === "w" ? -1 : 1;                 // walk back towards the pawn
  for(i = -1; i <= 1; i += 2){
    f = tf + i; r = tr + pdir;
    if(onBoard(f, r)){
      p = sq[idx(f, r)];
      if(p && p.c === by && p.t === "p") return true;
    }
  }
  for(i = 0; i < KNIGHT.length; i++){
    f = tf + KNIGHT[i][0]; r = tr + KNIGHT[i][1];
    if(onBoard(f, r)){
      p = sq[idx(f, r)];
      if(p && p.c === by && p.t === "n") return true;
    }
  }
  for(i = 0; i < AROUND.length; i++){
    f = tf + AROUND[i][0]; r = tr + AROUND[i][1];
    if(onBoard(f, r)){
      p = sq[idx(f, r)];
      if(p && p.c === by && p.t === "k") return true;
    }
  }
  for(i = 0; i < DIAG.length; i++){
    f = tf; r = tr;
    for(;;){
      f += DIAG[i][0]; r += DIAG[i][1];
      if(!onBoard(f, r)) break;
      p = sq[idx(f, r)];
      if(p){
        if(p.c === by && (p.t === "b" || p.t === "q")) return true;
        break;
      }
    }
  }
  for(i = 0; i < ORTHO.length; i++){
    f = tf; r = tr;
    for(;;){
      f += ORTHO[i][0]; r += ORTHO[i][1];
      if(!onBoard(f, r)) break;
      p = sq[idx(f, r)];
      if(p){
        if(p.c === by && (p.t === "r" || p.t === "q")) return true;
        break;
      }
    }
  }
  return false;
}

function kingOf(sq, c){
  for(var i = 0; i < 64; i++) if(sq[i] && sq[i].t === "k" && sq[i].c === c) return i;
  return -1;
}

/* ---------- pseudo-legal moves of the piece on `from` ---------- */
function pseudo(pos, from, allowEp){
  var p = pos.sq[from];
  if(!p) return [];
  var out = [], sq = pos.sq, me = p.c, them = me === "w" ? "b" : "w";
  var f = fileOf(from), r = rankOf(from), i, nf, nr, t;

  function add(nf, nr, mode){            // mode: "quiet", "capture" or "either"
    if(!onBoard(nf, nr)) return false;
    var to = idx(nf, nr), q = sq[to];
    if(q && q.c === me) return false;
    if(q && mode === "quiet") return false;
    if(!q && mode === "capture") return false;
    out.push(to);
    return !q;                            // true if the square was empty
  }
  function slide(dirs){
    for(var d = 0; d < dirs.length; d++){
      nf = f; nr = r;
      for(;;){
        nf += dirs[d][0]; nr += dirs[d][1];
        if(!add(nf, nr, "either")) break;
      }
    }
  }

  if(p.t === "p"){
    var dir = me === "w" ? 1 : -1;
    var home = me === "w" ? 1 : 6;
    if(add(f, r + dir, "quiet") && r === home) add(f, r + 2 * dir, "quiet");
    for(i = -1; i <= 1; i += 2){
      nf = f + i; nr = r + dir;
      if(!onBoard(nf, nr)) continue;
      t = idx(nf, nr);
      if(sq[t] && sq[t].c === them) out.push(t);
      else if(allowEp && t === pos.ep) out.push(t);
    }
  } else if(p.t === "n"){
    for(i = 0; i < KNIGHT.length; i++) add(f + KNIGHT[i][0], r + KNIGHT[i][1], "either");
  } else if(p.t === "b"){
    slide(DIAG);
  } else if(p.t === "r"){
    slide(ORTHO);
  } else if(p.t === "q"){
    slide(AROUND);
  } else if(p.t === "k"){
    for(i = 0; i < AROUND.length; i++) add(f + AROUND[i][0], r + AROUND[i][1], "either");
    // castling: the rights, an empty path, and no square the king crosses
    // (including the one it stands on) may be attacked
    var back = me === "w" ? 0 : 7;
    if(from === idx(4, back) && !attacked(sq, from, them)){
      var ks = me === "w" ? "K" : "k", qs = me === "w" ? "Q" : "q";
      if(pos.castle.indexOf(ks) >= 0 && !sq[idx(5, back)] && !sq[idx(6, back)] &&
         !attacked(sq, idx(5, back), them)) out.push(idx(6, back));
      if(pos.castle.indexOf(qs) >= 0 && !sq[idx(3, back)] && !sq[idx(2, back)] &&
         !sq[idx(1, back)] && !attacked(sq, idx(3, back), them)) out.push(idx(2, back));
    }
  }
  return out;
}

/* ---------- would this move leave our own king in check? ---------- */
function leavesKingExposed(pos, from, to){
  var sq = pos.sq.slice(), p = sq[from], me = p.c, them = me === "w" ? "b" : "w";
  if(p.t === "p" && to === pos.ep && fileOf(from) !== fileOf(to)){
    sq[idx(fileOf(to), rankOf(from))] = undefined;      // the pawn taken en passant
  }
  if(p.t === "k" && Math.abs(fileOf(to) - fileOf(from)) === 2){
    var back = rankOf(from);
    if(fileOf(to) === 6){ sq[idx(5, back)] = sq[idx(7, back)]; sq[idx(7, back)] = undefined; }
    else { sq[idx(3, back)] = sq[idx(0, back)]; sq[idx(0, back)] = undefined; }
  }
  sq[to] = p;
  sq[from] = undefined;
  var k = kingOf(sq, me);
  return k < 0 ? false : attacked(sq, k, them);
}

/* ---------- what this file is for ---------- */
function movesFrom(fen, from){
  var pos = typeof fen === "string" ? parse(fen) : fen;
  var i = typeof from === "string" ? sqIndex(from) : from;
  var p = pos.sq[i];
  if(!p) return [];
  var cand = pseudo(pos, i, p.c === pos.turn), out = [];
  for(var n = 0; n < cand.length; n++){
    if(!leavesKingExposed(pos, i, cand[n])) out.push(name(cand[n]));
  }
  return out;
}

function legalMoves(fen, colour){
  var pos = typeof fen === "string" ? parse(fen) : fen;
  var c = colour || pos.turn, out = [];
  for(var i = 0; i < 64; i++){
    if(!pos.sq[i] || pos.sq[i].c !== c) continue;
    var to = movesFrom(pos, i);
    for(var n = 0; n < to.length; n++) out.push(name(i) + to[n]);
  }
  return out.sort().join(" ");
}

window.MCOChess = { parse: parse, movesFrom: movesFrom, legalMoves: legalMoves };

})();
