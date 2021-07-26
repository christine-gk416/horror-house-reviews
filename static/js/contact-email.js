// Get modal by Id

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