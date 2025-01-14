TRAINING For Reproducibility Verification
=========================================


![GitHub issues](https://img.shields.io/github/issues-raw/labordynamicsinstitute/replicability-training.svg?style=flat) ![GitHub last commit](https://img.shields.io/github/last-commit/labordynamicsinstitute/replicability-training.svg?style=flat)


> ❗ This page is for Cornell-based students applying to work with the AEA Data Editor.

---

> Training will occur mostly virtually, through a combination of required self-study and live Zoom meetings. 
> - The live part of the training will take place on Day 1 **in person** (no exceptions). Additional meetings will happen on the following days using Zoom.
> - If your application to the LDI Replication Lab was accepted,  you will be receiving information soon.
> - Training is **open to anybody**, for free, but employment is only based on invitation after application.
> - All the remaining information here is open to anybody. 
> - Content is [![License: CC BY-NC 4.0](https://licensebuttons.net/l/by-nc/4.0/80x15.png)](https://creativecommons.org/licenses/by-nc/4.0/).

## General Training Schedule

Training happens three times a year:

- week prior to start of Fall classes (around Aug 16)
- week prior to start of Spring classes (around Jan 17)
- sometime prior to May exams (around April 22)

Day 1 is always a full day of training, and may occur on a weekend.

> **Next training will be January 19, 2025.**

## Applying 

Applications are open  approximately 4-6 weeks prior to the training day, and close approximately 10 days prior to the training day. For more information, see [https://www.ilr.cornell.edu/labor-dynamics-institute/student-employment-opportunities](https://www.ilr.cornell.edu/labor-dynamics-institute/student-employment-opportunities).

## Prior to Training


Please have a look at the [list of tasks](https://labordynamicsinstitute.github.io/ldilab-manual/02-02-pre-training-tasks.html) that should be accomplished before the first meeting. 

## Tentative Agenda

The training will start with an intensive (**in person**) day of [lectures/discussions](https://labordynamicsinstitute.github.io/replicability-training-presentation/#1), followed by exercises that you will do on your own, with daily touch-base meetings over Zoom.



> If you have not received an invitation and you think you should have, contact LDI (ldi@cornell.edu).

| Time  |  January 19, 2025     (Location: Ives 108)                           |
|-------|-----------------------------------------------------------|
|  8:00 | Breakfast  |
|  9:00 |  **[Introduction](https://labordynamicsinstitute.github.io/replicability-training-presentation/#1)**      |
| 10:00 |  **[Reproducible Practices](https://labordynamicsinstitute.github.io/replicability-training-presentation/part1a.html#1), [Template README](https://labordynamicsinstitute.github.io/replicability-training-presentation/part1b.html#1)**                     |
| 11:00 | **Data provenance, [Data Citations](https://labordynamicsinstitute.github.io/replicability-training-presentation/part2.html#1)**  |
| 12:00 |  Lunch Break                                               |
| 13:00 |  **What will you be doing in the Lab**                    |
| 14:00 |  **[Command Line/Git](https://labordynamicsinstitute.github.io/replicability-training-presentation/part4.html)**                    |
| 15:00 |  **A prototypical replication report**                        |
| 16:00 | **A walkthrough of the [Workflow](https://labordynamicsinstitute.github.io/ldilab-manual/11-00-jira-workflow.html)**|
| 17:00 | **[How to run Stata](https://labordynamicsinstitute.github.io/replicability-training-presentation/part5.html)** |
| 18:00 | End                           |



- as needed: Email questions

## Test cases and peer mentoring


**Tentative** Scheduled days:

- Day 1: Jan 21
- Day 2: Jan 23
- Day 3: Jan 27
- Day 4: Jan 30

### Test cases

Test cases are worked through, and jointly handled, including with repeated peer mentoring by senior (experienced) RAs in the Lab. Three (non-consecutive) days are set aside for the peer-mentoring and walk-throughs, but work on these test cases can be done any time (adapted to individual class and exam schedules). We *strongly* suggest doing these immediately after the in-person training, however, as experience has shown that those who delay too long will ultimately struggle later in their work.

- each test article should take you no more than 5 hours of work (decreasing as you progress)
  - Test article 1: Data is available, Stata
  - Test article 2: No data is available, only "dry" analysis
  - Test article 3: Data is available, Matlab
 

### Live Peer group mentoring with existing replicators
  - Day 1, 17:30 (first test article) (Zoom) (Gary, Marina, Ilanith)
  - Day 2, 17:30 (second test article) (Zoom) (Gary, Marina, Ilanith)
  - Day 3, 17:30 (third test article and general Q&A) (Zoom) (Gary, Marina, Ilanith)

### Schedule

> Items that are **bolded** are live meetings. Items that are *italicized* are in informal groups with peers, but live (in person or on Zoom). Other items are on your own time, but the time slot is the suggested time you should be doing them. 

## Schedule

<table>
  <tr>
    <th>Time</th>
    <th>Day 1</th>
    <th>Day 2</th>
    <th>Day 3</th>
    <th>Day 4</th>
  </tr>
  {% for row in site.data.schedule %}
    <tr>
      <td>{{ row.Time }}</td>
      <td>
        {% if row.Day1_fmt == "B" %}
          <strong>{{ row.Day1 }}</strong>
        {% elsif row.Day1_fmt == "I" %}
          <em>{{ row.Day1 }}</em>
        {% else %}
          {{ row.Day1 }}
        {% endif %}
      </td>
      <td>
        {% if row.Day2_fmt == "B" %}
          <strong>{{ row.Day2 }}</strong>
        {% elsif row.Day2_fmt == "I" %}
          <em>{{ row.Day2 }}</em>
        {% else %}
          {{ row.Day2 }}
        {% endif %}
      </td>
      <td>
        {% if row.Day3_fmt == "B" %}
          <strong>{{ row.Day3 }}</strong>
        {% elsif row.Day3_fmt == "I" %}
          <em>{{ row.Day3 }}</em>
        {% else %}
          {{ row.Day3 }}
        {% endif %}
      </td>
      <td>
        {% if row.Day4_fmt == "B" %}
          <strong>{{ row.Day4 }}</strong>
        {% elsif row.Day4_fmt == "I" %}
          <em>{{ row.Day4 }}</em>
        {% else %}
          {{ row.Day4 }}
        {% endif %}
      </td>
    </tr>
  {% endfor %}
</table>

Full Training Materials
----------------------

Please go to [https://labordynamicsinstitute.github.io/ldilab-manual/](https://labordynamicsinstitute.github.io/ldilab-manual/) for the full training materials.



