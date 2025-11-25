"""
ResumeInsight - AI Resume Analyzer
A powerful AI-driven resume analysis tool using Google's Gemini AI
"""
import streamlit as st
import os
from datetime import datetime

# Import utilities
from utils.pdf_processor import extract_text_from_pdf, validate_pdf, process_pdf_cached
from utils.gemini_client import initialize_gemini, generate_response, chat_with_gemini
from utils.prompts import (
    get_hr_evaluation_prompt,
    get_skill_enhancement_prompt,
    get_ats_match_prompt,
    get_resume_comparison_prompt,
    get_chat_system_prompt,
    get_simple_chat_prompt
)
from utils.visualizations import (
    create_match_gauge,
    create_category_bars,
    create_skills_radar,
    create_wordcloud,
    create_comparison_table,
    create_progress_bar,
    display_metric_cards
)


# Page configuration
st.set_page_config(
    page_title="ResumeInsight - AI Resume Analyzer",
    page_icon="🤖",
    layout="wide",
    initial_sidebar_state="expanded"
)


# Custom CSS for better aesthetics
st.markdown("""
<style>
    /* Main theme colors */
    :root {
        --primary-color: #00C853;
        --secondary-color: #1f1f1f;
        --background-color: #f5f7fa;
        --card-background: #ffffff;
    }
    
    /* Header styling */
    .main-header {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        padding: 2rem;
        border-radius: 10px;
        color: white;
        text-align: center;
        margin-bottom: 2rem;
        box-shadow: 0 4px 6px rgba(0,0,0,0.1);
    }
    
    .main-header h1 {
        margin: 0;
        font-size: 2.5rem;
        font-weight: 700;
    }
    
    .main-header p {
        margin: 0.5rem 0 0 0;
        font-size: 1.1rem;
        opacity: 0.95;
    }
    
    /* Feature cards */
    .feature-card {
        background: white;
        padding: 1.5rem;
        border-radius: 10px;
        box-shadow: 0 2px 4px rgba(0,0,0,0.1);
        margin-bottom: 1rem;
        border-left: 4px solid #667eea;
        transition: transform 0.2s, box-shadow 0.2s;
    }
    
    .feature-card:hover {
        transform: translateY(-2px);
        box-shadow: 0 4px 8px rgba(0,0,0,0.15);
    }
    
    /* Info boxes */
    .info-box {
        background: #E3F2FD;
        border-left: 4px solid #2196F3;
        padding: 1rem;
        border-radius: 5px;
        margin: 1rem 0;
        color: #1565C0;
    }
    
    .success-box {
        background: #E8F5E9;
        border-left: 4px solid #4CAF50;
        padding: 1rem;
        border-radius: 5px;
        margin: 1rem 0;
        color: #2E7D32;
    }
    
    .warning-box {
        background: #FFF3E0;
        border-left: 4px solid #FF9800;
        padding: 1rem;
        border-radius: 5px;
        margin: 1rem 0;
        color: #E65100;
    }
    
    /* Buttons */
    .stButton>button {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        color: white;
        border: none;
        border-radius: 5px;
        padding: 0.5rem 2rem;
        font-weight: 600;
        transition: all 0.3s;
    }
    
    .stButton>button:hover {
        transform: translateY(-2px);
        box-shadow: 0 4px 8px rgba(0,0,0,0.2);
    }
    
    /* Sidebar styling */
    .css-1d391kg {
        background-color: #f8f9fa;
    }
    
    /* Report section */
    .report-section {
        background: white;
        padding: 2rem;
        border-radius: 10px;
        box-shadow: 0 2px 4px rgba(0,0,0,0.1);
        margin: 1rem 0;
        color: #1f1f1f;
    }
    
    /* Chat messages */
    .chat-message {
        padding: 1rem;
        border-radius: 10px;
        margin: 0.5rem 0;
        color: #1f1f1f;
    }
    
    .user-message {
        background: #E3F2FD;
        margin-left: 2rem;
        color: #0D47A1;
    }
    
    .ai-message {
        background: #F3E5F5;
        margin-right: 2rem;
        color: #4A148C;
    }
</style>
""", unsafe_allow_html=True)


def display_header():
    """Display the main header"""
    st.markdown("""
    <div class="main-header">
        <h1>🤖 ResumeInsight</h1>
        <p>AI-Powered Resume Analysis & Optimization Tool</p>
    </div>
    """, unsafe_allow_html=True)


def save_report(content, filename):
    """Save report content to a text file"""
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    full_filename = f"{filename}_{timestamp}.txt"
    
    return content, full_filename


def hr_evaluation_page(resume_text, job_description):
    """HR Evaluation Feature"""
    st.markdown("### 🧠 HR Professional Evaluation")
    st.markdown('<div class="info-box">Get a comprehensive HR-style analysis of your resume with professional feedback on strengths, weaknesses, and hiring recommendations.</div>', unsafe_allow_html=True)
    
    if st.button("🚀 Generate HR Evaluation", key="hr_eval_btn"):
        with st.spinner("🔍 Analyzing your resume from an HR perspective..."):
            prompt = get_hr_evaluation_prompt(resume_text, job_description)
            response = generate_response(prompt)
            
            st.markdown('<div class="report-section">', unsafe_allow_html=True)
            st.markdown(response)
            st.markdown('</div>', unsafe_allow_html=True)
            
            # Download button
            report_content, filename = save_report(response, "HR_Evaluation_Report")
            st.download_button(
                label="📥 Download Report",
                data=report_content,
                file_name=filename,
                mime="text/plain"
            )


def skill_enhancement_page(resume_text, job_description):
    """Skill Enhancement Feature"""
    st.markdown("### 🚀 Skill Enhancement Suggestions")
    st.markdown('<div class="info-box">Receive personalized recommendations on skills to develop, courses to take, and certifications to pursue for career growth.</div>', unsafe_allow_html=True)
    
    if st.button("💡 Get Skill Recommendations", key="skill_btn"):
        with st.spinner("📚 Analyzing skill gaps and creating your learning roadmap..."):
            prompt = get_skill_enhancement_prompt(resume_text, job_description)
            response = generate_response(prompt)
            
            st.markdown('<div class="report-section">', unsafe_allow_html=True)
            st.markdown(response)
            st.markdown('</div>', unsafe_allow_html=True)
            
            # Download button
            report_content, filename = save_report(response, "Skill_Enhancement_Report")
            st.download_button(
                label="📥 Download Report",
                data=report_content,
                file_name=filename,
                mime="text/plain"
            )


def ats_match_page(resume_text, job_description):
    """ATS Match Analysis Feature"""
    st.markdown("### 📊 ATS Compatibility Analysis")
    st.markdown('<div class="info-box">Check how well your resume matches the job description and get a detailed ATS compatibility score with optimization tips.</div>', unsafe_allow_html=True)
    
    if st.button("🎯 Analyze ATS Match", key="ats_btn"):
        with st.spinner("⚙️ Running ATS compatibility analysis..."):
            prompt = get_ats_match_prompt(resume_text, job_description)
            response = generate_response(prompt)
            
            # Try to extract percentage from response
            try:
                # Look for percentage in the response
                import re
                match = re.search(r'Overall Match Score[:\s]+(\d+)%', response)
                if match:
                    percentage = int(match.group(1))
                    
                    # Display gauge chart
                    col1, col2 = st.columns([1, 2])
                    with col1:
                        fig = create_match_gauge(percentage)
                        st.plotly_chart(fig, use_container_width=True)
                    
                    with col2:
                        st.markdown('<div class="success-box">', unsafe_allow_html=True)
                        if percentage >= 80:
                            st.markdown("### ✅ Excellent Match!")
                            st.markdown("Your resume is highly compatible with this job posting.")
                        elif percentage >= 60:
                            st.markdown("### 🟡 Good Match")
                            st.markdown("Your resume shows good compatibility. Some improvements recommended.")
                        else:
                            st.markdown("### 🔴 Needs Improvement")
                            st.markdown("Consider optimizing your resume for better ATS compatibility.")
                        st.markdown('</div>', unsafe_allow_html=True)
            except:
                pass
            
            st.markdown('<div class="report-section">', unsafe_allow_html=True)
            st.markdown(response)
            st.markdown('</div>', unsafe_allow_html=True)
            
            # Download button
            report_content, filename = save_report(response, "ATS_Match_Report")
            st.download_button(
                label="📥 Download Report",
                data=report_content,
                file_name=filename,
                mime="text/plain"
            )


def resume_comparison_page():
    """Resume Comparison Feature"""
    st.markdown("### ⚖️ Resume Comparison")
    st.markdown('<div class="info-box">Upload two resumes to compare them side-by-side and see which one performs better for the job.</div>', unsafe_allow_html=True)
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("#### 📄 Resume 1")
        resume1_file = st.file_uploader("Upload First Resume (PDF)", type=['pdf'], key="resume1")
    
    with col2:
        st.markdown("#### 📄 Resume 2")
        resume2_file = st.file_uploader("Upload Second Resume (PDF)", type=['pdf'], key="resume2")
    
    job_desc = st.text_area("📋 Job Description", height=150, key="comp_job_desc", 
                            placeholder="Paste the job description here...")
    
    if st.button("🔍 Compare Resumes", key="compare_btn"):
        if not resume1_file or not resume2_file:
            st.error("⚠️ Please upload both resumes to compare")
            return
        
        if not job_desc:
            st.error("⚠️ Please provide a job description")
            return
        
        with st.spinner("⚖️ Comparing resumes..."):
            # Extract text from both resumes
            resume1_text = extract_text_from_pdf(resume1_file)
            resume2_text = extract_text_from_pdf(resume2_file)
            
            if resume1_text and resume2_text:
                prompt = get_resume_comparison_prompt(resume1_text, resume2_text, job_desc)
                response = generate_response(prompt)
                
                st.markdown('<div class="report-section">', unsafe_allow_html=True)
                st.markdown(response)
                st.markdown('</div>', unsafe_allow_html=True)
                
                # Download button
                report_content, filename = save_report(response, "Resume_Comparison_Report")
                st.download_button(
                    label="📥 Download Comparison Report",
                    data=report_content,
                    file_name=filename,
                    mime="text/plain"
                )


def chat_assistant_page(resume_text=None, job_description=None):
    """AI Chat Assistant Feature"""
    st.markdown("### 💬 AI Chat Assistant")
    st.markdown('<div class="info-box">Ask questions about your resume, get personalized advice, and receive real-time feedback from our AI assistant.</div>', unsafe_allow_html=True)
    
    # Initialize chat history
    if 'chat_history' not in st.session_state:
        st.session_state.chat_history = []
    
    # Display chat history
    chat_container = st.container()
    with chat_container:
        for message in st.session_state.chat_history:
            if message['role'] == 'user':
                st.markdown(f'<div class="chat-message user-message">👤 <strong>You:</strong> {message["content"]}</div>', unsafe_allow_html=True)
            else:
                st.markdown(f'<div class="chat-message ai-message">🤖 <strong>AI Assistant:</strong> {message["content"]}</div>', unsafe_allow_html=True)
    
    # Chat input
    user_question = st.text_input("💭 Ask a question about your resume:", key="chat_input", 
                                  placeholder="e.g., How can I improve my resume for this job?")
    
    col1, col2 = st.columns([1, 5])
    with col1:
        send_button = st.button("📤 Send", key="send_chat")
    with col2:
        if st.button("🗑️ Clear Chat", key="clear_chat"):
            st.session_state.chat_history = []
            st.rerun()
    
    if send_button and user_question:
        # Add user message to history
        st.session_state.chat_history.append({
            'role': 'user',
            'content': user_question
        })
        
        with st.spinner("🤔 Thinking..."):
            # Generate response
            if resume_text and job_description:
                system_prompt = get_chat_system_prompt(resume_text, job_description)
                full_prompt = f"{system_prompt}\n\nUser Question: {user_question}"
            else:
                full_prompt = f"{get_simple_chat_prompt()}\n\nUser Question: {user_question}"
            
            ai_response = generate_response(full_prompt)
            
            # Add AI response to history
            st.session_state.chat_history.append({
                'role': 'assistant',
                'content': ai_response
            })
        
        st.rerun()


def main():
    """Main application"""
    # Initialize Gemini
    if not initialize_gemini():
        st.error("⚠️ Failed to initialize Gemini AI. Please check your API key in the .env file.")
        st.info("💡 Create a .env file in the project root and add: GOOGLE_API_KEY=your_api_key_here")
        st.stop()
    
    # Display header
    display_header()
    
    # Sidebar
    with st.sidebar:
        st.markdown("## 📁 Upload Resume")
        uploaded_file = st.file_uploader("Choose your resume (PDF)", type=['pdf'], key="main_resume")
        
        st.markdown("## 📋 Job Description")
        job_description = st.text_area("Paste the job description here", height=200, 
                                       placeholder="Enter the job description you're applying for...")
        
        st.markdown("---")
        st.markdown("## 🎯 Select Analysis Type")
        
        analysis_type = st.radio(
            "Choose what you want to do:",
            [
                "🧠 HR Evaluation",
                "🚀 Skill Enhancement",
                "📊 ATS Match Analysis",
                "⚖️ Resume Comparison",
                "💬 AI Chat Assistant"
            ],
            index=0
        )
        
        st.markdown("---")
        st.markdown("### 📚 About")
        st.markdown("""
        **ResumeInsight** helps you:
        - ✅ Optimize for ATS systems
        - ✅ Get professional feedback
        - ✅ Identify skill gaps
        - ✅ Compare resumes
        - ✅ Get AI-powered advice
        """)
        
        st.markdown("---")
        st.markdown("🔒 **Privacy**: All data is processed securely. No resume data is stored permanently.")
    
    # Main content area
    if analysis_type == "⚖️ Resume Comparison":
        resume_comparison_page()
    elif analysis_type == "💬 AI Chat Assistant":
        resume_text = None
        if uploaded_file and validate_pdf(uploaded_file):
            resume_text = extract_text_from_pdf(uploaded_file)
        chat_assistant_page(resume_text, job_description)
    else:
        # For other features, require resume and job description
        if not uploaded_file:
            st.markdown('<div class="warning-box">⚠️ Please upload your resume to get started</div>', unsafe_allow_html=True)
            
            # Show feature preview
            st.markdown("### ✨ Features Overview")
            
            col1, col2, col3 = st.columns(3)
            
            with col1:
                st.markdown("""
                <div class="feature-card">
                    <h3>🧠 HR Evaluation</h3>
                    <p>Get professional HR-style feedback on your resume including strengths, weaknesses, and hiring recommendations.</p>
                </div>
                """, unsafe_allow_html=True)
            
            with col2:
                st.markdown("""
                <div class="feature-card">
                    <h3>🚀 Skill Enhancement</h3>
                    <p>Receive personalized skill gap analysis with learning resources and career growth roadmap.</p>
                </div>
                """, unsafe_allow_html=True)
            
            with col3:
                st.markdown("""
                <div class="feature-card">
                    <h3>📊 ATS Analysis</h3>
                    <p>Check ATS compatibility with percentage scoring, keyword analysis, and optimization tips.</p>
                </div>
                """, unsafe_allow_html=True)
            
            return
        
        if not job_description:
            st.markdown('<div class="warning-box">⚠️ Please provide a job description for better analysis</div>', unsafe_allow_html=True)
            return
        
        # Validate and extract text from PDF
        if validate_pdf(uploaded_file):
            resume_text = extract_text_from_pdf(uploaded_file)
            
            if not resume_text:
                st.error("❌ Could not extract text from the PDF. Please ensure it's a valid text-based PDF.")
                return
            
            # Show success message
            st.markdown(f'<div class="success-box">✅ Resume uploaded successfully! ({len(resume_text)} characters extracted)</div>', unsafe_allow_html=True)
            
            # Route to appropriate page
            if analysis_type == "🧠 HR Evaluation":
                hr_evaluation_page(resume_text, job_description)
            elif analysis_type == "🚀 Skill Enhancement":
                skill_enhancement_page(resume_text, job_description)
            elif analysis_type == "📊 ATS Match Analysis":
                ats_match_page(resume_text, job_description)


if __name__ == "__main__":
    main()
