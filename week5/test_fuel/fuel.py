import sys

def main():
    s = input("Fraction: ")
    percents = convert(s)
    print(gauge(percents))


def convert(s):
        try:
            x, y = s.split("/")
            x = int(x)
            y = int(y)
            if x > y and y != 0:
                raise ValueError
            elif y == 0:
                raise ZeroDivisionError
            res = float(x) / float(y)
            return res * 100.0
        except ValueError:
            raise ValueError()


def gauge(percents):
    if percents <= 1:
        return "E"
    elif percents >= 99:
        return "F"
    else:
        return f"{percents}%"


if __name__ == "__main__":
    main()
