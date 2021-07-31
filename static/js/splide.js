document.addEventListener( 'DOMContentLoaded', function () {
    new Splide( '.splide', {
        type   : 'loop',
        perPage: 3,
        focus  : 'center',
        i18n: {
            prev: 'Previous slide',
            next: 'Next slide',
        },
        slideFocus : true, 
    } ).mount();
} );


