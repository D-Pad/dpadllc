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
    
    <DpadLogo /> 
    
    <div id="visitor-count-container">
      <p>Player Count: {{ visitorCount }}</p> 
    </div> 
  
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

@media (max-width: 640px) {
  #visitor-count-container {
    font-size: 12px;
  } 
}
</style> 

