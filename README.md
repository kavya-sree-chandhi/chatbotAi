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

<img width="1587" height="367" alt="image" src="https://github.com/user-attachments/assets/57018854-e6d9-4752-b40f-297b8cc53f16" />

<img width="1917" height="962" alt="image" src="https://github.com/user-attachments/assets/f3cd6c02-88e3-41e4-b526-a19cb0e62f7f" />

<img width="1915" height="966" alt="image" src="https://github.com/user-attachments/assets/0a5114d2-e546-408e-80b5-81288cbd3610" />

## 🚀 How to Run (Setup Process)

1. **Clone the repository**
    ```bash
    git clone [https://github.com/kavya-sree-chandhi/chatbotAi.git]
    cd yourrepo
    ```

2. **Create and activate a Python virtual environment** (recommended)
    ```bash
    python -m venv venv
    # On Windows:
    venv\Scripts\activate
    # On Mac/Linux:
    source venv/bin/activate
    ```

3. **Install dependencies**
    ```bash
    pip install -r requirements.txt
    ```
    <details>
    <summary>Sample <code>requirements.txt</code></summary>

    ```
    
    langchain
    langchain-groq
    python-dotenv
    streamlit
    request
    colorlog

    ```
    </details>

4. **Set your Groq API key**
    - [Sign up for Groq](https://console.groq.com/keys) and copy your API key.
    - For demos, you may hardcode it, but for best practice, create a `.env` file:
        ```
        GROQ_API_KEY=your_actual_groq_api_key
        ```
      And update your code to use `os.getenv("GROQ_API_KEY")`.

5. **Run the app**
    ```bash
    streamlit run app.py
    ```
    - Open [http://localhost:8501](http://localhost:8501) in your browser.
    - Upload a PDF and start chatting!

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



   
