# Step-by-step guide to Jira workflow
This page provides step-by-step guidance for completing initial pre-publication replications through Jira.

See the Replication Revisions (link TK) page for guidance on revisions to previous replication attempts.

## 1. Advance the issue from Assigned to In Progress
- This lets us know that you have started working on replication.
- At this stage you should access and download the replication materials.
- Then you should 
  - [ ] create the Bitbucket repo (and add the `Bitbucket shortname` field)
  - [ ] commit the relevant replication materials, (verify that the `Git working location` is filled out) and 
  - [ ] commit the latest version of the LDI replication template.
- Carefully read the README and start taking notes about the paper: how many datasets are mentioned in the paper? Are they all provided with the archive? Is it clear from the README how to run the code?
  - [ ] Verify the `Code provenance` field - it should be pre-filled with the openICPSR link, but if the code is elsewhere, it needs to be adjusted.
- Advance the ticket to one of four options: Code, Alternative Workflow, Writing Report, or Incomplete
  - Code: Advance to this stage, then download the code (if not already done: this typically happens when the README is provided, but the code is elsewhere)
    - [ ] Journal should be set
    - [ ] Code provenance should be set
    - [ ] Type of Article should be set to "Yes" (has code and/or data)
  - Alternative Workflow: (only for individuals with Admin privilege)
  - Writing Report: no code or data were provided with the archive
  - Incomplete: more information/action is required before you can proceed

## 2. Code
- In this stage, you should 
  - [ ] review the code in detail, and 
  - [ ] start filling out the `code-check.xlsx` template.
- You should also have a notion now of where all the data is, from README, article, and if necessary the code
  - [ ] Fill out the Data Provenance field
- When you are ready to download the data (if separate), advance the ticket to one of two options: Data or Incomplete
  - Data: access data and fill out data data-related fields
  - Incomplete: more information/action is required before you can proceed

## 3. Data
- In this stage, you should be able to access all accessible data
  - [ ] Run the PII-checking code
  - [ ] Describe the data (do relevant variables have labels? Is the data readable?)
- Advance the ticket to one of two options: Write Preliminary Report or Incomplete
  - Write Preliminary Report: access data and fill out data data-related fields
  - Incomplete: more information/action is required before you can proceed


## 4. Write Preliminary Report
- At this stage, you need to fill out the REPLICATION.md up to the "Replication steps" part. 
- Commit this preliminary report to the Bitbucket repository.
  - [ ] The `Report location` field should be prefilled with the `Git working location` + `REPLICATION.md`. Check that the link works
- This allows for earlier identification of that issues that might warrant changes to the procedure. 
  - In particular, this is the stage where you might have identified that some, but not all data are not provided, and we can undertake steps there.
- Advance the ticket to one of three options: Verification, Code Review, or Incomplete
  - Verification: at least some of the data is accessible. In order to progress to this state,
    - [ ] Working location of data has to be filled out
    - [ ] Computing environment has to be selected.
  - Code Review: none of the data is accessible
  - Incomplete: more information/action is required before you can proceed

## 5. Code Review
- If at least some of the data is available in the archive, then proceed to Verification.

## 6. Verification


## 7. Writing Report


## 8. Report Under Review
- When you finish writing the report, copy its URL from the Bitbucket repo into the Report URL field.
- The URL will look like this:
> https://bitbucket.org/aeaverification/aearep-123/src/master/REPLICATION.md
- You are not finished yet! You must advance the ticket to Report Under Review to alert us that you have finished the replication.

