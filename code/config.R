# ###########################
# CONFIG: define  and filenames for later reference
# ###########################

replication_list_KEY <- "1pLxxyg01L-UkNpBWgP2xCRe7hIuUNw6e9BnVIqcO76c"
repllist.file <- file.path(dataloc,paste0("replication_list_DOI.Rds"))
issns.file <- file.path(dataloc,paste0("issns.Rds"))
addtl.file <- file.path(dataloc,paste0("addtl_doi.csv"))

# you may need to change this
Sys.setenv(crossref_email = "ldi@cornell.edu")


