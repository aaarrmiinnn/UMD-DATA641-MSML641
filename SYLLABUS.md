# DATA/MSAI/MSML 641 Syllabus

**Course**: DATA/MSAI/MSML 641: Natural Language Processing (cross-listed: DATA641 / MSAI641 / MSML641)
**Term**: Summer 2026
**Credits**: 3
**Instructor**: Armin Mehrabian

## Course Schedule

**Time**: Wednesdays 5:00pm - 8:30pm

**Format**: Online (asynchronous video content + live online sessions)

**Dates**: June 1, 2026 - August 21, 2026 (12 weeks)

## Contact Information

**Instructor**: Armin Mehrabian
**Email**: arminm@umd.edu
**Office Hours**: As needed

**Communication Preferences**:
- Email the instructor at arminm@umd.edu
- Important announcements sent via ELMS messaging
- Enable email and announcement notifications in ELMS

**Teaching Assistant**: TBD

## Course Description

This course introduces fundamental concepts and techniques for getting computers to deal intelligently with human language. Focused primarily on text (as opposed to speech), it offers grounding in:

- Core NLP methods for text processing (lexical analysis, sequential tagging, syntactic parsing, semantic representations, text classification, unsupervised discovery of latent structure)
- Key ideas in applying deep learning to language tasks
- Consideration of the role of language technology in modern society

## Prerequisites

- **Required**: DATA603 or MSML603 (Introduction to Machine Learning)
- **Skills Expected**:
  - Maximum likelihood estimation, Bayes' rule
  - k-nearest-neighbors, support vector machines, neural networks
  - Deep learning networks, dimensionality reduction, clustering
  - Comfortable programming in Python

## Learning Outcomes

By the end of this course, you will be able to:

1. **Understand** fundamental linguistic concepts relevant to automated processing of natural language text
2. **Identify** core NLP methods for text processing, including lexical analysis, sequential tagging, syntactic parsing, semantic representations, text classification, and unsupervised discovery of latent structure
3. **Analyze** and understand state-of-the-art algorithms and machine learning techniques, including deep learning, for reasoning about language data
4. **Implement** state-of-the-art machine learning algorithms for reasoning about language data

## Course Structure

**Online Format**:
- **Asynchronous Content** (~1.5 hours/week): Video lectures, readings, review questions, and supplementary materials — completed before the live session
- **Synchronous Live Sessions** (~2 hours/week): Wednesdays via Zoom, interactive lecture with in-class exercises, polls, demos, and Q&A
- **Hands-on Learning**: Code examples, exercises, and real-time problem solving

Each week includes:
- Asynchronous video content, readings, and review questions
- Live online session (~2 hours) with discussion, demos, exercises, and Q&A

## Course Resources

**Main Text**: Jurafsky and Martin, *Speech and Language Processing* (3rd edition)

**Recommended Background Resources**:
- Unix: Ken Church's "Unix for Poets"
- Python: NLTK Book, spaCy documentation
- Linear Algebra: 3Blue1Brown YouTube series
- Probability/Statistics: Stanford refresher materials
- Machine Learning: "A Course in Machine Learning" (Hal Daume III)

## Course Outline

Online sessions each Wednesday, 5:00pm - 8:30pm.

Each week includes **asynchronous content** (videos, readings, quizzes — complete before the live session) and a **synchronous live session** (lecture, discussion, demos).

### Week 1 - Word Meaning (June 3)
- **Asynchronous Videos**: V1 *Words, Words, Words! An Introduction*; V2 *Multi-Word Units and Collocations*; V3 *Introduction to Hypothesis Testing*; V4 *Introduction to Word Meaning and Lexicography*; V5 *Historical Approaches to Understanding Word Meaning*
- **Readings**: SLP Ch 1, 2 (through 2.4); Pinker pp. 83-89
- **Supplementary**:
  - Jay Alammar, [The Illustrated Word2Vec](https://jalammar.github.io/illustrated-word2vec/)
  - Ruder, [On Word Embeddings - Part 1](https://www.ruder.io/word-embeddings-1/)
- **Synchronous**: `lectures/week01_meaning.ipynb`

### Week 2 - Sequence Models (June 10)
- **Asynchronous Videos**: V1 *Introduction to Sequence Models*; V2 *Evaluation of Language Models*
- **Readings**: SLP Ch 3, 8 (through 8.4), 9, Appendix A, B
- **Supplementary**:
  - McCallum, [An Introduction to Conditional Random Fields](https://people.cs.umass.edu/~mccallum/papers/crf-tutorial.pdf)
  - Collins, [Tagging Problems and Hidden Markov Models](https://www.cs.columbia.edu/~mcollins/hmms-spring2013.pdf)
- **Synchronous**: `lectures/week02_sequence_models.ipynb`
- **Assignment**: Assignment_1 Posted

### Week 3 - Sequence Models (continued) (June 17)
- Continuation of Week 2 (see Week 2 async videos and readings).
- **Synchronous**: `lectures/week02_sequence_models.ipynb` (continued)

### Week 4 - Evaluation I (continued) (June 24)
- **Asynchronous Videos**: V1 *Evaluation in NLP*
- **Readings**: Resnik and Lin (2010), *Evaluation of NLP Systems*
- **Supplementary**:
  - Ruder, [Challenges and Opportunities in NLP Benchmarking](https://www.ruder.io/nlp-benchmarking/)
- **Synchronous**: `lectures/week04_evaluation.ipynb`
- **Note**: Part 1 of 2 (foundations and the benchmarking/leaderboard ecosystem). The LLM-era material continues in **Week 10 - Evaluation II**, after the Language Models lecture.
- **Assignment**: Project Proposal Due

### Week 5 - Vector Semantics and Embeddings (July 1)
- **Asynchronous Videos**: V1 *Introduction to Lexical Semantics*
- **Readings**: SLP Ch 6
- **Supplementary**:
  - Ruder, [Word Embeddings in 2017: Trends and Future Directions](https://www.ruder.io/word-embeddings-2017/)
  - Jay Alammar, [The Illustrated BERT, ELMo, and Co.](https://jalammar.github.io/illustrated-bert/)
- **Synchronous**: `lectures/week05_vector_semantics.ipynb`

### Week 6 - Vector Semantics and Embeddings (continued) (July 8)
- Continuation of Week 5 (see Week 5 async videos and readings).
- **Synchronous**: `lectures/week05_vector_semantics.ipynb` (continued)
- **Assignment**: Assignment_2 Posted, Work on project

### Week 7 - Neural Networks in NLP + Mid-Semester Presentations (July 15)
- **Asynchronous Videos**: V1 *Introduction to Neural Networks in NLP*
- **Readings**: SLP Ch 7 & 8
- **Supplementary**:
  - 3Blue1Brown, [Neural Networks](https://www.youtube.com/playlist?list=PLZHQObOWTQDNU6R1_67000Dx_ZCJB-3pi) (Ch 1-4)
  - Olah, [Understanding LSTM Networks](https://colah.github.io/posts/2015-08-Understanding-LSTMs/)
  - Stanford CS224N, [Language Models, RNNs, GRUs, and LSTMs](https://web.stanford.edu/class/cs224n/readings/cs224n-2019-notes05-LM_RNN.pdf)
- **Synchronous**: `lectures/week06_neural_networks_in_nlp.ipynb`. Mid-semester project presentations run in the first part of the session (see standup format in [project/guidelines.md](project/guidelines.md)).
- **Assignment**: Mid-semester project presentation, Work on project

### Week 8 - Transformers (July 22)
- **Asynchronous Videos**: V1 *Introduction to Transformers*
- **Readings**: SLP Ch 9
- **Supplementary**:
  - 3Blue1Brown, [Attention in Transformers, Visually Explained](https://www.youtube.com/watch?v=eMlx5fFNoYc)
  - 3Blue1Brown, [How might LLMs store facts](https://www.youtube.com/watch?v=9-Jl0dxWQs8)
  - Jay Alammar, [The Illustrated Transformer](https://jalammar.github.io/illustrated-transformer/)
  - Olah & Carter, [Attention and Augmented Recurrent Neural Networks](https://distill.pub/2016/augmented-rnns/) (interactive)
- **Synchronous**: `lectures/week07_transformers.ipynb`
- **Assignment**: Work on project

### Week 9 - Language Models, Fine-tuning and Post-Training (July 29)
- **Asynchronous Videos**: V1 *Large Language Models with Transformer Architecture*; V2 *Bidirectional Transformer Encoder and Masked Language Models*
- **Readings**: SLP Ch 10, 11, 12 ([Model Alignment, Prompting, and In-Context Learning](https://web.stanford.edu/~jurafsky/slp3/12.pdf))
- **Supplementary**:
  - Jay Alammar, [The Illustrated GPT-2](https://jalammar.github.io/illustrated-gpt2/)
  - Lilian Weng, [Prompt Engineering](https://lilianweng.github.io/posts/2023-03-15-prompt-engineering/) (covers RLHF, instruction tuning, chain-of-thought)
- **Synchronous**: `lectures/week08_mlm.ipynb`
- **Assignment**: Assignment_3 Posted, Work on project

### Week 10 - Evaluation II: LLM Benchmarks and LLM-as-a-Judge (August 5)
- **Asynchronous Videos**: Continues *Evaluation in NLP* from Week 4 (no new async video)
- **Readings**: Resnik and Lin (2010), *Evaluation of NLP Systems* (review)
- **Supplementary**:
  - Ruder, [The Evolving Landscape of LLM Evaluation](https://newsletter.ruder.io/p/the-evolving-landscape-of-llm-evaluation)
- **Synchronous**: `lectures/week08b_evaluation_llm.ipynb`
- **Note**: Part 2 of 2. Builds on the Language Models lecture (e.g., BERTScore uses BERT); covers standard LLM benchmarks, learned metrics, contamination, human evaluation, and LLM-as-a-judge.
- **Assignment**: Work on project

### Week 11 - Retrieval Augmented Generation (RAG) (August 12)
- **Asynchronous Videos**: V1 *Retrieval Augmented Generation (RAG)*
- **Readings**: SLP Ch 11
- **Supplementary**:
  - Lewis et al., [Retrieval-Augmented Generation for Knowledge-Intensive NLP Tasks](https://arxiv.org/abs/2005.11401)
  - NVIDIA, [What Is Retrieval-Augmented Generation?](https://blogs.nvidia.com/blog/what-is-retrieval-augmented-generation/)
  - Pinecone, [Retrieval-Augmented Generation Guide](https://www.pinecone.io/learn/retrieval-augmented-generation/)
- **Synchronous**: `lectures/week10_rag.ipynb`
- **Assignment**: Work on project

### Week 12 - Final Project Presentations (August 19)
- **Synchronous**: Student project presentations
- **Assignment**: Final Project Due

> **Dropped this term:** Graphs in NLP (`lectures/week09_graphs.ipynb`) is not on the live schedule due to the schedule slip, but remains available as optional material.

*Schedule subject to change - monitor ELMS for updates*

## Grading Structure

| Component | Weight | Description |
|-----------|--------|-------------|
| **Class Participation and Engagement** | 5% | Class participation, in-class exercises, contributions |
| **Homework Assignments** | 30% | Regular homework assignments throughout the semester |
| **Weekly Quizzes** | 20% | Weekly quizzes to assess understanding |
| **Final Project** | 45% | Build a startup: a team of 3 ships an NLP product (groups of 2 or 4 by special permission) |
| **Total** | 100% | |

### Grade Scale
| Grade | Threshold | Grade | Threshold |
|-------|-----------|-------|-----------|
| A+ | 97.00+ | C+ | 77.00-79.99 |
| A | 93.00-96.99 | C | 73.00-76.99 |
| A- | 90.00-92.99 | C- | 70.00-72.99 |
| B+ | 87.00-89.99 | D | 60.00-69.99 |
| B | 83.00-86.99 | F | 0.00-59.99 |
| B- | 80.00-82.99 | | |

## Course Component Details

### Class Participation and Engagement (5%)
- **Components**: In-class exercises, Zoom polls, in-class discussions, discussion board contributions
- **Expectations**: Regular questions, answers, and meaningful contributions during live sessions and on discussion boards
- **Assessment**: Based on active participation in synchronous activities (exercises, polls, discussions) and asynchronous engagement (discussion board posts)

### Homework Assignments (30%)
- **Count**: 3 assignments total
- **Schedule**: Assignment 1 (June 10), Assignment 2 (July 8), Assignment 3 (July 29)
- **Format**: Programming exercises and written responses
- **Purpose**: Reinforce lecture concepts through hands-on practice
- **Collaboration**: Individual work only, no peer collaboration (see Collaboration Policy)

### Weekly Quizzes (20%)
- **Frequency**: Weekly assessments
- **Format**: Short quizzes covering recent material
- **Purpose**: Track understanding and identify areas needing review
- **Resources**: Notes allowed; no web, no peer collaboration

### Final Project (45%)
- **Structure**: Build a startup. Teams of 3 form a named company and ship a working NLP product (groups of 2 or 4 by special permission)
- **How it works**: A weekly build, measure, learn loop with a short standup and a written report each week
- **Grading**: Weekly reports 30%, mid-semester checkpoint in Week 7 5%, final product and demo day in Week 12 10%
- **Timeline**: Full semester. Mid-semester demo in Week 7, demo day in Week 12
- **See**: [project/guidelines.md](project/guidelines.md) for the full description, timeline, and rubrics

## AI Policy

**LLM Usage Permitted** for ideation and drafting, with requirements:
- **Cite** all LLM tools used
- **Specify** which sections are AI-generated
- **Describe** how AI was used
- **Be prepared** to explain any submitted work

## Collaboration Policy

| Activity | Individual/Team | Notes Allowed | Resources Allowed |
|----------|----------------|---------------|-------------------|
| **Homework Assignments** | Individual | Yes | Web resources allowed, no peer collaboration |
| **Weekly Quizzes** | Individual | Yes | No web, no peer collaboration |
| **Final Project** | Team (3 people) | Yes | Web resources allowed |

## Success Tips

1. **Participate actively** in discussions and ask questions
2. **Manage time** effectively - block adequate study time
3. **Login regularly** to ELMS for announcements
4. **Don't fall behind** - each week builds on previous content
5. **Use notifications** - enable ELMS email alerts
6. **Ask for help** when needed

## Academic Integrity

All work must adhere to UMD's Code of Academic Integrity. Unauthorized sources (CourseHero, etc.) are prohibited. When in doubt about collaboration boundaries, ask in advance.

## Accessibility & Support

**Disability Services**: Contact ADS (301-314-7682, adsfrontdesk@umd.edu)
**Student Resources**: Writing Center, Counseling Center, Academic Support Services
**Basic Needs**: Food/housing assistance available through Student Affairs

## Communication

**Preferred Method**: Email
**Response Time**: Within 24 hours (typically M/W/F 7-9am EST)
**ELMS**: Important announcements - enable notifications

**What TO email about**: Personal, academic, intellectual concerns
**What NOT to email about**: Information easily found in syllabus/ELMS

## Acknowledgments

The asynchronous video lectures for this course were created by **Dr. Shabnam Tafreshi**, an expert in natural language processing and machine learning. Dr. Tafreshi passed away in October 2025. We honor her memory by continuing to share and learn from her work through these course videos.

---

*For complete university policies, visit: [UMD Graduate School Course Policies]()*
