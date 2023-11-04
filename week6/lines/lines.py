import sys


if len(sys.argv) < 2:
    sys.exit("Too few command-line arguments")
elif len(sys.argv) > 2:
    sys.exit("Too many command-line arguments")
elif sys.argv[1].find(".py") == -1:
    sys.exit("Not a Python file")
else:
    count = 0
    try:
        with open(f"{sys.argv[1]}") as file:
            for line in file:
                if line.lstrip().startswith("#"):
                    continue
                elif line.strip() == "":
                    continue
                else:
                    count += 1
    except FileNotFoundError:
        sys.exit("File does not exist")

print(count)