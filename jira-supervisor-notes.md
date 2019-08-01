# Notes for JIRA Supervisor

This collects various tasks for the JIRA Supervisors.

## Requests received
JIRA will receive requests sent to a specific email, including several maintenance emails from Manuscript Central. Each email generates an issue, unless the subject line references a previous issue. The following list identifies what to do with each type of issue/email.

- "[JOURNAL] - Account Modified in Manuscript Central" - Delete
- "Invitation to Review ..." 
  - Click on acceptance link. This email/issue should be the core of the review request.
  - Fill in Journal, MC number
  - Fill in "due date" as [date sent] + 10 working days
  - Verify in the PROOF.PDF whether an openICPSR repo has been created, or if a different location is used (Dataverse, etc.)
    - if openICPSR -  Do not yet assign!
    - if other - Assign!
- "Accepted Review ..." - this is notification only coming immediately after acceptance, should be deleted.

## ICPSR emails
openICPSR sends emails to the main AEA Data Editor email adress. 

- "[SOMEBODY] has invited you to collaborate on an ICPSR project" - notification of sharing, with direct link to project.
- "Comment Added to OPENICPSR-[NNNNNN]" 
  - This should mention the manuscript number ("Data deposit for AEJMicro-2018-NNNN")
  - Find the JIRA request for the same manuscript number - this may not yet exist!
  - If the JIRA issue was found, 
    - edit subject line to prepend "[AEAREP-ZZ]" (where ZZ is the issue number, and the square brackets are part of the text), and forward the message to the AEA Data Editor queue address.
    - edit the JIRA issue itself, and add the "openICPSR" number to the relevant field.
    - Also add the URL included in the email to data provenance
    - Do some basic checks on openICPSR repository
      - [ ] Manuscript Number is entered into the appropriate openICPSR field (under "Scope")
      - [ ] ZIP files were uploaded via "Import from ZIP" instead of "Upload Files" (there should be no ZIP files visible, except in certain circumstances, like when there are too many files)
      - [ ] No `__MACOS` directory
      - [ ] No empty directories

## Linking JIRA issues and openICPSR repositories
Two ways:
- parse through emails to dataeditor@aeapubs.org (search for manuscript number)
- search by title through [https://www.openicpsr.org/openicpsr/workspace](https://www.openicpsr.org/openicpsr/workspace)

Then enter the openICPSR number in the appropriate JIRA field.




  


