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
    localStorage.setItem("css", mode.href);
  });
}