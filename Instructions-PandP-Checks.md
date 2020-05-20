# Instructions for PandP checks

You will be assigned a Jira issue. It should look something like this:

![](images/Jira-screenshot.png)

Take note of the 4 highlighted fields:

-   \(1) the "AEAREP" number (identifier for the issue on Jira)

-   \(2) the "Manuscript Central Number" (identifier on the AEA's editorial system)

-   \(3) the "openICPSR Project Number" (identifier on the ICPSR system)

-   \(4) the link for "Code Provenance", which should direct you directly to openICPSR

> Here's the guidance document:
[https://aeadataeditor.github.io/aea-de-guidance/data-deposit-aea-guidance.html](https://aeadataeditor.github.io/aea-de-guidance/data-deposit-aea-guidance.html)

## Step 1

You should now do the following:

-   Open the link in (4) on openICPSR

<!-- -->

-   Open the form:
    > [https://fillabledocument.page.link/Kei1](https://fillabledocument.page.link/Kei1)

-   Assess the repository, filling out the form as you go along

    -   It is important that you enter the AEAREP and Manuscript numbers accurately. We suggest copying-and-pasting.

    -  If you need to find a repository, use this link: [https://www.openicpsr.org/openicpsr/tenant/openicpsr/module/aea/reports](https://www.openicpsr.org/openicpsr/tenant/openicpsr/module/aea/reports)
-   Submit the form.

- The form will get added to the issue after some delay (typically an
hour), as a PDF.

- Close the form after each issue, and open it again for the next one.

In Jira:

-   Move the issue forward by choosing "**Process PandP**" to status
     "*Submitted PandP Form*"
-   This indicates that you are waiting for the form to arrive

## Step 2

Once the form PDF has been added to the issue, you should return to the openICPSR repository. Depending on what's on the form, proceed to do one of the following:

### If the form has all "required" elements checked, you should "sign off":

- Write a "Project communication log" entry
    -   *Subject line:* AEAREP-xxx Data and Code Deposit for P&P  submission accepted

    -   *Content*: Thank you for uploading your code and data. This
         deposit is accepted. No computational verification was
         conducted, only compliance with required metadata was checked.

-   Back in Jira, move it through the workflow

    -   Choose "**Prepare for publication**"
        -   Resolution: *Evaluation only*
        -   MCRecommendationV2: *Accept*

### If the form does not have all "required" elements checked, make the following entry:


-   Write a "Project communication log" entry

    -   *Subject line:* AEAREP-XXX Modifications to make to your P&P
        deposit

    -   *Content:* Thank you for uploading your code and data. We have
         checked the deposit for compliance with the required metadata
        elements. Please see the attached form for modifications to
         make.

    -   Attach the PDF from the issue to the communication log.

-   Back in Jira,

    -   Choose "**Wait for openICPSR response (PandP)**"
        -   Resolution: "*Evaluation only*"
        -   MCRecommendationV2 = "Accept with changes"

    -   Later, once the issues have been resolved (typically days or
        weeks later) follow the process under "required elements
        checked"
