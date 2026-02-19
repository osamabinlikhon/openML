# Local & Cloud AI Deployment Guide

This project provides instructions and a client for running and interacting with LLMs locally (like Holo2-30B-A3B and Qwen2.5-Omni) and through managed gateways.

## Models

### 1. Holo2-30B-A3B-GGUF
[mradermacher/Holo2-30B-A3B-GGUF](https://huggingface.co/mradermacher/Holo2-30B-A3B-GGUF)

### 2. Qwen2.5-Omni-7B
[rockn/Qwen2.5-Omni-7B-Q4_K_M](https://ollama.com/rockn/Qwen2.5-Omni-7B-Q4_K_M)

### 3. SmoLM2
[Ollama: smollm2](https://ollama.com/library/smollm2)

## Backends & Gateways

### 1. Lemonade Server
[Lemonade](https://lemonade-server.ai/) is a fast local LLM, image, and speech generation server optimized for GPUs and NPUs.

**Pull and Run Holo2:**
```bash
lemonade-server pull user.Holo2-30B-A3B-GGUF --checkpoint mradermacher/Holo2-30B-A3B-GGUF:Q4_K_M --recipe llamacpp
lemonade-server run user.Holo2-30B-A3B-GGUF
```

### 2. Ollama
[Ollama](https://ollama.com/) is a popular tool for running LLMs locally.

**Installation:**
- **Linux:** `curl -fsSL https://ollama.com/install.sh | sh`
- **Windows (PowerShell):** `irm https://ollama.com/install.ps1 | iex`

**Run Models:**
```bash
ollama run smollm2
```

### 3. Wasmer
[Wasmer](https://wasmer.io/) allows you to run AI models as WebAssembly modules, ensuring portability and security.

**Run an AI model:**
```bash
wasmer run wasmer/llama-cpp --hf mradermacher/Holo2-30B-A3B-GGUF:Q4_K_M
```

**Wasmer Manifest (`wasmer.toml`):**
To publish or configure your AI application for Wasmer, you use a `wasmer.toml` file:
```toml
[package]
name = "my-user/my-ai-app"
version = "0.1.0"
description = "My local AI application"
license = "MIT"

[[command]]
name = "run-ai"
module = "wasmer/llama-cpp"
runner = "wasi"

[command.annotations.wasi]
main-args = ["--hf", "mradermacher/Holo2-30B-A3B-GGUF:Q4_K_M"]
```

### 4. Cloudflare AI Gateway
[Cloudflare AI Gateway](https://developers.cloudflare.com/ai-gateway/) allows you to observe and control your AI applications.

**OpenAI Compatible Endpoint:**
```bash
curl -X POST https://gateway.ai.cloudflare.com/v1/{account_id}/{gateway_id}/compat/chat/completions \
  --header 'Authorization: Bearer {api_token}' \
  --header 'Content-Type: application/json' \
  --data '{
    "model": "workers-ai/@cf/meta/llama-3.3-70b-instruct-fp8-fast",
    "messages": [{"role": "user", "content": "What is Cloudflare?"}]
  }'
```

### 5. llama.cpp
[llama.cpp](https://github.com/ggerganov/llama.cpp) provides a lightweight C++ implementation for inference.

**Run Server:**
```bash
llama-server -hf mradermacher/Holo2-30B-A3B-GGUF:Q4_K_M
```

### 6. Opencode Server
[Opencode](https://github.com/opencode-ai) is a programmable AI server with a type-safe SDK.

## API Integration

### Ollama API Examples
```bash
curl http://localhost:11434/api/chat -d '{
  "model": "smollm2",
  "messages": [{"role": "user", "content": "Hello!"}]
}'
```

### Opencode SDK (JS/TS)
```javascript
import { createOpencode } from "@opencode-ai/sdk"
const { client } = await createOpencode({
  config: { model: "anthropic/claude-3-5-sonnet-20241022" },
})
```

### Generic OpenAI-compatible Client (Python)
Works with Lemonade, LocalAI, llama-server, Ollama, Cloudflare AI Gateway, and Wasmer (if running a server).

**Usage:**
```bash
python client.py --base_url http://localhost:8000/v1 --model user.Holo2-30B-A3B-GGUF "Tell me a joke."
```
*(Common base URLs: Lemonade: http://localhost:8000/v1, LocalAI: http://localhost:8080/v1, Ollama: http://localhost:11434/v1, Cloudflare: https://gateway.ai.cloudflare.com/v1/{account_id}/{gateway_id}/compat)*
