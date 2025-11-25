"""
PDF Processing Utilities
Handles PDF text extraction and image conversion
"""
import PyPDF2
from pdf2image import convert_from_bytes
from PIL import Image
import io
import streamlit as st


def extract_text_from_pdf(pdf_file):
    """
    Extract text content from a PDF file
    
    Args:
        pdf_file: Uploaded PDF file object
        
    Returns:
        str: Extracted text content
    """
    try:
        pdf_reader = PyPDF2.PdfReader(pdf_file)
        text = ""
        
        for page in pdf_reader.pages:
            text += page.extract_text()
        
        return text.strip()
    
    except Exception as e:
        st.error(f"Error extracting text from PDF: {str(e)}")
        return None


def pdf_to_images(pdf_file):
    """
    Convert PDF pages to images
    
    Args:
        pdf_file: Uploaded PDF file object
        
    Returns:
        list: List of PIL Image objects
    """
    try:
        # Read PDF bytes
        pdf_bytes = pdf_file.read()
        
        # Convert to images
        images = convert_from_bytes(pdf_bytes)
        
        # Reset file pointer
        pdf_file.seek(0)
        
        return images
    
    except Exception as e:
        st.error(f"Error converting PDF to images: {str(e)}")
        return None


def validate_pdf(pdf_file):
    """
    Validate if the uploaded file is a valid PDF
    
    Args:
        pdf_file: Uploaded file object
        
    Returns:
        bool: True if valid PDF, False otherwise
    """
    try:
        pdf_reader = PyPDF2.PdfReader(pdf_file)
        # Try to access first page
        _ = pdf_reader.pages[0]
        pdf_file.seek(0)
        return True
    
    except Exception as e:
        st.error(f"Invalid PDF file: {str(e)}")
        return False


@st.cache_data
def process_pdf_cached(pdf_bytes):
    """
    Cached version of PDF processing to avoid re-processing same file
    
    Args:
        pdf_bytes: PDF file as bytes
        
    Returns:
        str: Extracted text content
    """
    try:
        pdf_file = io.BytesIO(pdf_bytes)
        pdf_reader = PyPDF2.PdfReader(pdf_file)
        text = ""
        
        for page in pdf_reader.pages:
            text += page.extract_text()
        
        return text.strip()
    
    except Exception as e:
        return f"Error: {str(e)}"
