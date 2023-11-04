import sys
import csv
from tabulate import tabulate

menu = []

if len(sys.argv) < 2:
    sys.exit("Too few command-line arguments")
elif len(sys.argv) > 2:
    sys.exit("Too many command-line arguments")
elif sys.argv[1].find(".csv") == -1:
    sys.exit("Not a CSV file")
else:
    try:
        with open(f"{sys.argv[1]}") as file:
            reader = csv.reader(file)
            for row in reader:
                menu.append(row)
    except FileNotFoundError:
        sys.exit("File does not exist")

print(tabulate(menu, headers="firstrow", tablefmt="grid"))
