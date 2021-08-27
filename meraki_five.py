import json
def com(a):
    if "i" in a:
        return complex(a["real"],b["img"])
    return a
b=json.loads('{"i":true, "real":4,"img":5}')
print(com(b))