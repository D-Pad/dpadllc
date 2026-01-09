<script setup lang="ts">
import { RouterLink, RouterView } from 'vue-router'
import AlienHunter from "@/components/art/AlienBounty.vue"
</script>

<template>

  <header>
    <div class="nav-bar-wrapper visible-div">
      <nav>
        <RouterLink to="/">Home</RouterLink>
        <RouterLink to="/about">About</RouterLink>
        <RouterLink to="/resume">Resume</RouterLink>
      </nav>
    </div>
  </header>

  <main id="main-content-section" class="visible-div-light">
    <RouterView />
  </main>

  <footer id="footer" class="visible-div">
    <span>Built with Vue.js</span>
    <span>•</span>
    <span>© 2026 D-Pad LLC</span>
    <span>•</span>
    <span>All rights reserved</span>
  </footer>

  <AlienHunter />

</template>

<style scoped>
#main-content-section {
  align-items: center;
}

.nav-bar-wrapper {
  align-items: center;
  overflow: hidden;
}
</style>
