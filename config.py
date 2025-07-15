import os
from dotenv import load_dotenv
from logger_config import setup_logger

load_dotenv()
logger = setup_logger(__name__)
class Config:
    """Configuration class for the chatbot application"""
    
    # API Configuration
    GROQ_API_KEY = os.getenv('GROQ_API_KEY')
    
    # Model Configuration
    MODEL_NAME = os.getenv('MODEL_NAME', 'mixtral-8x7b-32768')
    TEMPERATURE = float(os.getenv('TEMPERATURE', 0.7))
    MAX_TOKENS = int(os.getenv('MAX_TOKENS', 1024))
    
    # Application Configuration
    APP_NAME = os.getenv('APP_NAME', 'LangChain Groq Chatbot')
    
    @classmethod
    def validate_config(cls):
        """Validate that all required configuration is present"""
        if not cls.GROQ_API_KEY:
            logger.error("GROQ_API_KEY is not set in environment variables")
            raise ValueError("GROQ_API_KEY is required")
        
        logger.info("Configuration validated successfully")
        return True
# Validate configuration on import
Config.validate_config()