# ResumeInsight 🤖

**AI-Powered Resume Analysis & Optimization Tool**

A comprehensive AI-driven resume analysis application that helps job seekers optimize their resumes for ATS (Applicant Tracking System) compatibility and provides professional HR-level evaluation using Google's Gemini AI.

![Python](https://img.shields.io/badge/Python-3.7+-blue.svg)
![Streamlit](https://img.shields.io/badge/Streamlit-1.31.0-red.svg)
![Gemini AI](https://img.shields.io/badge/Gemini-AI-purple.svg)
![License](https://img.shields.io/badge/License-MIT-green.svg)

---

## ✨ Features

### 🧠 HR Professional Evaluation
- Comprehensive HR-style resume analysis
- Detailed feedback on strengths and weaknesses
- Technical and professional alignment assessment
- Communication and formatting quality evaluation
- Clear hiring recommendations

### 🚀 Skill Enhancement Suggestions
- Personalized skill gap analysis
- Practical improvement recommendations
- Short-term and long-term career growth roadmap
- Certification and course suggestions
- Hands-on project ideas for skill building

### 📊 ATS Match Analysis
- Percentage-based compatibility scoring
- Keyword and skill matching analysis
- Experience and role fit evaluation
- Education and certification alignment
- Visual progress indicators and interactive charts
- Actionable optimization tips

### ⚖️ Resume Comparison
- Side-by-side comparison of two resumes
- Detailed analysis of strengths and weaknesses
- Category-wise scoring comparison
- Clear recommendation on which resume performs better
- Structured comparison report

### 💬 AI Chat Assistant
- Interactive Q&A about your resume
- Personalized career advice and suggestions
- Real-time analysis and feedback
- Context-aware responses based on your resume and job description

---

## 🛠️ Technology Stack

- **Frontend**: Streamlit
- **AI Model**: Google Gemini 2.0 Flash
- **PDF Processing**: PyPDF2, pdf2image
- **Data Visualization**: Plotly, Matplotlib, WordCloud
- **Image Processing**: Pillow (PIL)
- **Environment Management**: python-dotenv

---

## 📋 Prerequisites

- Python 3.7 or higher
- Google API key for Gemini AI ([Get it here](https://makersuite.google.com/app/apikey))
- pip (Python package manager)

---

## 🚀 Installation

### 1. Clone or Download the Repository

```bash
# If using git
git clone <repository-url>
cd resume

# Or simply download and extract the files
```

### 2. Create a Virtual Environment (Recommended)

```bash
# Windows
python -m venv venv
venv\Scripts\activate

# macOS/Linux
python3 -m venv venv
source venv/bin/activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Set Up Environment Variables

Create a `.env` file in the project root directory:

```bash
# Copy the example file
copy .env.example .env  # Windows
cp .env.example .env    # macOS/Linux
```

Edit the `.env` file and add your Google API key:

```
GOOGLE_API_KEY=your_actual_api_key_here
```

**How to get your Google API Key:**
1. Visit [Google AI Studio](https://makersuite.google.com/app/apikey)
2. Sign in with your Google account
3. Click "Create API Key"
4. Copy the key and paste it in your `.env` file

---

## 📖 Usage

### Starting the Application

```bash
streamlit run app.py
```

The application will open in your default web browser at `http://localhost:8501`

### Using the Features

#### 1. Upload Resume & Job Description
- Click "Upload your Resume (PDF)" in the sidebar
- Paste the job description in the text area
- Select your desired analysis type

#### 2. HR Evaluation
- Select "🧠 HR Evaluation" from the sidebar
- Click "Generate HR Evaluation"
- Review the comprehensive HR analysis
- Download the report for future reference

#### 3. Skill Enhancement
- Select "🚀 Skill Enhancement"
- Click "Get Skill Recommendations"
- Review personalized learning roadmap
- Download the skill development plan

#### 4. ATS Match Analysis
- Select "📊 ATS Match Analysis"
- Click "Analyze ATS Match"
- View your match percentage and detailed breakdown
- Follow optimization tips to improve your score

#### 5. Resume Comparison
- Select "⚖️ Resume Comparison"
- Upload two resumes to compare
- Provide the job description
- Click "Compare Resumes"
- Review side-by-side analysis and recommendations

#### 6. AI Chat Assistant
- Select "💬 AI Chat Assistant"
- Ask questions about your resume
- Get personalized advice and suggestions
- Continue the conversation for deeper insights

---

## 📊 Sample Analysis Reports

### HR Evaluation Report Includes:
- 📋 Overall Impression
- 💪 Core Strengths (4-6 key points)
- 🎯 Technical & Professional Alignment (rated 1-10)
- 📊 Gap Analysis (Critical/Important/Nice-to-have)
- 💬 Communication & Presentation Quality (rated 1-10)
- ✅ Final Recommendation

### Skill Enhancement Report Includes:
- 🎯 Skill Gap Analysis
- 📚 Short-term Learning Roadmap (1-3 months)
- 📚 Long-term Learning Roadmap (3-12 months)
- 🏆 Recommended Certifications
- 💡 Practical Project Ideas
- 🚀 Career Growth Tips

### ATS Match Report Includes:
- 📊 Overall Match Score (percentage)
- 🔑 Matched & Missing Keywords
- 🛠️ Skills Assessment
- 💼 Experience Alignment
- 🎓 Education & Certifications
- ⚡ ATS Optimization Tips
- 📈 Competitive Analysis

---

## 🎯 Key Benefits

✅ **ATS Optimization**: Ensure your resume passes automated screening systems  
✅ **Professional Feedback**: Get HR-level analysis and recommendations  
✅ **Skill Development**: Identify gaps and get actionable improvement plans  
✅ **Competitive Analysis**: Compare your resume against others  
✅ **AI-Powered Insights**: Leverage advanced AI for personalized advice  
✅ **Time-Saving**: Get instant feedback instead of waiting for human review  
✅ **Data-Driven**: Make informed decisions based on detailed analytics  

---

## 🔒 Privacy & Security

- ✅ All data processing is done locally on your machine
- ✅ No resume data is stored permanently
- ✅ Google API is used only for AI analysis
- ✅ PDF files are processed in memory only
- ✅ No data is shared with third parties
- ✅ You have full control over your data

---

## 📁 Project Structure

```
resume/
├── app.py                      # Main Streamlit application
├── requirements.txt            # Python dependencies
├── .env.example               # Environment variables template
├── .gitignore                 # Git ignore rules
├── README.md                  # This file
└── utils/
    ├── __init__.py           # Package initializer
    ├── pdf_processor.py      # PDF handling utilities
    ├── gemini_client.py      # Gemini AI integration
    ├── prompts.py            # AI prompt templates
    └── visualizations.py     # Chart and graph utilities
```

---

## 🐛 Troubleshooting

### Common Issues

**Issue**: "GOOGLE_API_KEY not found"
- **Solution**: Make sure you created a `.env` file with your API key

**Issue**: "Could not extract text from PDF"
- **Solution**: Ensure your PDF is text-based, not scanned images. Try a different PDF.

**Issue**: "API quota exceeded"
- **Solution**: You've reached your API limit. Wait or upgrade your Google API plan.

**Issue**: "Module not found" errors
- **Solution**: Run `pip install -r requirements.txt` again

**Issue**: Application won't start
- **Solution**: Make sure you're in the correct directory and virtual environment is activated

---

## 🤝 Contributing

Contributions are welcome! Feel free to:
- Report bugs
- Suggest new features
- Submit pull requests
- Improve documentation

---

## 📝 License

This project is licensed under the MIT License - see the LICENSE file for details.

---

## 🙏 Acknowledgments

- **Google Gemini AI** for powering the intelligent analysis
- **Streamlit** for the amazing web framework
- **Open Source Community** for the excellent libraries used in this project

---

## 📧 Support

If you encounter any issues or have questions:
1. Check the Troubleshooting section above
2. Review the [Streamlit documentation](https://docs.streamlit.io/)
3. Check [Google AI documentation](https://ai.google.dev/docs)

---

## 🌟 Star This Project

If you find this tool helpful, please consider giving it a star! ⭐

---

**Made with ❤️ using Python, Streamlit, and Google Gemini AI**
