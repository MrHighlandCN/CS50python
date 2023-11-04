def main():
    percents = round(get_percents())
    if percents <= 1:
        print("E")
    elif percents >= 99:
        print("F")
    else:
        print(f"{percents}%")


def get_percents():
    while True:
        try:
            x, y = input("Fraction: ").split("/")
            x = int(x)
            y = int(y)
            if x > y:
                continue
            res = float(x) / float(y)
            return res * 100.0
        except ValueError:
            pass
        except ZeroDivisionError:
            pass


main()
