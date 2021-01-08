# AERI-2019-xxxx.R2 "PAPER TITLE" Validation and Replication results

You may want to consult [Unofficial Verification Guidance](https://social-science-data-editors.github.io/guidance/Verification_guidance.html) for additional tips and criteria.

SUMMARY
-------
This is a very small data and code supplement. However, as per AEA policy, we do request that code for simulations (Figures 1-3) be provided. There are also concerns about the data used for Figure 4.

- [SUGGESTED] Please add  citations of the supplementary data used to the article. Guidance on how to cite supplementary data is provided in the [AEA Sample References](https://www.aeaweb.org/journals/policies/sample-references) - see third example.

- [REQUIRED] Please provide complete code, including for appendix tables and figures, and identify source for inline numbers.

- [REQUIRED] The author should provide Matlab programs that take a particular file from Joe and John (2019) and construct the input data for this article. Alternatively, the author should provide an explanation why the data differ.

Details in the full report.

Data description
----------------

The only identified data are the data from Joe and John (2019).
- Article is cited
- Supplementary data are not separately cited - see citation guidance. URL to article landing page is provided in footnote.
- Modified data are provided.

> [SUGGESTED] Please add  citations of the supplementary data used to the article. Guidance on how to cite supplementary data is provided in the [AEA Sample References](https://www.aeaweb.org/journals/policies/sample-references) - see third example.



### ICPSR data deposit


- [NOTE] openICPSR metadata is sufficient.



Data checks
-----------
Data is in CSV format. The README provides sparse  documentation as to what the columns mean is provided. the code also reveals

```
z1 = data(:,1);
n1 = data(:,2);
z2 = data(:,3);
n2 = data(:,4);
```

Code description
----------------
The input data used here are derived from Joe and John (2019), but the data do not correspond to a particular file in the cited work. No transformation program is provided. There seem to be minor discrepancies. For instance, data downloaded from Joe and John (2019) show the following values (z1, n1, z2, n2) for studies 3, 4, 6, 7:

| Study | Obs1 | z-statistic1 | Obs2 | z-statistic2 |
|-------|------|--------------|------|--------------|
| 3     | 216  | **2.722**    | 360  | 3.25         |
| 4     | 162  | 2.559        | 264  | 2.995        |
| 6     | 158  |              | 156  | 7.714        |
| 7     | 54   | **-2.449**       | 96   | 0.42         |

Matching these by (Obs1, Obs2) to the data provided by the author (which does not contain study identifiers) shows

| z1          | Obs1| z2           | Obs2|
|-------------|-----|--------------|-----|
| **2.696**844261 | 216 | 3.290526731  | 360 |
| 2.575829304 | 162 | 2.967737925  | 264 |
| 3.290526731 | 158 | 7.713801329  | 156 |
| **2.575**829304 | 54  | -0.42066462  | 96  |

(We've highlighted two discrepancies, but none of the values match exactly, and some differ substantially).

> [REQUIRED] The author should provide Matlab programs that take a particular file from Joe and John (2019) and construct the input data for this article. Alternatively, the author should provide an explanation why the data differ.

Two Matlab programs are provided. README maps them to article sections and figures.

- line_fewer_markers.m: used by main program
- main_program.m: main program for Figure 4

No code is provided for the simulations in Figures 1-3, nor for the alternate analysis in the online appendix.

| Figure/Table #      | Program            | Line Number | Replicated?    |
|---------------------|--------------------|-------------|----------------|
| Figure 1            | not provided       |             | not replicated |
| Figure 2            | not provided       |             | not replicated |
| Figure 3            | not provided       |             | not replicated |
| Figure 4            | main_program.m |             | replicated     |
| Appendix Figure A.1 | not provided       |             | not replicated |
| Appendix Figure A.2 | not provided       |             | not replicated |

| In-text numbers     | Program            | Line Number | Replicated?    |
|---------------------|--------------------|-------------|----------------|
| Page 18, line 5-7   | main_program.m |             | not replicated |
| Page 19, line 2     | main_program.m |             | not replicated |

> NOTE: In-text numbers that reference numbers in tables do not need to be listed. Only in-text numbers that correspond to no table or figure need to be listed.

> NOTE: the in-text numbers are not specifically identified in either code or README.

> [REQUIRED] Please provide complete code, including for appendix tables and figures, and identify source for inline numbers.


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

### Figures


| Figure/Table #      | Program            | Line Number | Replicated?    |
|---------------------|--------------------|-------------|----------------|
| Figure 1            | not provided       |             | not replicated |
| Figure 2            | not provided       |             | not replicated |
| Figure 3            | not provided       |             | not replicated |
| Figure 4            | main_program.m |             | replicated     |
| Appendix Figure A.1 | not provided       |             | not replicated |
| Appendix Figure A.2 | not provided       |             | not replicated |


### In-Text Numbers
> INSTRUCTIONS: list page and line number of in-text numbers. If ambiguous, cite the surrounding text, i.e., "the rate fell to 52% of all jobs: verified".

[ ] There are no in-text numbers, or all in-text numbers stem from tables and figures.

[x] There are in-text numbers, but they are not identified in the code

| In-text numbers     | Program            | Line Number | Replicated?    |
|---------------------|--------------------|-------------|----------------|
| Page 18, line 5-7   | main_program.m |             |  replicated    |
| Page 19, line 2     | main_program.m |             |  replicated    |


Classification
--------------


- [ ] full replication
- [ ] full replication with minor issues
- [x] partial replication (see above)
- [ ] not able to replicate most or all of the results (reasons see above)
