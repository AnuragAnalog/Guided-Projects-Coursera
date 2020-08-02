# -*- coding: utf-8 -*-


temp_DNA = "ATGCCGCTAAACTGACATXXTCAGATC"
# temp_DNA[start:stop:step]
temp_DNA[0:9:1] 
temp_DNA[0:9] 


temp_DNA[27:0:-1]
temp_DNA[27:-1:-1]
temp_DNA[27::-1]
temp_DNA[::-1]

print(len(temp_DNA))

temp_DNA[len(temp_DNA):16:-1]
temp_DNA[len(temp_DNA)-10:len(temp_DNA):1]


temp_DNA[0]
temp_DNA[2]

# We cannot change the string
temp_DNA[2] = 'C'

'T' + 'h' + 'e' + ' ' + 'E' + 'n' + 'd' 
'The ' + 'End ' + 'of ' + 'task ' + '5'
