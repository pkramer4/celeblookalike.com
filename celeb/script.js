window.onload = showDevito;


var devitoArr = ["images/devito1.jpg","images/devito2.jpg","images/devito3.jpg"];

function showDevito() {
  console.log('hi');
  var randomNum = Math.floor(Math.random() * devitoArr.length);
  var img = document.createElement('img');
  img.setAttribute("id", "finalPhoto");
  img.src = devitoArr[randomNum];
  document.getElementById('photo').appendChild(img);

  var randomNum1 = Math.floor(Math.random() * 35);
  document.getElementById('eyes').innerHTML = randomNum1;

  var randomNum2 = Math.floor(Math.random() * 35);
  document.getElementById('hair').innerHTML = randomNum2;

  document.getElementById('shape').innerHTML = 100 - randomNum1 - randomNum2;
}
