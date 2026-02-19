# Local LLM Deployment Guide

This project provides instructions and a client for running and interacting with local LLMs (like Holo2-30B-A3B and Qwen2.5-Omni) using various backends.

## Models

### 1. Holo2-30B-A3B-GGUF
[mradermacher/Holo2-30B-A3B-GGUF](https://huggingface.co/mradermacher/Holo2-30B-A3B-GGUF)

### 2. Qwen2.5-Omni-7B
[rockn/Qwen2.5-Omni-7B-Q4_K_M](https://ollama.com/rockn/Qwen2.5-Omni-7B-Q4_K_M)

### 3. SmoLM2
[Ollama: smollm2](https://ollama.com/library/smollm2)

## Backends

### 1. Lemonade Server
[Lemonade](https://lemonade-server.ai/) is a fast local LLM, image, and speech generation server optimized for GPUs and NPUs.

**Installation:**
Visit [lemonade-server.ai](https://lemonade-server.ai/) to download the installer for your platform.

**Pull and Run Holo2:**
```bash
# Pull the model
lemonade-server pull user.Holo2-30B-A3B-GGUF --checkpoint mradermacher/Holo2-30B-A3B-GGUF:Q4_K_M --recipe llamacpp

# Run the model
lemonade-server run user.Holo2-30B-A3B-GGUF
```

### 2. Ollama
[Ollama](https://ollama.com/) is a popular tool for running LLMs locally.

**Installation:**
- **Linux:** `curl -fsSL https://ollama.com/install.sh | sh`
- **Windows (PowerShell):** `irm https://ollama.com/install.ps1 | iex`

**Run Models:**
```bash
ollama run hf.co/mradermacher/Holo2-30B-A3B-GGUF:Q4_K_M
ollama run rockn/Qwen2.5-Omni-7B-Q4_K_M
ollama run smollm2
```

### 3. LocalAI
[LocalAI](https://localai.io/) is a drop-in replacement for OpenAI API.

**Installation:**
```bash
curl https://localai.io/install.sh
```

### 4. llama.cpp
[llama.cpp](https://github.com/ggerganov/llama.cpp) provides a lightweight C++ implementation for inference.

**Installation:**
- **macOS:** `brew install llama.cpp`
- **Windows (WinGet):** `winget install llama.cpp`

**Run Server:**
```bash
llama-server -hf mradermacher/Holo2-30B-A3B-GGUF:Q4_K_M
```

## API Integration

### Ollama API Examples

#### Curl
```bash
curl http://localhost:11434/api/chat -d '{
  "model": "smollm2",
  "messages": [{"role": "user", "content": "Hello!"}]
}'
```

#### Python (ollama-python)
```bash
pip install ollama
```
```python
from ollama import chat

response = chat(
    model='smollm2',
    messages=[{'role': 'user', 'content': 'Hello!'}],
)
print(response.message.content)
```

#### JavaScript (ollama-js)
```bash
npm install ollama
```
```javascript
import ollama from 'ollama'

const response = await ollama.chat({
  model: 'smollm2',
  messages: [{role: 'user', content: 'Hello!'}],
})
console.log(response.message.content)
```

### Generic OpenAI-compatible Client
Many backends (Lemonade, LocalAI, llama-server, and Ollama) support the OpenAI API standard.

#### Python Client (Provided)
**Setup:**
```bash
pip install -r requirements.txt
```

**Usage:**
```bash
python client.py --base_url http://localhost:8000/v1 --model user.Holo2-30B-A3B-GGUF "Tell me a joke."
```
*(Common base URLs: Lemonade: http://localhost:8000/v1, LocalAI: http://localhost:8080/v1, Ollama: http://localhost:11434/v1, llama-server: http://localhost:8080/v1)*
