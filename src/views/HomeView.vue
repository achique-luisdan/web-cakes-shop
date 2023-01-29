<template>
  <header>
    <nav>
      <img
        src="src/assets/images/logo.svg"
        alt="Logo"
      />
      <ul>
        <li>
          <RouterLink to="/promotions">Promociones</RouterLink>
        </li>
        <li>
          <RouterLink to="/products">Productos</RouterLink>
        </li>
        <li>
          <a href="#">Pedidos</a>
        </li>
      </ul>
    </nav>
  </header>
  <main>
    <section class="row hero">
      <div class="column">
        <h2 class="title">¡Endulzamos los mejores momentos con tu familia!</h2>
        <h3>Dulces y juntos siempre.</h3>
        <div class="wrapper">
          <button>Pedir Ahora</button>
        </div>
      </div>
      <div class="column">
        <article class="slider">
          <img
            src="src/assets/images/cake1.jpg"
            alt="Torta 1"
            class="slide"
          />
          <img
            src="src/assets/images/cake2.jpg"
            alt="Torta 2"
            class="slide"
          />
          <img
            src="src/assets/images/cake3.jpg"
            alt="Torta 3"
            class="slide"
          />
        </article>
        <div class="indicators">
          <button
            class="indicator"
            @click="currentDiv(1)"
          ></button>
          <button
            class="indicator"
            @click="currentDiv(2)"
          ></button>
          <button
            class="indicator"
            @click="currentDiv(3)"
          ></button>
        </div>
      </div>
    </section>
  </main>
  <footer>
    <div>
      <img
        src="src/assets/images/logo.svg"
        alt="Logo"
      />
      <ul>
        <li>
          <a href="#">
            <img
              src="src/assets/images/facebook.png"
              alt="Ir a Facebook"
            />
          </a>
        </li>
        <li>
          <a href="#">
            <img
              src="src/assets/images/twitter.png"
              alt="Ir a Twitter"
            />
          </a>
        </li>
        <li>
          <a href="#">
            <img
              src="src/assets/images/instagram.png"
              alt="Ir a Instagram"
            />
          </a>
        </li>
      </ul>
    </div>
    <div>
      <hr />
      <h5>Cakes Shop (C) 2022. Todos los derechos reservados.</h5>
    </div>
  </footer>
</template>

<script lang="ts">
import { RouterLink } from 'vue-router';
export default {
  data() {
    return {
      slideIndex: 0,
    };
  },
  mounted() {
    this.carousel();
  },
  methods: {
    carousel() {
      let x = document.getElementsByClassName('slide');
      for (let i = 0; i < x.length; i++) {
        x[i].style.display = 'none';
      }
      this.slideIndex++;
      if (this.slideIndex > x.length) {
        this.slideIndex = 1;
      }
      x[this.slideIndex - 1].style.display = 'block';
      this.currentDiv(this.slideIndex);
      setTimeout(this.carousel, 4000); // 10 seconds
    },

    plusDivs(n: number) {
      this.showDivs((this.slideIndex += n));
    },

    currentDiv(n: number) {
      this.showDivs((this.slideIndex = n));
    },

    showDivs(n: number) {
      let i;
      var x = document.getElementsByClassName('slide');
      var dots = document.getElementsByClassName('indicator');
      if (n > x.length) {
        this.slideIndex = 1;
      }
      if (n < 1) {
        this.slideIndex = x.length;
      }
      for (i = 0; i < x.length; i++) {
        x[i].style.display = 'none';
      }
      for (i = 0; i < dots.length; i++) {
        dots[i].className = dots[i].className.replace('active', '');
      }
      x[this.slideIndex - 1].style.display = 'block';
      dots[this.slideIndex - 1].className += ' active';
    },
  },
};
</script>
