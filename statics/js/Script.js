//Scripts do Banner

document.addEventListener('DOMContentLoaded', () => {
    const slides = document.querySelectorAll('.carousel-slide');
    const indicators = document.querySelectorAll('.indicator');
    let currentIndex = 0;

    // Função para mostrar a imagem ativa
    function changeSlide(index) {
        // Remover a classe 'active' de todas as imagens e indicadores
        slides.forEach((slide) => slide.classList.remove('active'));
        indicators.forEach((indicator) => indicator.classList.remove('active'));

        // Adicionar a classe 'active' à imagem e indicador correspondente
        slides[index].classList.add('active');
        indicators[index].classList.add('active');
    }

    // Função para mover para a próxima imagem
    function nextSlide() {
        currentIndex = (currentIndex + 1) % slides.length; // Volta ao primeiro slide após o último
        changeSlide(currentIndex);
    }

    // Iniciar o carrossel com intervalo automático
    let autoSlide = setInterval(nextSlide, 3000); // Muda a imagem a cada 3 segundos

    // Adicionar evento de clique nos indicadores
    indicators.forEach((indicator, index) => {
        indicator.addEventListener('click', () => {
            clearInterval(autoSlide); // Para a mudança automática ao clicar no indicador
            changeSlide(index);
            autoSlide = setInterval(nextSlide, 3000); // Reinicia o carrossel após o clique
        });
    });
});
