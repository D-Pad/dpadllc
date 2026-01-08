<script setup lang="ts">
import { RouterLink, RouterView } from 'vue-router'
</script>

<template>

  <header>
    <div class="nav-bar-wrapper">
      <nav>
        <RouterLink to="/">Home</RouterLink>
        <RouterLink to="/about">About</RouterLink>
        <RouterLink to="/resume">Resume</RouterLink>
      </nav>
    </div>
  </header>

  <main>
    <RouterView />
  </main>

</template>

<style scoped>

</style>
