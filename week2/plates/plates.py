def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    if len(s) > 6 or len(s) < 2:
        return False
    firstNum = ""
    letCount = 0
    speChar = False
    for i in range(len(s)):
        if s[i] >= "A" and s[i] <= "Z":
            if firstNum != "":
                return False
            else:
                letCount += 1
        elif s[i] >= "0" and s[i] <= "9" and firstNum == "":
            firstNum = s[i]
        elif s[i] >= "0" and s[i] <= "9":
            continue
        else:
            speChar = True
    if speChar == True or firstNum == "0" or letCount < 2:
        return False
    elif firstNum != "" and s[len(s) - 1] >= "A" and s[len(s) - 1] <= "Z":
        return False
    else:
        return True


main()
