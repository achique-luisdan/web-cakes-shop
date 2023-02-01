<template>
  <section class="container">
    <h2 class="title">Promociones</h2>
    <div id="promotions">
      <article
        class="promotion"
        v-for="(product, index) in promotions"
        :key="index"
      >
        <img
          :src="product.image"
          alt=""
          height="200"
        />
        <header>
          <h3>{{ product.name }}</h3>
          <h3>
            ${{
              product.bestPromotion
                ? product.bestPromotion.price
                : product.price
            }}
          </h3>
          <h4 v-if="product.bestPromotion != undefined">
            ${{
              product.bestPromotion
                ? `
          ${product.price}
          `
                : ''
            }}
          </h4>
        </header>
        <div>
          {{ product.description ? product.description : 'Sin descripción' }}
        </div>
        <div>
          <button>Agregar al Carrito</button>
        </div>
      </article>
      <h2 v-if="message != ''">{{ message }}</h2>
    </div>
  </section>
</template>

<style></style>

<script lang="ts">
import type { Product } from '@/models/product';

export default {
  data() {
    return {
      promotions: Object as unknown as Product[],
      message: '',
    };
  },
  mounted() {
    this.getPromotions();
  },
  methods: {
    getPromotions() {
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
          this.promotions = data;
          if (this.promotions.length <= 0) {
            this.message = `No se encontraron productos disponibles.`;
          } else {
            this.message = '';
          }
        })
        .catch(error => {
          console.warn(error);
          this.message = `¡Ups! Algo salió mal [${error}]`;
        });
    },
  },
};
</script>
