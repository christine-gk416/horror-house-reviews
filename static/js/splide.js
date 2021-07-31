document.addEventListener('DOMContentLoaded', function () {
    new Splide( '.splide', {
        type   : 'loop',
        perPage: 3,
        focus  : 'center',

        breakpoints: {
            '812': {
                perPage: 2,
                gap    : '1rem',
            },
            '480': {
                perPage: 1,
                gap    : '1rem',
            },
        },

        i18n: {
            prev: 'Previous slide',
            next: 'Next slide',
        },
        slideFocus: true,



    } ).mount();
   
});


