import json
a={
    "Name" : "Abhishek",
    "Designation": "CEO of Navgurukul",
    "Gender":"male",
    "Age": 29
    }
with open('text.json','w') as f:
    json.dump(a,f,indent=4)
js=json.dumps(a)
print(js)
print(type(js))
print(type(a))

