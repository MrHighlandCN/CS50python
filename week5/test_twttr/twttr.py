def main():
    s = input("Input: ")
    s = shorten(s)
    print("Output:", s)


def shorten(s):
    n = len(s)
    i = 0
    while i < n:
        temp = s[i].lower()
        if temp == "u" or temp == "e" or temp == "o" or temp == "a" or temp == "i":
            s = s.replace(s[i], "", 1)
            n -= 1
        else:
            i += 1
    return s


if __name__ == "__main__":
    main()
