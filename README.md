# 🤖 AI-Powered Resume Screener

This project is a web application that leverages Google's Gemini AI to analyze and score resumes against job descriptions. It provides a quick and efficient way for recruiters or applicants to gauge the compatibility of a resume for a given role.



---

## ✨ Features

- **PDF Parsing**: Extracts text directly from uploaded PDF resumes.
- **AI-Powered Analysis**: Uses Google's `gemini-1.5-flash` model to understand and compare texts.
- **Compatibility Score**: Generates a percentage match score based on the job description.
- **Keyword Analysis**: Lists key skills and requirements from the job description that are missing in the resume.
- **Professional Summary**: Provides a concise, AI-generated summary of the candidate's profile.
- **Interactive UI**: A simple and user-friendly web interface built with Streamlit.

---

## 🛠️ Tech Stack

- **Language**: Python
- **AI/ML**: Google Generative AI (Gemini)
- **Web Framework**: Streamlit
- **Libraries**: PyPDF2, python-dotenv

---

## 🚀 Setup and Installation

To run this project locally, follow these steps:

1. **Clone the repository:**
   ```bash
   git clone [https://github.com/](https://github.com/)<ShrinithShetty>/ai-resume-screener.git
   cd ai-resume-screener


2. Create and activate a virtual environment:
   # Create the environment
   python -m venv venv

   # Activate on Windows
   venv\Scripts\activate

   # Activate on macOS/Linux
   source venv/bin/activate

3. Install the required dependencies:
   pip install -r requirements.txt

4. Set up your environment variables:
   Create a file named .env in the root of the project folder.
   Add your Google API key to the .env file as follows:
   GOOGLE_API_KEY="YOUR_API_KEY_HERE"


# Usage
Once the setup is complete, run the following command in your terminal to launch the Streamlit application:
streamlit run app.py
