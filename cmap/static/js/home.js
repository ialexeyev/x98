// CMAP: home page local scripts



//Production indicators: speedometer
let speedometers = document.getElementsByClassName('SpeedometerNeedle');
for(let i = 0; i < speedometers.length; i++) {
  if(i == 0) {
    speedometers[i].style.transform = "rotate(90deg)";
  }
  else if (i == 1) {
     speedometers[i].style.transform = "rotate(80deg)";
  }
  else if (i == 2) {
     speedometers[i].style.transform = "rotate(65deg)";
  }
  else if (i == 3) {
     speedometers[i].style.transform = "rotate(75deg)";
  }
}

