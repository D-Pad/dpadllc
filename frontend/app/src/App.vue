<script setup lang="ts">
import { RouterLink, RouterView } from 'vue-router'
import AlienHunter from "@/components/art/AlienBounty.vue"
</script>

<template>

  <header>
    <div class="nav-bar-wrapper visible-div">
      <nav>
        <div>
          <RouterLink class="nav-btn-main" to="/">Home</RouterLink>
          <RouterLink class="nav-btn-main" to="/chat">Chat</RouterLink>
        </div>
        <div>
          <RouterLink class="nav-btn-main" to="/about">About Us</RouterLink>
          <a 
            class="nav-btn-main"
            href="/dpad_llc_resume.pdf"
            target="_blank"
            rel="noopener"
          >
            Resume
          </a>
        </div> 
      </nav>
    </div>
  </header>

  <main id="main-content-section" class="visible-div-light">
    <RouterView v-slot="{ Component }">
      <keep-alive> 
        <component :is="Component" /> 
      </keep-alive>
    </RouterView> 
  </main>

  <div id="footer-wrapper">
    <footer id="footer" class="visible-div">
      <span>Built with Vue.js</span>
      <span>•</span>
      <span>© 2026 D-Pad LLC</span>
      <span>•</span>
      <span>All rights reserved</span>
    </footer>
  </div>

  <div id="social-media-wrapper">
    <div id="social-media-icon-row">
      <a 
        href="https://github.com/D-Pad"
        target="_blank"
        rel="noopener noreferrer"
      > 
        <img 
          class="social-media-icon" 
          src="@/assets/images/github.png" 
          alt="github" 
        />
      </a>
      <a 
        href="https://www.linkedin.com/in/chase-fincher-6770573a5/"
        target="_blank"
        rel="noopener noreferrer"
      > 
        <img 
          class="social-media-icon" 
          src="@/assets/images/linkdin.png" 
          alt="linkdin" 
        />
      </a>
    </div>
  </div>

  <AlienHunter />

  <div class="crt-overlay"></div>

</template>

<style scoped>
#main-content-section {
  align-items: center;
  margin-top: 10px; 
  padding: 5px;
}

#footer {
  margin-top: 30px;
  width: 100%;
  max-width: 1000px;
  border-radius: 20px;
  padding: 10px 40px;
  font-size: 14px;
  text-align: center;
}

#footer-wrapper {
  display: flex;
  justify-content: center;
  margin: 0px auto;
}

nav {
  display: flex;
  justify-content: space-around;
  align-items: center;
  gap: 16px;
}

.nav-bar-wrapper {
  align-items: center;
  overflow: hidden;
  border-radius: 30px;
  width: 100%;
  max-width: 700px;
  font-size: 18px;
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

#social-media-wrapper {
  width: 100%;
  margin: 30px auto 20px; 
  text-align: center;     
  z-index: 9999;
}

#social-media-icon-row {
  display: inline-block;    
}

.social-media-icon {
  width: 40px;
  height: auto;
  margin: 0 20px;
  vertical-align: middle;
  border-radius: 20px;

  box-shadow: 0 0 0 0 var(--cyan);
  transition: 
    box-shadow 0.4s ease,
    transform 0.3s ease;   
}

.social-media-icon:hover {
  box-shadow: 0 0 8px 4px var(--cyan);
  transform: scale(1.12);   
  cursor: pointer;
}

@media (max-width: 640px) {
  nav {
    flex-direction: column;
  }

  .nav-btn-main {
    width: 100%;
    text-align: center;
  }
}
</style>
