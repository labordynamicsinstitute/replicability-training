# Training for Jira-based workflow

For pre-publication verification, we use a Jira-based workflow quite similar to the post-publication processes described in the [Wiki](https://github.com/labordynamicsinstitute/replicability-training/wiki).

## Scope
Your supervisor will assign you to this workflow if needed. This workflow covers code and data, even when data may not be accessible.

This workflow does NOT cover assessment of data citations. This is covered by a different training.

## Overview

![workflow image](images/New_AEA_Data_Editor_Workflow_-_Jira.png)

The following table illustrates the flow and transitions. The `transition` field identifies the button that will appear in the interface
that needs to be clicked in order to progress an issue from the `From` state to the `To` state. The `Condition` field identifies
which form field needs to be filled out in order to be able to make the transition. `Blocked` is always an option, and leads to a "waiting state"
until a resolution can be found.

| From         | Transition           | → To           | Condition |
|:-------------|:---------------------|:---------------|:----------|
| Open         | Start task           | → In Progress  |           |
| In Progress  | Download code        | → Code         | `Entry questionnaire` has been filled out, `Journal` has been identified. |
| Code         | Access data          | →	Data          | `Code download URL` and `Git working location` have been filled out. |
| Data         | Data is accessible   | →	Verification  | `Location of data` has been filled out.|
| .            | Data not available   | →	Code review   | `Reason for non-accessibility of data` has been filled out.|
| Verification | Prepare report       | →	Report        | |
| Code review  | Prepare report       | →	Report        | |
| Report       | Submit for review    | →	Under Review  | `Report URL` has been filled out.|
| Under Review | Approve              | →  Approved    |Can only be done by **approvers**.|
| .            | Incomplete           | →  Incomplete  | n.a.      |
| Approved     | Done                 | → 	Done         | n.a.      |
| Incomplete   | Restart              | →  Code review |           |
| .            | Restart verification | → Verification |           |
| .            | Restart task         | → In Progress  |           |
| Blocked      | Reopen               | →  Open        | n.a.      |

### Notes
- The Entry Questionnaire is different for pre-publication verifications. Please consult with your supervisor.
- In the Issue form, please also fill out other fields, as noted.
- If code and/or data are provided by email, `Code download URL` should be filled out as "https://email.com".
- There are no drop-down menus, but once a value has been entered, it becomes available for future use. E.g., once `Stata` has been entered in software, it becomes a choice for future entries, and should be re-used.
- All code should be stored on Bitbucket Git repositories. When committing, always use [Smart Commits](https://confluence.atlassian.com/bitbucket/use-smart-commits-298979931.html)
- Data should be stored locally (currently) / in [Git LFS](https://confluence.atlassian.com/bitbucket/git-large-file-storage-in-bitbucket-829078514.html) (soon)
