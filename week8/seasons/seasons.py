from datetime import date
import sys
import inflect
import operator


p = inflect.engine()


def main():
    try:
        temp = input("Date of Birth: ")
        deltaDate = operator.sub(date.today(), date.fromisoformat(temp))
        print(convert(deltaDate.days))
    except ValueError:
        sys.exit("Invalid date")


def convert(time):
    minutes = time * 24 * 60
    res = p.number_to_words(minutes, andword="").capitalize()
    return f"{res} minutes"


if __name__ == "__main__":
    main()
