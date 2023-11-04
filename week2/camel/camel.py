s = input("camelCase: ")
res = ""
for i in s:
    if i.isupper():
        res += "_"
    res += i
res = res.lower()
print("snake_case:", res)
