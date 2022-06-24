// silder 'lo nuevo'
function App() {}

window.onload = function (event) {
    var app = new App();
    window.app = app;
};

App.prototype.processingButton = function(event) {
    const btn = event.currentTarget;
    const slickList = event.currentTarget.parentNode;
    const track = event.currentTarget.parentNode.querySelector('#track');
    const slick = track.querySelectorAll('.slick');
    const slickWidth = slick[0].offsetWidth;
    const trackWidth = track.offsetWidth;
    const listWidth = slickList.offsetWidth;

    track.style.left == ""  ? leftPosition = track.style.left = 0 : leftPosition = parseFloat(track.style.left.slice(0, -2) * -1);

    btn.dataset.button == "button-prev" ? prevAction(leftPosition,slickWidth,track) : nextAction(leftPosition,trackWidth,listWidth,slickWidth,track)
}

let prevAction = (leftPosition,slickWidth,track) => {
    if(leftPosition > 0) {
        console.log("entro 2")
        track.style.left = `${-1 * (leftPosition - slickWidth)}px`;
    }
}

let nextAction = (leftPosition,trackWidth,listWidth,slickWidth,track) => {
    if(leftPosition < (trackWidth - listWidth)) {
        track.style.left = `${-1 * (leftPosition + slickWidth)}px`;
    }
}


// menu desplegable
const menuBoton = document.querySelector('.nav__astyle2');
const menuDespl = document.querySelector('.nav__items');
const despl =  document.querySelectorAll('.list__button--click')
const listArrow = document.querySelectorAll('.list__item')

document.addEventListener('click', (event) =>{
    if (event.path[0] == menuBoton || menuDespl in [event.path]) {
        menuDespl.classList.toggle('open')
    } else if (event.path[1].classList[0] === despl[1].classList[0] || event.path[1].classList[0] === listArrow[1].classList[0]) {
        // no hace nada
    } else {
        menuDespl.classList.remove('open')
    }
});


// menu desplegable flechas
let listElements = document.querySelectorAll('.list__button--click');
listElements.forEach(listElement => {
    listElement.addEventListener('click', ()=>{
        
        listElement.classList.toggle('arrow');

        let height = 0;
        let menu = listElement.nextElementSibling;
        if(menu.clientHeight == "0"){
            height=menu.scrollHeight;
        }

        menu.style.height = `${height}px`;

    })
});