<template>
  <header>
    <nav>
      <RouterLink to="/">
        <img
          src="src/assets/images/logo.svg"
          alt="Logo"
        />
      </RouterLink>
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
</template>

<script lang="ts">
// eslint-disable-next-line @typescript-eslint/no-unused-vars
import { RouterLink } from 'vue-router';
export default {};
</script>
