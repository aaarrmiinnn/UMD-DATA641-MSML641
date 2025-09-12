# UMD DATA/MSML 641: Natural Language Processing

**Fall 2025 - University of Maryland**

This repository contains course materials for DATA/MSML 641: Natural Language Processing, a graduate-level course focusing on fundamental concepts and techniques for getting computers to deal intelligently with human language.

## 📋 Course Overview

This is a **blended learning course** with both synchronous and asynchronous components:
- **Synchronous**: 90-minute live lectures via Zoom (Mondays 7-9:45pm or Tuesdays 6-8:45pm)
- **Asynchronous**: Videos, readings, and interactive exercises (~75 minutes per week)

### Course Objectives
By the end of this course, you will be able to:
- Understand fundamental linguistic concepts relevant to automated text processing
- Identify core NLP methods: lexical analysis, sequential tagging, syntactic parsing, semantic representations, text classification
- Analyze and implement state-of-the-art algorithms including deep learning for language data
- Work with modern NLP frameworks and libraries

## 🗂️ Repository Structure

```
├── README.md                 # This file
├── SYLLABUS.md              # Complete course syllabus
├── requirements.txt          # Python dependencies
├── environment.yml          # Conda environment file
├── lectures/                # Synchronous lecture notebooks
│   ├── week01_introduction.ipynb
│   ├── week02_words_multiwords.ipynb
│   └── ...
├── async/                   # Asynchronous content
│   ├── videos/              # Video companion notebooks  
│   ├── readings/            # Reading guides and exercises
│   └── knowledge_checks/    # Quiz notebooks
├── assignments/             # Homework assignments
│   ├── assignment_0/
│   ├── assignment_1/
│   └── ...
├── project/                 # Final project materials
│   ├── guidelines.md
│   └── templates/
├── resources/               # Additional resources
│   ├── datasets/
│   ├── models/
│   └── utils/
├── docs/                    # Additional documentation
└── img/                     # Images and figures
```

## 🚀 Quick Start

### 1. Clone the Repository
```bash
git clone <repository-url>
cd umd-nlp-641
```

### 2. Set Up Python Environment

**Option A: Using Conda (Recommended)**
```bash
conda env create -f environment.yml
conda activate nlp641
```

**Option B: Using pip**
```bash
python -m venv nlp641
source nlp641/bin/activate  # On Windows: nlp641\\Scripts\\activate
pip install -r requirements.txt
```

### 3. Install Additional NLP Libraries
```bash
# Download spaCy models
python -m spacy download en_core_web_sm
python -m spacy download en_core_web_lg

# NLTK data (if using NLTK)
python -c "import nltk; nltk.download('punkt'); nltk.download('stopwords')"
```

### 4. Launch Jupyter
```bash
jupyter lab
# or
jupyter notebook
```

### 5. Test Your Installation
Open and run `resources/setup_test.ipynb` to verify your environment is configured correctly.

## 📚 Main Textbook
- **Jurafsky and Martin**: [Speech and Language Processing (3rd edition)](https://web.stanford.edu/~jurafsky/slp3/)

## 📅 Weekly Schedule

| Week | Date | Topic | Synchronous Lecture | Async Content |
|------|------|-------|--------------------|--------------| 
| 1 | Sep 1-2 | Introduction & NLP Pipeline | `lectures/week01_introduction.ipynb` | `async/week01/` |
| 2 | Sep 8-9 | Words and Multi-Words | `lectures/week02_words_multiwords.ipynb` | `async/week02/` |
| 3 | Sep 15-16 | Word & Sentence Meaning | `lectures/week03_meaning.ipynb` | `async/week03/` |
| 4 | Sep 22-23 | Sequential Structure | `lectures/week04_sequential.ipynb` | `async/week04/` |
| 5 | Sep 29-30 | Syntactic Structure | `lectures/week05_syntax.ipynb` | `async/week05/` |
| 6 | Oct 6-7 | Sentence Meaning & Evaluation | `lectures/week06_semantics_eval.ipynb` | `async/week06/` |
| 8 | Oct 20-21 | Machine Learning in NLP | `lectures/week08_ml_nlp.ipynb` | `async/week08/` |
| 9 | Oct 27-28 | Vector Semantics & Embeddings | `lectures/week09_embeddings.ipynb` | `async/week09/` |
| 10 | Nov 3-4 | Deep Learning for NLP | `lectures/week10_deep_learning.ipynb` | `async/week10/` |
| 11 | Nov 10-11 | Transformers | `lectures/week11_transformers.ipynb` | `async/week11/` |
| 12 | Nov 17-18 | Language Models & Fine-tuning | `lectures/week12_language_models.ipynb` | `async/week12/` |
| 13 | Nov 24-25 | RAG & Graphs in NLP | `lectures/week13_rag_graphs.ipynb` | `async/week13/` |
| 14 | Dec 1-2 | NLP Applications | `lectures/week14_applications.ipynb` | `async/week14/` |
| 15 | Dec 8-9 | Ethical AI & NLP | `lectures/week15_ethics.ipynb` | `async/week15/` |

## 📝 Assignments

- **Assignment 0**: Environment Setup & Basic NLP (Week 1)
- **Assignment 1**: Text Processing & Analysis (Week 2)
- **Assignment 2**: Syntactic Analysis (Week 5) 
- **Assignment 3**: Semantic Analysis & Evaluation (Week 6)
- **Assignment 4**: Advanced Applications (Week 13)
- **Final Project**: Team project with real-world NLP problem (Weeks 9-16)

## 🛠️ Tools & Libraries Used

- **Core**: Python 3.8+, Jupyter, NumPy, Pandas
- **NLP**: spaCy, NLTK, Transformers (Hugging Face)
- **ML/DL**: scikit-learn, PyTorch, TensorFlow  
- **Visualization**: matplotlib, seaborn, plotly
- **Utilities**: requests, beautifulsoup4, tqdm

## 💡 Tips for Success

1. **Stay Current**: Complete async content before synchronous lectures
2. **Participate**: Engage in discussions and ask questions
3. **Practice**: Work through code examples and modify them
4. **Collaborate**: Form study groups and work together on understanding concepts
5. **Resource Management**: Use office hours and TA sessions

## 🆘 Getting Help

- **Instructor**: Armin Mehrabian
- **TAs**: 
  - PWS1: Raman Selvakumar (ramans@umd.edu) - Monday 12-1 PM ET
  - PWS2: Palak Wadhwa (pwadhwa@umd.edu) - Monday 3-4 PM ET, Thursday 11 AM-12 PM ET
- **Technical Issues**: Check `docs/troubleshooting.md`
- **Course Policies**: See `SYLLABUS.md`

## 📄 License & Usage

Course materials are for educational use by enrolled students. Please respect copyright and academic integrity policies.

---

*Last updated: Fall 2025*