
from langchain_groq import ChatGroq
from langchain.schema import HumanMessage, SystemMessage
from config import Config
from logger_config import setup_logger
import streamlit as st

logger = setup_logger(__name__)
class GroqChatbot:
    """A simple chatbot using LangChain and Groq API"""
    
    def __init__(self):
        """Initialize the chatbot with Groq LLM"""
        print(f"GROQ KEY: {Config.GROQ_API_KEY}")
        try:
            self.llm = ChatGroq(
                groq_api_key=Config.GROQ_API_KEY,
                model_name="llama-3.1-8b-instant", #Config.MODEL_NAME,
                temperature=Config.TEMPERATURE,
                max_tokens=Config.MAX_TOKENS
            )
            
            self.system_message = SystemMessage(
                content="You are a helpful AI assistant. Provide clear, "
                       "concise, and helpful responses to user questions."
            )
            
            logger.info(f"Chatbot initialized with model: {Config.MODEL_NAME}")
            
        except Exception as e:
            logger.error(f"Failed to initialize chatbot: {e}")
            raise
    
    def get_response(self, user_input: str) -> str:
        """
        Get response from the chatbot for user input
        
        Args:
            user_input (str): User's message
            
        Returns:
            str: Chatbot's response
        """
        try:
            messages = [
                self.system_message,
                HumanMessage(content=user_input)
            ]
            
            logger.info(f"Processing user input: {user_input[:100]}...")
            response = self.llm(messages)
            logger.info("Response generated successfully")
            
            return response.content
            
        except Exception as e:
            logger.error(f"Error generating response: {e}")
            return "I apologize, but I encountered an error processing your request."
def main():
    """Main function for command-line interface"""
    logger.info("Starting LangChain Groq Chatbot")
    
    try:
        chatbot = GroqChatbot()
        
        print(f"\n🤖 {Config.APP_NAME}")
        print("=" * 50)
        print("Type 'quit', 'exit', or 'bye' to end the conversation\n")
        
        while True:
            user_input = input("You: ").strip()
            
            if user_input.lower() in ['quit', 'exit', 'bye']:
                print("\n👋 Goodbye! Thanks for chatting!")
                break
            
            if not user_input:
                continue
            
            response = chatbot.get_response(user_input)
            print(f"\n🤖 Bot: {response}\n")
            
    except KeyboardInterrupt:
        print("\n\n👋 Goodbye! Thanks for chatting!")
    except Exception as e:
        logger.error(f"Application error: {e}")
        print(f"An error occurred: {e}")
if __name__ == "__main__":
    main()