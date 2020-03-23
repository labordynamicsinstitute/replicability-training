# AERI-2019-xxxx.R2 "PAPER TITLE" Validation and Replication results

You may want to consult [Unofficial Verification Guidance](https://social-science-data-editors.github.io/guidance/Verification_guidance.html) for additional tips and criteria.

SUMMARY
-------
Thank you for your response, and for providing additional code and explanations. 

All figures are replicated, all numbers are output.

Data description
----------------

The only identified data are the data from Joe and John (2019).
- Article is cited
- Supplementary data are cited in README.
- Modified data are provided.

### ICPSR data deposit


- [NOTE] openICPSR metadata is sufficient.



Data checks
-----------
Data is in CSV format. Columns are described in the README.


Code description
----------------
The input data used here are derived from Joe and John (2019), file is identified in README. Authors provide code to go from the original file to the file processed here.



Several Matlab programs are provided. README maps them to article sections and figures.

- clean_replication_data.m cleans the Joe and John (2019) data
- prettier_lines.m: used by main program
- figure1.m-figure4.m, figureA1.m, figureA2.m: generate all figures.


| Figure/Table #      | Program            | Line Number | Replicated?   |
|---------------------|--------------------|-------------|---------------|
| Figure 1            | figure1.m          |             | replicated    |
| Figure 2            | figure2.m          |             | replicated    |
| Figure 3            | figure3.m          |             | replicated    |
| Figure 4            | figure4.m          |             | replicated    |
| Appendix Figure A.1 | figureA1.m         |             | replicated    |
| Appendix Figure A.2 | figureA2.m         |             | replicated    |

| In-text numbers     | Program            | Line Number | Replicated?    |
|---------------------|--------------------|-------------|----------------|
| Page 18, line 5-7   | figure4.m |             | replicated    |
| Page 19, line 2     | figure4.m |             | replicated    |




Replication steps
-----------------

1. Downloaded code from openICPSR provided.
2. Ran main program
5. Inspected Workspace, Figure

Computing Environment
---------------------

- CISER Shared Windows Server 2016, 256GB, Intel Xeon E5-4669 v3 @ 2.10Ghz (3 processors)
- Matlab R2019a

Findings
--------

See above.

Classification
--------------


- [x] full replication
- [ ] full replication with minor issues
- [ ] partial replication (see above)
- [ ] not able to replicate most or all of the results (reasons see above)
