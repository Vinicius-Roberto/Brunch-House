// script.js
document.getElementById('adicionar-carrinho').addEventListener('click', function() {
    const productId = this.dataset.productId;
  
    fetch(`/adicionar-ao-carrinho/${productId}`, {
      method: 'POST'
    })
    .then(response => response.json())
    .then(data => {
      if (data.success) {
        // Atualizar a quantidade na interface (se necessário)
        // ...
        alert('Produto adicionado ao carrinho!');
      } else {
        alert('Erro ao adicionar produto ao carrinho.');
      }
    })
    .catch(error => {
      console.error('Error:', error);
    });
  });