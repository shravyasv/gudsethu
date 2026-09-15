import json
print("--- 💐 WELCOME TO gudsethu 🌉🛖 ---")
try:
    with open("details.json","r")as file:
        details = json.load(file)
except FileNotFoundError:
    details = []

fields = {
    "PG": ["Name","Type", "Rent", "Deposit", "Timings", "Food", "Owner", "Address", "Area", "Contact"],
    "Hostel": ["Name","Type", "Stay Fees", "Mess Fees", "Deposit", "Timings", "Food", "Owner", "Warden", "Address", "Area", "Contact"],
    "Rental": ["Name","Type", "Rent", "Deposit", "Timings", "Owner", "Address", "Area", "Contact"],
    "Hotel": ["Name","Type", "Price", "Advance", "Address", "Area", "Contact"]
}

def add(category):
    d = {"Category": category}
    d.update({f: input(f"{f}: ") for f in fields[category]})
    details.append(d)
    with open("details.json","w") as file:
        json.dump(details,file,indent=4)
def delete_details():
    if not details:
        print("No stored details found.")
        return

    print("\n--- Stored Details ---")
    for i, x in enumerate(details, start=1):
        print(f"{i}. {x.get('Category')} - {x.get('Name')} - {x.get('Area')} - {x.get('Type')} - {x.get('Rent')}")

    try:
        num = int(input("\nEnter the number to delete: "))

        if 1 <= num <= len(details):
            removed = details.pop(num - 1)

            with open("details.json", "w") as file:
                json.dump(details, file, indent=4)

            print(f"Deleted: {removed.get('Name')} ✅")
        else:
            print("Invalid number ❌")

    except ValueError:
        print("Please enter a valid number.")
