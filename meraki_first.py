import json
a = '{"Name":"Ram", "Class":"true", "Age":9 }'
b = json.loads(a)
print(b)
print(type(b))
print(type(a))
    
