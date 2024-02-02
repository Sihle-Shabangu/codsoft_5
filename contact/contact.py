import csv
from tabulate import tabulate
from pyfiglet import Figlet


def main():
    print_title("Contact Book")
    while True:
        print("\n1. Add Contact\n2. View Contact List\n3. Search Contact\n4. Update Contact\n5. Delete Contact\n6. Exit")
        choice = input("Enter your choice (1-6): ")

        if choice == "1":
            add_contact()
        elif choice == "2":
            view_contact_list()
        elif choice == "3":
            search_contact()
        elif choice == "4":
            update_contact()
        elif choice == "5":
            delete_contact()
        elif choice == "6":
            print("Exiting the Contact Book. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 6.")


def add_contact():
    name = input("Enter full name: ")
    number = input("Enter phone number: ")
    email = input("Enter email address: ")
    address = input("Enter physical address: ")

    with open("contact.csv", "a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([name, number, email, address])
    print("Contact added successfully!")


def view_contact_list():
    with open("contact.csv", "r") as file:
        reader = csv.DictReader(file)
        contacts = list(reader)
    if contacts:
        print(tabulate(contacts, headers="keys", tablefmt="grid"))
    else:
        print("No contacts available.")


def search_contact():
    search_term = input("Enter name or phone number to search: ")
    with open("contact.csv", "r") as file:
        reader = csv.reader(file)
        contacts = [row for row in reader if any(search_term.lower() in field.lower() for field in row)]
    if contacts:
        headers = ["Full Name", "Phone Number", "Email", "Physical Address"]
        print(tabulate(contacts, headers=headers, tablefmt="grid"))
    else:
        print("No matching contacts found.")


def update_contact():
    name_to_update = input("Enter the full name of the contact to update: ")
    with open("contact.csv", "r") as file:
        reader = csv.reader(file)
        contacts = [row for row in reader]
    updated_contacts = []
    for contact in contacts:
        if name_to_update.lower() in contact[0].lower():
            new_number = input(f"Enter new phone number for {contact[0]}: ")
            contact[1] = new_number
            print("Contact updated successfully!")
        updated_contacts.append(contact)
    with open("contact.csv", "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerows(updated_contacts)


def delete_contact():
    name_to_delete = input("Enter the full name of the contact to delete: ")
    with open("contact.csv", "r") as file:
        reader = csv.reader(file)
        contacts = [row for row in reader]
    remaining_contacts = [contact for contact in contacts if name_to_delete.lower() not in contact[0].lower()]
    with open("contact.csv", "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerows(remaining_contacts)
    print("Contact deleted successfully!")


def print_title(title_text):
    custom_fig = Figlet()
    print(custom_fig.renderText(title_text))


if __name__ == "__main__":
    main()