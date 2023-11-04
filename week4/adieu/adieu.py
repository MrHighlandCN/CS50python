NameList = []
while True:
    try:
        s = input("Name: ")
        NameList.append(str(s))
    except EOFError:
        break
print()
print("Adieu, adieu, to ", end="")
if len(NameList) == 1:
    print(NameList[0])
elif len(NameList) == 2:
    print(f"{NameList[0]} and {NameList[1]}")
else:
    for i in NameList:
        if i == NameList[-1]:
            print(f"and {i}")
        else:
            print(f"{i}, ", end="")
