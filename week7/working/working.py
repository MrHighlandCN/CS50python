import re
import sys


def main():
    print(convert(input("Hours: ")))


def convert(s):
    hour = "([0-9]|1[0-2])(?::(0[0-9]|[1-5][0-9]))? (AM|PM)"
    matched = re.search(r"^" + hour + " to " + hour + "$", s)
    if matched:
        h1, m1, s1, h2, m2, s2 = matched.groups()
        h1 = int(h1)
        h2 = int(h2)
        if s1 == "PM" and h1 != 12:
            h1 = h1 + 12
        if s2 == "PM" and h2 != 12:
            h2 = h2 + 12
        if h1 == 12 and s1 == "AM":
            h1 = 0
        if m1 is None and m2 is None:
            str = f"{h1:02}:00 to {h2:02}:00"
        elif m1 is None and m2 is not None:
            str = f"{h1:02}:00 to {h2:02}:{m2}"
        elif m1 is not None and m2 is None:
            str = f"{h1:02}:{m1} to {h2:02}:00"
        else:
            str = f"{h1:02}:{m1} to {h2:02}:{m2}"
        return str
    else:
        sys.exit(ValueError)


if __name__ == "__main__":
    main()
