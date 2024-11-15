let currentIndex = 0;
const slides = document.querySelectorAll('.carousel-slide');
const indicators = document.querySelectorAll('.indicator');

// Função para mostrar a imagem atual e esconder as outras
function showSlide(index) {
    // Remove a classe 'active' de todos os slides e indicadores
    slides.forEach(slide => slide.classList.remove('active'));
    indicators.forEach(indicator => indicator.classList.remove('active'));

    // Adiciona a classe 'active' ao slide e indicador corretos
    slides[index].classList.add('active');
    indicators[index].classList.add('active');
}

// Função para mover para o próximo slide
function nextSlide() {
    currentIndex = (currentIndex + 1) % slides.length;
    showSlide(currentIndex);
}

// Função para mover para o slide anterior
function prevSlide() {
    currentIndex = (currentIndex - 1 + slides.length) % slides.length;
    showSlide(currentIndex);
}

// Alterna os slides automaticamente a cada 5 segundos
setInterval(nextSlide, 5000);

// Adiciona os eventos de clique nos indicadores
indicators.forEach((indicator, index) => {
    indicator.addEventListener('click', () => {
        currentIndex = index;
        showSlide(currentIndex);
    });
});

// Exibe o slide inicial
showSlide(currentIndex);
