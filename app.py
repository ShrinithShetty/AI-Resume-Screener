import streamlit as st
import google.generativeai as genai
import os
import PyPDF2 as pdf
import json
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Configure the Google Generative AI client
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

# --- Function to get response from Gemini Pro ---
def get_gemini_response(input_text):
    # Use the 'gemini-1.5-flash-latest' model as it's efficient
    model = genai.GenerativeModel('models/gemini-1.5-flash-latest')
    response = model.generate_content(input_text)
    # The response might be in a markdown format (like ```json ... ```), so we extract the JSON part.
    # This is a robust way to handle the output.
    try:
        # Find the start and end of the JSON block
        json_part = response.text.split('```json')[1].split('```')[0]
        return json.loads(json_part)
    except (IndexError, json.JSONDecodeError):
        # If the response is not as expected, return an error message
        st.error("Failed to parse the response from the AI. Please try again.")
        return None


# --- Function to extract text from a PDF file ---
def input_pdf_text(uploaded_file):
    reader = pdf.PdfReader(uploaded_file)
    text = ""
    for page in range(len(reader.pages)):
        page = reader.pages[page]
        text += str(page.extract_text())
    return text

# --- Streamlit App Interface ---

# Set the page title and layout
st.set_page_config(page_title="AI Resume Screener", layout="wide")
st.title("🤖 AI-Powered Resume Screener")
st.text("Compare a resume against a job description to get a compatibility score and analysis.")

# Input field for the Job Description
jd = st.text_area("Paste the Job Description here", height=300)

# File uploader for the Resume
uploaded_file = st.file_uploader("Upload Your Resume (PDF)", type="pdf", help="Please upload a PDF file.")

# Submit button
submit = st.button("Analyze Resume")

if submit:
    if uploaded_file is not None and jd:
        # Show a spinner while processing
        with st.spinner('Analyzing...'):
            resume_text = input_pdf_text(uploaded_file)
            
            # The prompt for the AI
            input_prompt = f"""
            You are a highly skilled and experienced technical HR manager with expertise in data science.
            Your task is to review the provided resume against a specific job description.

            You must perform a detailed analysis and provide the following in a strict JSON format with no extra text or markdown:
            1.  "JD_Match": A percentage match of the resume to the job description.
            2.  "Missing_Keywords": A list of key skills or technologies from the job description that are NOT found in the resume.
            3.  "Profile_Summary": A concise, professional summary (3-4 sentences) evaluating the candidate's strengths and weaknesses based on the provided texts.

            Here is the resume text:
            {resume_text}

            Here is the job description:
            {jd}
            """
            
            response_data = get_gemini_response(input_prompt)

            if response_data:
                st.subheader("Analysis Result")
                
                # Display the match percentage
                st.metric(label="Job Description Match", value=f"{response_data.get('JD_Match', 0)}%")
                
                # Display the profile summary
                st.subheader("Profile Summary")
                st.write(response_data.get('Profile_Summary', 'No summary provided.'))

                # Display missing keywords
                st.subheader("Missing Keywords")
                missing_keywords = response_data.get('Missing_Keywords', [])
                if missing_keywords:
                    for keyword in missing_keywords:
                        st.write(f"- {keyword}")
                else:
                    st.write("No missing keywords identified.")

    else:
        st.error("Please provide both the job description and the resume.")