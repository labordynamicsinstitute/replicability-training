# Draft instructions for running reproducibility check on Codespaces

## Start an environment on Github Codespaces

- Go to [https://github.com/labordynamicsinstitute/codespaces-stata-skeleton](https://github.com/labordynamicsinstitute/codespaces-stata-skeleton) and select "Code -> Codespaces -> Start new"
- When you have one running, you can re-use the previous one.

Alternate:

- Go to [https://github.com/codespaces] and select `labordynamicsinstitute/codespaces-stata-skeleton` from the dropdown menu. 

If neither of those options appear, contact the LDI Lab Administrator.

## Connect to local VS Code (optional but useful)

- Click on the green `Codespaces` button on the bottom left, choose "Open in VS Code" from menu that appears at top center.
- This will open a local VS Code instance with the same content. Your main window in the browser may or may not stay open.

## Processing cases

- Open a terminal (top menu, Terminal, New Terminal, or shortcut `shift-ctrl-\``.
- `cd ..` to be in `/workspaces`
- You can clone a Bitbucket case as usual. 
  - special command available: `aeagit [NNNN] http` where `[NNN]` is the `AEAREP-NNNN` number. The command should open a new VS Code instance, with the cloned repository in the file pane.
- All command line git functions should work, as should command line Stata.


## Administrator instructions

In order to enable a replicator to use this repository for Codespaces, they must be "collaborators". Apparently, that requires write access (to be verified).
