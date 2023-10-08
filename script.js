
function validateWave() {
  var wave1=false;
  wave1=validateWaveMe(document.getElementById("userid1").value);
  var wave2 =false;
  wave2= validateWaveMe(document.getElementById("userid2").value);
  if (wave1===true && wave2===true) {
    // alert("True");
    console.log("Submit done");
    document.getElementById("wavesubmit").onsubmit();
  } else {
    alert("សូមបញ្ចូលអោយបានត្រឹមត្រូវ!");
    return false;
    
  }
}
function validateWaveMe(waveEquation) {
  var regex1 = /[^a-z]/gi;
  var regex2 = /[!@#$%^&*()_+\-=\[\]{}<>;:.,'"\\|\/?]/g;
  var huotregex=/([0-9]+[sin(]+[0-9]|[t]|[\+\-]*[0-9\/\π]|[)]){5,20}/g;

  if (waveEquation.length != 0) {
    var sv, wavelist;
    waveEquation=waveEquation.replace(/\s/g,'');
    console.log(waveEquation);
    wavelist = waveEquation.trim().replace(/\s/g,'').toLowerCase().split("");

    sv = ["(", ")", "s", "i", "n", "t"];
    if(waveEquation.replace(regex1, "").length>4){
      console.log("false regex1");
      return false;
    }
    else if(waveEquation.match(regex2)==null){
      console.log("false regex2 step 1");
      return false;
    }
    else if(waveEquation.match(huotregex)==null)
    {
      console.log(waveEquation);
      console.log("huot check wave fail");
      return false;
    }
    else if(waveEquation.match(regex2).length>4){
      console.log("false regex2 step 2");
      return false;
    }
    else if(waveEquation.indexOf(')')!=(waveEquation.length-1)){
      console.log("not need anything after )");
      return false;
    }
    else if(waveEquation.indexOf('(')!=(waveEquation.indexOf('n')+1)){
      console.log("error between sin and (");
      return false;
    }
    
    else if (
      wavelist.includes(sv[0]) &&
      wavelist.includes(sv[1]) &&
      wavelist.includes(sv[2]) &&
      wavelist.includes(sv[3]) &&
      wavelist.includes(sv[4]) &&
      wavelist.includes(sv[5]) &&
      char_count(waveEquation,'+') <=1 &&
      char_count(waveEquation,'-') <=1 &&
      char_count(waveEquation,'s') == 1 &&
      char_count(waveEquation,'i') == 1 &&
      char_count(waveEquation,'n') == 1 &&
      char_count(waveEquation,'(') == 1 &&
      char_count(waveEquation,')') == 1 &&
      char_count(waveEquation,'/') <= 1 &&
      waveEquation.includes("sin(")  

    ){
      return true;
    }
    
    else{
        console.log("false total");
        return false;
    }
      
  }
  else{
    console.log("Null input");
    return false;
  }
}  

function getSample(){
  var listSample1=["4sin(100πt)","2sin(100πt+π/2)","4sin(10πt-3π/2)","2sin(50πt-π/2)","3sin(100πt-π/2)","3sin(600πt)","4sin(60πt+π/2)","8sin(100πt-2)","2sin(100πt+3/2)","2sin(100πt)"];
  var listSample2=["5sin(100πt)","6sin(100πt-π/4)","6sin(10πt-π/2)","6sin(50πt+π/2)","5sin(100πt)","5sin(60πt+π/3)","6sin(60πt+1)","2sin(100πt+1/2)","7sin(100πt+3π/2)","9sin(100πt)"];  
  var x=Math.floor(Math.random() * listSample1.length);
  document.getElementById("userid1").value=listSample1[x];
  document.getElementById("userid2").value=listSample2[x];
  console.log("user get Sample");
}

function char_count(str, letter) 
{
 var letter_Count = 0;
 for (var position = 0; position < str.length; position++) 
 {
    if (str.charAt(position) == letter) 
      {
      letter_Count += 1;
      }
  }
  return letter_Count;
}