# Preparing a Legacy Deposit for Updates by Authors

Post-publication, authors may wish to make changes to their deposit. In cases where the original deposit was created prior to July 2019, the deposit ownership should be assigned to the corresponding author.

When we receive such an email, the first step is to forward the email to dataeditor-queue@aeapubs.org to create a Jira issue. 
A record of all email correspondence should be kept on the issue by forward the emails to dataeditor-queue@aeapubs.org with the Jira issue in the subject line. 

The next step is to respond to the author(s) with some form of the email below.

```
Let me outline the process and send the link to the AEA policy on Data and Code revisions (https://www.aeaweb.org/journals/data/policy-revisions).


In order for you to make the updates to the deposit, we'll do the following:

- Request a transfer of deposit ownership from the AEA to you (at which point you should receive a notification from openICPSR).
- Share the deposit with your co-authors, giving them full access rights (including the right to re-submit).


Once we've completed the steps above, you will be able to update the deposit.

- The currently published V1 will remain available indefinitely, and will remain the version of record; the new version you are creating will be V2, and will be linked (in a very obvious way, with a banner) to V1.
- Do not create a second folder with "updated data" or similar; rather, simply delete any files that are obsolete and upload the files which you wish to add. What's there is what will end up being published.
- One suggestion: once you have updated the README, move it to the root folder for increased visibility.
- Once you are done, we strongly suggest you also update the remaining metadata in the deposit (see https://aeadataeditor.github.io/aea-de-guidance/data-deposit-aea.html for guidance).
- Once that is done, submit the deposit to us. We will check for completeness, and republish.

Please don't hesitate to ask if you have any questions.
```

### Original Jira Issue

One of the most efficient ways to search for the original Jira issue would be to take the Manuscript Number from the ICPSR deposit and search for it in Jira. If an original Jira issue does exist, link the two issues. 

Since in these cases the original deposit was created prior to July 2019, it is very possible that no original Jira issue exists (the paper pre-dates the current Data Editor process). In this case, post a comment to this effect on the new Jira issue and post another comment with the paper DOI.

### Jira Fields

- Journal
- Manuscript Central Identifier
- openICPSR Project Number
- MCStatus should be "Update" ("Revision" is also acceptable)


### Author Access

Necessary steps from our end:
1. Request a transfer of deposit ownership from AEA to the author. They should receive a notification from OpenICPSR.
2. Share the deposit with all authors of the manuscript, giving them full rights (including the right to re-submit).

### Transition

There is a specific transition in the Jira workflow called "Author submitted post-publication modifications" which enables the user to move the issue from "In progress" straight to "Pending openICPSR changes."

### Checks

Ensure that authors have "submitted to AEA", and that an updated README as well as any updated files are present.

In these cases we are only checking to verify what specific changes were made and that these changes are reflected in an updated README. The email correspondence should be checked, as should the logs. There should be no additional directories within the deposit called "update" or similar. See the revision policy.

The resolution should always be "Evaluation only."

### Moving to Publication

From here on, follow the usual workflow to publication of the deposit. In general, the AEA Data Editor, not the Editorial Office will publish the deposit. 

### Communicating to AEA Editorial Office

See Revision policy (link above). If the version of record is changed, this needs to be notified to the editorial office, so they can update the records. If a new version is created, no further action is needed.
