# Demo Day: Final Project Presentations

**DATA/MSML 641: Natural Language Processing**
**Tuesday December 1 and Tuesday December 8, 5:00pm, Zoom**

Demo day runs across two sessions so every team gets a real slot.
Your slot will be assigned in Session 11 (November 17).

**The submission deadline is 5:00pm Tuesday December 1 for every team**, whichever day you present.
Teams presenting on December 8 present the same submission.
Nothing committed after December 1 at 5:00pm is graded.

There are three deliverables: a presentation, your slides, and a written report, all submitted to your team repository.

The presentation, the report, and the grading all follow the same five areas listed below.
Cover them in your talk, and use them as the sections of your report.

---

## The five areas

| Area | What to cover |
|---|---|
| **1. Problem and users** | The problem you addressed, who it is for, and what they did before |
| **2. Product** | What you built and how the system works end to end, with one diagram |
| **3. NLP method and evaluation** | Your model or pipeline, your data and how you split it, your metric, a baseline for comparison, results on held-out data, and where the system fails |
| **4. User evidence** | What real users did with the running product, and what you changed as a result |
| **5. Ethics and limitations** | Data rights, privacy, bias, and what happens when the model is wrong |

---

## Presentation

- **15 minutes**, followed by 3 minutes for questions. The 15-minute limit is firm.
- **Include a demo, either live or recorded.** Show the product working rather than describing it. If you demo live, a recorded backup is a sensible precaution.
- Cover the five areas above.

---

## Slides

Submit your slides as either a **PDF** or a **Markdown** file, whichever you prefer.
Please do not submit a link to an online slide deck.

Whichever format you choose, open the file from your repository before the deadline and confirm that the images, diagrams, and formatting all display correctly.
If you submit Markdown, commit the image files alongside it and reference them with relative paths.

---

## Report

Two to five pages, or roughly 1,000 to 2,500 words.
Use the five areas above as your section headings, in the same order.

---

## Submission

Commit everything to `main` in your team repository:

```
reports/final/
├── README.md              Short summary, live URL, and setup instructions
├── slides.pdf  or  .md    Plus any image files, if Markdown
├── report.md              The report described above
└── demo.mp4               Optional. Your demo recording, if you use one
```

**Due on `main` before 5:00pm on Tuesday December 1.**
Grading is taken from the commit on `main` at that moment.

---

## Grading

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

### Two things that are scored explicitly

**Measure what you ship.**
Under area 3, the model or pipeline you report numbers for must be the one running in the product you demo.
If they differ, say so and explain why.
Reporting numbers for a system you did not ship, without saying so, scores zero for the evaluation part of area 3.

**Honest reporting (5 points).**
Points for publishing a negative result, reporting that your system lost to your own baseline, identifying a flaw in your own evaluation, or naming something that did not work and why.
A team that reports an honest failure scores these points.
A team that claims a win it cannot evidence does not.
