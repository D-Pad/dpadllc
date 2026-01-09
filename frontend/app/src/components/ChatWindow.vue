<script setup lang="ts">
import { ref } from 'vue'
import { fetchAiResponse } from "@/assets/scripts/fetch_data.ts"; 


const messages = ref<string[]>([])
const userInput = ref('')
const textarea = ref<HTMLTextAreaElement | null>(null)


const resizeTextarea = () => {
  if (textarea.value) {
    textarea.value.style.height = 'auto'  // Reset to shrink if needed
    textarea.value.style.height = `${textarea.value.scrollHeight}px`
  }
}


const sendMessage = () => {
  if (!userInput.value.trim()) return
  messages.value.push({ role: "user", content: userInput.value });
  fetchAiResponse(userInput.value);
  userInput.value = ''
}


const API_URL = import.meta.env.VITE_API_URL;


const fetchingResponse = ref(false);
const fetchAiResponse = async (prompt: str) => {

  fetchingResponse.value = true;
  messages.value.push({ role: "system", content: "" });
  
  const payload = {
    prompt: prompt
  };
  
  const response = await fetch(`${API_URL}/chat`, {
    method: "POST",
    headers: {
      "Content-Type": "application/json"
    },
    body: JSON.stringify(payload)
  });

  if (!response.ok) {
    throw new Error(`API Request error: ${resp.status}`);
  }

  const reader = response.body.getReader();
  const decoder = new TextDecoder();

  const index = messages.value.length - 1;
  while (true) {
    
    const { value, done } = await reader.read();
    if (done) break;
    
    const chunk = decoder.decode(value);
    messages.value[index].content += chunk; 
  };

  fetchingResponse.value = false;
}

const formatMessage = (text: string) => {
  return text
    .replace(/```([\s\S]*?)```/g, '<pre><code>$1</code></pre>')
    .replace(/\n/g, '<br>')
    .replace(
      /https?:\/\/[^\s<]+/g, 
      '<a href="$&" target="_blank" rel="noopener">$&</a>'
    );
}
</script>

<template>
  <div class="chat-container">
    <div class="chat-window" id="chat-window">
      <div 
        v-for="(msg, index) in messages"
        :key="index" 
        class="message-wrapper"
      >
        <div 
          class="message" 
          :class="{ user: msg.role === 'user', assistant: msg.role !== 'user' }"
        >
          <div 
            class="message-content" 
            v-html="formatMessage(msg.content)"
          >
          </div>
      
        </div>
      </div>
    </div>

    <div v-if="!fetchingResponse" class="input-container">
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
  width: 100%;
  max-width: 900px;           /* ← very important! */
  margin: 0 auto;
  display: flex;
  flex-direction: column;
  overflow: hidden;           /* ← prevents weird leaks */
}

.chat-window {
  flex: 1;
  overflow-y: auto;
  overflow-x: hidden;         /* ← crucial! */
  padding: 1rem;
  display: flex;
  flex-direction: column;
  gap: 1.2rem;
  width: 100%;
}

.message-wrapper {
  display: flex;
  width: 100%;
}

.message {
  max-width: 82%;             /* ← very important constraint */
  padding: 0.9rem 1.3rem;
  border-radius: 1.3rem;
  font-size: 1rem;
  line-height: 1.45;
  overflow-wrap: break-word;  /* modern & best */
  word-break: break-word;     /* fallback */
  hyphens: auto;              /* bonus for long words */
  width: fit-content;         /* ← very important! */
}

.message.user {
  margin-left: auto;
  background: var(--blue, #3b82f6);
  color: white;
  border-bottom-right-radius: 0.4rem;
}

.message.assistant {
  margin-right: auto;
  background: var(--gray-700, #374151);
  color: white;
  border-bottom-left-radius: 0.4rem;
}

/* Very important for newlines & code */
.message-content {
  white-space: pre-wrap;      /* keeps \n + wraps long lines */
  word-break: break-word;
}

/* Optional but very nice for code blocks */
.message-content pre {
  background: #1e293b;
  padding: 1rem;
  border-radius: 0.6rem;
  overflow-x: auto;
  margin: 0.8rem 0;
}

.message-content code {
  font-family: 'Consolas', 'Monaco', monospace;
  font-size: 0.92em;
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
