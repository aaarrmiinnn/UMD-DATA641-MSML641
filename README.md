# UMD DATA/MSML 641: Natural Language Processing

**Fall 2025 - University of Maryland**

This repository contains course materials for DATA/MSML 641: Natural Language Processing, a graduate-level course focusing on fundamental concepts and techniques for getting computers to deal intelligently with human language.

## 📋 Course Overview

This course focuses on **interactive lecture-based learning**:
- **Live lectures**: 90-minute sessions via Zoom (Mondays 7-9:45pm or Tuesdays 6-8:45pm)
- **Hands-on components**: Interactive Jupyter notebooks and coding exercises

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
├── lectures/                # Interactive lecture notebooks
│   ├── week01_introduction.ipynb
│   ├── week02_words_multiwords.ipynb
│   ├── week03_meaning.ipynb
│   ├── week03_hands_on_examples.ipynb
│   └── ...
├── project/                 # Final project materials
│   ├── guidelines.md
│   └── templates/
├── resources/               # Additional resources
│   ├── datasets/
│   ├── models/
│   ├── setup_test.ipynb     # Environment verification
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

| Week | Date | Topic | Lecture Materials |
|------|------|-------|------------------| 
| 1 | Sep 1-2 | Introduction & NLP Pipeline | `lectures/week01_introduction.ipynb` |
| 2 | Sep 8-9 | Words and Multi-Words | `lectures/week02_words_multiwords.ipynb` |
| 3 | Sep 15-16 | Word & Sentence Meaning | `lectures/week03_meaning.ipynb`, `lectures/week03_hands_on_examples.ipynb` |
| 4 | Sep 22-23 | Sequential Structure | `lectures/week04_sequential.ipynb` |
| 5 | Sep 29-30 | Syntactic Structure | `lectures/week05_syntax.ipynb` |
| 6 | Oct 6-7 | Sentence Meaning & Evaluation | `lectures/week06_semantics_eval.ipynb` |
| 8 | Oct 20-21 | Machine Learning in NLP | `lectures/week08_ml_nlp.ipynb` |
| 9 | Oct 27-28 | Vector Semantics & Embeddings | `lectures/week09_embeddings.ipynb` |
| 10 | Nov 3-4 | Deep Learning for NLP | `lectures/week10_deep_learning.ipynb` |
| 11 | Nov 10-11 | Transformers | `lectures/week11_transformers.ipynb` |
| 12 | Nov 17-18 | Language Models & Fine-tuning | `lectures/week12_language_models.ipynb` |
| 13 | Nov 24-25 | RAG & Graphs in NLP | `lectures/week13_rag_graphs.ipynb` |
| 14 | Dec 1-2 | NLP Applications | `lectures/week14_applications.ipynb` |
| 15 | Dec 8-9 | Ethical AI & NLP | `lectures/week15_ethics.ipynb` |

## 🎯 Course Components

- **Interactive Lectures**: Hands-on Jupyter notebooks with live coding and exercises
- **Final Project**: Team project with real-world NLP problem (Weeks 9-16)
- **Setup Verification**: Use `resources/setup_test.ipynb` to verify your environment

## 🛠️ Tools & Libraries Used

- **Core**: Python 3.8+, Jupyter, NumPy, Pandas
- **NLP**: spaCy, NLTK, Transformers (Hugging Face)
- **ML/DL**: scikit-learn, PyTorch, TensorFlow  
- **Visualization**: matplotlib, seaborn, plotly
- **Utilities**: requests, beautifulsoup4, tqdm

## 💡 Tips for Success

1. **Come Prepared**: Review readings before lectures for better engagement
2. **Participate**: Engage in discussions and ask questions during interactive sessions
3. **Practice**: Work through code examples and modify them to deepen understanding
4. **Collaborate**: Form study groups and work together on understanding concepts
5. **Resource Management**: Use office hours and TA sessions for additional support

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