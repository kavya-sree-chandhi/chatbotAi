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
## How it Works:

1. **Terminal Startup**
Shows your app initializing in the terminal with config and Groq model details.
Confirms: configuration is validated, and the chatbot is initialized with the selected model.
<img width="1587" height="367" alt="image" src="https://github.com/user-attachments/assets/57018854-e6d9-4752-b40f-297b8cc53f16" />


2. **Web UI (Initial State)**
On opening localhost:8501, you see the chatbotAi 🤖 title. There’s a user input box labeled “You:” and a Search button as shown:
<img width="1917" height="962" alt="image" src="https://github.com/user-attachments/assets/f3cd6c02-88e3-41e4-b526-a19cb0e62f7f" />


3. **Web UI (After Asking a Question)**
After submitting a question (e.g., “how is the weather in texas now?”), your chat displays:
-User’s message in blue.
-Bot’s response in green, giving a multi-line answer.
Each turn is appended, so you can have a conversation, one question and answer at a time.
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

## Workflow Diagram:

```mermaid
flowchart TD
    A[User opens Streamlit Web App] --> B[User enters question in text box]
    B --> C[User clicks Search button]
    C --> D[Streamlit passes question to GroqChatbot class]
    D --> E[GroqChatbot sends question to Groq LLM via LangChain]
    E --> F[Groq LLM returns generated response]
    F --> G[GroqChatbot receives response]
    G --> H[Streamlit app updates: displays Q&A in chat history]
    H --> I[User can enter another question]
    I --> B




   
