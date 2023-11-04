import json
import requests
import sys

if len(sys.argv) == 1:
    sys.exit("Missing command-line argument")
elif len(sys.argv) == 2:
    try:
        f = float(sys.argv[1])
    except ValueError:
        sys.exit("Command-line argument is not a number")
try:
    response = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
except requests.RequestException:
    sys.exit()

o = response.json()
rate = float(o["bpi"]["USD"]["rate"].replace(",", ""))
result = f * rate
print(f"${result:,.4f}")
