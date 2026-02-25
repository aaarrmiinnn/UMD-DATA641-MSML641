# UMD DATA/MSML 641: Natural Language Processing

**Spring 2026 - University of Maryland**

This repository contains course materials for DATA/MSML 641: Natural Language Processing, a graduate-level course focusing on fundamental concepts and techniques for getting computers to deal intelligently with human language.

## Course Overview

This course focuses on **interactive lecture-based learning**:
- **Live lectures**: Wednesdays 6:00pm - 8:45pm at Edward St. John Learning and Teaching Center (ESJ 226), Room 1215
- **Hands-on components**: Interactive Jupyter notebooks and coding exercises

### Course Objectives
By the end of this course, you will be able to:
- Understand fundamental linguistic concepts relevant to automated text processing
- Identify core NLP methods: lexical analysis, sequential tagging, syntactic parsing, semantic representations, text classification
- Analyze and implement state-of-the-art algorithms including deep learning for language data
- Work with modern NLP frameworks and libraries

## Repository Structure

```
├── README.md                 # This file
├── SYLLABUS.md              # Complete course syllabus
├── requirements.txt          # Python dependencies
├── environment.yml          # Conda environment file
├── lectures/                # Interactive lecture notebooks
│   ├── week01_meaning.ipynb
│   ├── week02_sequence_models.ipynb
│   ├── week03_syntactic_structure.ipynb
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

## Quick Start

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

## Main Textbook
- **Jurafsky and Martin**: [Speech and Language Processing (3rd edition)](https://web.stanford.edu/~jurafsky/slp3/)

## Course Outline

We will plan to meet in person each week, but I will indicate in advance of any class periods that need to move online.

| Week | Class Date | Topic | Lecture Materials |
|------|------------|-------|-------------------|
| 1 | January 28, 2026 | Class cancelled due to inclement weather | |
| 2 | February 4, 2026 | Word Meaning | `lectures/week01_meaning.ipynb` |
| 3 | February 11, 2026 | Sequence Models | `lectures/week02_sequence_models.ipynb` |
| 4 | February 18, 2026 | Syntactic Structure *(Optional)* | `lectures/week03_syntactic_structure.ipynb` |
| 5 | February 25, 2026 | Sentence Meaning | `lectures/week04_sentence_meaning.ipynb` |
| 6 | March 4, 2026 | Evaluation in NLP | `lectures/week05_evaluation.ipynb` |
| 7 | March 11, 2026 | Midterm | |
| 8 | March 18, 2026 | Spring Break | No Classes |
| 9 | March 25, 2026 | Mid-Semester Project Presentations | |
| 10 | April 1, 2026 | Vector Semantics and Embeddings | `lectures/week06_vector_semantics.ipynb` |
| 11 | April 8, 2026 | Neural Networks in NLP | `lectures/week07_neural_networks_in_nlp.ipynb` |
| 12 | April 15, 2026 | Transformers | `lectures/week08_transformers.ipynb` |
| 13 | April 22, 2026 | Language Models, Fine-tuning and Post-Training | `lectures/week09_mlm.ipynb` |
| 14 | April 29, 2026 | Retrieval Augmented Generation (RAG) | `lectures/week10_rag.ipynb` |
| 15 | May 6, 2026 | Graphs in NLP | `lectures/week11_graphs.ipynb` |
| 16 | May 13, 2026 | Final Exam + Final Project Presentations | |

## Course Components

- **Interactive Lectures**: Hands-on Jupyter notebooks with live coding and exercises
- **Final Project**: Team project with real-world NLP problem (Weeks 9-16)
- **Setup Verification**: Use `resources/setup_test.ipynb` to verify your environment

## Tools & Libraries Used

- **Core**: Python 3.8+, Jupyter, NumPy, Pandas
- **NLP**: spaCy, NLTK, Transformers (Hugging Face)
- **ML/DL**: scikit-learn, PyTorch, TensorFlow
- **Visualization**: matplotlib, seaborn, plotly
- **Utilities**: requests, beautifulsoup4, tqdm

## Tips for Success

1. **Come Prepared**: Review readings before lectures for better engagement
2. **Participate**: Engage in discussions and ask questions during interactive sessions
3. **Practice**: Work through code examples and modify them to deepen understanding
4. **Collaborate**: Form study groups and work together on understanding concepts
5. **Resource Management**: Use office hours and TA sessions for additional support

## Getting Help

- **Instructor**: Armin Mehrabian (arminm@umd.edu)
- **TA**: Palak Wadhwa (pwadhwa@umd.edu) - Monday 3-4 PM ET, Thursday 11 AM-12 PM ET
- **Technical Issues**: Check `docs/troubleshooting.md`
- **Course Policies**: See `SYLLABUS.md`

## License & Usage

Course materials are for educational use by enrolled students. Please respect copyright and academic integrity policies.

---

*Last updated: Spring 2026*
