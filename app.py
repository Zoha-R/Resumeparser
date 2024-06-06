import streamlit as st
import google.generativeai as genai
import os
import PyPDF2 as pdf

api_key = 'AIzaSyD5zgNSxwZryEWTp1GYyIKGBLKdtrelxJw'
genai.configure(api_key=api_key)

from langchain_community.document_loaders import PyPDFLoader
import PyPDF2

# def input_pdf_text(pages):
#     text = ""
#     for page in pages:
#         text += page.page_content
#     return text

# # Step 4: Load and split the PDF file using PyPDFLoader
# file_path ="/content/Ali Zulqarnain.pdf"
# loader = PyPDFLoader(file_path)
# pages = loader.load_and_split()

# # Step 5: Pass the pages to the input_pdf_text function to extract text
# text = input_pdf_text(pages)

# # Optional: Print the extracted text for verification
# print(text)

from dotenv import load_dotenv
load_dotenv()


# genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))


#gemini function

def get_gemini_response(input):
    model=genai.GenerativeModel('gemini-pro')
    response = model.generate_content(input)
    return response.text

#convert pdf to text
def input_pdf_text(uploaded_file):
    reader=pdf.PdfReader(uploaded_file)
    text=""
    for page in range(len(reader.pages)):
        page=reader.pages[page]
        text+=str(page.extract_text())
    return text


# jd = """Job Summary:

#     Design, develop, and deploy machine learning models
#     Improve product performance with ML solutions

# Key Responsibilities:

#     Develop and optimize ML models
#     Collaborate with teams to understand business needs
#     Preprocess and analyze large datasets
#     Build data pipelines for ML models
#     Conduct experiments and evaluate models
#     Stay updated with ML research and advancements
#     Present findings to stakeholders
#     Improve model accuracy through iteration

# Qualifications:

#     Degree in Computer Science, Data Science, Statistics, or related field
#     Experience as a Machine Learning Engineer or similar role
#     Proficiency in Python, R, or similar languages
#     Experience with ML frameworks (TensorFlow, PyTorch, scikit-learn)
#     Knowledge of data preprocessing, feature engineering, and model evaluation
#     Familiarity with big data technologies (Hadoop, Spark)
#     Understanding of software engineering best practices
#     Strong problem-solving and communication skills

# Preferred Qualifications:

#     Experience with cloud platforms (AWS, GCP, Azure)
#     Knowledge of deep learning, NLP, and computer vision
#     Experience in deploying ML models in production
#     Understanding of DevOps practices and CI/CD pipelines"""

input_prompt ="""

# ### As a skilled Application Tracking System (ATS) with advanced knowledge in technology and data science, your role is to meticulously evaluate a candidate's resume based on the provided job description. 

# ### Your evaluation will involve analyzing the resume for relevant skills, experiences, and qualifications that align with the job requirements. Look for key buzzwords and specific criteria outlined in the job description to determine the candidate's suitability for the position.

# ### Provide a detailed assessment of how well the resume matches the job requirements, highlighting strengths, weaknesses, and any potential areas of concern. Offer constructive feedback on how the candidate can enhance their resume to better align with the job description and improve their chances of securing the position.

# ### Your evaluation should be thorough, precise, and objective, ensuring that the most qualified candidates are accurately identified based on their resume content in relation to the job criteria.

# ### Remember to utilize your expertise in technology and data science to conduct a comprehensive evaluation that optimizes the recruitment process for the hiring company. Your insights will play a crucial role in determining the candidate's compatibility with the job role.
# resume={text}
# jd={jd}
# ### Evaluation Output:
# 1. Calculate the percentage of match between the resume and the job description. Give a number and some explation
# 2. Identify any key keywords that are missing from the resume in comparison to the job description.
# 3. Offer specific and actionable tips to enhance the resume and improve its alignment with the job requirements.
"""

# response = get_gemini_response(input_prompt)

# # Step 9: Print the response
# print(response)

##streamlit

st.title("DDS Smart ATS")
st.text("Imporve your ATS resume score Match")
jd = st.text_area("Paste job description here")
uploaded_file= st.file_uploader("Upload your resume", type="pdf", help= "Please upload the pdf")

submit =  st.button('Check Your Score')
if submit:
    if uploaded_file is not None:
        text =  input_pdf_text(uploaded_file)
        response=get_gemini_response(input_prompt.format(text=text, jd=jd))
        st.subheader(response)