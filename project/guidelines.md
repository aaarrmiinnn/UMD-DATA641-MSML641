# Final Project: Build a Startup

**DATA/MSAI/MSML 641: Natural Language Processing**

**Worth**: 45% of your final grade
**Team size**: 3 (your startup). Groups of 2 or 4 by special permission only.
**Duration**: The full 12-week summer term.

---

## The idea

This summer your team will operate like a startup. You will form a company, find a real problem, and ship a working NLP product that real people can use by demo day.

The company is pretend. You will not incorporate, raise money, or own equity, and there are no real customers or revenue. Everything else is real: the problem you pick should be real, the users you talk to should be real, and the product you ship should actually work. You are practicing the way a small team builds and ships, applied to a real NLP system.

It is still an NLP course. Your product must contain real NLP work that you build and evaluate (your own model, pipeline, or system, with a held-out evaluation and an honest error analysis). A thin wrapper around someone else's API is not a project.

## What to think about now that you are a startup

A project asks "is my method correct?" A startup also has to answer:

- **User and problem**: Who is this for? What do they do today, and why does it hurt?
- **Alternatives**: What already exists, and why is yours better for this user?
- **Value proposition**: One sentence. "We help [user] do [job] better, faster, or cheaper than [alternative]."
- **Distribution**: How will a real user find and start using this?
- **Cost**: What does one user request cost to serve (API, compute)?
- **North-star metric**: The one number that means it is working, for example task success rate.
- **Ethics and privacy**: Data licensing, personal data, bias, and what happens when the model is wrong.
- **Risk**: What is most likely to kill this, and what is the cheapest way to find out early?

Keep these on a one-page lean canvas and revisit it weekly.

## Your team

Three people. By the end of Week 1: form your team, choose a company name, create one shared GitHub repository, and assign roles.

Everyone writes code. On top of that, each member owns one hat:

| Hat | Accountable for |
|---|---|
| Product | The user, the roadmap, the lean canvas, the pitch |
| Engineering | Architecture, code review, repo health, deployment |
| Data and Evaluation | Data and licensing, the evaluation harness, metrics, error analysis |

Owning a hat means making sure that part of the company is healthy, not doing all of it alone.

## How you work: GitHub

Your repository is the record of your work.

- One shared repo per team. Submit the URL in Week 1.
- Every task is an issue with a label, assignee, and milestone. Keep a board (Todo, In Progress, In Review, Done).
- One branch per issue. A teammate reviews and approves each pull request before it merges. No direct pushes to main.
- Link commits and pull requests to the issues they close.

## The weekly rhythm

Every week: build, put it in front of a user, learn, report.

- **Standup** (last 30 to 40 minutes of lecture): 2 to 5 minutes per team. Demo over slides. Four beats: what we shipped, what we learned from users, our biggest blocker, next week's goal. Rotate the presenter.
- **Written report**: commit `reports/weekNN.md` before each session using [`reports/_TEMPLATE.md`](../reports/_TEMPLATE.md). Every claim links to the issue, pull request, or commit that backs it. A claim with no evidence does not count.

## Key dates

| When | What |
|---|---|
| Week 1 (June 3) | Form your startup: team, company name, repo, roles |
| Week 3 (June 17) | Project pitch: 5 minutes per team on what you are building and for whom |
| Week 6 (July 8) | Mid-semester presentation: working MVP and what users told you |
| Week 12 (August 19) | Demo day: live product, final pitch, technical appendix |

Every other week runs the standup and report rhythm above.

## Grading (45% of your course grade)

| Component | Share | Based on |
|---|---|---|
| Weekly reports | 30% | What you shipped, validated, and measured, with balanced contribution, all backed by evidence in your repo |
| Mid-semester presentation (Week 6) | 5% | A working MVP, real user evidence, and a clear pivot or persevere decision |
| Final product and demo day (Week 12) | 10% | A working product, real NLP depth, and a clear pitch |

Weekly reports are graded on the evidence in your repository (merged pull requests, issues, commits, deployed product), not on writing. A polished report with nothing behind it scores low.

**Weekly report criteria**: shipped something real, validated with users, tracked your metric, repo matches the report, balanced contribution, clear and honest communication.

**Final criteria**: the product works for a stranger; your own model or pipeline with a held-out evaluation and error analysis; evidence of how the product changed in response to users; a clear demo-day pitch; a short technical appendix covering architecture, data, evaluation, and ethics.

## Definitions

- **Shipped**: merged to main or deployed where a user can reach it. Not "almost done."
- **Validated**: you put it in front of a real user and measured the result. Your own confidence does not count.

## Ethics

Use only data you are licensed to use, anonymize personal information, test for bias, and document your sources. Version-control everything so your results reproduce.

## Getting help

Scope and feasibility: instructor office hours. Implementation: TA office hours. Team issues: contact the instructor privately.
