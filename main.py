import random
import json

from gudsethu.gudsethu import fields,details,add,delete_details

def register():
    print("\n--- CREATE ACCOUNT ---")

    first_name = input("First Name: ").strip()
    last_name = input("Last Name: ").strip()
    username = input("Username: ").strip()
    password = input("Password: ").strip()
    phone = input("Phone Number: ").strip()
    email = input("Email ID: ").strip()

    verification_code = random.randint(100000, 999999)

    print(f"Your verification code is: {verification_code}")

    entered_code = input("Enter verification code: ")

    if entered_code == str(verification_code):
        user = {
            "first_name": first_name,
            "last_name": last_name,
            "username": username,
            "password": password,
            "phone": phone,
            "email": email,
            "verified": True
        }

        try:
            with open("users.json", "r") as file:
                users = json.load(file)
        except (FileNotFoundError, json.JSONDecodeError):
            users = []
        if any(u["username"] == username for u in users):
            print("Username already exists ❌")
            return
        users.append(user)

        with open("users.json", "w") as file:
            json.dump(users, file, indent=4)

        print("Account created successfully ✅")

    else:
        print("Invalid verification code ❌")

def login():
    print("\n--- LOGIN ---")

    username = input("Username: ").strip()
    password = input("Password: ").strip()

    try:
          with open("users.json", "r") as file:
            content = file.read().strip()
            users = json.loads(content) if content else []
    except (FileNotFoundError, json.JSONDecodeError):
        print("No accounts found. Please register first.")
        return None

    for user in users:
        if user["username"] == username and user["password"] == password:
            print("Login successful ✅")

            print(f"Welcome, {user['first_name']}!")
            return user

    print("Invalid username or password ❌")
    return None
def dashboard(user):
    while True:
        choice = input("\n1.Member\n2.Visitor\n3.Delete\n4.Exit\nChoice: ")

        if choice == "1":
            cat = input("Category (PG/Hostel/Rental/Hotel): ").strip()
            if cat in fields:
                add(cat)
                print("Added ✅")
            else:
                print("Invalid category ❌")

        elif choice == "2":
            cat, area, type, stay_fees__rent__price = input("Category(PG/Hostel/Rental/Hotel):").strip(), input("Area: ").strip(),input("Type(Boys👦 / Girls👧)").strip(),input("Rent/Stay_fees/Price:").strip()

            found = [x for x in details
                 if x.get("Category","").lower() == cat.lower()
                 and x.get("Area", "").lower() == area.lower()
                 and x.get("Type","").lower() == type.lower()
                 or str(x.get("Rent/Stay_fees/Price:")) == str(stay_fees__rent__price)]

            if found:
                for x in found:
                    print("\nAvailable details🫠\n")
                    print("\n".join(f"{k}:{v}" for k, v in x.items()
                                if k!="Category" and k!="Area" and k!="Type" and k!="Rent/Stay_fees/Price:"))
            else:
                print("Details are not available 👎")

        elif choice == "3":
            delete_details()

        elif choice == "4":
            print("Thank You 🙏")
            break

while True:
    print("\n--- 💐 WELCOME TO gudsethu 🌉🛖 ---")
    print("1. Register")
    print("2. Login")
    print("3. Logout")

    choice = input("Choice: ")

    if choice == "1":
        register()

    elif choice == "2":
        user=login()
        if user:
            dashboard(user)
    

    elif choice == "3":
        print("Logged out successfully✔️")
        break

    else:
        print("Invalid choice ❌")   
