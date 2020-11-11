# multi_cover
A quick script to write multiple personalized Cover Letters in pdf

Written by Manuel A. Buen-Abad, 2020

Requirements
-----------------------------------------

1. Python
2. pdflatex
3. A CSV file containing the following information about the job positions you are applying to:  
  3.1 the first line being: #,ID,Institution,Position,Group,People,  
  3.2 the next lines being the number, some identifier, the name of the institution, a one sentence description of the position, the group in the institution with which you want to work or collaborate, and the PI/Boss/Head of Department to which the letter is addressed.  

How to run
-----------------------------------------

In the terminal, simply do:

	$ python multi_cover.py your_job_data_file

without the csv preffix.
