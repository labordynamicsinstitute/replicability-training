# Basics of Git

+ [General resources](https://try.github.io/)
+ [Git tutorial](https://guides.github.com/introduction/git-handbook/)

## Excerpt: Quick Overview

### Why a version control system?
You can review  history of code or text to find out:

+ _Which changes were made?_ Identify the lines that have been changed.
+ _Who made the changes?_ If multiple people work on a project, who made the particular change. Also tabulate contributions to the project by person.
+ _When were the changes made?_
+ _Why were changes needed?_ The ability to attach _log messages_ provides a lot of information.

### What's a repository?

A _repository = Git project_ is a  collection of files and folders, along with each file's revision history. There are
+ _commits_: collections of additions or modifications, a snapshot
+ _branches_: versions or variants of the main repository
+ _clones_: Each copy of the repository is complete - fully functional
+ _staging area_: an area on your computer where files and changes are collected prior to finalizing a _commit_

### What is Github or Bitbucket?
There are multiple services that host repositories, and that can serve as a central reference point for these repositories.
+ You _push_ to another repository - that could be on your buddy's computer, to a central entity (Github, Bitbucket) - however it is defined.
+ You _pull_ changes from another repository.
+ A _pull_ + _push_ is sometimes referred to as a _sync_ (synchronisation)

### Basic Git Commands
(also see the [Cheatsheet for Git](https://www.atlassian.com/git/tutorials/atlassian-git-cheatsheet))

+ `git clone` creates a local copy of a project that already exists remotely. The clone includes all the project's files, history, and branches.

+ `git add` stages a change. Git tracks changes to a working copy, but it's necessary to stage and take a snapshot of the changes to include them in the project’s history. This command performs _staging_, the first part of that two-step process. Any changes that are staged will become a part of the next snapshot and a part of the project's history.

+ `git commit` saves the snapshot to the project history and completes the change-tracking process. In short, a commit functions like taking a photo. Anything that's been staged with `git add` will become a part of the snapshot with `git commit`.

+ `git status` shows the status of changes as untracked, modified, or staged.

+ ` git pull` updates the local line of development with updates from its remote counterpart. You use this command if a teammate has made commits to a branch on a remote, and they would like to reflect those changes in their local environment. Or you made a commit on your laptop, and now want to continue the work on a remote desktop server.

+ `git push` updates the remote repository with any commits made locally to a branch. Think of it as publishing your changes.

### Taking it live

+ [Example slides](https://labordynamicsinstitute.github.io/computing4economists/Git_CL_Slides/Slides_Git_Example.pdf)
+ Let's go and do it ourselves (20 minutes)
