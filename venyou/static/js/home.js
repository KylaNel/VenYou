var myIndex = 0;
carousel();

function carousel() {
  var i;
  var x = document.getElementsByClassName("mySlides");
  var y = document.getElementsByClassName("w3-button w3-white w3-border-red w3-large");
  var z = document.getElementsByClassName("slideHeading");
  for (i = 0; i < x.length; i++) {
    x[i].style.display = "none";
    y[i].style.display = "none"; 
    z[i].style.display = "none"; 
  }
  myIndex++;
  if (myIndex > x.length) {myIndex = 1}    
  x[myIndex-1].style.display = "block";
  y[myIndex-1].style.display = "block";
  z[myIndex-1].style.display = "block";  
  setTimeout(carousel, 4000); // Change image every 4 seconds
}