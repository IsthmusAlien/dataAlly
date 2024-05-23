let minPriceInput = document.getElementById('min-price');
let maxPriceInput = document.getElementById('max-price');
let minPriceVal = document.getElementById('min-price-val');
let maxPriceVal = document.getElementById('max-price-val');
let sliderTrack = document.querySelector('.track');

let Info_con = document.querySelector('.detailed_info_con');
let Card = document.querySelector('.Card');

function detect(){
    minPriceVal.textContent = minPriceInput.value
    maxPriceVal.textContent = maxPriceInput.value
}

function gayab(){
    Info_con.style.display = 'none';
}

function show(){
    Info_con.style.display = "block";
}

setInterval(detect, 500);