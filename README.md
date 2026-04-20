# Docker AI Agent

A local AI agent that acts as a Docker expert. Ask it questions in plain English and it inspects your running containers and logs to explain errors, root causes, and fixes.

Runs 100% locally — no API keys needed.

---

## Demo

```
Enter your message:
how many containers are running?

There is 1 container running.
```

```
Enter your message:
show logs for my nginx container

[agent checks logs and explains any errors]
```

---

## Stack

| Component | Tool |
|-----------|------|
| LLM runtime | [Ollama](https://ollama.com) |
| Model | gemma4 |
| Agent framework | LangGraph |
| LLM wrapper | LangChain Ollama |
| Docker interface | subprocess → Docker CLI |

---

## Files

| File | Description |
|------|-------------|
| `agent.py` | Main AI agent — gemma4 + LangGraph with Docker tools |
| `gen_ai.py` | Simpler chat loop using tinyllama directly via Ollama |
| `requirements.txt` | Python dependencies |
| `SETUP_SUMMARY.md` | Full setup notes and session context |

---

## Prerequisites

- Python 3.x
- [Docker Desktop](https://www.docker.com/products/docker-desktop/) (must be running)
- [Ollama](https://ollama.com/download)

---

## Setup

**1. Clone the repo**
```bash
git clone https://github.com/MelvynJoseph10/docker-ai-agent.git
cd docker-ai-agent
```

**2. Install dependencies**
```bash
pip install -r requirements.txt
```

**3. Pull the model**
```bash
ollama pull gemma4
```

**4. Start Docker Desktop**

Make sure Docker Desktop is open and running before starting the agent.

**5. Run the agent**
```bash
python agent.py
```

---

## Usage

Once running, type any Docker-related question:

- `how many containers are running?`
- `show logs for my nginx container`
- `why is my container crashing?`
- `what does exit code 137 mean?`

---

## Windows Notes

- Use `pip install -r requirements.txt --user` if you hit permission errors
- Docker Desktop must be open — otherwise you'll get a pipe error on startup
- Ollama loads the model into RAM on first prompt — first response takes ~60 seconds

---

## Optional: Simpler Version

`gen_ai.py` is a lightweight version with no agent tools — just a plain chat loop:

```bash
ollama pull tinyllama
python gen_ai.py
```

---

## Known Warning

```
LangGraphDeprecatedSinceV10: create_react_agent has been moved to `langchain.agents`
```

Harmless — the agent works fine. Will be updated in a future release.
