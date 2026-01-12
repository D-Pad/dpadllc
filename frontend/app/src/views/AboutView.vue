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
h1 {
  color: var(--cyan);
  margin: 5px auto;
}

a {
  margin: 0px auto;
}

p {
  font-size: 24px;
  font-family: monospace;
} 

#header-wrapper {
  display: flex;
}

.page-wrapper {
  display: flex;
  justify-content: center;
  width: 100%;           
  max-width: 1200px; 
  padding: 0 20px;       
  height: 100%;
  align-items: center; 
  margin: auto;        
}

.page-content {
  max-width: 75%;
}
</style>

