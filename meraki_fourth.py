# import json
# a={
#     '4': 5, 
#     '6': 7, 
#     '1': 3, 
#     '2': 4
#     }
# b=(json.dumps(a,sort_keys=True,indent=4))
# print(b)
# print(type(b))




                # OR

import json
a={
    '4': 5, 
    '6': 7, 
    '1': 3, 
    '2': 4
    }
b=list(a)
b.sort()
dic={}
for i in b:
    dic[i]=a[i]
dic=json.dumps(dic,indent=4)
print(dic)