# AEJPol-2019-xxxx.R1  "PAPER TITLE" Validation and Replication results

You may want to consult [Unofficial Verification Guidance](https://social-science-data-editors.github.io/guidance/Verification_guidance.html) for additional tips and criteria.

SUMMARY
-------
- All tables and figures are replicated, with one minor discrepancy in Table 1.


- [REQUIRED] (Minor) Please provide debugged code, addressing the issues identified in this report.
  - **After this report was sent, updated code was sent to openICPSR.**
- [REQUIRED] (Minor) Please adjust your tables to account for the noted numerical discrepancies, or explain (in the README) discrepancies that a replicator should expect. 
  - This will be handled in copy-editing 
- [SUGGESTED] The authors should check if the three surveys are cataloged and stored in the World Bank Microdata catalog. If yes, referencing the relevant entries from the Microdata catalog is strongly suggested.
- [SUGGESTED] Several suggested metadata elements (Geographic Coverage, time period, Collection dates) are missing from the openICPSR deposit. These would enhance findability. Please consult our [additional deposit guidance](https://aeadataeditor.github.io/aea-de-guidance/data-deposit-aea-guidance.html)


Data description
----------------
### Surveys by World Bank: Baseline survey, 2-year (200x) and 6-year (201x) follow-ups (PII removed)

- Data Source: World Bank and the authors' survey
- The World Bank collected both a baseline survey and initial follow-up survey to assess short-run program impacts.
- Note that the raw survey datasets the authors have published have been modified slightly from the original raw data in order to remove PII. In particular, they have removed the recorded date of birth for all survey respondents (year and month of birth are still included).
- The original study  describing the first two surveys was cited in the manuscript. It appears that the last follow-up survey is conducted by the authors. Access information is detailed in the readme.

> [SUGGESTED] The authors provide data from Waves I and Wave II, and Wave III (conducted by the authors). Presumably, all three surveys are cataloged and stored in the World Bank Microdata catalog. Referencing the relevant entries from the Microdata catalog is strongly suggested, as it provides additional metadata and findability. This should be done in the manuscript.


### ICPSR data deposit

- [NOTE] openICPSR metadata is sufficient.

> [SUGGESTED] Several suggested metadata elements (Geographic Coverage, time period, Collection dates) are missing from the openICPSR deposit. These would enhance findability. Please consult our [additional deposit guidance](https://aeadataeditor.github.io/aea-de-guidance/data-deposit-aea-guidance.html)


Code description
----------------
- Each figure in the article corresponds to specific lines in the provided programs; see "code-check.xlsx" (end of this report) and "Readme.pdf" for details.
- The main analysis programs are written in Stata and the could be executed through the given master program `MASTER.do`.
- The code segment that changes the directories in every programs does not run properly. Manual changes are needed for individual .do file.
- Romano-Wolf p-values is calculated in the program, which takes a long time (could be more than a day in some computers as mentioned in the Readme). 
- No code is provided for Appendix Figure 1 and 3 since they they are not empirical. 

> [SUGGESTED] Please specify hardware requirements, and duration (execution time) for the last run, to allow replicators to assess the computational requirements.

Data checks
-----------
- All datasets are present for this manuscript.
- Data can be read using Stata, and have data variable labels
- Ran PII and results are reported in "pii_stata_output.csv".

Computing Environment
---------------------

- CISER Shared Windows Server 2016, 256GB, Intel Xeon E5-4669 v3 @ 2.10Ghz (3 processors)
- Stata/MP 16
 
Replication steps
-----------------
1. Downloaded data and code from the openIPCSR repository. 
2. Fixed directory errors in the all Stata programs and changed the package `fmttable` to `frmttable` in `MASTER.do`.
3. Ran `MASTER.do` per Readme.
4. Replicated all tables and figures.

> [SUGGESTED] Please add a setup program that installs all packages as noted above. Please specify all necessary commands. An example of a setup file can be found at https://github.com/gslab-econ/template/blob/master/config/config_stata.do

> [REQUIRED] Please provide debugged code, addressing the issues identified in this report.

Findings
--------

- Minor directory issues in the all do-files (the automated directory changing code does not work properly). Manual changes are needed

## Tables
- Table 1: replicated (minor difference in F-statistics)
  - Paper: Table 1, Col. 2: **456.783**
  - Reproduced: Table 1, Col 2: **456.812**
- Table 2-7: Fully replicated
- Appendix Table 1-29: Fully replicated

> [REQUIRED] Please adjust your tables to account for the noted numerical discrepancies, or explain (in the README) discrepancies that a replicator should expect. 

## Figures

- Appendix Figure 1: not empirical
- Appendix Figure 2: Fully replicated
- Appendix Figure 3: not empirical
- Appendix Figure 4: Fully replicated
- Appendix Figure 5: Fully replicated

## In-Text Numbers
[x] There are no in-text numbers, or all in-text numbers stem from tables and figures.

[ ] There are in-text numbers, but they are not identified in the code


Classification
--------------

- [ ] full replication
- [x] full replication with minor issues
- [ ] partial replication (see above)
- [ ] not able to replicate most or all of the results (reasons see above)

Code Check Table
----------------
| Figure/Table #    | Program              | Line Number | Replicated?                      |
|-------------------|----------------------|-------------|----------------------------------|
| Table 1           | table1.do            |             | minor difference in F-statistics |
| Table 2           | table2.do            |             | Yes                              |
| Table 3           | table3.do            |             | Yes                              |
| Table 4           | table4.do            |             | Yes                              |
| Table 5           | table5.do            |             | Yes                              |
| Table 6           | table6.do            |             | Yes                              |
| Table 7           | table7.do            |             | Yes                              |
| Appendix Table 1  | appendix_table1.do   |             | Yes                              |
| Appendix Table 2  | appendix_table2.do   |             | Yes                              |
| Appendix Table 3  | appendix_table3.do   |             | Yes                              |
| Appendix Table 4  | appendix_table4.do   |             | Yes                              |
| Appendix Table 5  | appendix_table5ab.do |             | Yes                              |
| Appendix Table 6  | appendix_table6.do   |             | Yes                              |
| Appendix Table 7  | appendix_table7.do   |             | Yes                              |
| Appendix Table 8  | appendix_table8.do   |             | Yes                              |
| Appendix Table 9  | appendix_table9.do   |             | Yes                              |
| Appendix Table 10 | appendix_table10.do  |             | Yes                              |
| Appendix Table 11 | appendix_table11.do  |             | Yes                              |
| Appendix Table 12 | appendix_table12.do  |             | Yes                              |
| Appendix Table 13 | appendix_table13.do  |             | Yes                              |
| Appendix Table 14 | appendix_table14.do  |             | Yes                              |
| Appendix Table 15 | appendix_table15.do  |             | Yes                              |
| Appendix Table 16 | appendix_table16.do  |             | Yes                              |
| Appendix Table 17 | appendix_table17.do  |             | Yes                              |
| Appendix Table 18 | appendix_table18.do  |             | Yes                              |
| Appendix Table 19 | appendix_table19.do  |             | Yes                              |
| Appendix Table 20 | appendix_table20.do  |             | Yes                              |
| Appendix Table 21 | appendix_table21.do  |             | Yes                              |
| Appendix Table 22 | appendix_table22.do  |             | Yes                              |
| Appendix Table 23 | appendix_table23.do  |             | Yes                              |
| Appendix Table 24 | appendix_table24.do  |             | Yes                              |
| Appendix Table 25 | appendix_table25.do  |             | Yes                              |
| Appendix Table 26 | appendix_table26.do  |             | Yes                              |
| Appendix Table 27 | appendix_table27.do  |             | Yes                              |
| Appendix Table 28 | appendix_table28.do  |             | Yes                              |
| Appendix Table 29 | appendix_table29.do  |             | Yes                              |
| Appendix Figure 1 | not empirical        |             | N/A                              |
| Appendix Figure 2 | appendix_figure2.do  |             | Yes                              |
| Appendix Figure 3 | not empirical        |             | N/A                              |
| Appendix Figure 4 | appendix_figure4.do  |             | Yes                              |
| Appendix Figure 5 | appendix_figure5.do  |             | Yes                              |