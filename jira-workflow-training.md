# Training for Jira-based workflow

For pre-publication verification, we use a Jira-based workflow similar to the post-publication processes described in the [Wiki](https://github.com/labordynamicsinstitute/replicability-training/wiki).

**Pre-publication verification is a priority and should be completed within a week of being assigned.**
- Typically these replications involve interacting with [openICPSR repositories](openICPSR_training.md) where code and data are stored.
- In addition to the information you will fill out in Jira, there is also a separate Data Citation Report (more on that below)

## Scope
Your supervisor will assign you to this workflow. This workflow covers code and data, even when data may not be accessible. Supervisor, see [other document](jira-supervisor-notes.md) for details.

This workflow **DOES NOT** cover assessment of data citations. This is covered by a different training.

## Overview

![workflow image](images/AEADataEditorWorkflow-20191028.png)

The following table illustrates the flow and transitions. The `transition` field identifies the button that will appear in the interface
that needs to be clicked in order to progress an issue from the `From` state to the `To` state. The `Condition` field identifies
which form field needs to be filled out in order to be able to make the transition. `Blocked` is always an option, and leads to a "waiting state"
until a resolution can be found.

| From         | Transition           | → To           | Condition |
|:-------------|:---------------------|:---------------|:----------|
| Open         | Start task           | → In Progress  |           |
| In Progress  | Download code        | → Code         | `Code provenance` have been filled out, `Journal` has been identified. |
| Code         | Access data          | →	Data          | `Git working location` has been filled out. |
| Data         | Prepare preliminary report | → Write Preliminary Report | |
| Write Preliminary Report | Data is accessible   | →	Verification  | `Location of data` has been filled out.|
| .            | Data not available   | →	Code review   | `Reason for non-accessibility of data` has been filled out.|
| Verification, Code review  | Prepare report       | →	Report        | |
| Report       | Submit for review    | →	Under Review  | `Report URL` has been filled out.|
| Under Review | Approve              | →  Approved    |Can only be done by **approvers**.|
| .            | Incomplete           | →  Incomplete  | n.a.      |
| Approved     | Done                 | → 	Done       | n.a.      |
| Multiple     | Need information     | → Incomplete   |  when information is missing |
| Incomplete   | Restart              | →  Code review |           |
| .            | Restart verification | → Verification |           |
| .            | Restart task         | → In Progress  |           |
| Blocked      | Reopen               | →  Open        | n.a.      |

### Notes
- In the **Issue form**, please also fill out other fields, as noted.
- If code and/or data are provided by email, `Code provenance` should be filled out with  "email", otherwise with a URL.
- There are no drop-down menus for `Software`, but once a value has been entered, it becomes available for future use. E.g., once `Stata` has been entered in software, it becomes a choice for future entries, and should be re-used.
- All code should be stored on Bitbucket Git repositories. 
  - The root repository should contain only our files (i.e., REPLICATION.md, etc.)
  - The paper's files should be in a subdirectory (e.g, `paper_archive`). Often this is created by the author-provided ZIP file - re-use it.
- When committing, **always** use [Smart Commits](https://confluence.atlassian.com/bitbucket/use-smart-commits-298979931.html), e.g.
> JRA-34 #comment corrected indent issue
- Data should be stored locally (currently) / in [Git LFS](https://confluence.atlassian.com/bitbucket/git-large-file-storage-in-bitbucket-829078514.html) (soon)
  - This is why it is important to identify the **exact URL** to download the data from (in Jira) - if somebody else needs to check what you are doing, they need to re-download the data
  - When data directories contain ONLY data (no README, no code), then you MUST create a "README.md" indicating where the data is stored - otherwise, git will not preserve the directory structure.
- Use JIRA to communicate with your supervisor as issues arise, including code that takes a long time to run. 

## Details
Additional details for each of the key stages are provided here. Below is a screenshot of a Jira ticket. Some things to note:
  - The blue `In Progress` box in the upper right is how you "advance" the Jira ticket. When you are first assigned a replication, this box will say `Open`.
  - The tall grey bar on the left side contains several handy links that you will use throughout the process.
    - Sometimes this box is not visible. To make it visible, edit the URL for the Jira ticket so that there are no characters after the ticket number (e.g. AEAREP-123). You may have to refresh the page after doing so.

![jira image](images/jira-snapshot.png)

### In Progress
The first thing you must do is advance the ticket from `Open` to `In Progress`. At this stage, you are collecting information. 
- start by [creating a repository](https://github.com/labordynamicsinstitute/replicability-training/wiki/Setting-up-a-repository-on-Bitbucket) 
  - the repository name should be the name of the JIRA issue (e.g., `aearep-123`)
  - populate the repository with the latest version of the [template](https://github.com/AEADataEditor/replication-template) 
  - delete unused files from the template! Then `git add` those that you keep around
- In the template, you will find code-check-TEMPLATE.xlsx. Use this to create a list of all Tables and Figures in the paper, and use this to guide you in [REPLICATION.md](https://github.com/AEADataEditor/replication-template/blob/master/REPLICATION.md).
- Then fill out the following fields in the Jira ticket (some may be pre-populated):
  - `Code provenance` In almost all cases, this is the openICPSR repo for which you will have received a notification email.
  - `Journal`
  - `Manuscript Central identifier`
- The following fields, located in the REPL. INFO tab on the bottom right of your Jira ticket, must also be filled out:
  - `TYPEOFARTICLE` "Does the article contain empirical work, simulations, or experimental work?" - typically the answer should be "Yes". You should answer "No" only if you read the article and find that it is entirely theoretical, no simulations or empirical work at all.
  - `RCT` Is the paper about a randomized control trial? This should be immediately obvious from the abstract.
  - `RCT NUMBER` If it is an RCT, fill in the associated RCT registration number (typically in the title page footnote)
  
You can now proceed to change the status to `Code`   

### Code
In this stage, download the code or the entire replication package, and populate the Bitbucket repository.
- Download the code from openICPSR (typicaly for most cases). See [openICPSR repositories](openICPSR_training.md) for instructions on downloading these materials.
- Populate the Bitbucket repository:
  - Use `git clone` to clone the Bitbucket repository onto your local computer. It should be named something like aearep-123.
  - Copy/paste the downloaded openICPSR folder into the local copy of the aearep-123 repository. The local repository should now have the relevant LDI replication template materials and the openICPSR folder containing the replication materials provided by the authors.
  - Perform a `git add`, `git commit`, `git push` sequence to populate the Bitbucket repo with the authors' replication materials (see above how to handle data).

Now you will establish a **list of Datasets used** and fill out the **Data Citation and Information** report.
- From the README provided by the authors, or the article itself, establish a list of datasets used in the article.
- Now you will fill out the **Data Citation and Information** report:
  - A link to the report can be found in the tall grey bar on the left side of the ticket. If this tall grey bar is not visible, then edit the url according to the directions above.
  - Fill out the `DATA CITATION REPORT` field on Jira with the date on which you complete this report.
  - Use the list of datasets to guide you when filling this out.
  - **AT THE SAME TIME:** write the corresponding `Data description` section of REPLICATION.md.
Add the list of datasets to the repository (`git add`, `git commit`)

Next fill out the following fields in the Jira ticket:
  - `Software Used` Start typing the name of the software program you will use for the replication. Softwares that have been used in the past will show up as options (e.g. start typing "Stata" and you will see it pop up).
  - `BITBUCKET SHORT NAME` Write the issue number (e.g. aearep-123). This should populate the `GIT WORKING LOCATION` field, which is the URL for the Bitbucket repo you created earlier.
  - `PROGRAMSEQUENCE` Does the README tell you the correct sequence for running the code?
  - `PROGRAMSDOCUMENTATION` Are the provided programs well commented? Are they documented in the README?
  - `PROGRAMSSTRUCTUREMANUAL` Does the README note any manual changes that you need to make to the code in order for it to run?

> Commit! 

You can now proceed to change the status to `Data` 

### Data
Fill out the following Jira fields:
  - `COMPUTING ENVIRONMENT` In which environment will you be executing the authors' code?
  - `DATA PROVENANCE` Where, specifically, are you accessing the data? Typically this is the openICPSR repo URL (same as `CODE PROVENANCE`
  - `DATAAVAILABILITYACESS` Is at least some of the data available?
  - `DATAAVAILABILITYEXCLUSIVE` 
  - `REASON FOR NON-ACCESSIBILITY OF DATA` Fill this out if **none** of the code can be run
  - `NUMBEROFDATASETS` How many datasets are used in the article? 
  - `DATASETSINCLUDED` How many of the datasets used in the article are actually provided by the authors?   
  - `WORKING LOCATION OF THE DATA` Where did you put the data? Examples: CISER, laptop, or Git LFS, or somewhere else

You can now proceed to change the status to `Write Preliminary Report`

### Write Preliminary Report 
At this stage, you need to fill out the REPLICATION.md up to the "Replication steps" part. 
- There is sample language for commonly encountered problems at the Fragments for REPLICATION.md link in the tall grey bar.
- Commit this preliminary report to the Bitbucket repository.
- This allows for earlier identification of that issues that might warrant changes to the procedure. 
  - In particular, this is the stage where you might have identified that some, but not all data are not provided, and we can undertake steps there.

> Commit! 

You can now proceed to change the status to `Verification` 

### Verification
In this stage, you are verifying the code, either using the provided data, or by inspecting the completeness of the source code. The [REPLICATION.md](https://github.com/AEADataEditor/replication-template/blob/master/REPLICATION.md) is the report.

Keep a log of what you do, what you find, and what does not work, in the `REPLICATION.md`.

Follow the steps [here](https://github.com/labordynamicsinstitute/replicability-training/wiki/Prepare_and_run_replication)

You should commit your report with intermediate results as you have them. Do __not__ wait until you have all the results finished. Commit frequently!

> Commit!

You can now proceed to change the status to `Writing Report`

### Writing Report
At this stage, you will write the final version of the report.
- There is sample language for commonly encountered problems at the Fragments for REPLICATION.md link in the tall grey bar.
- Clean up the REPLICATION.md - it should be factual, objective, and not written in the first person.
- Delete the lines in REPLICATION.md that say they should be deleted.

To complete this stage, enter the direct URL of the report, i.e., in the relevant repository:
> https://bitbucket.org/aeaverification/aearep-2/src/master/REPLICATION.md

You can now proceed to change the status to `Under Review`

## Replication Revisions
- See [revision guidance](https://github.com/labordynamicsinstitute/replicability-training/wiki/Revision-to-a-Replication) on the wiki.
- When receiving updated files from authors, do NOT create "update" or "new" directories. The current state of the repository should always correspond to the author's structure. Overwrite files, delete files. The previous state is preserved in Git. This will also tell you what files have changed.
- When running a second replication on the same archive, please be sure to have the committed "REPLICATION.md" be accurate when you commit it - do not let it contain holdover data from a previous replication attempt, as this can lead to confusion.
