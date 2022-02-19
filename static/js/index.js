
    function SwapDivsWithClick(div1, div2) {
      d1 = document.getElementById(div1);
      d2 = document.getElementById(div2);
      if (d2.style.display == "none") {
        d1.style.display = "none";
        d2.style.display = "block";
      } else {
        d1.style.display = "block";
        d2.style.display = "none";
      }
    }
 

  const deptId =  new URLSearchParams(window.location.search).get('dept');
  console.log('Dept id is: '+ deptId);
  var cse = document.getElementById('cse');
  var mech = document.getElementById('Mechanical');
  var civil = document.getElementById('Civil');
  var Electronics = document.getElementById('Electronics');
  var mba = document.getElementById('MBA');
  var bba = document.getElementById('BBA');
  var Bsc = document.getElementById('B.Sc');
  var bca = document.getElementById('BCA');
  var mca = document.getElementById('M.C.A');
  var llb = document.getElementById('LLb');
  var mca = document.getElementById('M.C.A');

  if (deptId  == 1) {    
    cse.style.display = 'block';
    // console.log('CSe dept is showing ');
  } else if(deptId == 2) {
    mech.style.display = 'block';  
    // console.log('mech dept is showing ');
  }else if(deptId == 3){
    civil.style.display = 'block';
  }else if(deptId == 4){
    Electronics.style.display = 'block';
  }else if(deptId == 5){
    mba.style.display = 'block';
  }else if(deptId == 6)
  {
    bba.style.display = 'block';
  }
  
