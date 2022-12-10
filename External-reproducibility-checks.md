# External reproducibility checks

If you have agreed to provide us with an external reproducibility check, we kindly ask that you follow these instructions.

## The manuscript and code are confidential at this stage

Do not post them to any public place. Use the resources we provide you with, or those that your institution provides you with. While we may provide you with Github or Bitbucket repositories, those are to remain private, i.e., require a login for access. 

Once you have completed the task, and committed all changes to the Git repo we provide you with, or sent us the report from a secure system, delete all data and code when told to do so (don't do this immediately, as we may have clarifying questions).

## Use a separate environment to run the code where possible

While you *can* use your laptop, you should follow certain procedures to both not affect the reproducibility check nor affect your usual working environment. Notes below.

## Use Git

We will provide you with the code in a Git repository (the data will be separate). If you have questions on how to use Git, please let us know, and we will help and guide you.

> You should NOT use the file upload capability of the web-based interface (i.e., Github.com, Bitbucket.com) if you can avoid it.

## Follow the procedures in the authors' README

You should follow instructions as closely as possible. However,

- you are not required to do extremely tedious or time-intensive manual steps.
- you are not required to "bog down" your personal laptop (see resources)
- you should lightly improve on the procedures, by following our replication procedures (below)
- you are not required to install software or packages that might mess up your own research

## Replication procedures

In addition to any setup instructions from authors, a few things to take into account

- Use the resources we provide you with, where possible
- Use the procedures to use "config.do" or similar files. 
  - This is always possible for Stata. See [instructions](https://labordynamicsinstitute.github.io/replicability-training-curriculum/stata-related-procedures.html#running-code-in-stata). 
  - Similar procedures are possible for Python and Julia (use `environments`)
  - Similar procedures are available, to some extent, for R (use separate libraries, if possible, or the `renv` or similar packages)
  - Matlab and SAS will always use whatever is installed system-wide - this is a known caveat.

## Log everything

Create a log file, if possible, for every run.

- For Stata, our [template config.do file](https://github.com/AEADataEditor/replication-template/blob/master/template-config.do) will handle this, if used correctly.
- For R, use "R CMD BATCH" to run code, even when using Rstudio (use the Terminal tab ).
- For Matlab, where possible, use "`sink`", but note that it might interfere with some programs.
- For Julia and Python, we have no good solutions other than to use the command line where possible, and capture the output.

Once you have a log file, commit it.

## Document everything

Keep a journal of what you are doing. You should be able to point to the journal, together with a log file or screenshots, to document problems, and how you solve them. 

An example:

>
> 1. Downloaded code and data from openICPSR
> 2. Added line to use `config.do`
> 3. Ran `main.do`  as instructed by the author
>   - I used the "right-click" method on Windows
> 4. Code stopped at the third step, looking for package `xyz`
> 5. Added the package to the relevant section in `config.do` so it would get installed, and ran the entire `main.do` again
> 6. Programs finished but no figures were output. Inspection of the code showed that they only display on-screen. Added `graph export` as PNG files at all relevant parts, then ran entire `main.do` again.

If the authors' instructions say to "view" something interactively, investigate native methods (`graph export`) to capture the information. Otherwise, use screenshot to capture the information. Make a note of that, too.

## Commit all logs, outputs, etc. to Git

All logs and outputs, but not data, should be committed to Git. 

## Compile a report

Our standard report template is included. You do not need to do the sections on Data Provenance unless explicitly asked to. You can start at the [Code description](https://github.com/AEADataEditor/replication-template/blob/a530d6d5a906646e015ca62fdd78a774dd793e7a/REPLICATION.md?plain=1#L162).

- Don't forget to report your computer and software configuration
- The report should be committed to git as well. There is no need to convert it to PDF.

## Send a report

Reports should be committed to git (**not** sent by email). An email notification that all is complete is sufficient. 

> Please "reply-all" to the email you received.

## Final confirmation

We will confirm to you when we have exhausted all our questions, at which point we will ask you to delete all code and data.

## Wrap-up: Delete all code and data

Once you have completed the task, and committed all changes to the Git repo we provide you with, or sent us the report from a secure system, AND have answered all of our clarifying quesitons, please delete all data and code. 


## Resources

You can have access to all the resources we regularly use:

- [CCSS ("CISER") compute nodes](https://ciser.cornell.edu/computing/computing-help/how-to-login/). If you do not have an account, request a Research account with "lv39" as sponsor. Do not use the restricted data access!
- [BioHPC compute cluster](https://biohpc.cornell.edu/lab/lab.aspx). If you do not have an account, request one. Even if you have an account, request to be added to the "lv39" lab.
- [CodeOcean](https://www.codeocean.com) - Don't forget to share with "dataeditor@aeapubs.org". Instructions are [here](https://labordynamicsinstitute.github.io/replicability-training-curriculum/access-to-computers.html#reproducibility-checks-in-codeocean)
- [WholeTale](https://labordynamicsinstitute.github.io/replicability-training-curriculum/access-to-computers.html#conducting-reproducibility-checks-on-wholetale)
- [Github Codespaces](https://github.com/codespaces) - with some caveats, talk to us
- Your laptop 

Matrix (tentative)

| Environment | Long-running | Big data | HPC |Stata | Matlab | Julia | Python | R | Docker |
|------------|--------------|----------|----|-------|--------|-------|--------|---|---|
| CCSS   | Max 3.5 weeks | M | -- | **Y** | **Y** | ? | M | M | -- |
| BioHPC | Any length    | **Y** | **Y** | **Y** | **Y** | **Y** | **Y** | **Y** | **Y** |
| CodeOcean| Any length  | -- | -- | **Y** | **Y** | **Y** | **Y** | **Y** | -- |
| WholeTale| Any length  | M | -- | **Y** | M | M | **Y** | **Y** | -- |
| Github CS| Max 12 h    | -- | -- | Y*| -- | Y*| **Y** | Y*| **Y** |
| Laptop   | Any length? | -- | -- | ? | ? | ? | ? | ? | ? |

Key:
- `Y` Unqualified "Yes" - good support
- `Y*` When using Docker images
- `M` Medium - some caveats
- `N` No - not recommended
