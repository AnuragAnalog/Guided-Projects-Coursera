# -*- coding: utf-8 -*-
# Adenine (A), Thymine (T), Cytosine (C), Guanine (G), Uracil (U)
# 
# DNA complementary base pairing rule
# A -> T
# C -> G
# G -> C
# T -> A

# RNA complementary base pairing rule
# A -> U
# C -> G
# G -> C
# T -> A

import tkinter
import tkinter.filedialog        
root = tkinter.Tk()
root.attributes('-alpha',0.3)
root.withdraw


temp_DNA = ''           # One line of Template DNA Sequence
comp_RNA = ''           # One line of Complementary RNA Sequence
covid_cDNA = ''         # Complete coronavirus cDNA
covid_RNA = ''          # Complete coronavirus RNA

#===== Retrive RNA from the cDNA Sequence =====================================
output_file = open('C:/Users/Administrator/Documents/covid_sequence.txt', 'w')

file_path = tkinter.filedialog.askopenfilename(parent=root)
root.destroy()

with open(file_path,'r') as input_data:
    header = input_data.readline().strip()    
    output_file.write(header + ' RNA sequence')
    for line in input_data:
        temp_DNA = line.strip()
        # Uncomment the following line to create a variable for the cDNA sequence
        # covid_cDNA = covid_cDNA + temp_DNA 
        comp_RNA = ""
        for base in temp_DNA:
            if base == "A":
                  comp_RNA = comp_RNA + 'U'
            elif base == "C":
                comp_RNA = comp_RNA + 'G'
            elif base == "G":
                comp_RNA = comp_RNA + 'C'
            elif base == "T":
                comp_RNA = comp_RNA + 'A'
            else:
                comp_RNA = comp_RNA + '?'
                
        covid_RNA = covid_RNA + comp_RNA
        output_file.write("\n" + comp_RNA)
        output_file.flush()
        #  Uncomment the print lines to see the data line by line
        # print(temp_DNA)        
        # print(comp_RNA)
        # print("===================================================")
        
input_data.close()
output_file.close()
#==============================================================================

