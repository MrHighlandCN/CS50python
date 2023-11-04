GList = {}

while True:
    try:
        item = input().upper()
        if item in GList:
            GList[item] += 1
        else:
            GList.update({item: 1})
    except EOFError:
        break
    except KeyError:
        pass
GList = sorted(GList.items())
for item, count in GList:
    print(f"{count} {item}")
