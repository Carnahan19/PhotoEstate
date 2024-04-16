var slideIndex = 1;
showSlides(slideIndex);

// Función para controlar los slides siguientes/anteriores
function plusSlides(n) {
  showSlides(slideIndex += n);
}

// Función para mostrar el slide
function showSlides(n) {
  var i;
  var slides = document.getElementsByClassName("carrousel-slide");
  if (n > slides.length) {slideIndex = 1}
  if (n < 1) {slideIndex = slides.length}
  for (i = 0; i < slides.length; i++) {
      slides[i].style.display = "none";
  }
  slides[slideIndex-1].style.display = "block";
}