// Toggles light mode / dark mode if button is clicked

window.onload = function () {

  var lightMode = document.querySelector(".btn-toggle");
  var mode = document.querySelector("#mode-link");
  var selected = localStorage.getItem("css");
    if (selected !== null) {
      mode.href = selected;
    } 


  lightMode.addEventListener("click", function () {

    if (mode.getAttribute("href") == "/static/css/dark-mode.css") {
      mode.href = "/static/css/light-mode.css";
    } else {
      mode.href = "/static/css/dark-mode.css";
    }

    // Adds the light / dark mode settings to local storage to run on Flask
    localStorage.setItem("css", mode.href);
  });
};