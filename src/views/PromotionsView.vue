<template>
  <div>
    <section class="container">
      <h2 class="title">Promociones</h2>
      <div id="promotions"></div>
    </section>
  </div>
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
      let $promotions = document.getElementById('promotions');
      // http://127.0.0.1:8000/promotions
      let url = 'http://localhost:3000/api/promotions';
      fetch(url)
        .then(response => {
          if (response.status === 200) {
            return response.json();
          } else {
            return [];
          }
        })
        .then(data => {
          const promotions = data;
          $promotions.innerHTML = '';
          promotions.forEach(productElement => {
            $promotions.innerHTML += `
                <article class="promotion">
                  <img src="${productElement.image}" alt="" height="200">
                  <header>
                    <h3>${productElement.name}</h3>
                    <h3>$${productElement.promotion.price}</h3>
                  </header>
                  <div>
                  ${productElement.description}
                  </div>
                  <div>
                    <button>Pedir Ahora</button>
                  </div>
                </article>
              `;
          });
          if (promotions.length <= 0) {
            $promotions.innerHTML = `No se encontraron promociones disponibles.`;
          }
        })
        .catch(error => {
          console.warn(error);
          $promotions.innerHTML = `¡Ups! Algo salió mal [${error}]`;
        });
    },
  },
};
</script>
