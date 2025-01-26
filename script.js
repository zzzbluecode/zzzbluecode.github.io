// script.js
document.addEventListener('DOMContentLoaded', function () {
    // Load the left panel into the placeholder
    fetch('left-panel.html?t=1737916834')    // fetch left-panel.html
        .then(response => response.text())
        .then(data => {
            // Inject the left panel HTML
            document.getElementById('left-panel-placeholder').innerHTML = data;

            // Show the main-content after the left panel is loaded
            document.querySelector('.main-content').style.display = 'block';
        })
        .catch(error => {
            console.error('Error loading left panel:', error);
        });
});
