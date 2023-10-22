function convertDegreetoRadian(deg) {
  return (Math.PI * deg) / 180;
}
function xAxis(v, t, theta) {
  return v * Math.cos(theta) * t;
}
function yAxis(g, v, t, theta, Yo) {
  return (-1 / 2) * g * t * t + v * Math.sin(theta) * t + Yo;
}
function XY(g, v, theta, x, yo) {
  return (
    (-1 * g * x * x) / (2 * v * v * Math.pow(Math.cos(theta), 2)) +
    x * Math.tan(theta) +
    yo
  );
}

class FindXY {
  findRoot;

  constructor(v, theta, g, yo) {
    this.v = v;
    this.theta = theta;
    this.g = g;
    this.yo = yo;
    this.findRoot = this.getResultObject();
  }
  getA() {
    return (
      (-1 * this.g) /
      (2 *
        Math.pow(this.v, 2) *
        Math.pow(Math.cos(convertDegreetoRadian(this.theta)), 2))
    );
  }
  getB() {
    return Math.tan(convertDegreetoRadian(this.theta));
  }
  getC() {
    return this.yo;
  }
  getResultObject() {
    return new SquareRoot(this.getA(), this.getB(), this.getC());
  }
}

class SquareRoot {
  x1;
  x2;
  resultX = "";
  constructor(a, b, c) {
    this.a = a;
    this.b = b;
    this.c = c;
    this.getRoot();
  }

  getDelta() {
    return Math.pow(this.b, 2) - 4 * this.a * this.c;
  }
  getDeltaAfter() {
    return Math.sqrt(this.getDelta());
  }
  getRoot() {
    if (this.getDeltaAfter() >= 0) {
      this.x1 = (-1 * this.b + this.getDeltaAfter()) / (2 * this.a);
      this.x2 = (-1 * this.b - this.getDeltaAfter()) / (2 * this.a);
      if (this.x1 >= this.x2) {
        this.resultX = this.x1.toString();
      } else {
        this.resultX = this.x2.toString();
      }
    } else {
      this.resultX = "No have result!";
    }
  }
}

function doCalculate() {
  var v = document.getElementById("v").value;
  var yo = document.getElementById("yo").value;
  var theta = document.getElementById("theta").value;
  v=v.toString();
  yo=yo.toString();
  theta=theta.toString();
  
  if(v.length>0&&yo.length>0&&theta.length>0){
    console.log("OK Submit");

    showValue();
  }
  else{
    alert("សូមបញ្ចូលអោយបានត្រឹមត្រូវ!");
    console.log("False Submit");
  }
}

function showValue(params) {
  var v = document.getElementById("v").value;
  var yo = document.getElementById("yo").value;
  var theta = document.getElementById("theta").value;

  var gRadio = document.getElementsByName("g");
  var g;
  for (var i = 0; i < gRadio.length; i++) {
    if (gRadio[i].checked) {
      g = gRadio[i].value;
    }
  }
  console.log(v, theta, g);
  fname(v, g, theta, yo);
  rs = new FindXY(v, theta, g, yo);
  aval = rs.getA().toFixed(3);
  bval = rs.getB();
  cval = rs.getC();
  var bv;
  var cv;
  if (bval > 0) {
    bv = "+" + bval.toFixed(3);
  } else {
    bv = bval.toFixed(3);
  }
  if (cval >= 0) {
    cv = "+" + cval;
  } else {
    cv = cval;
  }
  console.log(aval);
  var vvy = document.getElementById("getabc");
  var vvy1 = document.getElementById("getabc1");
  var hi = vvy.innerHTML;
  hi = hi.replace("/aval", aval);
  hi = hi.replace("/bval", bv);
  hi = hi.replaceAll("/cval", cv);
  vvy.innerHTML = hi;

  var hi1 = vvy1.innerHTML;
  hi1 = hi1.replace("/aval", aval);
  hi1 = hi1.replace("/bval", bv);
  hi1 = hi1.replaceAll("/cval", cv);
  vvy1.innerHTML = hi1;


  var mdelta=rs.findRoot.getDelta().toFixed(4);

  var vvy2 = document.getElementById("getDelta");
  var hi2 = vvy2.innerHTML;
  hi2 = hi2.replace("/aval", aval);
  hi2 = hi2.replace("/bval", bval.toFixed(3));
  hi2 = hi2.replaceAll("/cval", cval);
  hi2=hi2.replace("/re",mdelta);
  vvy2.innerHTML=hi2;


  var sqDelta = rs.findRoot.getDeltaAfter().toFixed(4);
  var sd = document.getElementById("sqrtDelta");
  let sd1 = sd.innerHTML;
  sd1 = sd1.replace("/sqrtDelta", sqDelta);
  sd.innerHTML = sd1;

  var x1 = rs.findRoot.x1.toFixed(4);
  var x2 = rs.findRoot.x2.toFixed(4);
  var x12 = document.getElementById("x12");
  var x123 = x12.innerHTML;
  x123 = x123.replace("/x1", x1);
  x123 = x123.replace("/x2", x2);
  x12.innerHTML = x123;

  var mresult = rs.findRoot.resultX;
  mrr = parseFloat(mresult).toFixed(4);
  console.log(mresult);
  var xm12 = document.getElementById("mresult");
  var xm123 = xm12.innerHTML;
  xm123 = xm123.replace("/mresult", mrr);
  xm12.innerHTML = xm123;
  document.getElementById("answer").hidden = false;
}

function fname(v, g, theta, yo) {
  var vdoc = document.getElementById("valueGive");
  vo = vdoc.innerHTML;
  var value0 = vo.replace("/vo", v);
  value1 = value0.replace("/g", g);
  value2 = value1.replace("/theta", theta);
  value3 = value2.replace("/yo", yo);
  vdoc.innerHTML = value3;

  console.log(v, g, theta);

  var vv = document.getElementById("sh");
  var msh = vv.innerHTML;
  msh = msh.replace("/yo", yo);
  msh = msh.replace("/vo", v);
  msh = msh.replaceAll("/theta", theta);
  msh = msh.replace("/g", g);
  vv.innerHTML = msh;

  // document.getElementById("thetag").value=theta;
}
function getExample(params) {
    var mclick=document.getElementById("example");
    if(mclick.checked){
        document.getElementById("v").value=9.8;
        document.getElementById("yo").value=2.2;
        document.getElementById("theta").value=45;
        document.getElementById("radio1").checked=true;
        document.getElementById("ex").hidden=false;
    }
    else{
        document.getElementById("v").value="";
        document.getElementById("yo").value="";
        document.getElementById("theta").value="";
        document.getElementById("radio1").checked=true;
        document.getElementById("ex").hidden=true;
    }
    
}