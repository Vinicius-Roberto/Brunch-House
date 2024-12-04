// script.js
const botoesAdicionar = document.querySelectorAll('.adicionar');
botoesAdicionar.forEach(botao => {
  botao.addEventListener('click', function() {
    const productId = this.dataset.productId;
  
    fetch(`/adicionar-ao-carrinho/${productId}`, {
      method: 'POST'
    })
    .then(response => response.json())
    .then(data => {
      if (data.success) {
        // Atualizar a quantidade na interface (se necessário)
        // ...
        window.location.reload(true)
      } else {
        alert('Erro ao adicionar produto ao carrinho.');
      }
    })
    .catch(error => {
      console.error('Error:', error);
    });
  });
})


// Selecionar todos os botões de remoção
const botoesRemover = document.querySelectorAll('.remover');

botoesRemover.forEach(botao => {
    botao.addEventListener('click', function() {
        const productId = this.dataset.productId;

        fetch(`/remover-do-carrinho/${productId}`, {
            method: 'POST'
        })
        .then(response => response.json())
        .then(data => {
            if (data.success) {
                // Remover o item da lista de produtos na página
                // Atualizar o total do carrinho (se necessário)
                // ...
                window.location.reload(true)
            } else {
                alert('Erro ao remover produto do carrinho: ' + data.error);
            }
        })
        .catch(error => {
            console.error('Error:', error);
            alert('Ocorreu um erro inesperado ao remover o produto.');
        });
    });
});
