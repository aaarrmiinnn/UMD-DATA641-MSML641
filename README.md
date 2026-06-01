# UMD DATA/MSAI/MSML 641: Natural Language Processing

**Summer 2026 - University of Maryland**

This repository contains course materials for DATA/MSAI/MSML 641: Natural Language Processing (cross-listed as DATA641 / MSAI641 / MSML641), a graduate-level course focusing on fundamental concepts and techniques for getting computers to deal intelligently with human language.

## Course Overview

This course focuses on **interactive lecture-based learning**:
- **Online sessions**: Wednesdays 5:00pm - 8:30pm (Online)
- **Asynchronous content**: Video lectures, readings, and review questions
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

Online sessions each Wednesday, 5:00pm - 8:30pm. See `SYLLABUS.md` for full async content (videos, readings, supplementary materials) for each week.

| Week | Class Date | Topic | Lecture Materials |
|------|------------|-------|-------------------|
| 1 | June 3, 2026 | Word Meaning | `lectures/week01_meaning.ipynb` |
| 2 | June 10, 2026 | Sequence Models | `lectures/week02_sequence_models.ipynb` |
| 3 | June 17, 2026 | Evaluation in NLP | `lectures/week05_evaluation.ipynb` |
| 4 | June 24, 2026 | Vector Semantics and Embeddings | `lectures/week06_vector_semantics.ipynb` |
| 5 | July 1, 2026 | Neural Networks in NLP | `lectures/week07_neural_networks_in_nlp.ipynb` |
| 6 | July 8, 2026 | Mid-Semester Project Presentations | Mid-semester project presentation |
| 7 | July 15, 2026 | Transformers | `lectures/week08_transformers.ipynb` |
| 8 | July 22, 2026 | Language Models, Fine-tuning and Post-Training | `lectures/week09_mlm.ipynb` |
| 9 | July 29, 2026 | Retrieval Augmented Generation (RAG) | `lectures/week11_rag.ipynb` |
| 10 | August 5, 2026 | Graphs in NLP | `lectures/week10_graphs.ipynb` |
| 11 | August 12, 2026 | Frontier NLP: Agents, Multimodal and Beyond | _TBD (notebook in development)_ |
| 12 | August 19, 2026 | Final Project Presentations | Final project due |

## Course Components

- **Online Lectures**: Asynchronous video content with live online sessions
- **Hands-on Components**: Interactive Jupyter notebooks and coding exercises
- **Final Project**: Build a startup. Teams of 3 ship a working NLP product over the full semester with weekly progress reports. See [project/guidelines.md](project/guidelines.md)
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
- **TA**: TBD
- **Technical Issues**: Check `docs/troubleshooting.md`
- **Course Policies**: See `SYLLABUS.md`

## Acknowledgments

The asynchronous video lectures for this course were created by **Dr. Shabnam Tafreshi**, an expert in natural language processing and machine learning. Dr. Tafreshi passed away in October 2025. We honor her memory by continuing to share and learn from her work through these course videos.

## License & Usage

[![CC BY 4.0](https://img.shields.io/badge/License-CC%20BY%204.0-lightgrey.svg)](https://creativecommons.org/licenses/by/4.0/)

These course materials are released under the [Creative Commons Attribution 4.0 International (CC BY 4.0)](https://creativecommons.org/licenses/by/4.0/) license.

You are free to **use, share, and adapt** these materials for any purpose — including commercially — as long as you give appropriate credit:

> *Armin Mehrabian, DATA/MSAI/MSML 641: Natural Language Processing, University of Maryland, Summer 2026. Available at: https://github.com/aaarrmiinnn/UMD-DATA641-MSML641*

---

*Last updated: Summer 2026*
