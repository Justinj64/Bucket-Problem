# Data backup task 
(Tested on : Python 3.8.6)

## - Problem Definition
Buckets 1 and 2 contain backup of code and database respectively.  
Each file name contains the date it was backed up on.

The task is to **delete** the files from these buckets that do not fit the below criteria.

Following files are to be kept and rest are to be deleted:
1. backups of last 5 days
2. backups of last 4 Saturdays
3. backups of last day of each month

## - Steps

- In the code you need to edit the path where the .txt files(buckets) reside.
- Execute the file with the command "python BackupCleaner.py"
