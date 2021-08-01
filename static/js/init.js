(function($){
  $(function(){

    $('.sidenav').sidenav({
      edge: 'right',
    });
    $('.tooltipped').tooltip();
    $('.parallax').parallax();
  }); // end of document ready
})(jQuery); // end of jQuery name space

$(document).ready(function() {
  $("nav [href]").each(function() {
      if (this.href == window.location.href) {
          $(this).addClass("active");
      }
  });
});