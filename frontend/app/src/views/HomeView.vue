<script setup lang="ts">
import { ref, onMounted, onUnmounted } from "vue";
import DpadLogo from "@/components/art/DpadLogo.vue";


const visitorCount = ref<number>(0);
const fetchVisitorCount = async () => {
  const resp = await fetch("/api/data", {
    method: "POST", 
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify(
      {
        dataId: "visitorCount"
      }
    )
  });
  const data = await resp.json();
  visitorCount.value = data.visitorCount;
}


const pageMode = ref("initial");
const setMode = (newMode) => {
  pageMode.value = newMode;
}

let loopInterval: number | undefined = undefined;
onMounted(async () => {
  await fetchVisitorCount(); 
  loopInterval = setInterval(async () => {
    await fetchVisitorCount(); 
  }, 20000);
});


onUnmounted(() => {
  clearInterval(loopInterval);
});
</script>

<template>
 
  <div id="content-wrapper">
    
    <template v-if="pageMode === 'initial'">
      
      <DpadLogo /> 
      
      <div id="visitor-count-container">
        <p>Player Count: {{ visitorCount }}</p> 
      </div>
    
      <div id="btn-wrapper" @click="setMode('login')">
        <button class="btn">Login</button>
      </div>
    
    </template>

    <template v-else-if="pageMode === 'login'">
     
      <div id="login-form-wrapper">

        <div class="form-row">
          <span>User Name:</span>
          <input type="text">
        </div>
        
        <div class="form-row">
          <span>Password:</span>
          <input type="text">
        </div>

      </div>

    </template>
  
  </div>

</template>

<style scoped> 
#logo-header {
  display: flex; 
  margin: 15px auto;
  width: 100%;
  justify-content: center;
}

#content-wrapper {
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-content: center;
  margin: 30px auto;
  width: 80%;
  height: 70%;
}

#visitor-count-container {
  display: flex;
  justify-content: center;
  font-size: 20px;
  color: var(--pink);
}

#btn-wrapper {
  display: flex;
  margin: auto;
  justify-content: center;
}

.form-row {
  display: flex;
  align-content: center;
}

@media (max-width: 640px) {
  #visitor-count-container {
    font-size: 12px;
  } 
}
</style> 

