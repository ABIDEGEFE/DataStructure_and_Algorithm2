# we can use 'find' utility to find files and directories starting from specfic path
# combining with -exec opition we can apply commands on the found items
# we can also find based on name, type, size, modification and accessed time etc.

find / -type f -name "fileName" -exec rm {} \;
# above command will find and remove all files named "fileName" starting from root directory
# {} is a placeholder for the found file, \; indicates the end of the command to be executed
# we can also use wildcards in the name to match specific patterns

find / -type d -name *esk*p -exec touch {}/newfile.txt \;
# above command will find all directories with names containing "esk" starting from root directory
# and create a new empty file named newfile.txt inside each of those directories
# the pattern may find "desk", "esky", "desktop" etc.

find / -type f -size +100M -exec mv {} /path/to/large_files/ \;
# above command will find all files larger than 100 megabytes starting from root directory
# and move them to /path/to/large_files/ directory
# +100M indicates files larger than 100 megabytes

find / -type f -mtime +30 -exec rm {} \;
# above command will find all files modified more than 30 days ago starting from root directory
# and remove them
# +30 indicates files modified more than 30 days ago
# we can also use -atime for accessed time and -ctime for changed time
# we can use - to indicate less than specified days, e.g., -30 for less than 30 days

find / -type f -cmin -60 -and -size -10M -exec cp {} /path/to/recent_small_files/ \;
# above command will find all files changed within the last 60 minutes and smaller than 10 megabytes
# starting from root directory and copy them to /path/to/recent_small_files/ directory
# -cmin -60 indicates files changed within the last 60 minutes
# -size -10M indicates files smaller than 10 megabytes
# -and is used to combine multiple conditions