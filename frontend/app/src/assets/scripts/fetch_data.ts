
const API_URL = import.meta.env.VITE_API_URL;


export const fetchAiResponse = async (prompt: str) => {
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

  while (true) {
    const { value, done } = await reader.read();
    if (done) break;
    const chunk = decoder.decode(value);
    console.log(chunk); 
  };
}

