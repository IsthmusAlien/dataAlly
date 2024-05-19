let minPriceInput = document.getElementById('min-price');
let maxPriceInput = document.getElementById('max-price');
let minPriceVal = document.getElementById('min-price-val');
let maxPriceVal = document.getElementById('max-price-val');
let sliderTrack = document.querySelector('.track');

function detect(){
    minPriceVal.textContent = minPriceInput.value
    maxPriceVal.textContent = maxPriceInput.value
}

setInterval(detect, 500);