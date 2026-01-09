
const API_URL = import.meta.env.VITE_API_URL;


export const fetchAiResponse = async (prompt: str) => {
  const payload = {
    prompt: prompt
  };
  
  const resp = await fetch(`${API_URL}/chat`, {
    method: "POST",
    headers: {
      "Content-Type": "application/json"
    },
    body: JSON.stringify(payload)
  });

  if (!resp.ok) {
    throw new Error(`API Request error: ${resp.status}`);
  }

  const data = await resp.json();

  console.log("RESPONSE", data);

  return data
}

