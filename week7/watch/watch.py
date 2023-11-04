import re
import sys


def main():
    print(parse(input("HTML: ")))


def parse(s):
    temp = "youtu.be"
    matched = re.search(r'"https?://(?:www\.)?youtube\.com/embed(/.+)"', s)
    if matched:
        return "https://" + temp + matched.group(1)
    else:
        return "None"


if __name__ == "__main__":
    main()
