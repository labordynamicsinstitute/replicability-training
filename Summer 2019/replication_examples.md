# Examples of Replicable Articles: Good, Bad, and In the Middle

## A good example
**Article**: [10.1257/pol.20140215](https://bitbucket.org/aeaverification/aej-policy-10.1257-pol.20140215-atp44/src/master/)

**Why it is replicable**:
 + Thorough README, provides clear instructions for reproduction.
 + Code runs without errors.
 + Output is clearly labeled.

[Report](https://bitbucket.org/aeaverification/aej-policy-10.1257-pol.20140215-atp44/src/master/Replication%20Results/replication-template-1.1/REPLICATION.txt)

## A bad example
**Article**: [10.1257/pol.20150388](https://bitbucket.org/aeaverification/aej-policy-10.1257-pol.20150388/src/master/)

**Why it is ***not*** replicable**:
 + "Ran the file "regressions_AEJ.do" and ran into the error "command adjustrcspline_nograph is unrecognized". This command was not
available through stata or ssc, nor was I able to find it online. I tried the .ado files for adjustrcspline alone, but it seems
that the authors made their own specific command that they did not provide in the directory. I ran into a similar issue with 
"custominvlink". Their websites did not have the .ado files necessary."
 + "The third .do file "graph_gas_coal_gen" requires results from "regressions_AEJ" according to the readme and therefore the output 
from that file cannot be replicated."

[Report](https://bitbucket.org/aeaverification/aej-policy-10.1257-pol.20150388/src/master/POL2015-0388_data/replication.txt)

## An example in the middle
**Article**: [10.1257/pol.20140483](https://bitbucket.org/aeaverification/aej-pol-10.1257-pol.20140483-reh279/src/master/)

**Why it is in the middle**:
 + "For the .do file creating table 6, the .do file stopped unexpectedly when creating the fifth column."
 + "About half of the .do files have errors relating to variables not being found...the variables
were generated with other code, but that code was not included in the .do files they provided."

[Report](https://bitbucket.org/aeaverification/aej-pol-10.1257-pol.20140483-reh279/src/master/data/replication.txt)
