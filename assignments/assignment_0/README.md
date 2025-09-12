# Assignment 0: Environment Setup & Basic NLP

**Due**: Before Week 2 synchronous session  
**Points**: 10 (completion-based)  
**Collaboration**: Individual work  

---

## 🎯 Learning Objectives

By completing this assignment, you will:
1. Set up your development environment for NLP work
2. Familiarize yourself with basic Python NLP libraries
3. Practice working with Jupyter notebooks
4. Understand the course submission process

## 📋 Prerequisites

- Python 3.8+ installed
- Basic Python programming knowledge
- Git/GitHub account (for accessing course materials)

## 🛠️ Tasks

### Task 1: Environment Setup (30 minutes)

1. **Clone the course repository**
   ```bash
   git clone [repository-url]
   cd umd-nlp-641
   ```

2. **Create Python environment** (choose one method):

   **Option A: Using Conda (Recommended)**
   ```bash
   conda env create -f environment.yml
   conda activate nlp641
   ```

   **Option B: Using pip**
   ```bash
   python -m venv nlp641
   source nlp641/bin/activate  # Windows: nlp641\\Scripts\\activate
   pip install -r requirements.txt
   ```

3. **Download language models**
   ```bash
   python -m spacy download en_core_web_sm
   python -m spacy download en_core_web_lg
   ```

4. **Test installation**
   - Open `resources/setup_test.ipynb` in Jupyter
   - Run all cells successfully
   - Take a screenshot showing successful execution

### Task 2: Basic NLP Exploration (45 minutes)

Complete the notebook `assignment_0.ipynb` (provided in this directory):

1. **Text Processing Basics**
   - Tokenization with different methods
   - Case handling and punctuation
   - Stop word filtering

2. **Language Detection**
   - Detect languages in multilingual text
   - Analyze confidence scores

3. **Simple Analytics**
   - Word frequency analysis  
   - Reading level assessment
   - Basic text statistics

4. **spaCy Pipeline**
   - Process text through spaCy pipeline
   - Extract tokens, POS tags, and named entities
   - Visualize dependency parsing

### Task 3: Reflection Questions (15 minutes)

Answer the following questions in the notebook:

1. What challenges did you encounter during setup? How did you resolve them?

2. Compare the tokenization results from different methods (split(), NLTK, spaCy). What differences do you notice?

3. Give an example of when language detection might fail and explain why.

4. What are three potential applications of the NLP techniques you explored?

5. What questions do you have about NLP after this exploration?

## 📤 Submission Instructions

### What to Submit
Upload to ELMS:
1. **assignment_0.ipynb** - Completed notebook with all outputs
2. **setup_screenshot.png** - Screenshot showing successful setup test
3. **reflection.pdf** - Your answers to reflection questions (can be exported from notebook)

### Submission Format
- Ensure all code cells have been executed and show outputs
- Include your name and date at the top of the notebook
- Use clear markdown formatting for written responses
- File size limit: 10MB total

### Grading Rubric (10 points total)

| Component | Points | Criteria |
|-----------|--------|----------|
| **Environment Setup** | 3 | All installations successful, screenshot provided |
| **Task Completion** | 5 | All notebook exercises completed with correct outputs |
| **Code Quality** | 1 | Clean, readable code with appropriate comments |
| **Reflection** | 1 | Thoughtful answers demonstrating understanding |

### Due Date
**Monday, September 8 at 11:59 PM EST** (before Week 2 class)

## 💡 Tips for Success

1. **Start Early**: Don't wait until the last minute - setup issues can take time to resolve
2. **Ask for Help**: Use Slack, office hours, or email if you get stuck
3. **Document Issues**: Keep track of any problems you encounter for the reflection
4. **Test Everything**: Make sure your notebook runs from top to bottom without errors
5. **Read Error Messages**: They often contain helpful information for debugging

## 🆘 Getting Help

- **Technical Issues**: Check `docs/troubleshooting.md` first
- **Office Hours**: See syllabus for TA availability  
- **Discussion Forum**: Post questions for peer help
- **Email**: Contact TAs for urgent issues

## 🔗 Resources

### Required Reading
- Course README.md (setup instructions)
- spaCy documentation: https://spacy.io/
- NLTK documentation: https://nltk.org/

### Optional Resources
- [Python for NLP Guide](https://realpython.com/nltk-nlp-python/)
- [Jupyter Notebook Tutorial](https://jupyter.org/try)
- [Git/GitHub Basics](https://guides.github.com/introduction/git-handbook/)

---

**Questions?** Don't hesitate to ask! This assignment is designed to ensure everyone starts on equal footing.