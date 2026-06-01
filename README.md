## Setup Instructions

1. Clone the repository

```bash
git clone https://github.com/chaitraask-013/AI-Resume-Analyzer.git
```

2. Install dependencies

```bash
pip install -r requirements.txt
```

3. Get a Groq API Key

4. Open `app.py`

Replace:

```python
GROQ_API_KEY = "YOUR_GROQ_API_KEY"
```

with your own Groq API Key.

5. Run the application

```bash
streamlit run app.py
```


# AI Resume Analyzer

An AI-powered Resume Analyzer built using Python, Streamlit, PyPDF2, Groq API, and Llama 3.3.

## Features

- Upload Resume PDF
- Extract Resume Text
- AI-Powered Analysis
- ATS Score Evaluation
- Strengths & Weaknesses Detection
- Missing Skills Identification
- Suggestions for Improvement
- Download Analysis Report

## Technologies Used

- Python
- Streamlit
- PyPDF2
- Groq API
- Llama 3.3

## How It Works

Resume Upload
↓
PDF Text Extraction
↓
AI Analysis using Llama 3.3
↓
ATS Score & Suggestions
↓
Download Report

## Future Enhancements

- Resume vs Job Description Matching
- Real ATS Score Progress Bar
- PDF Report Generation
- Resume Ranking System
