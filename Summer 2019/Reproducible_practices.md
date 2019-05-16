# Reproducible practices

The analysis in a scientific article should be reproducible by others.

- [An introduction](https://labordynamicsinstitute.github.io/computing4economists/documents/basics_of_version_control.pdf)

# The TIER protocol
The TIER (Transparency in Economic Research) Protocol is one instantiation of good practices. Others have taught these same practices for years, without labeling or disseminating them. Thus you will find many examples of this, and many versions of this. But for illustration purposes, let's walk through the basic principles as explained by the TIER Protocol.

![TIER protocol](https://bucketeer-82911c16-8ccd-4854-b255-5b3ebba24d7c.s3.amazonaws.com/images/TIER-folder-illustration-v3.0.width-800.png)

There are a few key concepts. Good code and data management
- separates data and code ("Command files")
- separates _acquired data_ ("original data" in the TIER terminology) from _created data_ ("Analysis data")
- document _provenance_ - where does the acquired data come from, and possibly, where does the code come from

## A few subtleties
- Notice that this doesn't work with Excel - which does not have a separation between data and code
- Excel is not alone, a few other software packages (which you may encounter) are mostly or purely "point-and-click"

![stay away](https://upload.wikimedia.org/wikipedia/commons/thumb/a/a8/Creative-Tail-biohazard.svg/128px-Creative-Tail-biohazard.svg.png)

# A generic workflow

- [An example](https://github.com/ncrncornell/workflow-text/blob/master/text/ced2ar-workflow.pdf)
- [Data flow concept](https://github.com/labordynamicsinstitute/replicability-training/wiki/Data-flow)

**[ INPUT DATA ]  ---( Cleaning program )---> [ ANALYSIS DATA ]**

**[ ANALYSIS DATA ] ---( Analysis program )---> [ TABLES / FIGURES ]**

<div class="mermaid">
graph TD;
    subgraph Dataflow;
    A((Input data)) ==>  B[Cleaning programs];
    B ==> C((Analysis data));
    C ==> D[Analysis programs] 
    D ==> E((Outputs));
    end;
    B -.-> F(("Auxiliary data<br/>(created)"));
    F -.-> C;
    
</div>


## Making it reproducible
- the data and its source  should clearly identified
  - URL or DOI
  - Citation
- Each table or figure should be attributable to a specific program
  - Need not be one-to-one
  - Should be clearly identified within the program output
     - Great: one output file per table/figure
     - Good: labels within the log file
     - Bad: no identification other than in the README
- Dependencies need to be identified
  - Many scientists re-use other people's code = packages
  - Popular for Stata:  [Statistical Software Components (SSC)](https://www.stata.com/support/ssc-installation/) or [Stata Journal](https://www.stata-journal.com/)
  - Popular for R: [Comprehensive R Archive Network (CRAN)](https://cran.r-project.org/)
  - Increasingly popular for all of the above: Github
  - Such packages need to be identified, and should be cited.
