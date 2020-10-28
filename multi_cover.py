import os
import csv
import sys

# the name of the csv file with the job data
job_data_file = sys.argv[1]


def tex_lines(ident, inst, pos, group, people):
    """
    Returns the lines to be written into the tex input files.
    """
    
    return ['% {}.txt\n'.format(ident),
            '\def\institution{'+inst+'}\n',
            '\def\position{'+pos+'}\n',
            '\def\group{'+group+'}\n',
            '\def\people{'+people+'}\n']



with open(job_data_file+'.csv') as data:
    
    reader = csv.reader(data)
    rows = list(reader)
    
    # finding the indices with the appropriate data
    id_idx = rows[0].index('ID')
    inst_idx = rows[0].index('Institution')
    position_idx = rows[0].index('Position')
    group_idx = rows[0].index('Group')
    people_idx = rows[0].index('People')
    
    # reading each entry row of the data    
    for row in rows[1:]:
        
        lines = tex_lines(row[id_idx],
                          row[inst_idx],
                          row[position_idx],
                          row[group_idx],
                          row[people_idx])
        
        # writing the input files
        with open('cl_'+row[id_idx]+'.txt', 'w') as tex_file:
            tex_file.writelines(lines)
        
        # generating the pdfs
        os.system('pdflatex -jobname=cl_'+row[id_idx]+' cover_letter_xxxx.tex')
        # deleting the useless files
        os.system('rm *.log && rm *.aux')
