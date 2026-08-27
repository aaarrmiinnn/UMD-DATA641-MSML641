# DATA/MSML 641 Syllabus

**Course**: DATA/MSML 641: Natural Language Processing (cross-listed: DATA641 / MSML641)
**Term**: Fall 2026
**Section**: PWS1
**Credits**: 3
**Instructor**: Armin Mehrabian

## Course Schedule

**Time**: Tuesdays 5:00pm - 7:00pm

**Format**: Online (asynchronous video content + live online sessions)

**Dates**: September 1, 2026 - December 8, 2026 (14 sessions)

**No class**: Tuesday October 13, 2026 (Fall Break)

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

This course introduces fundamental concepts and techniques for getting computers to deal intelligently with human language.
Focused primarily on text (as opposed to speech), it offers grounding in:

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
- **Asynchronous Content** (~1.5 hours/week): Video lectures, readings, review questions, and supplementary materials, completed before the live session
- **Synchronous Live Sessions** (2 hours/week): Tuesdays via Zoom, interactive lecture with in-class exercises, polls, demos, and Q&A
- **Hands-on Learning**: Code examples, exercises, and real-time problem solving

Each week includes:
- Asynchronous video content, readings, and review questions, all due by 4:00pm Tuesday
- Live online session, 5:00pm to 7:00pm Tuesday

## Course Resources

**Main Text**: Jurafsky and Martin, *Speech and Language Processing* (3rd edition)

**Recommended Background Resources**:
- Unix: Ken Church's "Unix for Poets"
- Python: NLTK Book, spaCy documentation
- Linear Algebra: 3Blue1Brown YouTube series
- Probability/Statistics: Stanford refresher materials
- Machine Learning: "A Course in Machine Learning" (Hal Daume III)

## Course Outline

Live sessions run Tuesdays, 5:00pm to 7:00pm, on Zoom.

Each week has **asynchronous content** (videos, readings, quizzes) due by **4:00pm on the Tuesday of that week**, before the live session.

### Session 1 - Word Meaning (September 1)
- **Asynchronous Videos**: V1 *Words, Words, Words! An Introduction*; V2 *Multi-Word Units and Collocations*; V3 *Introduction to Hypothesis Testing*; V4 *Introduction to Word Meaning and Lexicography*; V5 *Historical Approaches to Understanding Word Meaning*
- **Readings**: SLP Ch 1, 2 (through 2.4); Pinker pp. 83-89
- **Supplementary**:
  - Jay Alammar, [The Illustrated Word2Vec](https://jalammar.github.io/illustrated-word2vec/)
  - Ruder, [On Word Embeddings - Part 1](https://www.ruder.io/word-embeddings-1/)
- **Synchronous**: Course introduction and `lectures/session01_word_meaning.ipynb`

### Session 2 - Sequence Models (September 8)
- **Asynchronous Videos**: V1 *Introduction to Sequence Models*; V2 *Evaluation of Language Models*
- **Readings**: SLP Ch 3, Appendix A, Appendix B
- **Supplementary**:
  - McCallum, [An Introduction to Conditional Random Fields](https://people.cs.umass.edu/~mccallum/papers/crf-tutorial.pdf)
  - Collins, [Tagging Problems and Hidden Markov Models](https://www.cs.columbia.edu/~mcollins/hmms-spring2013.pdf)
- **Synchronous**: `lectures/session02_sequence_models.ipynb`

### Session 3 - Evaluation in NLP (September 15)
- **Asynchronous Videos**: V1 *Evaluation in NLP*
- **Readings**: Resnik and Lin (2010), *Evaluation of NLP Systems*
- **Supplementary**:
  - Ruder, [Challenges and Opportunities in NLP Benchmarking](https://www.ruder.io/nlp-benchmarking/)
- **Synchronous**: `lectures/session03_evaluation.ipynb`
- **Project**: Project kickoff. Teams, company name, and repository URL are due today. See [project/guidelines.md](project/guidelines.md)
- **Assignment**: Assignment 1 posted

### Session 4 - Vector Semantics and Embeddings (September 22)
- **Asynchronous Videos**: V1 *Introduction to Lexical Semantics*
- **Readings**: SLP Ch 6
- **Supplementary**:
  - Ruder, [Word Embeddings in 2017: Trends and Future Directions](https://www.ruder.io/word-embeddings-2017/)
  - Jay Alammar, [The Illustrated BERT, ELMo, and Co.](https://jalammar.github.io/illustrated-bert/)
- **Synchronous**: `lectures/session04_vector_semantics.ipynb`
- **Project**: `reports/session04.md` due by 5:00pm

### Session 5 - Neural Networks in NLP (September 29)
- **Asynchronous Videos**: V1 *Introduction to Neural Networks in NLP*
- **Readings**: SLP Ch 7 & 8
- **Supplementary**:
  - 3Blue1Brown, [Neural Networks](https://www.youtube.com/playlist?list=PLZHQObOWTQDNU6R1_67000Dx_ZCJB-3pi) (Ch 1-4)
  - Olah, [Understanding LSTM Networks](https://colah.github.io/posts/2015-08-Understanding-LSTMs/)
  - Stanford CS224N, [Language Models, RNNs, GRUs, and LSTMs](https://web.stanford.edu/class/cs224n/readings/cs224n-2019-notes05-LM_RNN.pdf)
- **Synchronous**: `lectures/session05_neural_networks.ipynb`
- **Project**: `reports/session05.md` due by 5:00pm
- **Assignment**: Assignment 1 due by 5:00pm

### Session 6 - Transformers (October 6)
- **Asynchronous Videos**: V1 *Introduction to Transformers*
- **Readings**: SLP Ch 9
- **Supplementary**:
  - 3Blue1Brown, [Attention in Transformers, Visually Explained](https://www.youtube.com/watch?v=eMlx5fFNoYc)
  - 3Blue1Brown, [How might LLMs store facts](https://www.youtube.com/watch?v=9-Jl0dxWQs8)
  - Jay Alammar, [The Illustrated Transformer](https://jalammar.github.io/illustrated-transformer/)
  - Olah & Carter, [Attention and Augmented Recurrent Neural Networks](https://distill.pub/2016/augmented-rnns/) (interactive)
- **Synchronous**: `lectures/session06_transformers.ipynb`
- **Project**: `reports/session06.md` due by 5:00pm

### Fall Break - No Class (October 13)

No live session and no asynchronous content this week.
Fall Break runs Monday October 12 to Tuesday October 13.

### Session 7 - Mid-Semester Project Presentations (October 20)
- **Asynchronous Content**: None
- **Synchronous**: `lectures/session07_midsemester_presentations.ipynb`. Every team presents for 5 minutes plus 2 for questions a working MVP, the user evidence behind it, and a pivot or persevere decision. See [project/guidelines.md](project/guidelines.md)
- **Project**: Mid-semester presentation. No written report is due this week, the presentation replaces it
- **Assignment**: Assignment 2 posted

### Session 8 - Language Models, Fine-tuning and Post-Training (October 27)
- **Asynchronous Videos**: V1 *Large Language Models with Transformer Architecture*; V2 *Bidirectional Transformer Encoder and Masked Language Models*
- **Readings**: SLP Ch 10, 11, 12 ([Model Alignment, Prompting, and In-Context Learning](https://web.stanford.edu/~jurafsky/slp3/12.pdf))
- **Supplementary**:
  - Jay Alammar, [The Illustrated GPT-2](https://jalammar.github.io/illustrated-gpt2/)
  - Lilian Weng, [Prompt Engineering](https://lilianweng.github.io/posts/2023-03-15-prompt-engineering/) (covers RLHF, instruction tuning, chain-of-thought)
- **Synchronous**: `lectures/session08_language_models.ipynb`
- **Project**: `reports/session08.md` due by 5:00pm

### Session 9 - Evaluation II: LLM Benchmarks and LLM-as-a-Judge (November 3)
- **Asynchronous Videos**: None. This session continues *Evaluation in NLP* from Session 3
- **Readings**: Resnik and Lin (2010), *Evaluation of NLP Systems* (review)
- **Supplementary**:
  - Ruder, [The Evolving Landscape of LLM Evaluation](https://newsletter.ruder.io/p/the-evolving-landscape-of-llm-evaluation)
- **Synchronous**: `lectures/session09_evaluation_llm.ipynb`
- **Note**: Part 2 of 2. Builds on Session 8, since learned metrics such as BERTScore depend on the models covered there. Covers standard LLM benchmarks, learned metrics, contamination, human evaluation, and LLM-as-a-judge
- **Project**: `reports/session09.md` due by 5:00pm
- **Assignment**: Assignment 2 due by 5:00pm

### Session 10 - Retrieval Augmented Generation (RAG) (November 10)
- **Asynchronous Videos**: V1 *Retrieval Augmented Generation (RAG)*
- **Readings**: SLP Ch 11
- **Supplementary**:
  - Lewis et al., [Retrieval-Augmented Generation for Knowledge-Intensive NLP Tasks](https://arxiv.org/abs/2005.11401)
  - NVIDIA, [What Is Retrieval-Augmented Generation?](https://blogs.nvidia.com/blog/what-is-retrieval-augmented-generation/)
  - Pinecone, [Retrieval-Augmented Generation Guide](https://www.pinecone.io/learn/retrieval-augmented-generation/)
- **Synchronous**: `lectures/session10_rag.ipynb`
- **Project**: `reports/session10.md` due by 5:00pm
- **Assignment**: Assignment 3 posted

### Session 11 - Graphs in NLP (November 17)
- **Asynchronous Videos**: V1 *Graphs in NLP*; V2 *NLP Applications*; V3 *NLP and the Use Case in Social Science*
- **Readings**: SLP Ch 13, 14, 15
- **Supplementary**:
  - Sanchez-Lengeling et al., [A Gentle Introduction to Graph Neural Networks](https://distill.pub/2021/gnn-intro/) (Distill.pub)
- **Synchronous**: `lectures/session11_graphs.ipynb`
- **Project**: `reports/session11.md` due by 5:00pm

### Session 12 - Frontier NLP: Agents, Multimodal and Beyond (November 24)
- **Asynchronous Videos**: V1 *Social Biases in AI*; V2 *Ethical Considerations in NLP and AI*
- **Readings**: Anthropic, [Building Effective Agents](https://www.anthropic.com/engineering/building-effective-agents); Yao et al., [ReAct](https://arxiv.org/abs/2210.03629); Wei et al., [Chain-of-Thought Prompting](https://arxiv.org/abs/2201.11903)
- **Supplementary**:
  - Lilian Weng, [LLM Powered Autonomous Agents](https://lilianweng.github.io/posts/2023-06-23-agent/)
  - HuggingFace, [Vision Language Models Explained](https://huggingface.co/blog/vlms)
  - Anthropic, [Introducing the Model Context Protocol](https://www.anthropic.com/news/model-context-protocol)
- **Synchronous**: `lectures/session12_frontier_nlp.ipynb`
- **Project**: `reports/session12.md` due by 5:00pm. This is the final weekly report
- **Assignment**: Assignment 3 due by 5:00pm
- **Note**: Thanksgiving Recess begins the following day, Wednesday November 25

### Session 13 - Demo Day, Part 1 (December 1)
- **Asynchronous Content**: None
- **Synchronous**: `lectures/session13_demo_day_part1.ipynb`. Final project presentations, first group of teams, 12 minutes each plus 3 for questions
- **Project**: Final project is due by 5:00pm today for **every** team, whether presenting today or on December 8. See [project/final-presentation.md](project/final-presentation.md)

### Session 14 - Demo Day, Part 2 (December 8)
- **Asynchronous Content**: None
- **Synchronous**: `lectures/session14_demo_day_part2.ipynb`. Final project presentations, second group of teams, 12 minutes each plus 3 for questions
- **Note**: Last session of the term. The last day of classes is Friday December 11

*Schedule subject to change. Monitor ELMS for updates.*

## Grading Structure

| Component | Weight | Description |
|-----------|--------|-------------|
| **Class Participation and Engagement** | 5% | In-class exercises, polls, discussion board contributions |
| **Homework Assignments** | 30% | 3 assignments, 10% each |
| **Weekly Quizzes** | 20% | Asynchronous video completion quizzes and weekly topic quizzes |
| **Final Project** | 45% | Build a startup: a team of 4 or 5 ships an NLP product |
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

### Homework Assignments (30%)
- **Count**: 3 assignments, 10% each
- **Schedule**: Assignment 1 posted September 15, due September 29. Assignment 2 posted October 20, due November 3. Assignment 3 posted November 10, due November 24
- **Format**: Programming exercises and written responses
- **Deadline**: 5:00pm on the due date
- **Collaboration**: Individual work only, no peer collaboration (see Collaboration Policy)

### Weekly Quizzes (20%)
- **Video completion quizzes**: One per asynchronous video, 1 point each, due 4:00pm Tuesday
- **Topic quizzes**: One per teaching session, 10 points each, due 5:00pm Tuesday
- **Purpose**: Confirm the asynchronous content was watched and read before the live session
- **Resources**: Notes allowed. No web, no peer collaboration

### Final Project (45%)
- **Structure**: Build a startup. Teams of 4 or 5 form a named company and ship a working NLP product
- **How it works**: A weekly build, measure, learn loop with a written report committed to your team repository each week
- **Grading**: Weekly reports 30%, mid-semester presentation 5%, final product and demo day 10%
- **Timeline**: Starts Session 3 (September 15). Mid-semester presentation Session 7 (October 20). Demo day Sessions 13 and 14 (December 1 and 8)
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
| **Final Project** | Team | Yes | Web resources allowed |

## Success Tips

1. **Participate actively** in discussions and ask questions
2. **Manage time** effectively, block adequate study time
3. **Login regularly** to ELMS for announcements
4. **Don't fall behind**, each week builds on previous content
5. **Use notifications**, enable ELMS email alerts
6. **Ask for help** when needed

## Academic Integrity

All work must adhere to UMD's Code of Academic Integrity.
Unauthorized sources (CourseHero and similar) are prohibited.
When in doubt about collaboration boundaries, ask in advance.

## Accessibility & Support

**Disability Services**: Contact ADS (301-314-7682, adsfrontdesk@umd.edu)
**Student Resources**: Writing Center, Counseling Center, Academic Support Services
**Basic Needs**: Food and housing assistance available through Student Affairs

## Communication

**Preferred Method**: Email
**Response Time**: Within 24 hours (typically M/W/F 7-9am EST)
**ELMS**: Important announcements, enable notifications

**What TO email about**: Personal, academic, intellectual concerns
**What NOT to email about**: Information easily found in the syllabus or ELMS

## Acknowledgments

The asynchronous video lectures for this course were created by **Dr. Shabnam Tafreshi**, an expert in natural language processing and machine learning.
Dr. Tafreshi passed away in October 2025.
We honor her memory by continuing to share and learn from her work through these course videos.

---

*For complete university policies, visit: [UMD Graduate School Course Policies]()*
