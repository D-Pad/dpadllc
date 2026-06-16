<script setup lang="ts">

</script>

<template>

  <div id="resume-wrapper">
  
    <h1>My Resumes</h1>
  
    <p>
      Click either of the links below to view the corresponding resume. 
    </p>

    <div id="bullet-list">
      <ul>
        <li>
          <a  
            class="resume_link"
            href="/SWE_Resume.pdf"
            target="_blank"
            rel="noopener">
            Full Stack Developer
          </a>
        </li>

        <li>
          <a  
            class="resume_link"
            href="/Machinist_Resume.pdf"
            target="_blank"
            rel="noopener">
            CNC Machinist
          </a>
        </li>
      </ul>
    </div>

  </div>

</template>

<style scoped>
#resume-wrapper {
  margin: auto;
  align-content: center;
  font-size: 16px;
}

h1 {
  margin: auto;
  text-align: center;
}

p {
  margin: 10px auto;
  width: 75%;
  text-align: center;
}

#bullet-list {
  display: flex;
  justify-content: center;
  align-items: center;
  margin: auto; 
}

li {
  margin-bottom: 10px;
} 


@media (max-width: 640px) {
  #resume-wrapper {
    font-size: 12px;
  }
}
</style>

