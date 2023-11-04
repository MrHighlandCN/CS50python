import sys
import csv

Info = []

if len(sys.argv) < 3:
    sys.exit("Too few command-line arguments")
elif len(sys.argv) > 3:
    sys.exit("Too many command-line arguments")
elif sys.argv[1].find(".csv") == -1:
    sys.exit(f"{sys.argv[1]} is not a csv file")
elif sys.argv[2].find(".csv") == -1:
    sys.exit(f"{sys.argv[2]} is not a csv file")
else:
    try:
        with open(f"{sys.argv[1]}") as file:
            reader = csv.DictReader(file)
            for row in reader:
                Last, First = row["name"].replace(" ", "").split(",")
                House = row["house"]
                Info.append({"LastName": Last, "FirstName": First, "House": House})
    except FileNotFoundError:
        sys.exit(f"Could not read {sys.argv[1]}")

with open(f"{sys.argv[2]}", "w") as file:
    fieldnames = ["first", "last", "house"]
    writer = csv.DictWriter(file, fieldnames=fieldnames)
    writer.writeheader()
    for info in Info:
        writer.writerow(
            {
                "first": info["FirstName"],
                "last": info["LastName"],
                "house": info["House"],
            }
        )
