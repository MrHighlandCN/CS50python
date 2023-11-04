def main():
    greeting = input("Greeting: ")
    value = value(greeting)
    print(f"${value}")


def value(greeting):
    greeting = greeting.strip().lower()
    if "hello" in greeting:
        return 0
    elif greeting.find("h") == 0:
        return 20
    else:
        return 100


if __name__ == "__main__":
    main()
