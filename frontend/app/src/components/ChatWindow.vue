<script setup lang="ts">
import { ref } from 'vue'
import { fetchAiResponse } from "@/assets/scripts/fetch_data.ts"; 

// Optional: example message storage
const messages = ref<string[]>([])
const userInput = ref('')

const textarea = ref<HTMLTextAreaElement | null>(null)

const resizeTextarea = () => {
  if (textarea.value) {
    textarea.value.style.height = 'auto'  // Reset to shrink if needed
    textarea.value.style.height = `${textarea.value.scrollHeight}px`
  }
}

function sendMessage() {
  if (!userInput.value.trim()) return
  messages.value.push(userInput.value)
  fetchAiResponse(userInput.value);
  userInput.value = ''
}
</script>

<template>
  <div class="chat-container">
    <div class="chat-window" id="chat-window">
      <div v-for="(msg, index) in messages" :key="index" class="message user">
        {{ msg }}
      </div>
    </div>

    <div class="input-container">
      <textarea
        ref="textarea"
        v-model="userInput"
        id="user-prompt"
        placeholder="Enter your prompt..."
        rows="1"
        @input="resizeTextarea"
        @keydown.enter.exact.prevent="sendMessage"
      />
      <button @click="sendMessage">Send</button>
    </div>
  </div>
</template>

<style scoped>
.chat-container {
  height: 80vh;
  display: flex;
  flex-direction: column;
  width: 70%;
  margin: auto;
}

.chat-window {
  flex: 1;                 
  overflow-y: auto;        
  display: flex;
  flex-direction: column;
  gap: 1rem;
}

.message {
  max-width: 80%;
  padding: 0.8rem 1.2rem;
  border-radius: 1.2rem;
}

.message.user {
  align-self: flex-end;
  background: var(--blue);
  color: white;
}

.input-container {
  display: flex;
  align-items: center;
  gap: 10px;
}

.input-container button {
  padding: 0.8rem 1.5rem;
  border-radius: 2rem;
  background: var(--red); /* or your theme color */
  color: white;
  border: none;
  cursor: pointer;
}

#user-prompt {
  flex: 1;
  padding: 12px 16px;
  border: 1px solid var(--red, #ff0040);
  border-radius: 24px;
  background: rgba(255, 255, 255, 0.05);
  color: #fff;
  font-size: 16px;
  outline: none;
  resize: none;          /* Disable manual resize handle */
  overflow: hidden;      /* Hide scrollbar while growing */
  min-height: 48px;      /* Minimum single-line height */
  max-height: 200px;     /* Optional: cap at ~8 lines to allow scrolling after */
  line-height: 1.5;      /* Helps smooth growth */
  transition: height 0.2s ease; /* Smooth animation */
  width: 80%;
}
</style>
