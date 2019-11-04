# Pre-publication Replication Example

Lars Vilhuber and David Wasser

November 2019



## Walking Through An Example

-   We will work through an example of a pre-publication replication
    together

-   We will use a replication package that has already been published on
    openICPSR: \#110803

-   You will need to set up an account on openICPSR

-   Do each step on your computer

-   Keep the Wiki open in another tab


## Outline

1. Access article and download materials
2. Create repo with template
3. Populate repo
5. JIRA Process
6. Verification
7. Committing and pushing to repo

## Access article and download materials

-   Find the issue on JIRA and advance it from **Open** to **In
    Progress**

-   The pdf of the manuscript will be attached to the JIRA issue

-   The openICPSR project URL will already be in the Code Provenance field, click on it
        - If not, request access from the JIRA administrator (Lars or David) via a note in the comments
-   Follow the [directions](https://github.com/labordynamicsinstitute/replicability-training/blob/master/openICPSR_training.md) on the wiki for downloading them.

-   You should see a project named “Data and Code for Uncertainty and Business Cycles Replication File”

-   On the righthand side, click **Download This Project**

## Create repo

-   Repositories for AEA Verification are on
    [https://bitbucket.org/aeaverification/](https://bitbucket.org/aeaverification/)

-   Follow the instructions in the Wiki for [creating a new repo](https://github.com/labordynamicsinstitute/replicability-training/wiki/Setting-up-a-repository-on-Bitbucket)

-   **Today only**: Add your netid to the end of the repo name

-   Repository name should be the same as the JIRA ticket number, e.g.
    `aearep-14` or `training-10`

-   **Today only**: Make the repo name “TRAINING-nn-netid” where "nn" corresponds to the specific Jira ticket assigned to you.

## Populate repo

-   Follow the instructions in the Wiki for [cloning a repo](https://github.com/labordynamicsinstitute/replicability-training/wiki/Populating_repository_for_replication)

-   Delete unneccessary files from the template: for this example, you should only save: REPLICATION.md, .gitignore,
    and SRC

-   Save the downloaded materials from the openICPSR deposit in your repo (hint: they are probably in your downloads folder).

-   Now we will use git to `add`, `commit`, and `push` these files to Bitbucket

-   In the terminal, navigate to the repo. Then:

    1.  Use `git add` to add the appropriate files (careful!)

    2.  Commit:
        `git commit -m REPO NAME #comment Write your commit message here`

        -   This is “smart commit” that syncs JIRA and Bitbucket

    3.  Push: `git push origin master`

-   Check Bitbucket – our files should be there now

-   This replication is in Matlab, but most of the replications you do will be in Stata

-   The most important difference between the Stata process and the Matlab process is the `config.do` file in Stata (see the wiki for [help](https://github.com/labordynamicsinstitute/replicability-training/wiki/Prepare_and_run_replication) on this)

## JIRA Process

-   Fill out the Jira fields according to the [training](https://github.com/labordynamicsinstitute/replicability-training/blob/master/jira-workflow-training.md). 

-   Go all the way through Writing the Preliminary Report.
    
## Verification

-   Let’s try to replicate Figure 1 today

-   Log into CISER

-   Create a directory in Documents for this example called
    “jira_example”

-   Use `git clone` to get your Bitbucket repo and its contents into this folder

-   Open `gen_figure1.m` in Matlab and run it

-   What do you find?

Committing and pushing to repo
------------------------------

## Committing and pushing to repo

-   After running the code, we will write our report and then `git commit` and `git push` again.

-   Always remember: commit frequently, push (at least) daily


