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


temp_DNA = "ATGCCGCTAAACTGACATXXTCAGATC"    # Template DNA Sequence
temp_RNA = "AUGCCGCUAAACUGACAUXXUCAGAUC"    # use this sequence for the Revers    
reve_Sequence = ''                          # Reverse RNA Sequence
comp_RNA = ''                               # Complementary RNA Sequence
reve_comp_RNA = ''                          # Reverse-Complement RNA Sequence

#===== a- Reverse RNA Sequence ===============================================
# You need to write code here to reverse the RNA sequenc
reve_Sequence = temp_RNA[::-1]
print(temp_RNA)
print(reve_Sequence)
#=============================================================================

#===== b- Complementary RNA Sequence =========================================
comp_RNA = ""                               # Make sure the comp_RNA is empty
# You need 'for' loob to read the template DNA sequenc and 'if'
# statments to add the complement base to the 'comp_RNA'
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
print(temp_DNA)
print(comp_RNA)
# ============================================================================

# c- Reverse-Complement RNA Sequence =========================================
reve_comp_RNA = ""                          # Make sure reve_comp_RNA is empty
# Like the previous code but in reverse order.
for base in temp_DNA:
    if base == "A":
        reve_comp_RNA = reve_comp_RNA + 'T'
    elif base == "C":
        reve_comp_RNA = reve_comp_RNA + 'G'
    elif base == "G":
        reve_comp_RNA = reve_comp_RNA + 'C'
    elif base == "T":
        reve_comp_RNA = reve_comp_RNA + 'A'
    else:
        reve_comp_RNA = reve_comp_RNA + '?'
print(temp_DNA)
print(reve_comp_RNA)
# ============================================================================