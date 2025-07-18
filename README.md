# chatbotAi

A modular, extensible AI chatbot and agent platform using [LangChain](https://github.com/langchain-ai/langchain), [Groq LLM API](https://groq.com/), and [Streamlit](https://streamlit.io/).  
Includes code for simple chatbots, graph-based agents, and tool-augmented assistants.

---

## 🚀 Overview

This project demonstrates how to build a robust conversational AI application in Python using:

- **LangChain** for LLM abstraction and orchestration
- **Groq LLM** as the model backend
- **Streamlit** for rapid web UI (optional)
- **LangGraph** for advanced agent/graph-based flows
- **Custom tools** (like dog care guidance, web search)
- **Secure configuration** and colorful logging

You can use the CLI chatbot, experiment with tool-based agents, or extend it for your own tasks!

---

## ✨ Features

- 💬 **Conversational AI**: Chatbot with natural language support using Groq’s LLM.
- 🕸️ **Graph & Agent Flows**: Create complex multi-step reasoning and tool invocation flows with LangGraph.
- 🛠️ **Custom Tools**: Example agents with custom Python functions (like dog care and search).
- 🔐 **Secure Config**: API keys via `.env`/environment/config.py, never hard-coded.
- 📋 **Structured Logging**: Colorful, developer-friendly logs.
- 🖥️ **CLI & Web UI**: Run in terminal, Streamlit, or Jupyter (for LangGraph demos).
- 🧑‍💻 **Educational**: Modular, easy to understand and extend for research or learning.

---

## Workflow
graph TD
    A[User starts chatbot (runs script)] --> B[Chatbot initializes Groq LLM and logging]
    B --> C[System message ("You are a helpful AI assistant...") is set]
    C --> D[Wait for user input in loop]
    D --> E[User enters a message]
    E --> F[Input + system message sent to Groq LLM via LangChain]
    F --> G[LLM generates a response]
    G --> H[Bot prints response to user]
    H --> D
    D --> I{User types 'exit', 'quit', or 'bye'?}
    I -- No --> E
    I -- Yes --> J[Chatbot prints goodbye and exits]
