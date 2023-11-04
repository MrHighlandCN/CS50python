n = 50
while n > 0:
    print("Amount Due:", n)
    i = int(input("Insert Coin: "))
    if i != 5 and i != 10 and i != 25:
        continue
    else:
        n -= i
print("Change Owed:", abs(n))
