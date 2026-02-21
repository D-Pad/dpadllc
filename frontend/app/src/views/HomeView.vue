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


const pageMode = ref<string>("initial");
const setMode = (newMode: string) => {
  pageMode.value = newMode;
}


// User login and registration functions 
const userName = ref<string>("");
const userPassword = ref<string>("");
const registerName = ref<string>("");
const registerPassword = ref<string>("");
const registerPasswordConf = ref<string>("");
const registerInviteCode = ref<string>("");
const hasRegistered = ref<boolean>(false);
const statusMessage = ref<string>("");
const statusClass = ref<string>("");

const signInOrUp = async (mode: string) => {

  let bodyObj = null;
  if (mode === "register") {
    bodyObj = {
      username: registerName.value,
      password: registerPassword.value,
      passwordConf: registerPasswordConf.value,
      inviteCode: registerInviteCode.value,
      mode: mode
    };
  } else if (mode === "login") {
    bodyObj = {
      username: userName.value,
      password: userPassword.value,
      mode: mode 
    }
  };

  const resp = await fetch("/api/user", {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify(bodyObj)
  });
  
  const data = await resp.json();
  
  if (data.status !== 200) {
    statusMessage.value = data.reason.toUpperCase();
    statusClass.value = "error";
  }
  else {
    statusClass.value = "";
    statusMessage.value = data.reason;
    await new Promise(resolve => setTimeout(resolve, 2000));
    statusMessage.value = "";
    setMode("login");
  }

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
     
      <div class="login-form-wrapper">

        <div class="form-row">
          <div class="form-label">
            <label>User Name:</label>
          </div>
          <div class="form-input">
            <input type="text" v-model="userName">
          </div>
        </div>
        
        <div class="form-row">
          <div class="form-label">
            <label>Password:</label>
          </div>
          <div class="form-input">
            <input type="text" v-model="userPassword">
          </div>
        </div>

        <div class="btn-wrapper">
          <button class="btn">Sign In</button>
        </div>

      </div>

      <div id="invite-code-wrapper">
        <span>
          Enter registration invite code 
          <a href="#" class="invite-link" @click="setMode('invite')">here</a> 
        </span>
      </div>

    </template>

    <template v-else-if="pageMode === 'invite'">
     
      <div class="login-form-wrapper">
        
        <div class="form-row">
          <div class="form-label">
            <label>User Name:</label>
          </div>
          <div class="form-input">
            <input type="text" v-model="registerName">
          </div>
        </div>
        
        <div class="form-row">
          <div class="form-label">
            <label>Password:</label>
          </div>
          <div class="form-input">
            <input type="password" v-model="registerPassword">
          </div>
        </div>
        
        <div class="form-row">
          <div class="form-label">
            <label>Confirm Password:</label>
          </div>
          <div class="form-input">
            <input type="password" v-model="registerPasswordConf">
          </div>
        </div>

        <div class="form-row">
          <div class="form-label">
            <label>Invite Code:</label>
          </div>
          <div class="form-input">
            <input type="text" v-model="registerInviteCode">
          </div>
        </div>

        <div class="btn-wrapper">
          <button class="btn" @click="signInOrUp('register')">
            Register
          </button>
        </div>

        <div>
          <span id="status-message" :class="statusClass">
            {{ statusMessage }}
          </span>
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

.login-form-wrapper {
  display: flex;
  flex-direction: column; 
  justify-content: center;
  align-items: center;    
  margin: 0 auto;     
  gap: 1rem;          
  width: 100%;
  height: 100%;
}

#invite-code-wrapper {
  font-size: 20px;
  display: flex;
  justify-content: center;
  margin: 30px auto 0px auto;
}

#status-message {
  margin-top: 50px;
  font-size: 20px; 
}

.error {
  color: var(--red);
}

@media (max-width: 640px) {
  .btn {
    font-size: 10px;
    margin: 20px;
    padding: 5px;
  } 

  .login-form-wrapper {
    margin-top: 40px; 
    gap: 0.5rem;          
  }

  #visitor-count-container {
    font-size: 10px;
  } 

  .login-form-wrapper {
    margin: 0px auto;
  }

  #invite-code-wrapper {
    font-size: 10px;
    justify-content: left;
  }
}
</style> 

