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
        
        <h2>Software and Hardware</h2>
        <p>
          We offer a wide range of technology services at D-Pad LLC, tailored 
          for individuals, small businesses, and growing organizations. From 
          computer repairs and custom PC builds to advanced software 
          engineering and website development, we provide reliable solutions 
          designed to keep your systems running smoothly. Whether you need 
          virus removal, hardware upgrades, operating system installations, 
          or soldering repairs on small electronics, we bring years of 
          hands-on technical experience to every project. Software development 
          is our specialty, and we take pride in building efficient, scalable 
          solutions that solve real-world problems.
        </p>

        <h2>Graphic Design</h2>
        <p>
          In addition to technical services, we also offer professional 
          graphic design. With an experienced designer on our team, we can 
          help with branding, logos, marketing materials, and digital design 
          needs. Ensuring your technology and visual identity work 
          seamlessly together. At D-Pad LLC, our goal is simple: provide 
          complete, dependable tech and design services all in one place.
        </p>

      </template>

      <template v-else-if="section === 'about'">

        <div id="header-wrapper">
          <h1>About D-Pad LLC</h1>
        </div>

        <p>
          D-Pad LLC is a small, independent software development, electronic 
          harware repair, and graphic design studio based in Marion, Arkansas. 
          We specialize in designing and delivering production-ready web 
          applications with clean architecture, reliable infrastructure, and 
          polished visual design.
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

        <div id="contact-wrapper">
          <div class="contact-row">
            <div class="contact-left">Email:</div>
            <div class="contact-right">
              <a href="mailto:dpadllc@proton.me" class="contact-link">
                dpadllc@proton.me
              </a>
            </div>
          </div>
          
          <div class="contact-row">
            <div class="contact-left">Phone:</div>
            <div class="contact-right">
              <a href="tel:+19014223400" class="contact-link">
                (901)-422-3400
              </a>
            </div>
          </div>
        </div>
        
        <p>
          Messaging us on  
          <a href="https://www.facebook.com/profile.php?id=61587323279371">
            Facebook</a> is more reliable than email. Phone calls or text 
          messages are best. 
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
  margin: 0px auto 50px auto;
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

h2 {
  color: var(--yellow);
  font-size: 24px;
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

.contact-link {
  color: var(--cyan);
}

@media (max-width: 640px) {
 
  .contact-row {
    font-size: 16px;
  }
  
  .page-content p {
    font-size: 16px;    
  }

  .page-content h1 {
    font-size: 18px;    
  }

  .page-content h2 {
    font-size: 16px;
  }

  .page-wrapper {
    max-height: 40vh;
    padding: 0px; 
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

  #inner-nav-wrapper {
    display: flex;
    margin: 0px auto 20px auto;
    justify-content: center;
  }

  #inner-nav {
    font-size: 12px;
    gap: 0px;
    padding: 0px; 
  }

  .inner-nav-btn {
    padding: 5px;
  }

  #contact-wrapper {
    margin: 20px 0px;
  }
  
  .contact-row {
    justify-content: none;
    text-align: left;
  }

  .contact-left {
    width: 10%;
  }

  .contact-right {
    margin-left: 20px; 
    width: 90%;
  }

}
</style>

