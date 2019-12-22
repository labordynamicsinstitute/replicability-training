# Preparing Deposit for Publication

1. Open the issue on JIRA
2. Click on the "Submit to MC" transition
3. In the pop-up, you should have all the necessary information
   - Note: links in the pop-up window are not clickable: double-click, then use right-click to "Open in New Tab"
   - `MCEntryURL`  has the link to Manuscript Central (MC) in order to submit
   - `Manuscript Central Identifier` to find the manuscript
   - `MCRecommendationV2` (should have) has the information to choose in MC
   - `Git working location` has the information to clone the repository
4. If necessary, clone the Bitbucket repository associated with the issue 
   -  If not already created, make a `REPLICATION.pdf` file from the markdown `REPLICATION.md` using Visual Studio Code, then commit and push!
5. Open the Manuscript Central link (double-click, right-click, open in new tab)
   1. Let LastPass fill in password to access Manuscript Central
   2. Click on the review tab and identify the MC number of the paper
   3. Select "Continue Review"
   4. Always click "Yes" when asked: Would you be willing to review a revision of this manuscript?
   5. Select the recommendation as noted in the Issue (`MCRecommendationV2`)
   6. Copy-paste the "Summary" part from `REPLICATION.md` in the comments to the author. Add "Details are in the full report."
   7. Select and upload the `REPLICATION.pdf`, click on "For author and  editor"
   8. Re-verify all information
   9. Click on "Submit"
6. Back in the pop-up, 
   1. Paste the same "Summary" into the "Comment" field on JIRA
   2. Click on "Submit to MC"
