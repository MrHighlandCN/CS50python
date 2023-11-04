from validator_collection import validators

email = input("What's your email address? ")

try:
    email_address = validators.email(email)
    print("Valid")
except ValueError:
    print("Invalid")
