import re
import sys


def main():
    print(count(input("Text: ")))


def count(s):
    s = s.lower()
    str = re.findall(r"\bum\b", s)
    return len(str)


if __name__ == "__main__":
    main()
