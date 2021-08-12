//Form Modal//

// Open form and modal on click
window.addEventListener("load", () => {

  let modal = document.getElementById("modal");
  let formBtn = document.getElementById("form-btn");
  let closeForm = document.getElementById("close-form");

  formBtn.onclick = function () {
    modal.style.display = "block";
  };

  //Open form if button is hightlighted by keyboard tabs by pressing Enter

  formBtn.addEventListener("keyup", function (event) {
    event.preventDefault();
    if (event.key === "Enter") {
      document.getElementById("form-btn").click();
    }
  });

  // Form and modal close when <span> element is clicked on
  closeForm.onclick = function () {
    modal.style.display = "none";
  };

  // Form closes if anywhere outside the form is clicked

  window.onclick = function (event) {
    if (event.target == modal) {
      modal.style.display = "none";
    }
  };


  //Default EmailJS

  document.getElementById("contactForm").addEventListener("submit", function (event) {
    event.preventDefault();
    emailjs.sendForm("gmail", "horror_house", this)


      //Sweet Alert

      .then(function () {
        swal("Hello there!", "We've recieved your message and will be back in touch soon", "success", {
          button: "Thank you!",
        });

      }, function (error) {
        swal("Oops", "Something went wrong!", "error");
      });

    // Reset form after submission   

    document.getElementById("contactForm").reset();
  });
});