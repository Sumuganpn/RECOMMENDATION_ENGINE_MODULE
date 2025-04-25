🎓 Academic Assistant and Recommendation System
This project is a Flask-based web application designed to assist students in discovering personalized educational opportunities including courses, skill-building materials, study resources, internships, and projects. The system leverages Retrieval-Augmented Generation (RAG) using LangChain, FAISS, HuggingFace Embeddings, and Ollama's LLaMA2 model.

🚀 Features
🔍 Personalized Recommendations: Generates customized suggestions based on user profile.

📄 Excel-Based Knowledge Base: Loads structured academic data from multiple Excel sheets.

🤖 LLM-Powered Querying: Uses LangChain’s RetrievalQA with Ollama + LLaMA2 for natural language query processing.

🔗 Multi-Category Support: Supports five categories:

Courses

Skills

Study Materials

Internships

Projects

⚙️ Dynamic Prompt Templates: Tailored prompt structure per category for precise and informative output.

🗂️ Folder Structure
pgsql
Copy
Edit
├── flask/
│   ├── Documents/
│   │   ├── Courses.xlsx
│   │   ├── SkillStacks.xlsx
│   │   ├── StudyResources.xlsx
│   │   ├── Internships.xlsx
│   │   └── Projects.xlsx
│   ├── templates/
│   │   ├── home.html
│   │   ├── index.html
│   │   └── results.html
│   └── app.py  <-- (main application file)
🧠 Technologies Used
Flask – Python micro-framework for the web interface.

LangChain – For building the RAG pipeline.

HuggingFace Embeddings (BAAI/bge-small-en-v1.5) – For semantic vector generation.

FAISS – Facebook AI Similarity Search for vector storage and retrieval.

Ollama + LLaMA2 – For LLM-powered response generation.

Pandas – For Excel data processing.

🔧 Setup Instructions
1. Clone the Repository
bash
Copy
Edit
git clone https://github.com/your-username/academic-assistant.git
cd academic-assistant
2. Install Dependencies
bash
Copy
Edit
pip install -r requirements.txt
Ensure you have ollama installed and LLaMA2 model pulled:

bash
Copy
Edit
ollama run llama2
3. Place Your Excel Files
Make sure the following Excel files are located in flask/Documents/:

Courses.xlsx

SkillStacks.xlsx

StudyResources.xlsx

Internships.xlsx

Projects.xlsx

4. Run the Application
bash
Copy
Edit
python app.py
Navigate to http://127.0.0.1:5000 in your browser.

🧾 How It Works
User Input: The user fills out a form with their academic profile, interests, and preferences.

Query Building: A detailed query string is constructed from the input.

Vector Search: The system searches relevant vectors using FAISS per category.

LLM Generation: Retrieved context is passed to Ollama's LLaMA2 model using a category-specific prompt.

Results Rendering: The final recommendations are displayed to the user.

📌 Customization
Modify prompt templates for each category inside app.py.

Update or expand Excel files in flask/Documents for new data.

🧪 Example Use Case
Input:

Interest: Data Science

Skills: Python, SQL

Experience: Intermediate

Preferred Learning Style: Visual

Internship Location: Remote

Project Area: Machine Learning

Output:

Recommended Courses on Data Science

Skill gaps and suggestions

Videos and books on Python/SQL

Remote internships starting soon

ML-based project opportunities

🛡️ License
This project is licensed under the MIT License.

🤝 Contributors
Sumugan P N – Developer, RAG Integration

You can add more contributors here...
