<template>

  <!-- src="@/assets/images/palms.png" -->
  <img 
    src="@/assets/images/neon_palm.png"
    alt="Palm Tree"
    id="palm-tree" 
  />
</template>

<style scoped>
#palm-tree {
  position: fixed;
  width: 1000px;
  height: auto;
  pointer-events: none;
  top: -100px;
  right: -200px;
  z-index: -1;
} 


@media (max-width: 640px) {
  #palm-tree {
    display: none;
  }
}
</style>

