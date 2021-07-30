//Form Modal//

// Get modal by Id
window.addEventListener("load", () => {

  let modal = document.getElementById("modal");

  // Get the button that pops out the modal and form

  let formBtn = document.getElementById("form-btn");

  // Get the <span> element that closes the modal

  let closeForm = document.getElementById("close-form");

  // Form and modal open when button is clicked on 

  formBtn.onclick = function () {
    modal.style.display = "block";
  };

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

  // Actions to take when the contact form is submitted

  document.getElementById("contactForm").addEventListener("submit", function (event) {

    // If the event does not get explicitly handled, default action not taken

    event.preventDefault();

    // Send form information to the correct account and using the correct template and default email service

    emailjs.sendForm("gmail", "horror_house", this)


    //Sweet Alert
    
      // Show Sweet Alert pop-up and post-submit message

      .then(function () {
        swal("Hello there!", "We've recieved your message and will be back in touch soon", "success", {
          button: "Thank you!",
        });

        // Show a console error if form doesn't submit properly

      }, function (error) {
        swal("Oops", "Something went wrong!", "error")
        console.log("FAILED...", error);
      });

    // Reset form after submission   

    document.getElementById("contactForm").reset();
  });
});