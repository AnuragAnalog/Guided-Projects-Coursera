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
reve_DNA = ''                               # Reverse DNA Sequence
comp_DNA = ''                               # Complementary DNA Sequence
reve_comp_DNA = ''                          # Reverse-Complement DNA Sequence

#===== a- Reverse DNA ========================================================
reve_DNA = temp_DNA[::-1]
print(temp_DNA)
print(reve_DNA)
#=============================================================================

#===== b- Complementary DNA Sequence =========================================
comp_DNA = ""                               # Make sure the comp_DNA is empty
# You need 'for' loob to read the template DNA sequenc and 'if'
# statments to add the complement base to the 'comp_DNA'
for i in temp_DNA:
    if i == "A":
        comp_DNA = comp_DNA + 'T'
    elif i == "C":
        comp_DNA = comp_DNA + 'G'
    elif i == "G":
        comp_DNA = comp_DNA + 'C'
    elif i == "T":
        comp_DNA = comp_DNA + 'A'
    else:
        comp_DNA = comp_DNA + '?'
print(temp_DNA)
print(comp_DNA)
# ============================================================================

# c- Reverse-Complement DNA Sequence =========================================
reve_comp_DNA = ""                          # Make sure reve_comp_DNA is empty
for base in temp_DNA:
    if base == "A":
        reve_comp_DNA = reve_comp_DNA + 'T'
    elif base == "C":
        reve_comp_DNA = reve_comp_DNA + 'G'
    elif base == "G":
        reve_comp_DNA = reve_comp_DNA + 'C'
    elif base == "T":
        reve_comp_DNA = reve_comp_DNA + 'A'
    else:
        reve_comp_DNA = reve_comp_DNA + '?'
print(temp_DNA)
print(reve_comp_DNA)
# ============================================================================