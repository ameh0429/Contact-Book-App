contact_book = {}

print("Welcome to the Contact Book App!")

while True:
    print("\nSimple Contact Book Menu:")
    print("1. Add a new contact")
    print("2. Look up a contact")
    print("3. List all contacts")
    print("4. Delete a contact")
    print("5. Exit")

    choice = input("Please enter your choice (1-5): ")

    if choice == "1":
        name =input("Enter the name of the contact: ")
        phone_number = input("Enter the phone number of the contact: ")
        contact_book[name] = phone_number
        print(f"Name and Phone number added successfully!")

    elif choice == "2":
        contact_name = input("Enter the name of the contact you want to look up: ")
        if contact_name in contact_book:
            print(f"{contact_name}: {contact_book[contact_name]}")
        else:
            print("Contact does not exist!")

    elif choice == "3":       
        if len(contact_book) == 0:
            print("Contact book is empty! Please add contact")
        else:
            print("Contacts in your contact_book:")
            for contact, value in contact_book.items():
                print(f"{contact}: {value}")

    elif choice == "4":
        if len(contact_book) == 0:
            print("Contact book is empty! Please add contact")
        else:
            print("Contacts in your contact_book:")
            for contact, value in contact_book.items():
                print(f"{contact}: {value}")
            delete_contact = input("Enter a name to delete from the contact book: ")
            if delete_contact in contact_book:
                del contact_book[delete_contact]
                print(f"{delete_contact} has been deleted successfully!")
            else:
                print("Contact not found!")
                
    elif choice == "5":
        print("Existing Contact Book App! Goodbye!")
        break
    else:
        print("Invalid choice! Try again!")
                
               
            
