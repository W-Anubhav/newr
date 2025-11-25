"""
PDF Processing Utilities
Handles PDF text extraction and validation
"""
import PyPDF2
import io
import streamlit as st


def extract_text_from_pdf(pdf_file):
    """
    Extract text content from a PDF file with robust error handling
    
    Args:
        pdf_file: Uploaded PDF file object
        
    Returns:
        str: Extracted text content
    """
    try:
        pdf_reader = PyPDF2.PdfReader(pdf_file)
        text = ""
        
        for page_num, page in enumerate(pdf_reader.pages):
            try:
                # Extract text from page
                page_text = page.extract_text()
                
                # Clean invalid surrogate characters
                if page_text:
                    # Remove surrogate pairs that cause encoding issues
                    page_text = page_text.encode('utf-8', errors='ignore').decode('utf-8', errors='ignore')
                    text += page_text
                    
            except Exception as page_error:
                # Skip problematic pages silently but continue with others
                continue
        
        if not text.strip():
            st.error("❌ No text could be extracted from the PDF. It might be a scanned image or encrypted.")
            return None
            
        return text.strip()
    
    except Exception as e:
        st.error(f"❌ Error reading PDF file: {str(e)}")
        st.info("💡 Try: 1) Re-saving the PDF, 2) Using a different PDF, or 3) Converting to a text-based PDF")
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
            try:
                page_text = page.extract_text()
                if page_text:
                    # Clean invalid surrogate characters
                    page_text = page_text.encode('utf-8', errors='ignore').decode('utf-8', errors='ignore')
                    text += page_text
            except:
                continue
        
        return text.strip()
    
    except Exception as e:
        return f"Error: {str(e)}"
