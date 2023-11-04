import random


def main():
    level = get_level()
    score = 0
    for _ in range(10):
        x = generate_integer(level)
        y = generate_integer(level)
        res = x + y
        for i in range(3):
            try:
                ans = int(input(f"{x} + {y} = "))
                if ans == res:
                    score += 1
                    break
                elif i == 2:
                    print("EEE")
                    print(f"{x} + {y} = {res}")
                else:
                    print("EEE")
            except ValueError:
                print("EEE")
                pass
    print("Score:", score)


def get_level():
    while True:
        try:
            level = int(input("Level: "))
            if level != 1 and level != 2 and level != 3:
                continue
            else:
                return level
        except ValueError:
            pass


def generate_integer(level):
    match level:
        case 1:
            return random.randint(0, 9)
        case 2:
            return random.randint(10, 99)
        case 3:
            return random.randint(100, 999)


if __name__ == "__main__":
    main()
