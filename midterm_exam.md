# DATA/MSML 641: Natural Language Processing
## Take-Home Midterm Exam

**University of Maryland, College Park**
**Fall 2025**
**Instructor**: Armin Mehrabian

---

## Instructions

- **Total Points**: 100 points (5 questions, 20 points each)
- **Time Limit**: You have 48 hours from receipt to submit your solutions
- **Format**: Submit your answers as a single PDF file via ELMS Canvas
- **Collaboration Policy**: This is an individual exam. You may consult course materials (lectures, textbooks, notes) but you **may not** discuss problems with other students or use AI assistants
- **Show Your Work**: For all mathematical problems, show each step of your calculation. Partial credit will be awarded for correct methodology even if the final answer is incorrect
- **Rounding**: Unless otherwise specified, round final answers to 3 decimal places

---

## Question 1: Language Models and Smoothing (20 points)

You are building a bigram language model. You have the following training corpus:

```
<s> the dog barked </s>
<s> the cat meowed </s>
<s> the dog ran </s>
```

Where `<s>` and `</s>` are start and end tokens respectively.

### Part A (10 points)
Construct the complete bigram probability table showing P(w₂|w₁) for all observed bigrams in the corpus. Present your answer as a table with columns: Bigram, Count, and Probability.

### Part B (6 points)
Calculate the probability of the sentence `<s> the cat ran </s>` under your bigram model. If any bigram has zero probability, state this explicitly and explain what it means for the sentence probability.

### Part C (4 points)
Using Add-1 (Laplace) smoothing, calculate the smoothed probability P("ran"|"cat").

Given: Vocabulary V = {`<s>`, the, dog, cat, barked, meowed, ran, `</s>`}, so |V| = 8.

---

## Question 2: Hidden Markov Models (20 points)

You are building a POS tagger using an HMM with:
- **States**: {DET, NOUN, VERB}
- **Observations**: {the, dog, ran, walked}

**Initial Probabilities π:**
```
π(DET) = 0.7,  π(NOUN) = 0.2,  π(VERB) = 0.1
```

**Transition Probabilities A:**
```
         DET    NOUN   VERB
DET      0.0    0.8    0.2
NOUN     0.0    0.2    0.8
VERB     0.3    0.5    0.2
```

**Emission Probabilities B:**
```
         the    dog    ran    walked
DET      0.9    0.05   0.01   0.01
NOUN     0.1    0.4    0.1    0.1
VERB     0.0    0.0    0.6    0.4
```

### Part A (10 points)
Calculate the joint probability P(tags=[DET, NOUN, VERB], words="the dog ran"). Show all steps.

### Part B (10 points)
For the sentence "the dog walked", calculate the probability of these two tag sequences:
1. [DET, NOUN, VERB]
2. [DET, VERB, NOUN]

Which sequence is more likely? Does this match your linguistic intuition? Explain briefly (2-3 sentences).

---

## Question 3: Evaluation Metrics (20 points)

### Part A: BLEU and ROUGE (12 points)

You are evaluating a machine translation system with:
- **Reference**: "the cat is on the mat"
- **Candidate**: "the cat sat on the mat"

Calculate:
1. Unigram precision (p₁)
2. Bigram precision (p₂)
3. BLEU-2 score using:

$$
\text{BLEU-2} = BP \times \exp\left(\frac{1}{2} \log p_1 + \frac{1}{2} \log p_2\right)
$$

where:
$$
BP = \begin{cases}
1 & \text{if } c > r \\
e^{(1-r/c)} & \text{if } c \leq r
\end{cases}
$$

4. ROUGE-1 recall
5. ROUGE-2 recall

### Part B: pass@k Metric (8 points)

A code generation model generates n=50 solutions to a problem. When tested, c=15 solutions pass all test cases.

Calculate **pass@1**, **pass@5**, and **pass@10** using:

$$
\text{pass@k} = 1 - \frac{\binom{n-c}{k}}{\binom{n}{k}}
$$

Explain why pass@k increases as k increases and what this tells us about model performance (3-4 sentences).

---

## Question 4: TF-IDF and Cosine Similarity (20 points)

### Part A: TF-IDF (12 points)

You have three documents:
```
Doc 1: "cat dog cat"
Doc 2: "dog bird dog"
Doc 3: "cat bird fish"
```

For the word **"dog"**:

1. Calculate the **term frequency (TF)** in each document using log normalization.
2. Calculate the **inverse document frequency (IDF)**.
3. Calculate the **TF-IDF weight** for "dog" in each document.

### Part B: Cosine Similarity (8 points)

Three words are represented as vectors in a 3-dimensional space [computer, animal, food]:

```
king  = [2, 5, 1]
lion  = [1, 8, 2]
pizza = [1, 0, 9]
```

Calculate:
1. Cosine similarity between "king" and "lion"
2. Cosine similarity between "king" and "pizza"

Which pair is more semantically similar? Does this match your intuition based on the dimensions? Explain briefly (2-3 sentences).

---

## Question 5: NLP Concepts and Evaluation (20 points)

### Part A: Zero Probability Problem (6 points)
Explain the "zero probability problem" in n-gram language models. Why is this a serious issue for real-world applications? Name two smoothing techniques that address this problem and briefly describe how ONE of them works.

### Part B: Precision vs Recall in NLP (7 points)
Consider a named entity recognition (NER) system that identifies person names in text.

**Test sentence**: "Barack Obama met with Angela Merkel in Berlin."
**Gold standard**: {Barack Obama, Angela Merkel} (2 person names)
**System output**: {Barack Obama, Berlin} (identified as person names)

1. Calculate precision and recall for this system.
2. If you had to optimize for only one metric (precision OR recall) in a sensitive application like extracting names from legal documents, which would you choose and why? (3-4 sentences)

### Part C: Evaluation Metrics Selection (7 points)
You are building three different NLP systems. For each system below, recommend the most appropriate evaluation metric from the options provided and justify your choice in 2-3 sentences:

**System 1**: Machine translation from English to French
- Options: BLEU, ROUGE, F1-score, pass@k

**System 2**: Abstractive summarization that condenses news articles into single sentences
- Options: BLEU, ROUGE, Accuracy, Perplexity

**System 3**: A code generation model for a developer IDE
- Options: BLEU, pass@k, ROUGE, Accuracy

---

## Submission Checklist

Before submitting, ensure your PDF includes:
- ✓ Your name and student ID on the first page
- ✓ Clear labels for each question and part
- ✓ All mathematical work shown step-by-step
- ✓ Final answers clearly marked or boxed
- ✓ Written explanations are clear and concise

**Good luck!**
