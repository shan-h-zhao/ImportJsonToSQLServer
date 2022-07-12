# ImportJsonToSQLServer

## Purpose: Import json into sql server databases
## 5 steps:
### (1) python step1Concat.py
This script loops through the subdirectories to concatinate all .gz files into one .gz file, separately by days.
This works for upper level directories too (meaning, concatenating all .gz by months), but the file is too large for the memory to handle
### (2) unzip the .gz
Unzip the .gz file. Add .json to the end of the unzipped file.
### (3) python step2AddComma.py
This scrip loops through all lines in a .json to add a comma (,) at the end of each line, except for the last line. Also add square brackets to the beginning and end of the file. The processed .json file can be used for importing to sql server.
### (4) run the step3ImportJson.sql in sql server
This scrip creates a sql server db table for importing from the .json. Deals with nested json structures.
### (5) union the tables into one in sql server
