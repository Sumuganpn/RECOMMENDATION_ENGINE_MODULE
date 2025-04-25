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
5. [Configuration](#configuration)
6. [Usage](#usage)
7. [API Endpoints](#api-endpoints)
8. [Examples](#examples)
9. [Troubleshooting & FAQs](#troubleshooting--faqs)
10. [Contributing](#contributing)
11. [License](#license)
12. [Acknowledgments](#acknowledgments)

---

## Features

- 🔍 **Personalized AI Recommendations** based on user profile and preferences
- 📊 **Excel-Based Knowledge Base** (Courses, Skills, Materials, Internships, Projects)
- 🤖 **Natural Language Queries** processed via LangChain + Ollama LLM
- ⚡ **Fast Similarity Search** with FAISS vector store
- 📝 **Custom Prompt Templates** per category for consistent output format
- 🔒 **Local LLM Hosting** with Ollama for privacy and speed
- 🌐 **Web UI** built with Flask and Jinja templates

---

## Tech Stack

| Component             | Technology                             |
|-----------------------|----------------------------------------|
| **Backend**           | Flask                                  |
| **Embeddings**        | HuggingFace (`BAAI/bge-small-en-v1.5`) |
| **Vector Store**      | FAISS                                  |
| **RAG Orchestration** | LangChain RetrievalQA                  |
| **LLM**               | Ollama + LLaMA2                        |
| **Data Handling**     | Pandas + Excel                         |
| **Frontend**          | HTML, CSS (Bootstrap optional)         |

---

## Project Structure

```bash
academic-assistant/
├── flask/
│   ├── app.py                 # Main Flask application
│   ├── Documents/             # Excel data sources
│   │   ├── Courses.xlsx
│   │   ├── SkillStacks.xlsx
│   │   ├── StudyResources.xlsx
│   │   ├── Internships.xlsx
│   │   └── Projects.xlsx
│   └── templates/             # Jinja2 templates for UI
│       ├── home.html
│   │   ├── index.html
│   │   └── results.html
├── requirements.txt           # Python dependencies
├── README.md                  # Project documentation
└── LICENSE                    # MIT License file
```

---

## Installation

1. **Clone Repository**
   ```bash
   git clone https://github.com/your-username/academic-assistant.git
   cd academic-assistant/flask
   ```

2. **Create Virtual Environment** (optional but recommended)
   ```bash
   python -m venv venv
   source venv/bin/activate  # Linux/Mac
   venv\Scripts\activate   # Windows
   ```

3. **Install Dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Download & Run LLaMA2 Model**
   ```bash
   ollama pull llama2                        
   ollama run llama2                          
   ```

5. **Start Flask Application**
   ```bash
   python app.py
   ```

6. **Access in Browser**: Open [http://127.0.0.1:5000](http://127.0.0.1:5000)

---

## Configuration

1. **Excel Files**: Ensure your Excel files are placed in `flask/Documents/`.
2. **File Paths**: Update paths in `app.py` under `excel_config` if necessary.
3. **LLM Settings**: Adjust temperature, model name, or other parameters in the `ollama_llm` instantiation.

---

## Usage

1. Navigate to the **Home** page to see project overview.
2. Go to **Recommendation Bot** (`/chatbot`) to fill in your profile:
   - Name, interests, skills, learning style, time commitment, etc.
   - Select categories for recommendations.
3. Submit to view tailored suggestions.

---

## API Endpoints

| Endpoint   | Method | Description                               |
|------------|--------|-------------------------------------------|
| `/`        | GET    | Home page                                 |
| `/chatbot` | GET    | Chatbot form page                         |
| `/query`   | POST   | Process form data and return recommendations |


---

## Examples

**Sample Input**
```text
Interest: Data Science
Skills: Python, SQL
Experience: Intermediate
Learning Style: Visual
Study Time: 8 hours/week
Internship Location: Remote
Project Area: Machine Learning
```

**Sample Output**
```
ID: 205
Title: Advanced Data Science
Rating: 4.8
Number of Reviews: 1,200
Number of Published Lectures: 60
Duration: 15 hours
---
Skill: Deep Learning
---
Resource Name: Hands-On Machine Learning
Type: Book
Link: http://example.com/ml-book
---
Internship Title: ML Intern
Company Name: AI Solutions
Location: Remote
Start Date: 2025-06-15
Duration: 3 months
Stipend: $1500/month
---
Project Title: Image Classification App
Problem Statement: Build a CNN-based classifier
Required Skills: Python, TensorFlow
```

---

## Troubleshooting & FAQs

**Q1: Missing Excel file errors?**
- Verify the path and file name in `app.py` under `excel_config`.

**Q2: LLaMA model not loading?**
- Ensure `ollama pull llama2` completed successfully.
- Check your Ollama installation and environment.

**Q3: Performance is slow?**
- Pre-generate FAISS indices and cache them.
- Increase system memory or use a smaller embedding model.


---


## Contributing

1. Fork the repository
2. Create a branch: `git checkout -b feature/YourFeature`
3. Commit your changes: `git commit -m "Add YourFeature"`
4. Push to your branch: `git push origin feature/YourFeature`
5. Open a Pull Request

Please follow the [Code of Conduct](CODE_OF_CONDUCT.md).

---

## License

Distributed under the **MIT License**. See `LICENSE` for details.

---

## Acknowledgments

- [LangChain](https://github.com/hwchase17/langchain)
- [FAISS](https://github.com/facebookresearch/faiss)
- [HuggingFace Embeddings](https://huggingface.co)
- [Ollama](https://ollama.ai)
- Inspiration from various educational platforms and RAG implementations.
