import re
import sys


def main():
    print(validate(input("IPv4 Address: ")))


def validate(ip):
    flag = "(([1-9]?[0-9])|(2[0-4][0-9])|(1[0-9]{2})|(25[0-5]))"
    matched = re.search(r"^" + flag + "\." + flag + "\." + flag + "\." + flag + "$", ip)
    if matched:
        return True
    else:
        return False


...


if __name__ == "__main__":
    main()
