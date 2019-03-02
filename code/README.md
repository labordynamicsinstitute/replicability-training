---
title: "Obtaining lists of articles to replicate"
author: "Lars Vilhuber"
date: "3/1/2019"
output: 
  html_document: 
    keep_md: yes
---



## Sources
We have two sources:

- the existing list of articles to replicate on Google Sheets
- CrossRef, for new articles

We load relevant libraries here.


## Instructions
This file, when executed, will

- download the latest Replication list from Google Drive
- download DOI for all publications for a number of journals from CrossRef
- identify the ones that are new
- provide a CSV that can be manually uploaded

The program will check for prior files, and will NOT download new data if those files are present. Thus, to get a fresh run, 

- delete ` data/outputs/replication_list_DOI.Rds ` if you want to re-download the list of articles from Google Drive
- delete ` data/interwrk/new.Rds ` to re-download files from CrossRef

## Data locations

Permanent data is in

> data/outputs

and should be committed to the repository.

Temporary data is in

> data/interwrk

and can (should) be deleted after completion.

## Current list of DOI
We first obtain the current list of DOI. This is not failsafe - it assumes there *is* such a list.



```r
if (file.exists(repllist.file)) {
	print(paste0("File ",repllist.file," exists."))
} else	{
gs_auth()
# Extract Google Sheet Information Object
replication_list.gs <- gs_key(replication_list_KEY)

# Print worksheet names
gs_ws_ls(replication_list.gs)

# 
ws <- gs_ws_ls(replication_list.gs)
for (x in 1:length(ws)) {

  # Extract list and tidy
	tmp.ws <- gs_read(replication_list.gs,ws=x) %>% select(DOI)
	tmp.ws$worksheet <- ws[x]
	names(tmp.ws) <- sub("\\?","",names(tmp.ws))

	# Save
	saveRDS(tmp.ws,file = file.path(interwrk,paste0("replication_list_",x,".Rds")))

	# Pause so Google doesn't freak out
	Sys.sleep(10)
	rm(tmp.ws)

}
# End of else statement
} 
```

```
## [1] "File data/outputs/replication_list_DOI.Rds exists."
```

```r
# now we combine them, and clean them up
```



```r
# Compile all the worksheets except for "2009 missing online material"
if (file.exists(repllist.file)) {
	repllist <- readRDS(file = repllist.file)
} else {
repllist <- NA
for ( x in 1:length(ws) ) {
  if ( ws[x] != "2009 missing online material" ) {
    print(paste("Processing",ws[x]))
    if ( x == 1 ) {
      # Read in the first list and set variable types
      repllist <- readRDS(file = file.path(interwrk,paste0("replication_list_",x,".Rds")))
    } else {
      # Read in the subsequent lists and set variable types
      tmp <- readRDS(file = file.path(interwrk,paste0("replication_list_",x,".Rds")))

      # Add to master dataframe
      repllist <- bind_rows(repllist,tmp)
      rm(tmp)
    }
  }
}
saveRDS(repllist,file = repllist.file)
# end of else
}
uniques <- repllist %>% select(DOI) %>% distinct() %>% rename(doi = DOI)
```

- We read 1097 records on 2019-03-01.
- There are **846** unique records. 


```r
# Each journal has a ISSN
if (!file.exists(issns.file)) {
issns <- data.frame(matrix(ncol=3,nrow=5))
names(issns) <- c("journal","issn","lastdate")
tmp.date <- c("2016-01")
issns[1,] <- c("American Economic Journal: Applied Economics","1945-7790",tmp.date)
issns[2,] <- c("American Economic Journal: Economic Policy","1945-774X",tmp.date)
issns[3,] <- c("American Economic Journal: Macroeconomics", "1945-7715",tmp.date)
issns[4,] <- c("American Economic Journal: Microeconomics", "1945-7685",tmp.date)
issns[5,] <- c("American Economic Review","1944-7981",tmp.date)

saveRDS(issns, file= issns.file)
}

issns <- readRDS(file = issns.file)
```

Now read DOI for all later dates.

```r
if (!file.exists(issns.file)) {
	new.df <- NA
	for ( x in 1:nrow(issns) ) {
		new <- cr_journals(issn=issns[x,"issn"], works=TRUE,
				   filter=c(from_pub_date=issns[x,"lastdate"]),
				   select=c("DOI","title","published-print","volume","issue","container-title"),
				   limit= 500)
		if ( x == 1 ) {
      		new.df <- as.data.frame(new$data)  
    	} else {
      		new.df <- bind_rows(new.df,as.data.frame(new$data))
    	}
	}
	saveRDS(new.df, file= file.path(interwrk,paste0("new.Rds")))
}
new.df <- readRDS(file= file.path(interwrk,paste0("new.Rds")))
```

We read 580 records for 4 journals:


container.title                                 records
---------------------------------------------  --------
American Economic Journal: Applied Economics        149
American Economic Journal: Economic Policy          166
American Economic Journal: Macroeconomics           116
American Economic Journal: Microeconomics           149



Of these, 333 records for 4 journals were new:


container.title                                 records
---------------------------------------------  --------
American Economic Journal: Applied Economics         50
American Economic Journal: Economic Policy          166
American Economic Journal: Macroeconomics            54
American Economic Journal: Microeconomics            63

The new records can be found [here](data/outputs/addtl_doi.csv).


