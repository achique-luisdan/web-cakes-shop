<template>
  <section class="container">
    <h2 class="title">Productos</h2>
    <div id="products"></div>
  </section>
</template>

<style></style>

<script lang="ts">
export default {
  data() {
    return {
      promotions: [],
    };
  },
  mounted() {
    this.getPromotions();
  },
  methods: {
    getPromotions() {
      let $products = document.getElementById('products');
      let url = 'http://localhost:3000/api/products';
      fetch(url)
        .then(response => {
          if (response.status === 200) {
            return response.json();
          } else {
            return [];
          }
        })
        .then(data => {
          const products = data;
          $products.innerHTML = '';
          products.forEach(
            (product: {
              [x: string]: any;
              image: any;
              name: any;
              price: any;
              description: any;
            }) => {
              $products.innerHTML += `
                <article class="promotion">
                  <img src="${product.image}" alt="" height="200">
                  <header>
                    <h3>${product.name}</h3>
                    <h3>$${
                      product.bestPromotion
                        ? product.bestPromotion.price
                        : product.price
                    }</h3>
                    ${
                      product.bestPromotion
                        ? '<h4>$' + product.price + '</h4>'
                        : ''
                    }
                  </header>
                  <div>
                  ${
                    product.description
                      ? product.description
                      : 'Sin descripción'
                  }
                  </div>
                  <div>
                    <button>Agregar al Carrito</button>
                  </div>
                </article>
              `;
            }
          );
          if (products.length <= 0) {
            $products.innerHTML = `No se encontraron promociones disponibles.`;
          }
        })
        .catch(error => {
          console.warn(error);
          $products.innerHTML = `¡Ups! Algo salió mal [${error}]`;
        });
    },
  },
};
</script>
