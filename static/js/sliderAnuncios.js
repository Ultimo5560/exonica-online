// silder anuncios
let slider = document.querySelector(".slider__contenedor")
let sliderIndividual = document.querySelectorAll(".slider__contenido")
let contador = 1;
let intervalo = 6000;
let width = sliderIndividual[0].clientWidth;
window.addEventListener("resize", function(){
    width = sliderIndividual[0].clientWidth;
})

setInterval(function(){
    slides();
},intervalo);

function slides(){
    slider.style.transform = "translate("+(-width*contador)+"px)";
    slider.style.transition = "transform .8s";
    contador++;

    if(contador == sliderIndividual.length){
        setTimeout(function(){
            slider.style.transform = "translate(0px)";
            slider.style.transition = "transform .7s";
            contador=1;
        },6000)
    }
}