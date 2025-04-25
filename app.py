from flask import Flask, request, render_template
from langchain.docstore.document import Document
from langchain.embeddings import HuggingFaceEmbeddings
from langchain.vectorstores import FAISS
from langchain.chains import RetrievalQA
from langchain_community.llms import Ollama
from langchain.prompts import PromptTemplate
import pandas as pd
import os

app = Flask(__name__)

# Configuration for Excel sheets
excel_config = {
    "courses": {
        "path": "flask/Documents/Courses.xlsx",
        "content_cols": ["id", "title", "rating", "num_reviews", "num_published_lectures", "duration"],
        "embeddings": HuggingFaceEmbeddings(model_name="BAAI/bge-small-en-v1.5")
    },
    "skills": {
        "path": "flask/Documents/SkillStacks.xlsx",
        "content_cols": ["skills"],
        "embeddings": HuggingFaceEmbeddings(model_name="BAAI/bge-small-en-v1.5")
    },
    "studymaterials": {
        "path": "flask/Documents/StudyResources.xlsx",
        "content_cols": ["Resource_Name", "Type", "Link"],
        "embeddings": HuggingFaceEmbeddings(model_name="BAAI/bge-small-en-v1.5")
    },
    "internships": {
        "path": "flask/Documents/Internships.xlsx",
        "content_cols": ["internship_title", "company_name", "location", "start_date", "duration", "stipend"],
        "embeddings": HuggingFaceEmbeddings(model_name="BAAI/bge-small-en-v1.5")
    },
    "projects": {
        "path": "flask/Documents/Projects.xlsx",
        "content_cols": ["Project Title", "Problem Statement", "Required Skills"],
        "embeddings": HuggingFaceEmbeddings(model_name="BAAI/bge-small-en-v1.5")
    }
}

ollama_llm = Ollama(model="llama2:latest", temperature=0.3)

vector_stores = {}

# Process Excel files
for category, config in excel_config.items():
    file_path = config["path"]
    if not os.path.exists(file_path):
        print(f"Skipping {category}: File not found - {file_path}")
        continue
    df = pd.read_excel(file_path)
    missing_cols = [col for col in config["content_cols"] if col not in df.columns]
    if missing_cols:
        print(f"Skipping {category}: Missing columns {missing_cols}")
        continue
    documents = []
    for _, row in df.iterrows():
        content = "\n".join([f"{col}: {row[col]}" for col in config["content_cols"]])
        metadata = {"category": category, "source": file_path}
        documents.append(Document(page_content=content, metadata=metadata))
    vector_stores[category] = FAISS.from_documents(documents=documents, embedding=config["embeddings"])

# Prompt templates for each category
courses_qa_template = """
You are an academic assistant. Provide a list of courses based ONLY on the context below, which is extracted from the Courses Excel file.
Each course must be displayed with the following details, one per line:
- ID: [value]
- Title: [value]
- Rating: [value]
- Number of Reviews: [value]
- Number of Published Lectures: [value]
- Duration: [value]
Separate each course with "---" on a new line. Do NOT add any extra information beyond the requested fields. If no relevant courses are found, respond ONLY with: "Not found in database."
Example output:
ID: 101
Title: Python Basics
Rating: 4.5
Number of Reviews: 1200
Number of Published Lectures: 50
Duration: 10 hours
---
ID: 102
Title: Data Science Intro
Rating: 4.7
Number of Reviews: 800
Number of Published Lectures: 40
Duration: 12 hours
Context: {context}
List of relevant courses:
"""

skills_qa_template = """
You are an academic assistant. Provide a list of skills based ONLY on the context below, which is extracted from the Skills Excel file.
Each skill must be displayed as:
- Skill: [value]
Separate each skill with "---" on a new line. Do NOT add any extra information. If no relevant skills are found, respond ONLY with: "Not found in database."
Example output:
Skill: Python
---
Skill: Data Analysis
Context: {context}
List of relevant skills:
"""

studymaterials_qa_template = """
You are an academic assistant. Provide a list of study materials based ONLY on the context below, which is extracted from the Study Materials Excel file.
Each study material must be displayed with the following details, one per line:
- Resource Name: [value]
- Type: [value]
- Link: [value]
Separate each study material with "---" on a new line. Do NOT add any extra information beyond the requested fields. If no relevant materials are found, respond ONLY with: "Not found in database."
Example output:
Resource Name: Python Crash Course
Type: Book
Link: http://example.com/python
---
Resource Name: SQL Tutorial
Type: Video
Link: http://example.com/sql
Context: {context}
List of relevant study materials:
"""

internships_qa_template = """
You are an academic assistant. Provide a list of internship opportunities based ONLY on the context below, which is extracted from the Internships Excel file.
Each internship must be displayed with the following details, one per line:
- Internship Title: [value]
- Company Name: [value]
- Location: [value]
- Start Date: [value]
- Duration: [value]
- Stipend: [value]
Separate each internship with "---" on a new line. Do NOT add any extra information beyond the requested fields. If no relevant internships are found, respond ONLY with: "Not found in database."
Example output:
Internship Title: Software Intern
Company Name: TechCorp
Location: Remote
Start Date: 2025-06-01
Duration: 3 months
Stipend: $1000/month
---
Internship Title: Data Analyst Intern
Company Name: DataInc
Location: New York
Start Date: 2025-07-01
Duration: 6 months
Stipend: $1200/month
Context: {context}
List of relevant internships:
"""

projects_qa_template = """
You are an academic assistant. Provide a list of project opportunities based ONLY on the context below, which is extracted from the Projects Excel file.
Each project must be displayed with the following details, one per line:
- Project Title: [value]
- Problem Statement: [value]
- Required Skills: [value]
Separate each project with "---" on a new line. Do NOT add any extra information beyond the requested fields. If no relevant projects are found, respond ONLY with: "Not found in database."
Example output:
Project Title: Web App Development
Problem Statement: Build a responsive website
Required Skills: HTML, CSS, JavaScript
---
Project Title: AI Chatbot
Problem Statement: Create a conversational AI
Required Skills: Python, NLP
Context: {context}
List of relevant projects:
"""

def query_database_by_category(user_query: str, category: str) -> str:
    vectorstore = vector_stores.get(category)
    if not vectorstore:
        return f"No data available for category: {category}"
    if category == "courses":
        prompt_template = courses_qa_template
    elif category == "skills":
        prompt_template = skills_qa_template
    elif category == "studymaterials":
        prompt_template = studymaterials_qa_template
    elif category == "internships":
        prompt_template = internships_qa_template
    elif category == "projects":
        prompt_template = projects_qa_template
    else:
        return "Invalid category selected."
    
    qa_chain = RetrievalQA.from_chain_type(
        llm=ollama_llm,
        chain_type="stuff",
        retriever=vectorstore.as_retriever(),
        chain_type_kwargs={"prompt": PromptTemplate.from_template(prompt_template)}
    )
    
    try:
        result = qa_chain.invoke({"query": user_query})
        return result["result"]
    except Exception as e:
        return f"Error processing query for {category}: {str(e)}"

def build_query(details: dict) -> str:
    name = details.get("name", "User")
    interest = details.get("interest", "")
    skills = details.get("skills", "")
    experience = details.get("experience", "")
    learning_style = details.get("learning_style", "")
    study_time = details.get("study_time", "")
    extra_info = details.get("extra_info", "")
    internship_location = details.get("internship_location", "")
    internship_start_date = details.get("internship_start_date", "")
    internship_duration = details.get("internship_duration", "")
    stipend_expectation = details.get("stipend_expectation", "")
    project_area = details.get("project_area", "")
    project_complexity = details.get("project_complexity", "")
    project_extra = details.get("project_extra", "")
    
    query = (
        f"My name is {name}. I am interested in {interest}. "
        f"My current skills include {skills}. I have a(n) {experience} experience level, "
        f"and I prefer a {learning_style} learning style. "
        f"I can dedicate about {study_time} per week for learning. "
        f"Additional academic information: {extra_info}. "
        f"For internship opportunities, I prefer locations like {internship_location}, starting around {internship_start_date}, "
        f"with a duration of {internship_duration} and stipend expectations of {stipend_expectation}. "
        f"For project opportunities, I am interested in projects related to {project_area} with a {project_complexity} complexity, "
        f"and here is some extra project information: {project_extra}. "
        "Based on this, what courses, skills improvements, study materials, internship opportunities, or project opportunities would you recommend?"
    )
    return query

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/chatbot')
def chatbot():
    return render_template('index.html')

@app.route('/query', methods=['POST'])
def handle_query():
    details = {
        "name": request.form.get("name", "").strip(),
        "interest": request.form.get("interest", "").strip(),
        "skills": request.form.get("skills", "").strip(),
        "experience": request.form.get("experience", "").strip(),
        "learning_style": request.form.get("learning_style", "").strip(),
        "study_time": request.form.get("study_time", "").strip(),
        "extra_info": request.form.get("extra_info", "").strip(),
        "internship_location": request.form.get("internship_location", "").strip(),
        "internship_start_date": request.form.get("internship_start_date", "").strip(),
        "internship_duration": request.form.get("internship_duration", "").strip(),
        "stipend_expectation": request.form.get("stipend_expectation", "").strip(),
        "project_area": request.form.get("project_area", "").strip(),
        "project_complexity": request.form.get("project_complexity", "").strip(),
        "project_extra": request.form.get("project_extra", "").strip()
    }
    selected_categories = request.form.getlist("categories")
    if not selected_categories:
        return render_template('index.html', error="Please select at least one recommendation category.")
    if not details["interest"] or not details["skills"]:
        return render_template('index.html', error="Please provide your interests and skills.")
    user_query = build_query(details)
    responses = {}
    for category in selected_categories:
        responses[category] = query_database_by_category(user_query, category)
    return render_template('results.html', responses=responses, query=user_query)

if __name__ == '__main__':
    app.run(debug=True)
