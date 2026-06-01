import streamlit as st
from PyPDF2 import PdfReader
from groq import Groq


GROQ_API_KEY = "YOUR_GROQ_API_KEY"

client = Groq(api_key=GROQ_API_KEY)


st.title("📄 AI Resume Analyzer")

st.write("Upload your resume and get AI-powered feedback!")



uploaded_file = st.file_uploader(
    "Choose your Resume",
    type=["pdf"]
)



if uploaded_file:

    st.success("Resume uploaded successfully!")

    reader = PdfReader(uploaded_file)

    text = ""

    for page in reader.pages:

        extracted_text = page.extract_text()

        if extracted_text:
            text += extracted_text

    st.subheader("📃 Extracted Resume Text")

    st.text(text)


    if st.button("Analyze Resume"):

        prompt = f"""
You are an expert ATS Resume Analyzer.

Analyze the following resume and provide:

1. ATS Score out of 100
2. Strengths
3. Weaknesses
4. Missing Skills
5. Suggestions for Improvement

Resume:

{text}
"""

        try:

            response = client.chat.completions.create(
                model="llama-3.3-70b-versatile",
                messages=[
                    {
                        "role": "user",
                        "content": prompt
                    }
                ]
            )

            analysis = response.choices[0].message.content

            st.subheader("AI Analysis")

            # Demo Progress Bar
            st.progress(85)

            st.write(analysis)

            st.download_button(
                label="Download Report",
                data=analysis,
                file_name="resume_analysis.txt",
                mime="text/plain"
            )

        except Exception as e:

            st.error(f"Error: {e}")