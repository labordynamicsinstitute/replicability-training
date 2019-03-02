# ###########################
# CONFIG: define paths and filenames for later reference
# ###########################

# Change the basepath depending on your system

basepath <- rprojroot::find_root(rprojroot::has_file("pathconfig.R"))
setwd(basepath)

# Main directories
interwrk <- file.path("data","interwrk")
dataloc <- file.path("data","outputs")


programs <- file.path(basepath)

for ( dir in list(interwrk,dataloc)){
	if (file.exists(dir)){
	} else {
	dir.create(file.path(dir),recursive = TRUE)
	}
}
