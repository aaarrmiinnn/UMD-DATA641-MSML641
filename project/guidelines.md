# Final Project: Build a Startup

**DATA/MSAI/MSML 641: Natural Language Processing**

**Worth**: 45% of your final grade
**Team size**: 3 people (your startup). Groups of 2 or 4 only by special permission.
**Duration**: All 12 weeks of the summer term.

---

## The idea

This summer your team is a startup. Over 12 weeks you will form a company, find a real problem worth solving, and ship a working NLP product that real people can use by demo day.

You are not writing a term paper about a model. You are building and launching something. That single change reshapes how you work: you make decisions for a user instead of a grader, you ship in small weekly increments instead of one big deliverable, and you measure success by whether the product actually works for someone, not only by a benchmark number.

It is still an NLP course. Your product must contain real NLP work that you build and evaluate: your own model, pipeline, or system, with a proper held-out evaluation and an honest error analysis. A thin wrapper around someone else's API is not a project.

## How this differs from a normal course project

| A normal project | Your startup |
|---|---|
| Delivers a report and code | Ships a working product a stranger can use |
| Judged on rigor and metrics | Judged on whether it works for a real user and is technically sound |
| One big deliverable at the end | Weekly build, measure, learn loop |
| A group splitting tasks | A team with a name and clear roles |
| Asks "is my method correct?" | Also asks "does anyone want this, and how do they get it?" |

## What to think about beyond the code

Technical excellence with no answer to "who wants this and how do they reach it" is a failed startup, even when the model is good. Keep a one-page lean canvas and revisit it every week. Be ready to answer:

- **User and problem**: Who exactly is this for? What do they do today to cope, and why does that hurt? Why now?
- **Alternatives and differentiation**: What already exists (other tools, a chatbot, a spreadsheet, nothing)? Why is yours better for this user specifically?
- **Value proposition**: One sentence. "We help [user] do [job] better, faster, or cheaper than [alternative]."
- **Distribution**: How would a real user ever find and start using this? A product nobody can reach has no fit.
- **Cost and sustainability**: What does it cost to serve one user request (API calls, compute)? This shapes your architecture.
- **North-star metric**: The one number that means "it is working" (for example task success rate, or weekly returning users), not just F1.
- **Ethics, privacy, and safety**: Data licensing, personal data, bias, and what happens when the model is wrong. This is a graded NLP competency, not an afterthought.
- **Biggest risk**: What single thing is most likely to kill this project, and what is the cheapest test to find out early?

## Your team

Three people. By the end of Week 1 you must:

1. Form your team.
2. Choose a company name.
3. Create your GitHub repository and add all members.
4. Assign roles.

**Everyone is an engineer and writes code.** On top of that, each member owns one hat that they are accountable for:

| Hat | Owns | Accountable for |
|---|---|---|
| Product lead | The user and the roadmap | Customer interviews, scope, the lean canvas, the pitch |
| Engineering lead | The codebase and the repo | Architecture, code review, repo health, deployment |
| Data and Evaluation lead | Data and the truth | Datasets and licensing, the evaluation harness, metrics, error analysis |

Owning a hat does not mean doing all of that work alone. It means making sure that part of the company exists and is healthy. Groups of 2 combine Product and Data on one person; groups of 4 add a Design and UX lead.

## How you work: GitHub

Your repository is the record of your work, and your weekly assessment is based on what is actually in it.

- Every member creates a GitHub account. Your team has one shared repository. Submit the URL in Week 1.
- **Issues for everything**: every task, bug, or feature is an issue with a label, an assignee, and a milestone. No silent work.
- **Project board**: maintain a board with columns Todo, In Progress, In Review, Done. The board is your status.
- **Milestones map to course weeks** so progress is visible.
- **Branch and pull request**: one branch per issue. A teammate reviews and approves the pull request before it merges. No direct pushes to main.
- **Link your work**: reference the issue your commit or pull request closes (for example, `Closes #14`).
- **Hygiene files**: a README that says what the product is and how to run it, a LICENSE, and an issue template.

## The weekly rhythm

Every week follows the same loop: build, put it in front of a user, learn, report. There are two parts.

### 1. Standup (last 30 to 40 minutes of each lecture)

Each team gives a 2 to 5 minute update. **Demo over slides.** Four beats, in order:

1. What we shipped this week (show it live or a short screen capture).
2. What we learned from users or metrics (one number or one user quote).
3. Our biggest challenge or blocker.
4. Next week's one goal.

Rotate which member presents each week so everyone practices. "Shipped" means merged or deployed, not "almost done."

### 2. Written weekly report

Before each session, commit a report to your repository as `reports/weekNN.md`, using the template in [`reports/_TEMPLATE.md`](../reports/_TEMPLATE.md). Every claim must link to the issue, pull request, or commit that backs it. A claim with no linked evidence does not count.

## Timeline

| Week | Session | Project focus | Due that week |
|---|---|---|---|
| 1 | Jun 3 | Kickoff: form your startup | Team, company name, repo, roles |
| 2 | Jun 10 | Discovery: interview real users, run a demand test (a landing page or sign-up test) | Lean canvas v1, problem validated |
| 3 | Jun 17 | Scope the MVP, start building the core flow | MVP scope |
| 4 | Jun 24 | Build the MVP, first task-success test with users | Working core flow |
| 5 | Jul 1 | Iterate on user feedback | Weekly report |
| 6 | Jul 8 | **Mid-semester demo**: working MVP, user evidence, pivot or persevere decision | Mid-semester checkpoint |
| 7 | Jul 15 | Build, measure, learn | Weekly report |
| 8 | Jul 22 | Deepen the NLP core, evaluate it properly | Weekly report |
| 9 | Jul 29 | Iterate, improve the metric | Weekly report |
| 10 | Aug 5 | Harden the product | Weekly report |
| 11 | Aug 12 | Measure fit: run a "would you miss it" survey, check returning users; polish | PMF reading, weekly report |
| 12 | Aug 19 | **Demo day**: live product, pitch, technical appendix | Final deliverables |

Weeks 6 and 12 are presentation sessions, so they have no separate written weekly report.

## How you are graded

The final project is 45% of your course grade, split as follows.

| Component | Share of course | Based on |
|---|---|---|
| Weekly reports (10 reports, 3% each) | 30% | What you shipped, what you validated, your metrics, and balanced contribution, all backed by evidence in your repository |
| Mid-semester checkpoint (Week 6) | 5% | A working MVP, real user evidence, and a clear pivot or persevere decision |
| Final product and demo day (Week 12) | 10% | A working product, real NLP depth, and the quality of your pitch |
| **Total** | **45%** | |

Weekly reports are assessed against the rubric below, based on the evidence in your repository (merged pull requests, issues, commits, and your deployed product), not on writing quality. A polished report with nothing shipped behind it scores low; a plain report backed by real work scores high.

### Weekly report rubric

Each weekly report is scored on these criteria:

| Criterion | What earns full marks |
|---|---|
| Shipped | Something real merged or deployed this week, with linked pull requests or commits |
| Validation | Concrete evidence of learning from users (an interview, usage data, or a task-success test), not an opinion |
| Metrics | Your north-star metric tracked against last week |
| Process and repo hygiene | Issues, board, and pull requests match what the report claims |
| Contribution balance | Every member shows evidence of contribution |
| Communication | Clear and honest about blockers, with a concrete next goal |

### Mid-semester checkpoint rubric (Week 6)

- A working MVP of the core flow that someone outside the team can use.
- Evidence from real users (interviews or usage), not assumptions.
- A clear, reasoned pivot or persevere decision based on that evidence.
- A functioning team: roles active, repository healthy, contribution balanced.

### Final and demo day rubric (Week 12)

- **Product (does it work)**: a live, working product that a stranger can use for the core task.
- **NLP depth**: your own model, pipeline, or system, with a held-out evaluation and an honest error analysis. Report your metric and where the system fails.
- **Validation arc**: evidence of how the product changed in response to users across the term.
- **Pitch**: a clear demo-day presentation (problem, who it is for, live demo, what you learned, what is next).
- **Technical appendix**: a short write-up of your architecture, data, evaluation, and ethics considerations.

## What "shipped" and "validated" mean

- **Shipped**: merged to your main branch or deployed where a user can reach it. Not "written locally," not "almost done."
- **Validated**: you put the work in front of a real user and measured the result. A landing-page sign-up, an interview insight, a task-success rate, or a returning user all count. Your own confidence does not.

## Project ideas

Strong projects address a real problem with real NLP. Some directions:

- **Information extraction and analysis**: sentiment tracking, financial or legal document analysis, clinical note structuring.
- **Generation and summarization**: report generation from data, factual summarization, documentation assistance.
- **Question answering and search**: domain-specific question answering, semantic search over a specialized corpus, a support chatbot.
- **Language understanding**: intent recognition, essay scoring, text simplification for accessibility.
- **Multilingual**: cross-lingual retrieval, translation quality estimation, code-switching detection.

Pick a problem where you can reach real users this summer. A narrow problem solved well beats a broad problem solved shallowly.

## Data and resources

- **Data sources**: public datasets (Kaggle, UCI, Hugging Face), APIs (with proper permissions), academic and shared-task datasets. Use only data you are licensed to use, and anonymize personal information.
- **Computing**: personal laptops for prototyping, Google Colab for free GPU, university HPC with instructor approval.

## Ethics

- **Data privacy**: use publicly available or properly licensed data, anonymize personal information, and document your sources and licensing.
- **Fairness**: test for bias across groups, discuss societal impact, and propose mitigations.
- **Reproducibility**: version control everything, document seeds and hyperparameters, and write clear setup instructions.

## Getting help

- **Project scope and feasibility**: instructor office hours.
- **Technical implementation**: TA office hours.
- **Data access and ethics**: email the instructor.
- **Team issues**: contact the instructor privately.

---

The goal is to ship something real that you are proud of, built the way a small team actually builds: in the open, week by week, for a user who is not you.
