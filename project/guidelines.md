# Final Project: Build a Startup

**DATA/MSML 641: Natural Language Processing, Fall 2026**

**Worth**: 45% of your final grade
**Team size**: 4 or 5
**Runs**: Session 3 (September 15) through demo day (December 1)

This is the only project document. Everything you need is here.

| | |
|---|---|
| [The idea](#the-idea) | What you are building and why |
| [Your team](#your-team) | Size, hats, what is due at Session 3 |
| [How you work](#how-you-work-github) | The GitHub rules |
| [Checklist, week by week](#checklist-week-by-week) | **Start here each week** |
| [Weekly reports](#weekly-reports) | Where they go, what they say, when they are due |
| [Mid-semester presentation](#mid-semester-presentation-session-6) | October 6 |
| [Demo day](#demo-day-sessions-13-and-14) | December 1 and 8, and the final submission |
| [Grading](#grading) | Every rubric |
| [Where teams lose marks](#where-teams-lose-marks) | Read this one twice |

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

### What to think about now that you are a startup

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

---

## Your team

Four or five people.
The first two sessions are yours to find teammates and pick a problem.
Nothing is due before Session 3.

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

---

## How you work: GitHub

Your repository is the record of your work.

- One shared repo per team. Submit the URL by Session 3. It can be public or private. If private, add the instructor (`aaarrmiinnn`) as a collaborator.
- Every task is an issue with a label, assignee, and milestone. Keep a board (Todo, In Progress, In Review, Done).
- One branch per issue. A teammate reviews and approves each pull request before it merges. No direct pushes to `main`.
- **Turn on branch protection on `main`** requiring one approving review. This is checked once, in Session 4.
- Link commits and pull requests to the issues they close.

There is no weekly live standup this term.
The written report is the record, and it is what gets graded.
Some sessions will feature two or three teams demoing live. Volunteering is welcome and counts toward participation.

---

## Checklist, week by week

Every deadline is **5:00pm Eastern on a Tuesday**, the start of the live session.

### Now through Session 3 (Tuesday, September 15): form your startup

Nothing is graded yet. All of it is due at Session 3.

- [ ] Find teammates. **Four or five people**
- [ ] Agree on a company name
- [ ] Agree on a problem and who has it. One sentence: "We help [user] do [job] better, faster, or cheaper than [alternative]"
- [ ] Create **one shared GitHub repository** for the team
- [ ] If the repo is private, add `aaarrmiinnn` as a collaborator
- [ ] Assign hats, one each
- [ ] Turn on **branch protection** on `main`, requiring one approving review
- [ ] Create the `reports/` directory in your repo
- [ ] Submit the repository URL

If you do not have a team by Session 3, tell the instructor rather than going quiet.

### The weekly loop, from Session 4 onward

The same five moves every week.

- [ ] **Build.** Merge something to `main` or deploy it. Not "almost done"
- [ ] **Put it in front of a user.** A real person, using the running product
- [ ] **Capture the raw evidence at the time.** Commit it to the repo **this week**, not later
- [ ] **Measure.** One number, compared to last week's number
- [ ] **Write the report.** `reports/sessionNN.md` on `main`, before 5:00pm Tuesday

### Session by session

| Session | Date | What is due from you |
|---|---|---|
| 3 | Tue Sep 15 | **Team, company name, repo URL, roles, branch protection on** |
| 4 | Tue Sep 22 | `reports/session04.md` · branch protection is checked today |
| 5 | Tue Sep 29 | `reports/session05.md` |
| 6 | Tue Oct 6 | **Mid-semester presentation.** No written report this week |
| - | Tue Oct 13 | Fall Break, no class |
| 7 | Tue Oct 20 | `reports/session07.md` |
| 8 | Tue Oct 27 | `reports/session08.md` |
| 9 | Tue Nov 3 | `reports/session09.md` |
| 10 | Tue Nov 10 | `reports/session10.md` |
| 11 | Tue Nov 17 | `reports/session11.md` · demo day slots assigned today |
| 12 | Tue Nov 24 | `reports/session12.md`, your last weekly report |
| 13 | Tue Dec 1 | **Final project due 5:00pm, every team.** Demo day, part 1 |
| 14 | Tue Dec 8 | Demo day, part 2 |

---

## Weekly reports

Eight reports, one per week from Session 4, and they carry 30% of your project grade.
The mechanics are strict, so read this once carefully and you will not lose marks to filing errors.

### Where it goes, exactly

| | |
|---|---|
| Repository | Your team repository |
| Branch | `main` |
| Directory | `reports/` at the root |
| Filename | `sessionNN.md`, always two digits |
| Template | Copy [`../reports/_TEMPLATE.md`](../reports/_TEMPLATE.md) |
| Deadline | 5:00pm Tuesday |

**Correct**: `reports/session04.md`

**Wrong, and will not be found**: `reports/session4.md`, `weekly_reports/session04.md`, `Weekly Reports/Session 04.md`, `reports/Session04.md`, `docs/reports/session04.md`, or a report left on a feature branch and never merged to `main`.

**The number is the session number**, not a count of your own project weeks, so it always matches a date on the syllabus.

Eight reports: `session04`, `session05`, `session07`, `session08`, `session09`, `session10`, `session11`, `session12`.
There is no `session06.md`, because the mid-semester presentation replaces it.
There are no reports for Sessions 1, 2, or 3, because your team does not exist yet.

### The deadline is a commit, not a push

**Grading is taken from the commit on `main` at 5:00pm Tuesday.**
Work pushed after that is not counted for that week.
It counts for the following week instead, so nothing is wasted, but a late push cannot rescue a missed report.

### What each report is scored on

1. **Shipped something real.** Merged to `main` or deployed
2. **Validated with a user.** See [Where teams lose marks](#where-teams-lose-marks)
3. **Tracked your metric.** A number, compared to last week's
4. **Repo matches the report.** The linked issues, pull requests, and commits exist and say what the report says. Pull requests carry a teammate's review
5. **Balanced contribution.** Every member has visible work in the repo this week
6. **Clear and honest communication.** See [honest reporting](#honest-reporting-is-worth-marks)

Reports are graded on the evidence in your repository, not on the writing.
A polished report with nothing behind it scores low.
Every claim links to the issue, pull request, or commit that backs it.

---

## Mid-semester presentation (Session 6)

**Tuesday October 6.** Worth **5%** of your course grade.
Five minutes per team, plus two for questions.
No written report is due this week.

- [ ] **Demo the MVP.** Show it running. Not slides about it running
- [ ] **Show what a real user did with it**, and the evidence you captured
- [ ] **Report your metric** against your baseline
- [ ] **State a decision:** pivot or persevere, and why
- [ ] Rotate your presenter, so it is not the same person on demo day

An honest "this did not work, and here is what we learned" scores better than a claim you cannot show.

---

## Demo day (Sessions 13 and 14)

**Tuesday December 1 and Tuesday December 8, 5:00pm to 7:00pm, Zoom.**
Demo day runs across two sessions so every team gets a real slot.
Your slot is assigned in Session 11, on November 17.

**The submission deadline is 5:00pm Tuesday December 1 for every team**, whichever day you present.
Teams presenting on December 8 present the same submission.
Nothing committed after that moment is graded.

### The five areas

Cover these in your talk, and use them as the section headings of your report, in this order.

| Area | What to cover |
|---|---|
| **1. Problem and users** | The problem you addressed, who it is for, and what they did before |
| **2. Product** | What you built and how the system works end to end, with one diagram |
| **3. NLP method and evaluation** | Your model or pipeline, your data and how you split it, your metric, a baseline for comparison, results on held-out data, and where the system fails |
| **4. User evidence** | What real users did with the running product, and what you changed as a result |
| **5. Ethics and limitations** | Data rights, privacy, bias, and what happens when the model is wrong |

### Presentation

- **12 minutes**, followed by 3 minutes for questions. The 12-minute limit is firm
- **Include a demo, either live or recorded.** Show the product working rather than describing it. If you demo live, a recorded backup is a sensible precaution

### Slides

Submit as either a **PDF** or a **Markdown** file. Please do not submit a link to an online slide deck.
Open the file from your repository before the deadline and confirm the images and formatting display correctly.
If you submit Markdown, commit the image files alongside it and use relative paths.

### Report

Two to five pages, roughly 1,000 to 2,500 words, using the five areas as section headings.

### What to commit

To `main`, before 5:00pm on December 1:

```
reports/final/
├── README.md              Short summary, live URL, and setup instructions
├── slides.pdf  or  .md    Plus image files, if Markdown
├── report.md              The report described above
└── demo.mp4               Optional, if you use a recorded demo
```

### Final checklist

- [ ] The product works for a stranger, following the setup instructions in your README
- [ ] `report.md` uses the five areas as headings, in order
- [ ] Slides open from the repo and the images render
- [ ] Demo ready, with a recorded backup if demoing live
- [ ] **The model you report numbers for is the model running in the demo.** If not, you say so and explain why
- [ ] You have named something that did not work

---

## Grading

The project is 45% of your course grade, split like this:

| Component | Share | Based on |
|---|---|---|
| Weekly reports | 30% | What you shipped, validated, and measured, with balanced contribution, all backed by evidence in your repo |
| Mid-semester presentation (Session 6) | 5% | A working MVP, real user evidence, and a clear pivot or persevere decision |
| Final product and demo day | 10% | A working product, real NLP depth, and a clear pitch |

### Demo day, out of 100

| Area | Points |
|---|---|
| 1. Problem and users | 10 |
| 2. Product | 20 |
| 3. NLP method and evaluation | 25 |
| 4. User evidence | 15 |
| 5. Ethics and limitations | 10 |
| Honest reporting | 5 |
| Presentation and delivery | 15 |
| **Total** | **100** |

The first five are assessed on both your presentation and your report.
"Presentation and delivery" covers your use of the time, the demo, and your answers to questions.

---

## Where teams lose marks

Two things account for most lost marks. Neither is about the modelling.

### User evidence

**Validated means a real user used your running product and you captured what happened, at the time.**

**Counts:**
- A session recording or screen recording of someone using the product
- A timestamped usage log showing a real user's session
- A task test: you gave someone a task, and recorded whether they completed it and how long it took
- A dated screenshot of the product in the user's hands, with notes taken during the session

**Does not count:**
- An interview about the idea
- A reaction to a mockup, a slide, or a description
- Feedback on your report rather than on your product
- Your own team using the product
- A summary written at the end of term recalling what users said earlier

**Commit the raw artifact in the week the claim is made.**
A claim made in Session 8 and evidenced in Session 12 scores as unevidenced.
Anonymize anything personal before committing it.

### Pull request review

Every pull request needs a teammate's approving review before it merges.
Self-merging in eight seconds is visible in the repo and costs marks under "repo matches the report".
Turn on branch protection at Session 3 and this takes care of itself.

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

---

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
