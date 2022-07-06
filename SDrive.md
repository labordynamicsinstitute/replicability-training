# Working with Restricted-Access Data on the S: Drive

In cases where we have gained access to restricted data, that data is placed in a folder, i.e. "LDILab/aearep-xxxx-nda_Implicit", on the S: drive. We require that the RA **NOT** make any copies of the data or move the data from the directory on the S: drive. This precaution is to ensure that the data has once central location from which it should be deleted once we have completed our process.

The `Working location of the data` field on Jira should contain the path to the data on the S: drive. You should have your regularly cloned workspace on the U: drive, separate from the data on the S: drive. We will then use code (i.e. Stata globals etc.) to write to the data on the S: drive.

### Stata Example 1

Some replication packages make this very straightforward, usually by the inclusion of a global specifically set for a "confidential" data folder. It may contain a master file that looks something like this...

```
*					Master File							*
*														*
*********************************************************
*********************************************************



******************************************
*** Set-up the directories and install packages
******************************************

***set the working directory here:
global path "C:/Users/author/path"

*** The raw data folder contains two subdirectories, one for the public data and one for the confidential
global rawdata "$path/data"
global public "$rawdata/public"
global confidential "$rawdata/confidential"

global code "$path/code"
global results "$path/output"
```
1. Include the `config.do` in the master file as usual.
2. In the `config.do`, create a new global for the S: drive. For example: `global sdrive "S:/LDILab/aearep-1234-nda_Implicit"`
3. In the master file, incorporate the `rootdir` from the `config.do` as the main global `path`. This should reflect your workspace on the U: drive.
4. Incorporate the new global `sdrive` to set the authors' global `confidential`. 


Updated for the S: drive:
```
*					Master File							*
*														*
*********************************************************
*********************************************************

include "config.do"

******************************************
*** Set-up the directories and install packages
******************************************

***set the working directory here:
global path "$rootdir"

*** The raw data folder contains two subdirectories, one for the public data and one for the confidential
global rawdata "$path/data"
global public "$rawdata/public"
global confidential "$sdrive/confidential"

global code "$path/code"
global results "$path/output"
```




