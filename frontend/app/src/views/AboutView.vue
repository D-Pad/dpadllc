<script setup lang="ts">
import { ref } from 'vue';

const section = ref<string>("services");

const setSection = (newSection: string) => {
  section.value = newSection;
}
</script>

<template>
  
  <div class="page-wrapper">
    
    <div class="page-content">

      <div id="inner-nav-wrapper">
        <div class="visible-div" id="inner-nav">
          <div 
            @click="setSection('services')" 
            class="nav-btn-main inner-nav-btn"
          >
            Services
          </div>
          <div 
            @click="setSection('contact')" 
            class="nav-btn-main inner-nav-btn"
          >
            Contact
          </div>
          <div 
            @click="setSection('about')" 
            class="nav-btn-main inner-nav-btn"
          >
            About
          </div>
        </div>
      </div>

      <template v-if="section === 'services'">
        
        <div id="header-wrapper">
          <h1>Services</h1>
        </div>

        <p>
          We offer a variety of tech related services at D-Pad LLC, from 
          computer repairs and custom PC builds, to software engineering 
          services and website design.
        </p>

      </template>

      <template v-else-if="section === 'about'">

        <div id="header-wrapper">
          <h1>About D-Pad LLC</h1>
        </div>

        <p>
          D-Pad LLC is a small, independent software development and graphic 
          design studio based in Marion, Arkansas. We specialize in designing 
          and delivering production-ready web applications with clean 
          architecture, reliable infrastructure, and polished visual 
          design.
        </p>
        
        <p>
          The studio is owned and operated by husband-and-wife team Chase and 
          Alecia Fincher. Chase is a full-stack developer with over four years 
          of professional experience building and deploying modern, 
          containerized web applications. His work spans backend services, 
          database design, real-time systems, single-page frontend applications, 
          and Linux-based production infrastructure.
        </p>
        
        <p>
          Alongside software development, D-Pad LLC offers professional graphic 
          design services, helping ensure that every project is not only 
          technically sound but also visually cohesive and user-focused.
        </p>
        
        <p>
          As a small team, we take a hands-on, detail-oriented approach to 
          every project. We work directly with our clients to create solutions 
          that are maintainable, performant, and built to last. Our services 
          are available through contract engagements.
        </p>
   
      </template>

      <template v-else-if="section === 'contact'">

        <div id="header-wrapper">
          <h1>Contact Information</h1>
        </div>

        <div id="contact-wrapper">
          <div class="contact-row">
            <div class="contact-left">Email:</div>
            <div class="contact-right">dpadllc@proton.me</div>
          </div>
          
          <div class="contact-row">
            <div class="contact-left">Phone:</div>
            <div class="contact-right">(901)-422-3400</div>
          </div>
        </div>
        
        <p>
          Please message us on Facebook if possible. Otherwise, feel free to 
          call us. We don't check emails as often as other sources.
        </p>

      </template>
    
    </div>
  
  </div>

</template>


<style scoped>
html, body {
  height: 100%;
  margin: 0;
  padding: 0;
  overflow: hidden;
}

#inner-nav-wrapper {
  display: flex;
  margin: 0px auto 30px auto;
  justify-content: center;
}

#inner-nav {
  display: flex;
  gap: 20px;
  justify-content: center;
  padding: 0px 40px;
  border-radius: 30px;
  font-size: 18px;
  color: var(--red);
}

.page-wrapper {
  display: flex;
  justify-content: center;
  align-items: center;    
  width: 100%;
  max-width: 1200px;
  height: 75dvh;          
  max-height: 75dvh;
  margin: 0 auto;
  padding: 0 20px;
  overflow: hidden;
  box-sizing: border-box;
}

.page-content {
  width: 100%;                
  height: 100%;               
  overflow-y: auto;           
  overflow-x: hidden;

  -webkit-overflow-scrolling: touch;

  padding: 1.5rem;   
  box-sizing: border-box;
}

.inner-nav-btn:hover {
  cursor: pointer; 
}

p {
  font-size: 24px;
  font-family: monospace;
  margin: 1em 0;
  line-height: 1.5;
}

h1 {
  color: var(--cyan);
  margin: 5px auto;
}

#header-wrapper {
  display: flex;
  justify-content: center;  
  text-align: center;
}

#contact-wrapper {
  margin: 30px 0px 50px 0px;
}

.contact-row {
  display: flex;
  width: 70%;
  justify-content: center;
  margin: 10px auto;
  font-size: 32px;
  font-family: monospace;
}

.contact-left {
  width: 40%;
  text-align: right;
  color: var(--pink);
}

.contact-right {
  width: 60%;
  padding-left: 20px;
}

@media (max-width: 640px) {
  .page-content p {
    font-size: 16px;    
  }

  .page-content h1 {
    font-size: 18px;    
  }

  .page-wrapper {
    max-height: 40vh;
  }

  .form-row, .form-row input {
    font-size: 10px;
    flex-direction: column;
    justify-content: left;
    padding: 0.2rem;
  }

  .form-row {
    height: 40vh;
    display: block;
  }

  .form-label {
    width: 100%;
    text-align: left;
  }

}
</style>

