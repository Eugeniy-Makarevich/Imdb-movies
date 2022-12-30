# script to split box_office columns by budget,gross,opening weekend gross

import re
key_words = ['Budget','Cumulative', 'Opening'] 
col_names= ['Budget','Gross','Opening weekend']
for index,word in enumerate(key_words):
    regex =".*'"+word+".*?': '([\S]+[0-9]+,[\S]+[0-9])"
    dataset[col_names[index]] = [re.findall(regex, row) if isinstance(row,str) 
                                 else None for row in dataset['box office'] ] 

