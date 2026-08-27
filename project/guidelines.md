# Final Project: Build a Startup

**DATA/MSML 641: Natural Language Processing**

**Worth**: 45% of your final grade
**Team size**: 4 or 5 (your startup)
**Duration**: Session 3 (September 15) through demo day (December 1)

---

## The idea

This term your team will operate like a startup.
You will form a company, find a real problem, and ship a working NLP product that real people can use by demo day.

The company is pretend.
You will not incorporate, raise money, or own equity, and there are no real customers or revenue.
Everything else is real: the problem you pick should be real, the users you talk to should be real, and the product you ship should actually work.
You are practicing the way a small team builds and ships, applied to a real NLP system.

It is still an NLP course.
Your product must contain real NLP work that you build and evaluate: your own model, pipeline, or system, with a held-out evaluation and an honest error analysis.
A thin wrapper around someone else's API is not a project.

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

Four or five people.
The first two sessions are yours to find teammates and pick a problem.
Nothing is due before Session 3.

**By Session 3 (September 15)**: form your team, choose a company name, create one shared GitHub repository, assign roles, and submit the repository URL.

Everyone writes code. On top of that, each member owns one hat:

| Hat | Accountable for |
|---|---|
| Product | The user, the roadmap, the lean canvas, the pitch |
| Engineering | Architecture, code review, repo health, deployment |
| Data and Evaluation | Data and licensing, the evaluation harness, metrics, error analysis |
| Users and Research | Recruiting users, running sessions, capturing the raw evidence |
| Operations (teams of 5) | Planning, the board, the weekly report, keeping the repo honest |

Owning a hat means making sure that part of the company is healthy, not doing all of it alone.
A team of four covers the first four hats.

## How you work: GitHub

Your repository is the record of your work.

- One shared repo per team. Submit the URL by Session 3. It can be public or private. If private, add the instructor (`aaarrmiinnn`) as a collaborator.
- Every task is an issue with a label, assignee, and milestone. Keep a board (Todo, In Progress, In Review, Done).
- One branch per issue. A teammate reviews and approves each pull request before it merges. No direct pushes to `main`.
- **Turn on branch protection on `main`** requiring one approving review. This will be checked once, in Session 4. Self-merging without a review costs marks under "repo matches the report".
- Link commits and pull requests to the issues they close.

## The weekly rhythm

Every week: build, put it in front of a user, learn, report.

There is no weekly live standup this term.
The written report is the record, and it is what gets graded.
Some sessions will feature two or three teams demoing live. Volunteering is welcome and counts toward participation.

### The written report

Commit one report per week to your team repository.
This is the single most-weighted part of your project grade, so the mechanics are strict and worth reading twice.

**Where it goes, exactly:**

| | |
|---|---|
| Branch | `main` |
| Directory | `reports/` at the root of your repository |
| Filename | `sessionNN.md`, always two digits |
| Template | Copy [`reports/_TEMPLATE.md`](../reports/_TEMPLATE.md) from this course repo |
| Deadline | 5:00pm Tuesday, the start of the live session |

**Correct**: `reports/session04.md`

**Wrong, and will not be found**: `reports/session4.md`, `weekly_reports/session04.md`, `Weekly Reports/Session 04.md`, `reports/Session04.md`, `docs/reports/session04.md`, a report left on a feature branch and never merged to `main`.

**The number is the session number, not a count of your own project weeks.**
It always matches the session number in the syllabus, so it always matches a date.
This is the whole schedule:

| Report file | Due at Session | Date |
|---|---|---|
| `reports/session04.md` | 4 | Tuesday September 22 |
| `reports/session05.md` | 5 | Tuesday September 29 |
| `reports/session06.md` | 6 | Tuesday October 6 |
| no report | 7 | Mid-semester presentation replaces it |
| `reports/session08.md` | 8 | Tuesday October 27 |
| `reports/session09.md` | 9 | Tuesday November 3 |
| `reports/session10.md` | 10 | Tuesday November 10 |
| `reports/session11.md` | 11 | Tuesday November 17 |
| `reports/session12.md` | 12 | Tuesday November 24 |

Eight reports. There is no `session07.md`, and there are no reports for Sessions 1, 2, or 3.

**Grading is taken from the commit on `main` at 5:00pm Tuesday.**
Work pushed after that time is not counted for that week.
It will count for the following week instead, so nothing is wasted, but a late push cannot rescue a missed report.

Every claim links to the issue, pull request, or commit that backs it.
A claim with no evidence does not count.

## Key dates

| When | What |
|---|---|
| Session 3, September 15 | Form your startup: team, company name, repo URL, roles |
| Session 4, September 22 | First weekly report. Branch protection checked |
| Session 7, October 20 | Mid-semester presentation: working MVP and what users told you |
| Session 12, November 24 | Final weekly report |
| Session 13, December 1 | **Final project due, 5:00pm, for every team.** Demo day part 1 |
| Session 14, December 8 | Demo day part 2 |

Demo day is split across two sessions so each team gets a real slot rather than a rushed one.
**The deadline is December 1 for everyone**, whichever day you present.
Teams presenting on December 8 are presenting the same submission, not a further week of work.
Your presentation slot will be assigned in Session 11.

## Grading (45% of your course grade)

| Component | Share | Based on |
|---|---|---|
| Weekly reports | 30% | What you shipped, validated, and measured, with balanced contribution, all backed by evidence in your repo |
| Mid-semester presentation (Session 7) | 5% | A working MVP, real user evidence, and a clear pivot or persevere decision |
| Final product and demo day | 10% | A working product, real NLP depth, and a clear pitch |

Weekly reports are graded on the evidence in your repository (merged pull requests, issues, commits, deployed product), not on writing.
A polished report with nothing behind it scores low.

### Weekly report criteria

Each report is scored against these:

1. **Shipped something real.** Merged to `main` or deployed. Not "almost done."
2. **Validated with a user.** See the standard below. This is where most teams lose marks.
3. **Tracked your metric.** A number, compared to last week's number.
4. **Repo matches the report.** The linked issues, pull requests, and commits exist and say what the report says they say. Pull requests carry a review from a teammate.
5. **Balanced contribution.** Every member has visible work in the repo this week.
6. **Clear and honest communication.** See the honesty credit below.

### The user evidence standard

Most teams lose marks here, so read this carefully.

**Validated means a real user used your running product and you captured what happened, at the time it happened.**

What counts:
- A session recording or screen recording of someone using the product
- A timestamped usage log showing a real user's session
- A task test: you gave someone a task, and you recorded whether they completed it and how long it took
- A dated screenshot of the product in the user's hands, alongside notes taken during the session

What does not count:
- An interview about the idea
- A reaction to a mockup, a slide, or a description
- Feedback on your report rather than on your product
- Your own team using the product
- A summary written at the end of term recalling what users said earlier

**Commit the raw artifact to your repository in the week the claim is made.**
A claim made in Week 8 and evidenced in Week 12 scores as unevidenced.
Anonymize anything personal before committing it.

### Honest reporting is worth marks

A report that says "we shipped X, it lost to our own baseline, here is why we think that is, and here is what we are changing" scores **higher** than one claiming a win it cannot evidence.

Specifically credited:
- Publishing a negative result
- Reporting that your system lost to your baseline
- Identifying a flaw in your own evaluation
- Naming a week where you shipped nothing, and why

Discovering your approach does not work is a real result.
Hiding it is not, and it is usually visible in the repo anyway.

### Measure what you ship

The model or pipeline you report numbers for must be the one running in the product you demo.
If they differ, say so explicitly and explain why.
Reporting numbers for a system you did not ship, without saying so, is scored as unevidenced.

## Definitions

- **Shipped**: merged to `main` or deployed where a user can reach it. Not "almost done."
- **Validated**: a real user used the running product and you captured the raw evidence at the time. Your own confidence does not count.

## Ethics

Use only data you are licensed to use, anonymize personal information, test for bias, and document your sources.
Version-control everything so your results reproduce.

## Getting help

Scope and feasibility: instructor office hours.
Implementation: TA office hours.
Team issues: contact the instructor privately.
