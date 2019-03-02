####################################
# global libraries used everywhere #
####################################

pkgTest <- function(x)
{
	if (!require(x,character.only = TRUE))
	{
		suppressPackageStartupMessages(install.packages(x,dep=TRUE))
		if(!require(x,character.only = TRUE)) stop("Package not found")
	}
	return("OK")
}

global.libraries <- c("dplyr","devtools","rprojroot","googlesheets","rcrossref")

results <- sapply(as.list(global.libraries), pkgTest)
