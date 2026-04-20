# Agentic AI for DevOps — Setup Summary

## What This Project Does

A local AI agent that acts as a Docker expert. You ask it questions in plain English and it:
- Checks running Docker containers (`docker ps`)
- Reads container logs (`docker logs <name>`)
- Explains errors, root causes, and fixes in 1-2 lines

Built with **LangGraph + LangChain + Ollama**, runs 100% locally — no API keys needed.

---

## Stack

| Component | Tool/Model |
|-----------|-----------|
| LLM runtime | Ollama |
| Model | gemma4 |
| Agent framework | LangGraph (`create_react_agent`) |
| LLM wrapper | LangChain Ollama |
| Tools | subprocess calls to Docker CLI |

---

## Files

| File | Purpose |
|------|---------|
| `agent.py` | Main AI agent — uses gemma4 + LangGraph with Docker tools |
| `gen_ai.py` | Simpler chat loop using tinyllama directly via Ollama (no agent) |
| `requirements.txt` | Python dependencies |

---

## How to Run

### Prerequisites
- Python 3.x
- Docker Desktop (must be running)
- Ollama installed and running

### 1. Install Python dependencies
```bash
pip install -r requirements.txt --user
```

### 2. Pull the model
```bash
ollama pull gemma4
```

### 3. Start Docker Desktop
Make sure Docker Desktop is open and the whale icon in the taskbar is stable.

### 4. Run the agent
```bash
python agent.py
```

Type your question at the prompt, e.g.:
- `how many containers are running?`
- `show logs for my nginx container`
- `why is my container crashing?`

---

## Windows-Specific Notes

- Install Ollama via the `.exe` installer from [ollama.com/download](https://ollama.com/download)
- Run `pip install --user` if you hit permission errors on `pip install`
- Docker Desktop must be open before running the agent — otherwise Docker CLI commands fail with a pipe error:
  ```
  open //./pipe/dockerDesktopLinuxEngine: The system cannot find the file specified.
  ```

---

## Dependencies (from requirements.txt)

```
langchain-ollama
ollama
langgraph
langchain
```

---

## Known Warnings

```
LangGraphDeprecatedSinceV10: create_react_agent has been moved to `langchain.agents`
```

This is a deprecation warning — the agent still works. To silence it in a future update, change the import in `agent.py`:

```python
# Old
from langgraph.prebuilt import create_react_agent

# New (future)
from langchain.agents import create_react_agent
```

---

## Session Notes (for Claude)

- gemma4 takes ~60 seconds to load on first prompt — this is normal
- The agent correctly queries live Docker state (tested with a running nginx container)
- `gen_ai.py` requires `tinyllama` — pull with `ollama pull tinyllama` if needed
- On first run, Ollama loads the model into RAM; subsequent queries are faster
