month = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December",
]

while True:
    try:
        date = input("Date: ").strip()
        if "/" in date:
            m, d, y = date.split("/")
            if m in month:
                continue
        elif "," in date:
            date = date.replace(",", "")
            m, d, y = date.split(" ")
        else:
            continue
        d = int(d)
        y = int(y)
        if m in month:
            m = month.index(m) + 1
        else:
            m = int(m)
        if 0 < m <= 12 and 0 < d <= 31:
            break
    except ValueError:
        pass

print(f"{y}-{m:02}-{d:02}")
