import json

dictionary ={
    "name" : "sathiyajith",
    "rollno" : 56,
    "cgpa" : 8.6, 
    "phonenumber" : "9976770500"
}
print(type(dictionary))

with open("first.json","w") as f:
    json_object = json.dump(dictionary,f,indent=4)
    print(type(json_object))


with open("first.json","r") as f:
    j=json.load(f)
    print(j)
    print(type(j))


