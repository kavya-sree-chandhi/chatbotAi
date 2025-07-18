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

---

## Visual Diagram

```mermaid
graph TD
    A(User starts chatbot) --> B(Chatbot initializes Groq LLM and logging)
    B --> C(System message set: You are a helpful AI assistant)
    C --> D(Wait for user input in loop)
    D --> E(User enters a message)
    E --> F(Messages sent to Groq LLM via LangChain)
    F --> G(LLM generates response)
    G --> H(Bot prints response to user)
    H --> D
    D --> I{Did user type exit, quit, or bye'}
    I -- No --> E
    I -- Yes --> J(Chatbot prints goodbye and exits)



   
