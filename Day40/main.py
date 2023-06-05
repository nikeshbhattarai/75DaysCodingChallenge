import requests

SHEETY_API = "https://api.sheety.co/75327416cb3e93bd5260e25a6055c289"

print(
    "Welcome to Angela's Flight Club.\n"
    "We find the best flight deals and email you."
    )
first_name = input("What is your first name?\n")
last_name = input("What is your last name?\n")
email = input("What is your email?\n")
re_check_email = input("Type your email again.\n")

if email == re_check_email:
    print("You're in the club!")
    parameters = {
        "user": {
            "firstName": first_name,
            "lastName": last_name,
            "email": email
        }
    }
    response = requests.post(url=f"{SHEETY_API}/flightDeals/users", json=parameters)
    print(response.text)
else:
    print("Sorry the email didnot match retype your email.")
