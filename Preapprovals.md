## Generic Guidance
- Pre-approvals usually can be completed rather quickly and should be prioritized.
- The pre-approver should not be running any of the code or downloading any of the data unless asked to do so.
- The language for the `[REQUIRED]` tag comments is drawn from the [Sample Language for Reports](https://github.com/AEADataEditor/aea-de-guidance/blob/fab4c3f3c52e619a696dfafc4a55dacb6460f54a/sample-language-report.md). To ensure uniformity across reports, pre-approvers are encouraged to use the phrases verbatim.

## Preliminary Steps for Pre-approving Reports
1. The "Review for pre-approval" transition in Jira requires specific permissions. If you have not been granted this permission, please reach out to your supervisor. 
2. Clone the Bitbucket repository of the report that requires pre-approval to the local machine or CISER machine. **Do not download the openICPSR deposit!**  The pre-approver checks and finalizes the report but does not redo the whole replication.
3. Skim through the report and note if it is an original replication or a revision.  Follow the steps below correspondingly.


## Original Replication Report
1. Delete all of the `INSTRUCTIONS` comments of the report.
1. Check if the replication requires **IRB approval/RCT registration**.  These are commonly found in papers that utilize randomized experiments involving human participants.  Ensure that the manuscript contains the necessary approval information and insert relevant `[REQUIRED]` or `[SUGGESTED]` tag comments wherever necessary.
1. Read through the **Data Sources section** of the report and check for completeness.
   - Reports sometimes might be missing data sources.  Cross-check this with the manuscript and the README.  This is usually the most time-intensive part of the pre-approval.
   - The report should accurately reflect whether the data source has been cited and whether its location/access modality has been provided. 
   - Insert relevant `[REQUIRED]` or `[SUGGESTED]` tag comments.
2. Check the **Data checks section** for completion.
   - Check if the PII scan output is present in the repository.
   - Insert relevant `[REQUIRED]` or `[SUGGESTED]` tag comments.
2. Check the **Code checks section** for completion.
   - Check if the completed Code check spreadsheet is present in the repository.
   - Insert relevant `[REQUIRED]` or `[SUGGESTED]` tag comments.
4. Check the **Stated Requirements section** for completion and insert relevant `[REQUIRED]` or `[SUGGESTED]` tag comments.
5. Carefully read through the **Replication steps section.**
   - Ensure that this report section is coherent in its description of the steps the replicator took to perform the entire replication.
   - If the replicator noted that the code contains bugs, the error message/error code should be explicitly listed.
   - **The pre-approver should not be rerunning any of the code!**
   - Communication between the pre-approver and replicator is encouraged so that any confusing/unclear language used in this section can be clarified.
   - Insert relevant `[REQUIRED]` or `[SUGGESTED]` tag comments.
6. Check the **Computing Environment of the Replicator section** for completion. 
7. Format the results in the **Findings section** into tables by utilizing the the Excel-to-Markdown Extension in Visual Studio.
   - Check if the output/log files have been pushed to the Bitbucket repository.
   - If there are discrepancies between the replicated tables and figures and those of the manuscript, the report should contain images/screenshots to highlight the differences.
   - If there are numerous tables and figures that exhibit discrepancies, these should be put into a .zip file.  This action should be noted in the **Summary section** as well as mentioned in a JIRA comment.
8. Ensure the classification of the replication fits the degree of replicability.
9. Fill out the **Summary section** of the report.
   - Highlight the merits of the replication i.e. how many figures/tables were replicated, if data citations were properly completed, etc.
   - Create a list of required items.
   - Use a script or manually copy-paste all of the `[REQUIRED]` tags to this list.
      - [aeareq.bash](https://gist.github.com/larsvilhuber/d4e1d8d55da0d6daecd6415acbbe974f) extracts the `[REQUIRED]` tags and places them at the top of the REPLICATION.md 
   - Repeat for `[SUGGESTED]` tag items.
10. (Re)generate the PDF of the report.
   - Use MarkdownPDF package if you are using Visual Studio Code
   - Use a script: [aeaready.bash](https://gist.github.com/larsvilhuber/a89e6d842b563e3ab3fcf9e86fd37e48) creates the PDF from the REPLICATION.md, crafts the commit message and pushes it to the repository.  It requires additional pieces of software that are noted in the link.

11. Commit and push all changes to the repository.  Advance the JIRA ticket to "Pre-approved."  The pre-approval is now complete!

**Notes:** The pre-approver should reach out to the original replicator for clarifications should there be any confusions during the course of pre-approving the report.  If bugs in the code seem trivial i.e. missing packages, missing `Results` directory, replicator cannot find output etc., the pre-approver should reach out to the original replicator for further clarification.

For the majority of the `[REQUIRED]` comment tags, it is best to use them verbatim to preserve uniformity across our reports.  However, there are times where a more accurate description can help the author pinpoint what exactly is required of them.

For example, say we have a scenario where the author did not include code for Table A.6 in the code deposit but everything else has been provided and replicates perfectly.

Instead of writing:
```
> [REQUIRED] Please provide complete code, including for construction of the analysis data from raw data, and for appendix tables and figures, and identify source for inline numbers.
```
It is clearer to the authors if we write:
```
> [REQUIRED] Please provide complete code for appendix tables and figures, in particular Table A.6.
```


## Revision Report
The checklist of items to review are roughly the same as above.  In addition:
- The pre-approver should check that `[We REQUESTED]` tags are used in place of `[REQUIRED]` tags.  These tags should be preceded by a ">" to create a comment rather than "-," which creates a bullet point.
   - [aeareview.bash](https://gist.github.com/larsvilhuber/05bfc1b4d3dcabd10b04705e8b45198e) changes all the `[REQUIRED]` to `[We REQUESTED]`.
- The report should reflect the **current** state of the replication.
- In the **Summary Section:**
   - Ensure that the summary reflects the **current** state of the replication.  See [Revision Guidelines](https://github.com/labordynamicsinstitute/replicability-training/wiki/Revision-to-a-Replication) for more guidance on what this means for revisions.
   - Create a list of persisting issues that require attention.
   - Create a separate list of completed items.
