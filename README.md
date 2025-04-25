# 🎓 Academic Assistant & Recommendation System

A **Flask**-based web application that provides **personalized**, **Retrieval-Augmented Generation (RAG)**-powered recommendations for:

- 📚 **Courses**  
- 🛠️ **Skills**  
- 📖 **Study Materials**  
- 💼 **Internships**  
- 💡 **Projects**  

It uses **LangChain**, **FAISS**, **HuggingFace Embeddings**, and **Ollama’s LLaMA2**.

---

## Table of Contents

1. [Features](#features)  
2. [Tech Stack](#tech-stack)  
3. [Project Structure](#project-structure)  
4. [Installation](#installation)  
5. [Usage](#usage)  
6. [Hello](#hello)  
7. [Contributing](#contributing)  
8. [License](#license)  

---

## Features

- 🔍 **Personalized AI Recommendations**  
- 📊 **Excel-Based Knowledge Base** (Courses, Skills, Materials, Internships, Projects)  
- 🤖 **Natural Language Queries** via LangChain + Ollama  
- ⚡ **Fast Similarity Search** with FAISS  
- 🔧 **Custom Prompt Templates** per category  

---

## Tech Stack

| Component        | Technology                           |
|------------------|--------------------------------------|
| **Backend**      | Flask                                |
| **Embeddings**   | HuggingFace (`BAAI/bge-small-en-v1.5`) |
| **Vector Store** | FAISS                                |
| **RAG Orchestration** | LangChain RetrievalQA          |
| **LLM**          | Ollama + LLaMA2                      |
| **Data Handling**| Pandas + Excel                       |

---

## Project Structure

```bash
academic-assistant/
├── flask/
│   ├── app.py
│   ├── Documents/
│   │   ├── Courses.xlsx
│   │   ├── SkillStacks.xlsx
│   │   ├── StudyResources.xlsx
│   │   ├── Internships.xlsx
│   │   └── Projects.xlsx
│   └── templates/
│       ├── home.html
│       ├── index.html
│       └── results.html
└── requirements.txt
