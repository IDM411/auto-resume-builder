🚀 AI Resume Architect (Techy Purple Edition)
The AI Resume Architect is a privacy-first, high-performance local application designed to re-engineer master resumes into high-scoring, ATS-optimized documents. Leveraging the Qwen 2.5 32B model via Ollama, it applies elite recruiter logic and the STAR method to ensure your experience matches job descriptions with 100% integrity.

🛠️ Key Features
Deep ATS Optimization: Injects high-priority technical nouns and semantic synonyms found in job descriptions.

The "Company Scout": Enter a company URL to automatically scrape their mission, history, and values to align your resume with their culture.

Strategic Match Dashboard: Real-time "Before vs. After" scoring and recruiter critique.

STAR-Method Re-writing: Every bullet point is re-architected into Situation, Task, Action, and Result.

Strategic Change Log: A GitHub-style "Diff View" showing exactly what was changed and the tactical reasoning behind it.

Local & Private: No data ever leaves your 64GB workstation. Zero API costs, 100% data sovereignty.

⚙️ Tech Stack
Backend: Python 3.10+, FastAPI, Uvicorn

Frontend: HTML5, CSS3 (Glassmorphism), Vanilla JavaScript

AI Engine: Ollama running Qwen2.5:32b

Libraries: * trafilatura (Web Scraping)

pdfplumber (PDF Extraction)

python-docx & fpdf (Document Generation)

🚀 Setup & Installation
1. Prerequisites
Windows 10/11 with 32GB+ RAM (64GB recommended for 32B model).

Ollama installed.

2. Pull the Model
Open your terminal and pull the heavy-duty architect:

PowerShell
ollama pull qwen2.5:32b
3. Clone & Environment Setup
PowerShell
git clone https://github.com/IDM411/auto-resume-builder.git
cd auto-resume-builder
python -m venv venv
.\venv\Scripts\activate
pip install -r requirements.txt
4. Launch the Architect
PowerShell
python -m uvicorn main:app --reload
Visit http://localhost:8000 to start architecting.

📝 Recruiter Logic Used
This system doesn't just "fix grammar." It follows a specific Decision Matrix:

Categorization: Intelligent deduplication between "Work Experience" and "Projects."

Keyword Density: Prioritizing hard skill nouns over soft skill fluff.

STAR Validation: Ensuring every bullet point includes a quantifiable result.

Culture Mapping: Re-indexing your "Summary" to reflect the company's specific mission retrieved by the Scout.

🛡️ License
Distributed under the MIT License. See LICENSE for more information.

Pro-Tip for Developers
Since the Qwen 32B model is ~19GB, the initial "cold start" takes about 60s on a 64GB system. The backend is configured with keep_alive: -1, meaning once it's loaded into your VRAM/RAM, subsequent tailoring sessions will be nearly instantaneous.

Why this is a "Power User" project
If you are pushing this to GitHub to show recruiters, make sure to highlight the Local LLM aspect. It shows you understand:

Data Privacy: Handling sensitive resume data without third-party APIs.

System Architecture: Managing large models and high-memory workloads.

Full-Stack Development: Connecting a modern UI to a complex AI backend.

Does this README cover everything you've built, or should we add a "Roadmap" section for features you want to add next?
