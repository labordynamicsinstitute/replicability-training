# Basic info

The ICPSR deposit is noted in the JIRA ticket, if it already exists. There is no specific field in Jira for CodeOcean, but check the "Computing Environment" to see if "CodeOcean", and the "Working location" may contain the URL to the CodeOcean capsule. If not, check the comments.

When there is an ICPSR deposit, check that the deposit is fully committed to Bitbucket. Ensure that you have a ZIP file from the deposit (presumably called `12345.zip`) stored locally on your computer or CISER, which includes all data files.

# Populating CodeOcean for author-interaction

See separate notes

# General guidelines about a full migration of CodeOcean to openICPSR

## On CodeOcean

- all runs should be completed, and all editing done.
- download the capsule (Menu "Capsule -> Export..." and tick the box to include the data)

## On the Bitbucket repo

> The following can be done on CISER or on your own computer, you will not need to run any code.

- create a new directory in the Bitbucket repo that corresponds to the specific capsule. Just as we do with openICPSR, re-use the numerical part of the URL, here prefixed with "`capsule-`", e.g. if the URL is "https://codeocean.com/capsule/0687784/tree" then create a directory "`capsule-0687784`"
- from the command line, unzip the capsule ZIP file, e.g. 
```
cd capsule-*
unzip ../57033059-76d7-422d-8301-d173e3520f07.zip
```
You should end up, within that directory, with 4 additional directories, and one file:
```
REPRODUCING.md
code/
data/
environment/
metadata/
```
- Add all these directories to Bitbucket (it is normal that the data files will not be added), and commit to Bitbucket:
```
git add *
git commit -m 'Files from CodeOcean capsule 0687784'
git push
```

