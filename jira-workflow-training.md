# Training for Jira-based workflow

For pre-publication verification, we use a Jira-based workflow quite similar to the post-publication processes described in the [Wiki](https://github.com/labordynamicsinstitute/replicability-training/wiki).

## Scope
Your supervisor will assign you to this workflow if needed. This workflow covers code and data, even when data may not be accessible.

This workflow does NOT cover assessment of data citations. This is covered by a different training.

## Overview


The following table illustrates the flow and transitions. The `transition` field identifies the button that will appear in the interface
that needs to be clicked in order to progress an issue from the `From` state to the `To` state. The `Condition` field identifies
which form field needs to be filled out in order to be able to make the transition. `Blocked` is always an option, and leads to a "waiting state"
until a resolution can be found.

|From|	Transition		|→ To | Condition |
|:---|:---------------|:----|:----------|
Open | Start task     |→ In Progress|   |
In Progress	  | Download code       |→ Code         ||
Code	        | Access data         |→	Data        ||
Data	        | Data is accessible  |→	Verification||
.             | Data not available  |→	Code review ||
Verification	| Prepare report      |→	Report      ||
Code review	  | Prepare report      |→	Report      ||
Report	      | Submit for review   |	→	Under Review||
Under Review	| Approve |→  Approved |   |
.             | Incomplete |→  Incomplete | n.a. |
Approved	    | Done       |→ 	Done      | n.a. |
Incomplete	  | Restart    |→  Code review | |
.             | Restart verification|→ Verification ||
.             | Restart task        |→ In Progress  ||
Blocked	      | Reopen     |→  Open       | n.a. |
