import os

CONTACTS_FILE = 'contacts.txt'

def load_contacts():
    """Load contacts from a file into a dictionary."""
    contacts = {}
    if os.path.exists(CONTACTS_FILE):
        with open(CONTACTS_FILE, 'r') as file:
            for line in file:
                name, phone = line.strip().split(',', 1)
                contacts[name] = phone
    return contacts

def save_contacts(contacts):
    """Save contacts from the dictionary to a file."""
    with open(CONTACTS_FILE, 'w') as file:
        for name, phone in contacts.items():
            file.write(f'{name},{phone}\n')

def add_contact(contacts):
    """Add a new contact to the dictionary."""
    name = input("Enter contact name: ").strip()
    if name in contacts:
        print("Contact already exists.")
    else:
        phone = input("Enter contact phone number: ").strip()
        contacts[name] = phone
        save_contacts(contacts)
        print("Contact added successfully.")

def delete_contact(contacts):
    """Delete a contact from the dictionary."""
    name = input("Enter contact name to delete: ").strip()
    if name in contacts:
        del contacts[name]
        save_contacts(contacts)
        print("Contact deleted successfully.")
    else:
        print("Contact not found.")

def search_contact(contacts):
    """Search for a contact in the dictionary."""
    name = input("Enter contact name to search: ").strip()
    if name in contacts:
        print(f'Name: {name}, Phone: {contacts[name]}')
    else:
        print("Contact not found.")

def display_contacts(contacts):
    """Display all contacts."""
    if contacts:
        print("Contacts List:")
        for name, phone in contacts.items():
            print(f'Name: {name}, Phone: {phone}')
    else:
        print("No contacts found.")

def main():
    contacts = load_contacts()
    
    while True:
        print("\nContact Book Menu:")
        print("1. Add Contact")
        print("2. Delete Contact")
        print("3. Search Contact")
        print("4. Display All Contacts")
        print("5. Exit")
        
        choice = input("Enter your choice (1-5): ").strip()
        
        if choice == '1':
            add_contact(contacts)
        elif choice == '2':
            delete_contact(contacts)
        elif choice == '3':
            search_contact(contacts)
        elif choice == '4':
            display_contacts(contacts)
        elif choice == '5':
            print("Exiting Contact Book. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == '__main__':
    main()