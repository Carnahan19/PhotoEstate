// This function is called for each container to set up the slider functionality
function initializeSlider(container) {
  // Find the slider input within the current container
  const slider = container.querySelector('.slider');

  // Update the --position variable of the current container based on the slider's value
  slider.addEventListener('input', (e) => {
    const newPosition = `${e.target.value}%`;
    container.style.setProperty('--position', newPosition);
  });
}

// Run the initializeSlider function for each container on the page
document.addEventListener('DOMContentLoaded', (e) => {
  document.querySelectorAll('.container').forEach(initializeSlider);
});