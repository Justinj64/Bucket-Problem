# Data backup task 
  (Tested on : Python 3.8.6)

## - Problem Definition
Buckets 1 and 2 contain backup of code and database respectively.  
Each file name contains the date it was backed up on.

Your task is to **delete** the files from these buckets that do not fit the below criteria.

Following files are to be kept and rest are to be deleted:
1. backups of last 5 days
2. backups of last 4 Saturdays
3. backups of last day of each month

Code should be scalable in nature i.e. addition of any new buckets should **not** require any changes to the core logic of the code

Note: You cannot create any new files in bucket1 and bucket2 folders.

An Object-Oriented Approach is expected in the solution.

## - Steps

- Inside the code you need to Edit the path where the .txt files reside.
- Execute the file with the command "python BackupCleaner.py"
