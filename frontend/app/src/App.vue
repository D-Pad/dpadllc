<script setup lang="ts">
import { RouterLink, RouterView } from 'vue-router'
import AlienHunter from "@/components/art/AlienBounty.vue"
</script>

<template>

  <header>
    <div class="nav-bar-wrapper visible-div">
      <nav>
        <RouterLink to="/">Home</RouterLink>
        <RouterLink to="/about">About Us</RouterLink>
        <a
          href="/dpad_llc_resume.pdf"
          target="_blank"
          rel="noopener"
        >
          Resume
        </a>
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

  <div class="crt-overlay"></div>

</template>

<style scoped>
#main-content-section {
  align-items: center;
  padding: 5px;
}

#footer {
  margin-top: 30px;
}

.nav-bar-wrapper {
  align-items: center;
  overflow: hidden;
  border-radius: 30px;
  width: 400px; 
}

.crt-overlay {
  position: fixed;
  inset: 0;
  pointer-events: none;           
  z-index: 2;                  
  background: repeating-linear-gradient(
    to bottom,
    transparent 0,
    transparent 3px,
    rgba(0, 0, 0, 0.15) 3px,
    rgba(0, 0, 0, 0.15) 6px
  );
  background-size: 100% 6px;
  mix-blend-mode: multiply;       
  opacity: 0.75;
  image-rendering: pixelated;     
}

.crt-overlay::after {
  content: "";
  position: absolute;
  inset: 0;
  background: linear-gradient(
    to bottom,
    transparent 0%,
    rgba(255, 255, 255, 0.08) 8%,
    transparent 25%
  );
  animation: scan 10s linear infinite;
  pointer-events: none;
}

@keyframes scan {
  0% {
    transform: translateY(-120%);
  }
  100% {
    transform: translateY(120vh);
  }
}
</style>
