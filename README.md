# 🚀 AI Resume Architect (Techy Purple Edition)

**AI Resume Architect** is a privacy-first, high-performance local application built to re-engineer master resumes into high-scoring, ATS-optimized documents. Using **Qwen 2.5 32B via Ollama**, it applies recruiter-style logic and the **STAR method** to tailor resume content to job descriptions while keeping everything aligned with the candidate’s real experience.

---

## 🛠️ Features

- **Deep ATS Optimization**  
  Injects high-priority technical keywords and semantic synonyms from job descriptions to improve ATS relevance.

- **Strategic Match Dashboard**  
  Shows a real-time **before vs. after** comparison with recruiter-style critique.

- **STAR-Method Rewriting**  
  Reworks bullet points using the **Situation, Task, Action, Result** structure.

- **Strategic Change Log**  
  Displays a GitHub-style **diff view** so users can clearly see what changed and why.

- **Local and Private**  
  No data leaves your machine. No API costs, no cloud dependency, and full control over sensitive resume data.

---

## ⚙️ Tech Stack

### Backend
- Python 3.10+
- FastAPI
- Uvicorn

### Frontend
- HTML5
- CSS3
- Vanilla JavaScript

### AI Engine
- Ollama
- Qwen2.5:32b

### Libraries
- `pdfplumber` for PDF extraction
- `python-docx` and `fpdf` for document generation
- `trafilatura` for web scraping *(planned / optional future feature)*

---

## 🚀 Setup and Installation

### 1. Prerequisites
- Windows 10/11
- 32GB+ RAM minimum
- 64GB RAM recommended for the 32B model
- Ollama installed

### 2. Pull the Model

```powershell
ollama pull qwen2.5:32b
