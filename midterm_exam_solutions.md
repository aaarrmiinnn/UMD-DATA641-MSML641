# DATA/MSML 641: Natural Language Processing
## Take-Home Midterm Exam - SOLUTIONS

**University of Maryland, College Park**
**Fall 2025**
**Instructor**: Armin Mehrabian

---

## Question 1: Language Models and Smoothing (20 points)

**Given corpus:**
```
<s> the dog barked </s>
<s> the cat meowed </s>
<s> the dog ran </s>
```

---

### Part A (10 points): Bigram Probability Table

**Step 1: Count all bigrams**

| Bigram | Count |
|--------|-------|
| (`<s>`, the) | 3 |
| (the, dog) | 2 |
| (the, cat) | 1 |
| (dog, barked) | 1 |
| (dog, ran) | 1 |
| (cat, meowed) | 1 |
| (barked, `</s>`) | 1 |
| (meowed, `</s>`) | 1 |
| (ran, `</s>`) | 1 |

**Step 2: Count first words**

| Word | Count |
|------|-------|
| `<s>` | 3 |
| the | 3 |
| dog | 2 |
| cat | 1 |
| barked | 1 |
| meowed | 1 |
| ran | 1 |

**Step 3: Calculate P(w₂|w₁)**

| Bigram (w₁, w₂) | Count | P(w₂\|w₁) |
|-----------------|-------|-----------|
| (`<s>`, the) | 3 | 3/3 = 1.000 |
| (the, dog) | 2 | 2/3 = 0.667 |
| (the, cat) | 1 | 1/3 = 0.333 |
| (dog, barked) | 1 | 1/2 = 0.500 |
| (dog, ran) | 1 | 1/2 = 0.500 |
| (cat, meowed) | 1 | 1/1 = 1.000 |
| (barked, `</s>`) | 1 | 1/1 = 1.000 |
| (meowed, `</s>`) | 1 | 1/1 = 1.000 |
| (ran, `</s>`) | 1 | 1/1 = 1.000 |

---

### Part B (6 points): P(`<s> the cat ran </s>`)

**Bigrams needed:**
- (`<s>`, the) ✓
- (the, cat) ✓
- (cat, ran) ✗ **NOT observed**
- (ran, `</s>`) ✓

**Calculation:**
```
P(sentence) = P(the|<s>) × P(cat|the) × P(ran|cat) × P(</s>|ran)
            = 1.0 × 0.333 × 0 × 1.0
            = 0
```

**Explanation:** The bigram (cat, ran) never appeared in training, so P(ran|cat) = 0/1 = 0. When any bigram has zero probability, the entire sentence probability becomes zero. This is the "zero probability problem"—the model cannot handle any word sequence it hasn't seen before, even if it's grammatically valid.

**Answer: 0**

---

### Part C (4 points): Add-1 Smoothing

**Given:**
- Count(cat, ran) = 0
- Count(cat) = 1
- |V| = 8

**Calculation:**
```
P_smoothed("ran"|"cat") = (0 + 1) / (1 + 8)
                         = 1/9
                         = 0.111
```

**Answer: 0.111**

---

## Question 2: Hidden Markov Models (20 points)

### Part A (10 points): P([DET, NOUN, VERB], "the dog ran")

**Step-by-step:**
```
π(DET) = 0.7
P("the"|DET) = 0.9
P(NOUN|DET) = 0.8
P("dog"|NOUN) = 0.4
P(VERB|NOUN) = 0.8
P("ran"|VERB) = 0.6

P = 0.7 × 0.9 × 0.8 × 0.4 × 0.8 × 0.6
  = 0.096768
```

**Answer: 0.097**

---

### Part B (10 points): "the dog walked"

**Sequence 1: [DET, NOUN, VERB]**
```
π(DET) = 0.7
P("the"|DET) = 0.9
P(NOUN|DET) = 0.8
P("dog"|NOUN) = 0.4
P(VERB|NOUN) = 0.8
P("walked"|VERB) = 0.4

P₁ = 0.7 × 0.9 × 0.8 × 0.4 × 0.8 × 0.4 = 0.064512
```
**Answer: 0.065**

**Sequence 2: [DET, VERB, NOUN]**
```
π(DET) = 0.7
P("the"|DET) = 0.9
P(VERB|DET) = 0.2
P("dog"|VERB) = 0.0    ← Zero!
P(NOUN|VERB) = 0.5
P("walked"|NOUN) = 0.1

P₂ = 0.7 × 0.9 × 0.2 × 0.0 × 0.5 × 0.1 = 0
```
**Answer: 0.000**

**Which is more likely?**
Sequence 1 ([DET, NOUN, VERB]) with probability 0.065.

**Linguistic intuition:** Yes, this matches intuition perfectly. "The dog walked" follows standard English grammar (Determiner-Noun-Verb). The sequence [DET, VERB, NOUN] is ungrammatical—determiners don't precede verbs. Our emission probabilities correctly capture that "dog" cannot be a verb (P("dog"|VERB) = 0).

---

## Question 3: Evaluation Metrics (20 points)

**Given:**
- Reference: "the cat is on the mat"
- Candidate: "the cat sat on the mat"

### Part A (12 points): BLEU and ROUGE

**1. Unigram precision (p₁)**
```
Candidate: [the, cat, sat, on, the, mat] (6 total)
Reference: [the, cat, is, on, the, mat]

Matches: the✓, cat✓, sat✗, on✓, the✓, mat✓ = 5

p₁ = 5/6 = 0.833
```

**2. Bigram precision (p₂)**
```
Candidate bigrams: [(the,cat), (cat,sat), (sat,on), (on,the), (the,mat)] (5)
Reference bigrams: [(the,cat), (cat,is), (is,on), (on,the), (the,mat)]

Matches: (the,cat)✓, (cat,sat)✗, (sat,on)✗, (on,the)✓, (the,mat)✓ = 3

p₂ = 3/5 = 0.600
```

**3. BLEU-2**
```
c = 6, r = 6  → BP = 1

BLEU-2 = 1 × exp(0.5×log(0.833) + 0.5×log(0.600))
       = exp(0.5×(-0.1827) + 0.5×(-0.5108))
       = exp(-0.34675)
       = 0.707
```

**4. ROUGE-1 recall**
```
Reference: [the, cat, is, on, the, mat] (6)
Found in candidate: the✓, cat✓, is✗, on✓, the✓, mat✓ = 5

ROUGE-1 = 5/6 = 0.833
```

**5. ROUGE-2 recall**
```
Reference bigrams: [(the,cat), (cat,is), (is,on), (on,the), (the,mat)] (5)
Found in candidate: (the,cat)✓, (cat,is)✗, (is,on)✗, (on,the)✓, (the,mat)✓ = 3

ROUGE-2 = 3/5 = 0.600
```

---

### Part B (8 points): pass@k

**Given:** n=50, c=15

**pass@1:**
```
C(35,1) = 35
C(50,1) = 50
pass@1 = 1 - 35/50 = 0.300
```

**pass@5:**
```
C(35,5) = 324,632
C(50,5) = 2,118,760
pass@5 = 1 - 324,632/2,118,760 = 0.847
```

**pass@10:**
```
C(35,10) = 183,579,396
C(50,10) = 10,272,278,170
pass@10 = 1 - 183,579,396/10,272,278,170 = 0.982
```

**Explanation:**
pass@k increases with k because we're measuring the probability that **at least one** of k samples is correct. With more attempts, we're more likely to find a correct solution. This reveals that while the model only gets it right 30% of the time on first try (pass@1), it has the knowledge to generate correct solutions—they just aren't always ranked first. In practical IDE settings where developers review multiple suggestions, pass@k is more meaningful than simple accuracy.

---

## Question 4: TF-IDF and Cosine Similarity (20 points)

**Documents:**
```
Doc 1: "cat dog cat"
Doc 2: "dog bird dog"
Doc 3: "cat bird fish"
```

### Part A (12 points): TF-IDF for "dog"

**1. Term Frequency (TF)**
```
Doc 1: count=1 → tf = 1 + log₁₀(1) = 1.000
Doc 2: count=2 → tf = 1 + log₁₀(2) = 1.301
Doc 3: count=0 → tf = 0
```

**2. Inverse Document Frequency (IDF)**
```
Documents with "dog": Doc1✓, Doc2✓, Doc3✗
N = 3, df = 2

idf("dog") = log₁₀(3/2) = log₁₀(1.5) = 0.176
```

**3. TF-IDF**
```
Doc 1: 1.000 × 0.176 = 0.176
Doc 2: 1.301 × 0.176 = 0.229
Doc 3: 0.000 × 0.176 = 0.000
```

| Document | TF | IDF | TF-IDF |
|----------|-----|-----|--------|
| Doc 1 | 1.000 | 0.176 | 0.176 |
| Doc 2 | 1.301 | 0.176 | 0.229 |
| Doc 3 | 0.000 | 0.176 | 0.000 |

---

### Part B (8 points): Cosine Similarity

**Vectors:**
```
king  = [2, 5, 1]
lion  = [1, 8, 2]
pizza = [1, 0, 9]
```

**1. cos(king, lion)**
```
Dot product: (2×1) + (5×8) + (1×2) = 44
|king| = √(4 + 25 + 1) = √30 = 5.477
|lion| = √(1 + 64 + 4) = √69 = 8.307

cos(king, lion) = 44 / (5.477 × 8.307) = 0.967
```

**2. cos(king, pizza)**
```
Dot product: (2×1) + (5×0) + (1×9) = 11
|pizza| = √(1 + 0 + 81) = √82 = 9.055

cos(king, pizza) = 11 / (5.477 × 9.055) = 0.222
```

**Which is more similar?**
(king, lion) with 0.967 vs (king, pizza) with 0.222. This matches intuition: both "king" and "lion" have high animal dimension values (5 and 8), reflecting their association with living creatures and royalty. "Pizza" has zero in the animal dimension but high food value (9), placing it in a different semantic domain entirely.

---

## Question 5: NLP Concepts and Evaluation (20 points)

### Part A (6 points): Zero Probability Problem

**Explanation:**
The zero probability problem occurs when an n-gram language model encounters a word sequence it has never seen during training. Because the model assigns zero probability to unseen n-grams, the entire sentence probability becomes zero even if the sentence is perfectly valid.

**Why it's serious:**
In real-world applications, it's impossible to observe all possible word combinations in training data. This means the model will frequently assign zero probability to novel but grammatically correct sentences, making it unusable for generation tasks and causing severe underestimation in evaluation.

**Two smoothing techniques:**
1. **Add-1 (Laplace) smoothing**
2. **Add-k smoothing**
3. **Interpolation smoothing**
4. **Kneser-Ney smoothing**

(Any two are acceptable)

**How Add-1 smoothing works:**
Add-1 smoothing adds 1 to all n-gram counts (both observed and unobserved) before calculating probabilities. For a bigram: P(w₂|w₁) = (Count(w₁,w₂) + 1) / (Count(w₁) + |V|), where |V| is vocabulary size. This reserves a small amount of probability mass for unseen bigrams, ensuring no sequence gets exactly zero probability. The denominator increases by |V| to maintain a valid probability distribution.

---

### Part B (7 points): Precision vs Recall in NER

**Given:**
- Gold: {Barack Obama, Angela Merkel}
- System: {Barack Obama, Berlin}

**1. Calculate metrics:**

True Positives (TP): Barack Obama (correctly identified)
False Positives (FP): Berlin (incorrectly identified as person)
False Negatives (FN): Angela Merkel (missed)

```
Precision = TP / (TP + FP) = 1 / (1 + 1) = 1/2 = 0.500
Recall = TP / (TP + FN) = 1 / (1 + 1) = 1/2 = 0.500
```

**Answer: Precision = 0.500, Recall = 0.500**

**2. Which to optimize for legal documents?**

**Choose: Precision**

In legal document processing, false positives are extremely costly—incorrectly identifying a location or organization as a person could lead to serious legal errors, privacy violations, or contractual mistakes. It's better to miss some person names (lower recall) than to incorrectly tag non-persons as people (lower precision). Legal applications prioritize accuracy of what is extracted over completeness, since humans can review and catch omissions more easily than they can detect false inclusions in large document sets.

(Alternatively, a well-argued case for **Recall** could be accepted if the student argues that missing key parties in a contract is more serious than false identifications, which can be filtered manually.)

---

### Part C (7 points): Metric Selection

**System 1: Machine Translation (English → French)**

**Recommended: BLEU**

BLEU is specifically designed for machine translation evaluation. It measures n-gram precision between candidate and reference translations, rewarding translations that use similar words and phrases as human references. The brevity penalty prevents systems from gaming the metric with short outputs. BLEU correlates well with human judgments of translation quality and is the standard metric in MT research.

---

**System 2: Abstractive Summarization**

**Recommended: ROUGE**

ROUGE is ideal for summarization because it measures **recall**—how much of the reference content appears in the system summary. Unlike BLEU (precision-focused), ROUGE ensures the summary captures the key information from the original. For abstractive summarization that condenses articles into single sentences, we want to verify that important content isn't lost, making recall-based metrics more appropriate than precision-based ones.

---

**System 3: Code Generation for IDE**

**Recommended: pass@k**

pass@k is the standard metric for code generation because it measures **functional correctness** (does the code pass tests?) rather than surface similarity. In an IDE, developers typically review multiple suggestions (top-k), so pass@10 better reflects real usage than pass@1. Unlike BLEU or ROUGE, which would only measure lexical overlap, pass@k tests whether generated code actually works, which is what matters for programming tasks.

---

## Grading Rubric Summary

**Question 1 (20 pts):** Language Models
- Part A: Bigram table (10)
- Part B: Sentence probability (6)
- Part C: Smoothing (4)

**Question 2 (20 pts):** HMMs
- Part A: Joint probability (10)
- Part B: Compare sequences (10)

**Question 3 (20 pts):** Evaluation Metrics
- Part A: BLEU/ROUGE (12)
- Part B: pass@k (8)

**Question 4 (20 pts):** Vector Semantics
- Part A: TF-IDF (12)
- Part B: Cosine similarity (8)

**Question 5 (20 pts):** Concepts
- Part A: Zero probability (6)
- Part B: Precision/Recall (7)
- Part C: Metric selection (7)

---

## Common Mistakes

1. **Q1:** Not recognizing zero probability; incorrect vocabulary count
2. **Q2:** Confusing emission/transition; missing zero probabilities
3. **Q3:** Confusing precision/recall; BLEU brevity penalty errors
4. **Q4:** Using ln instead of log₁₀; forgetting square roots
5. **Q5:** Vague explanations; not justifying metric choices

---

**End of Solutions**
