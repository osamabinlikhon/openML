# Local LLM Deployment Guide

This project provides instructions and a client for running and interacting with local LLMs (like Holo2-30B-A3B and Qwen2.5-Omni) using various backends.

## Models

### 1. Holo2-30B-A3B-GGUF
[mradermacher/Holo2-30B-A3B-GGUF](https://huggingface.co/mradermacher/Holo2-30B-A3B-GGUF)

### 2. Qwen2.5-Omni-7B
[rockn/Qwen2.5-Omni-7B-Q4_K_M](https://ollama.com/rockn/Qwen2.5-Omni-7B-Q4_K_M)

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
*Note: If installed from source, use `lemonade-server-dev` instead.*

### 2. Ollama
[Ollama](https://ollama.com/) is a popular tool for running LLMs locally.

**Run Holo2:**
```bash
ollama run hf.co/mradermacher/Holo2-30B-A3B-GGUF:Q4_K_M
```

**Run Qwen2.5-Omni:**
```bash
ollama run rockn/Qwen2.5-Omni-7B-Q4_K_M
```

### 3. LocalAI
[LocalAI](https://localai.io/) is a drop-in replacement for OpenAI API.

**Installation:**
```bash
curl https://localai.io/install.sh
```

**Run Holo2:**
```bash
local-ai run huggingface://mradermacher/Holo2-30B-A3B-GGUF/Holo2-30B-A3B.IQ4_XS.gguf
```

### 4. llama.cpp
[llama.cpp](https://github.com/ggerganov/llama.cpp) provides a lightweight C++ implementation for inference.

**Installation:**
- **macOS:** `brew install llama.cpp`
- **Windows (WinGet):** `winget install llama.cpp`

**Run Holo2 Server (OpenAI-compatible):**
```bash
llama-server -hf mradermacher/Holo2-30B-A3B-GGUF:Q4_K_M
```

**Run Holo2 CLI Inference:**
```bash
llama-cli -hf mradermacher/Holo2-30B-A3B-GGUF:Q4_K_M
```

### 5. Other Compatible Applications
These models can also be run in many other local AI environments:
- **LM Studio:** Search for models and download GGUFs.
- **Jan:** Add model paths to your Jan settings.
- **MLX LM (Apple Silicon):** `pip install mlx-lm` and use `mlx_lm.generate`.

## API Integration

All the above tools provide OpenAI-compatible API endpoints at `/v1/chat/completions` (OpenAI standard) or equivalent local paths.

### Python Client
You can use the provided `client.py` to interact with your local server.

**Setup:**
```bash
pip install -r requirements.txt
```

**Usage:**
```bash
python client.py --base_url http://localhost:8000/v1 --model user.Holo2-30B-A3B-GGUF "Tell me a joke."
```
*(Common base URLs: Lemonade: http://localhost:8000/v1, LocalAI: http://localhost:8080/v1, Ollama: http://localhost:11434/v1, llama-server: http://localhost:8080/v1)*
