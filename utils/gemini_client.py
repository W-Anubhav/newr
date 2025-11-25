"""
Google Gemini AI Client
Handles all interactions with Google's Gemini AI API
"""
import google.generativeai as genai
import streamlit as st
import os
from dotenv import load_dotenv


# Load environment variables
load_dotenv()


def initialize_gemini():
    """
    Initialize Gemini AI with API key
    
    Returns:
        bool: True if successful, False otherwise
    """
    try:
        api_key = os.getenv("GOOGLE_API_KEY")
        
        if not api_key:
            st.error("⚠️ GOOGLE_API_KEY not found. Please add it to your .env file")
            return False
        
        genai.configure(api_key=api_key)
        return True
    
    except Exception as e:
        st.error(f"Error initializing Gemini AI: {str(e)}")
        return False


@st.cache_resource
def get_gemini_model(model_name="gemini-2.0-flash-exp"):
    """
    Get Gemini model instance (cached)
    
    Args:
        model_name: Name of the Gemini model to use
        
    Returns:
        GenerativeModel: Gemini model instance
    """
    try:
        return genai.GenerativeModel(model_name)
    except Exception as e:
        st.error(f"Error loading model: {str(e)}")
        return None


def generate_response(prompt, model_name="gemini-2.0-flash-exp"):
    """
    Generate response from Gemini AI
    
    Args:
        prompt: Input prompt text
        model_name: Name of the Gemini model to use
        
    Returns:
        str: Generated response text
    """
    try:
        model = get_gemini_model(model_name)
        
        if not model:
            return "Error: Could not load Gemini model"
        
        response = model.generate_content(prompt)
        return response.text
    
    except Exception as e:
        error_msg = str(e)
        
        # Handle common errors
        if "API_KEY" in error_msg.upper():
            return "Error: Invalid API key. Please check your GOOGLE_API_KEY in .env file"
        elif "QUOTA" in error_msg.upper():
            return "Error: API quota exceeded. Please try again later"
        elif "RATE_LIMIT" in error_msg.upper():
            return "Error: Rate limit exceeded. Please wait a moment and try again"
        else:
            return f"Error generating response: {error_msg}"


@st.cache_data(ttl=3600)
def generate_cached_response(prompt, model_name="gemini-2.0-flash-exp"):
    """
    Cached version of generate_response to avoid redundant API calls
    
    Args:
        prompt: Input prompt text
        model_name: Name of the Gemini model to use
        
    Returns:
        str: Generated response text
    """
    return generate_response(prompt, model_name)


def chat_with_gemini(messages, model_name="gemini-2.0-flash-exp"):
    """
    Have a conversation with Gemini AI
    
    Args:
        messages: List of message dictionaries with 'role' and 'content'
        model_name: Name of the Gemini model to use
        
    Returns:
        str: AI response
    """
    try:
        model = get_gemini_model(model_name)
        
        if not model:
            return "Error: Could not load Gemini model"
        
        # Start chat session
        chat = model.start_chat(history=[])
        
        # Send all messages except the last one as history
        for msg in messages[:-1]:
            if msg['role'] == 'user':
                chat.send_message(msg['content'])
        
        # Send the last message and get response
        response = chat.send_message(messages[-1]['content'])
        return response.text
    
    except Exception as e:
        return f"Error in chat: {str(e)}"
