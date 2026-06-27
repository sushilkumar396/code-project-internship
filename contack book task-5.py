import json
import os

CONTACTS_FILE = "contacts.json"

def load_contacts():
    """Loads contacts from a JSON file, initializing an empty dictionary if missing."""
    if not os.path.exists(CONTACTS_FILE):
        return {}
    try:
        with open(CONTACTS_FILE, "r") as file:
            return json.load(file)
    except json.JSONDecodeError:
        return {}

def save_contacts(contacts):
    """Saves the active contacts dictionary state back to local storage."""
    with open(CONTACTS_FILE, "w") as file:
        json.dump(contacts, file, indent=4)

def add_contact(contacts):
    """Creates a new contact record using the phone number as a unique key identifier."""
    print("\n--- Add New Contact ---")
    name = input("Enter Name: ").strip()
    phone = input("Enter Phone Number: ").strip()
    
    if not name or not phone:
        print("Error: Name and Phone Number are required fields.")
        return

    if phone in contacts:
        print(f"A contact with phone number '{phone}' already exists under the name '{contacts[phone]['name']}'.")
        return

    email = input("Enter Email Address: ").strip()
    address = input("Enter Physical Address: ").strip()

    contacts[phone] = {
        "name": name,
        "email": email if email else "N/A",
        "address": address if address else "N/A"
    }
    save_contacts(contacts)
    print(f"Contact for '{name}' successfully saved!")

def view_contacts(contacts):
    """Displays a birds-eye overview index of names and phone numbers."""
    print("\n--- Contact List ---")
    if not contacts:
        print("Your contact book is currently empty.")
        return

    for index, (phone, details) in enumerate(contacts.items(), start=1):
        print(f"{index}. Name: {details['name']} | Phone: {phone}")

def search_contact(contacts):
    """Queries contacts across both partial name strings and phone fields."""
    print("\n--- Search Contacts ---")
    query = input("Enter Name or Phone Number to search: ").strip().lower()
    
    if not query:
        print("Search term cannot be empty.")
        return

    results_found = False
    for phone, details in contacts.items():
        if query in details['name'].lower() or query in phone:
            print(f"\nFound match:")
            print(f"Name: {details['name']}")
            print(f"Phone: {phone}")
            print(f"Email: {details['email']}")
            print(f"Address: {details['address']}")
            results_found = True
            
    if not results_found:
        print("No matching contacts found.")

def update_contact(contacts):
    """Modifies property fields of an existing user record safely."""
    print("\n--- Update Contact ---")
    phone = input("Enter the Phone Number of the contact to update: ").strip()

    if phone not in contacts:
        print("Contact not found.")
        return

    current = contacts[phone]
    print(f"\nModifying layout details for: {current['name']}")
    print("Press Enter without typing to keep current values.")

    new_name = input(f"New Name [{current['name']}]: ").strip()
    new_email = input(f"New Email [{current['email']}]: ").strip()
    new_address = input(f"New Address [{current['address']}]: ").strip()

    if new_name:
        current['name'] = new_name
    if new_email:
        current['email'] = new_email
    if new_address:
        current['address'] = new_address

    save_contacts(contacts)
    print("Contact record updated successfully!")

def delete_contact(contacts):
    """Removes a targeted address directory block profile mapping securely."""
    print("\n--- Delete Contact ---")
    phone = input("Enter the Phone Number of the contact to delete: ").strip()

    if phone in contacts:
        removed_name = contacts[phone]['name']
        del contacts[phone]
        save_contacts(contacts)
        print(f"Contact record for '{removed_name}' has been deleted.")
    else:
        print("Contact not found.")

def main():
    contacts = load_contacts()
    
    while True:
        print("\n===== SMART CONTACT BOOK =====")
        print("1. Add New Contact")
        print("2. View All Saved Contacts")
        print("3. Search Contact Profiles")
        print("4. Update Contact Record")
        print("5. Delete Contact Record")
        print("6. Save & Exit Program")
        
        choice = input("Select an option (1-6): ").strip()
        
        if choice == "1":
            add_contact(contacts)
        elif choice == "2":
            view_contacts(contacts)
        elif choice == "3":
            search_contact(contacts)
        elif choice == "4":
            update_contact(contacts)
        elif choice == "5":
            delete_contact(contacts)
        elif choice == "6":
            print("Closing address system book layout. Goodbye!")
            break
        else:
            print("Invalid system entry choice. Please pick from options 1 to 6.")

if __name__ == "__main__":
    main()
