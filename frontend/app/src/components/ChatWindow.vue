<script setup lang="ts">
import { ref, onMounted, nextTick, watch } from 'vue'


const messages = ref<{ role: 'user' | 'system'; content: string }[]>([])
const userInput = ref('')
const textarea = ref<HTMLTextAreaElement | null>(null)
const chatWindow = ref<HTMLDivElement | null>(null)


watch(messages, async () => {
  await nextTick();
  const el = chatWindow.value;
  if (el) el.scrollTop = el.scrollHeight;
}, { deep: true });


const resizeTextarea = () => {
  if (textarea.value) {
    textarea.value.style.height = 'auto'  // Reset to shrink if needed
    textarea.value.style.height = `${textarea.value.scrollHeight}px`
  }
}


const sendMessage = () => {
  if (!userInput.value.trim()) return
  messages.value.push({ role: "user", content: userInput.value });
  fetchAiResponse(userInput.value, "chat");
  userInput.value = ''
}


const fetchingResponse = ref(false);
const fetchAiResponse = async (prompt: string, endpoint: string) => {

  try {
    fetchingResponse.value = true;
    messages.value.push({ role: "system", content: "" });
    
    const payload = {
      prompt: prompt
    };
    
    const response = await fetch(`/api/${endpoint}`, {
      method: "POST",
      headers: {
        "Content-Type": "application/json"
      },
      body: JSON.stringify(payload)
    });

    if (!response.ok) {
      throw new Error(`API Request error: ${response.status}`);
    }

    if (!response.body) {
      throw new Error('Response body is null')
    }

    const reader = response.body.getReader();
    const decoder = new TextDecoder();

    const index = messages.value.length - 1;
    while (true) {
      
      const { value, done } = await reader.read();
      if (done) break;
      
      const chunk = decoder.decode(value, { stream: true });

      if (messages.value[index]) {
        messages.value[index].content += chunk; 
      }
    };

  } catch (error) {
    console.error("LLM response failed", error);
  } finally {
    fetchingResponse.value = false;
  }
    
  await nextTick();
  const el = chatWindow.value;
  if (el) el.scrollTop = el.scrollHeight;

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


onMounted(async () => {
  await fetchAiResponse("", "welcome");
});
</script>

<template>
  <div class="chat-container">

    <div class="chat-window" id="chat-window" ref="chatWindow">
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

    <div id="footer-msg">
      <span id="footer-text">
        Try "Tell me about yourself." or "What is this?"
      </span>
    </div>
  </div>
</template>

<style scoped>
.chat-container {
  height: 75vh;
  width: 100%;
  max-width: 900px;           
  margin: 0 auto;
  display: flex;
  flex-direction: column;
  /* 
  overflow: hidden; 
  */      
}

.chat-window {
  flex: 1;
  overflow-y: auto;
  overflow-x: hidden;       
  display: flex;
  padding: 30px;
  flex-direction: column;
  gap: 1.2rem;
  width: 100%;
  min-height: 0;
}

.chat-window::-webkit-scrollbar {
  display: none;
}

.message-wrapper {
  display: flex;
  width: 100%;
}

.message {
  max-width: 82%;             
  padding: 0.9rem 1.3rem;
  border-radius: 1.3rem;
  font-size: 14px;;
  line-height: 1.45;
  overflow-wrap: break-word;  
  word-break: break-word;     
  hyphens: auto;              
  width: fit-content;  
}

.message.user {
  margin-left: auto;
  background: var(--cyan);
  color: black;
  border-bottom-right-radius: 0.4rem;
  box-shadow: 
    0px 0px 10px 7px var(--green) inset,
    0px 0px 5px 3px var(--green);
}

.message.assistant {
  margin-right: auto;
  background: var(--yellow);
  color: black;
  border-bottom-left-radius: 0.4rem;
  box-shadow: 
    0px 0px 10px 5px var(--red) inset,
    0px 0px 5px 3px var(--red);
}

.message-content {
  white-space: pre-wrap;  
  word-break: break-word;
}

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
  background: var(--red); 
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
  resize: none;          
  overflow: hidden;      
  min-height: 48px;      
  max-height: 200px;     
  line-height: 1.5;      
  transition: height 0.2s ease; 
  width: 80%;
}

#footer-msg {
  display: flex;
  justify-content: center;
  padding-top: 10px; 
  color: #777;
}
</style>
