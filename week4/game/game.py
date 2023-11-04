import random

while True:
    try:
        level = int(input("Level: "))
        if level > 0:
            break
    except ValueError:
        pass

res = random.randint(1, level)

while True:
    try:
        n = int(input("Guess: "))
        if n < 1:
            continue
    except ValueError:
        continue

    if n == res:
        print("Just right!")
        break
    elif n < res:
        print("Too small!")
    else:
        print("Too large!")
