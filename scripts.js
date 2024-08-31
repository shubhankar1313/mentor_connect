let currentSlide = 0;

function showSlide(index) {
    const slides = document.querySelectorAll('.slide');
    if (index >= slides.length) currentSlide = 0;
    if (index < 0) currentSlide = slides.length - 1;
    slides.forEach(slide => slide.style.transform = `translateX(-${currentSlide * 100}%)`);
}

setInterval(() => {
    currentSlide++;
    showSlide(currentSlide);
}, 3000);