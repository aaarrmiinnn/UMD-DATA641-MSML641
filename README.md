# UMD DATA/MSML 641: Natural Language Processing

**Fall 2026 - University of Maryland**

This repository contains course materials for DATA/MSML 641: Natural Language Processing (cross-listed as DATA641 / MSML641), a graduate-level course focusing on fundamental concepts and techniques for getting computers to deal intelligently with human language.

## Course Overview

This course focuses on **interactive lecture-based learning**:
- **Live sessions**: Tuesdays 5:00pm - 7:00pm (Online, Zoom)
- **Asynchronous content**: Video lectures, readings, and review questions, due 4:00pm Tuesday
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
│   ├── session01_word_meaning.ipynb
│   ├── session02_sequence_models.ipynb
│   └── ...
├── project/                 # Final project materials
│   ├── guidelines.md
│   └── final-presentation.md
├── reports/                 # Weekly report template and instructions
├── resources/               # Additional resources
│   └── setup_test.ipynb     # Environment verification
├── docs/                    # Additional documentation
└── img/                     # Images and figures
```

## Quick Start

### 1. Clone the Repository
```bash
git clone https://github.com/aaarrmiinnn/UMD-DATA641-MSML641.git
cd UMD-DATA641-MSML641
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

Live sessions run Tuesdays, 5:00pm to 7:00pm.
See `SYLLABUS.md` for the full asynchronous content (videos, readings, supplementary materials) for each session.

| Session | Date | Topic | Lecture Materials |
|---------|------|-------|-------------------|
| 1 | Tuesday, September 1, 2026 | Word Meaning | `lectures/session01_word_meaning.ipynb` |
| 2 | Tuesday, September 8, 2026 | Sequence Models | `lectures/session02_sequence_models.ipynb` |
| 3 | Tuesday, September 15, 2026 | Evaluation in NLP | `lectures/session03_evaluation.ipynb` |
| 4 | Tuesday, September 22, 2026 | Vector Semantics and Embeddings | `lectures/session04_vector_semantics.ipynb` |
| 5 | Tuesday, September 29, 2026 | Neural Networks in NLP | `lectures/session05_neural_networks.ipynb` |
| 6 | Tuesday, October 6, 2026 | Transformers | `lectures/session06_transformers.ipynb` |
| - | Tuesday, October 13, 2026 | **Fall Break, no class** | |
| 7 | Tuesday, October 20, 2026 | Mid-Semester Project Presentations | `lectures/session07_midsemester_presentations.ipynb` |
| 8 | Tuesday, October 27, 2026 | Language Models, Fine-tuning and Post-Training | `lectures/session08_language_models.ipynb` |
| 9 | Tuesday, November 3, 2026 | Evaluation II: LLM Benchmarks and LLM-as-a-Judge | `lectures/session09_evaluation_llm.ipynb` |
| 10 | Tuesday, November 10, 2026 | Retrieval Augmented Generation (RAG) | `lectures/session10_rag.ipynb` |
| 11 | Tuesday, November 17, 2026 | Graphs in NLP | `lectures/session11_graphs.ipynb` |
| 12 | Tuesday, November 24, 2026 | Frontier NLP: Agents, Multimodal and Beyond | `lectures/session12_frontier_nlp.ipynb` |
| 13 | Tuesday, December 1, 2026 | Demo Day, Part 1 | `lectures/session13_demo_day_part1.ipynb` |
| 14 | Tuesday, December 8, 2026 | Demo Day, Part 2 | `lectures/session14_demo_day_part2.ipynb` |

> **Note:** Notebook filenames match the session number, so `session03_evaluation.ipynb` is the Session 3 lecture on September 15.
> The same number is used in the syllabus, in ELMS, and in your weekly report filenames.
> `lectures/optional_sentence_meaning.ipynb` is not on the live schedule this term but remains available as optional material.

## Course Components

- **Online Lectures**: Asynchronous video content with live online sessions
- **Hands-on Components**: Interactive Jupyter notebooks and coding exercises
- **Final Project**: Build a startup. Teams of 4 or 5 ship a working NLP product with weekly progress reports. See [project/guidelines.md](project/guidelines.md)
- **Setup Verification**: Use `resources/setup_test.ipynb` to verify your environment

## Tools & Libraries Used

- **Core**: Python 3.8+, Jupyter, NumPy, Pandas
- **NLP**: spaCy, NLTK, Transformers (Hugging Face)
- **ML/DL**: scikit-learn, PyTorch, TensorFlow
- **Visualization**: matplotlib, seaborn, plotly
- **Utilities**: requests, beautifulsoup4, tqdm

## Tips for Success

1. **Come Prepared**: Complete the asynchronous content before the live session
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

The asynchronous video lectures for this course were created by **Dr. Shabnam Tafreshi**, an expert in natural language processing and machine learning.
Dr. Tafreshi passed away in October 2025.
We honor her memory by continuing to share and learn from her work through these course videos.

## License & Usage

[![CC BY 4.0](https://img.shields.io/badge/License-CC%20BY%204.0-lightgrey.svg)](https://creativecommons.org/licenses/by/4.0/)

These course materials are released under the [Creative Commons Attribution 4.0 International (CC BY 4.0)](https://creativecommons.org/licenses/by/4.0/) license.

You are free to **use, share, and adapt** these materials for any purpose, including commercially, as long as you give appropriate credit:

> *Armin Mehrabian, DATA/MSML 641: Natural Language Processing, University of Maryland, Fall 2026. Available at: https://github.com/aaarrmiinnn/UMD-DATA641-MSML641*

---

*Last updated: Fall 2026*
