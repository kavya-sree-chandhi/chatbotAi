# chatbotAi 🤖

A modular, extensible AI chatbot and agent platform using [LangChain](https://github.com/langchain-ai/langchain), [Groq LLM API](https://groq.com/), and [Streamlit](https://streamlit.io/).  
Includes code for simple chatbots, graph-based agents, and tool-augmented assistants.

---

## 📖 Introduction

**chatbotAi** is a flexible Python conversational AI platform.  
You can use it as a simple chatbot, build graph-based agents with LangGraph, or extend it with your own tools and APIs.  
It supports secure configuration, colorful logging, and can run in the terminal, on the web (Streamlit), or as a notebook demo.

---

## 🚀 Overview

This project demonstrates how to build robust conversational AI applications using:

- **LangChain** for LLM abstraction and workflow orchestration
- **Groq LLM** as the model backend
- **Streamlit** for rapid web UI (optional)
- **LangGraph** for agent and graph-based flows
- **Custom tools** (e.g., knowledge base, web search, utilities)
- **Secure configuration** and developer-friendly logging

---

## ✨ Features

- 💬 **Conversational AI**: Chatbot with natural language support using Groq’s LLM.
- 🕸️ **Graph & Agent Flows**: Create complex, multi-step reasoning and tool invocation flows with LangGraph.
- 🛠️ **Custom Tools**: Easily add your own functions (e.g., calculators, search).
- 🔐 **Secure Config**: API keys via `.env`/environment/config.py, never hard-coded.
- 📋 **Structured Logging**: Colorful, developer-friendly logs.
- 🖥️ **CLI & Web UI**: Run in terminal, Streamlit, or Jupyter (for demos).
- 🧑‍💻 **Educational**: Modular and easy to understand or extend.

---

## 🧭 Workflow

<details>
<summary>Visual Workflow Diagram (Click to expand)</summary>

```mermaid
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
