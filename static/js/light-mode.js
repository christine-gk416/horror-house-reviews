var lightMode = document.querySelector(".btn-toggle");
var mode = document.querySelector("#mode-link");

 lightMode.addEventListener("click", function() {
 
  if (mode.getAttribute("href") == "static/css/dark-mode.css") {
      mode.href = "static/css/light-mode.css";
    } else {
    mode.href = "static/css/dark-mode.css";
  }
});