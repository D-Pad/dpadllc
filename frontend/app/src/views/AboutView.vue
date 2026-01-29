<script setup lang="ts">
  
</script>

<template>
  
  <div class="page-wrapper">
    
    <div class="page-content">

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

}
</style>

