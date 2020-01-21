# Notes for JIRA Supervisor

This collects various tasks for the JIRA Supervisors.

## Requests received
JIRA will receive requests sent to a specific email, including several maintenance emails from Manuscript Central. Each email generates an issue, unless the subject line references a previous issue. The following list identifies what to do with each type of issue/email.

- "[JOURNAL] - Account Modified in Manuscript Central" - Delete (should be obsolete)
- "Invitation to Review ..." - these are for "Revise and Resubmit"
  - Click on acceptance link. This email/issue should be the core of the review request.
  - Fill in Journal, MC number
  - Check if this is a revision by searching by MC number in previous issues. If yes, **link** the two issues ("is revision of")
  - Fill in "due date" as [date sent] + 10 **working** days (typically 14 calendar days)
  - Verify in the PROOF.PDF whether an openICPSR repo has been created, or if a different location is used (Dataverse, etc.)
    - if openICPSR -  Do not yet assign!
    - if other - Assign!
- "Accepted Review ..." - this is notification only coming immediately after acceptance, should be deleted.
## Recording decisions in Manuscript Central
### Revise and Resubmit cases
- Accept - Goes forward to (full) "Acceptance"
- Revise-and-resubmit - Goes to another round of "Conditional Acceptance", with revisions requested
- Reject - Goes back to the Editor for re-consideration
### Conditional Acceptance cases
- Accept - Goes forward to (full) "Acceptance"
- Accept with Changes - Goes forward to (full) "Acceptance", but there are conditions imposed (possibly changes to reference citations at the copy-editing stage, TBD)
- Conditional Accept; Manuscript Ready - Remains in "Conditional Accept" stage (because there are program- or data-related issues that need to be solved), but no changes are expected to the manuscript (which could possibly start the copy-editing process)
- Conditional Accept - changes need to be made, manuscript remains in "Conditional Accept" stage (= old "Revise and Resubmit")
- Revise and Resubmit - changes are major, manuscript returns to the "Revise and Resubmit" stage (= old "Reject")

## ICPSR emails
openICPSR sends emails to the main AEA Data Editor email adress. 

- "[SOMEBODY] has invited you to collaborate on an ICPSR project" - notification of sharing, with direct link to project. 
  - Can be archived, no further action needed.
- "Comment Added to OPENICPSR-[NNNNNN]" 
  - This should mention the manuscript number ("Data deposit for AEJMicro-2018-NNNN")
  - Find the JIRA request for the same manuscript number - this may not yet exist!
  - If the JIRA issue was found, 
    - edit subject line to prepend "AEAREP-ZZ" (where ZZ is the issue number and forward the message to the AEA Data Editor queue address.
    - edit the JIRA issue itself, and add the "openICPSR" number to the relevant field.
    - Do some basic checks on openICPSR repository. Sample email (delete lines not relevant prior to sending via the Communication Log. Alternatively, this can be added to the REPLICATION.md to provide information only once to researchers.
```
after a quick initial review of this deposit within the AEA Repository, please make the following adjustments:
    - [REQUIRED] Manuscript Number should be entered into the appropriate field (under "Scope")
    - [REQUIRED] Please add JEL Classification
    - [SUGGESTED] Please add Subject Terms (optional, but suggested)
    - [SUGGESTED] Please add Data Type
    - [REQUIRED] ZIP files should be uploaded via "Import from ZIP" instead of "Upload Files" (there should be no ZIP files visible, except in certain circumstances, like when there are too many files). Please delete the ZIP files, and re-upload using the "Import from ZIP" function.
    - [REQUIRED] Please delete the `__MACOS` directory
    - [REQUIRED] Please delete empty directories
    - [REQUIRED] Please delete any redundant (obsolete) files
    - Further guidance can be found at https://aeadataeditor.github.io/aea-de-guidance/data-deposit-aea-guidance.html
 DO NOT REPUBLISH THE PROJECT YET.
 
 Once we have received the manuscript through Manuscript Central, we will proceed to a more thorough review, and may have additional change requests.
 ```

## Linking JIRA issues and openICPSR repositories
Two ways:
- parse through emails to dataeditor@aeapubs.org (search for manuscript number)
- search by title through [https://www.openicpsr.org/openicpsr/workspace](https://www.openicpsr.org/openicpsr/workspace)

Then 
- enter the openICPSR number in the appropriate JIRA field.
- share the openICPSR deposit with the assigned RA's email  

## Setting up new team members

### System set up

#### Jira
- Log in to Jira as admin
- Choose "People"
- Choose "Manage users" (may need to log in again)
- Add emails (separated by commas), as "Basic" users, add to "training" group.
#### Bitbucket
- Go to Bitbucket
- Choose team "aeaverification"
- "Members > Manage Team", select "Developers"
- Add individual email addresses
### Setting up training
- Use ICPSR 117322 as "initial submission"
- Assign Training cases (one per user)
- Share ICPSR 117322
- Bulk-create a training issue for all users

  


