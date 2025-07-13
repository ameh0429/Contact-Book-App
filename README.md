# Contact-Book-App

## Project Overview
This is a console-based application that allows users to manage a basic contact list. It leverages Python's dictionary data structure to store contact names and their corresponding phone numbers. The application provides a menu-driven interface for adding new contacts, looking up existing ones, listing all stored contacts, and deleting contacts.

## Features
- **Add Contact**: Allows users to input a contact's name and phone number, which are then stored in the contact book.
- **Look Up Contact**: Users can search for a contact by name, and if found, the application displays their phone number. It handles cases where the contact does not exist.
- **List All Contacts**: Displays all stored contact names and their phone numbers in an easy-to-read format. It also informs the user if the contact book is empty.
- **Delete Contact**: Provides the ability to remove an existing contact from the book by name. It includes checks for an empty book and for contacts not found.
- **Menu-Driven Interface**: Guides the user through options with clear prompts.
- **Continuous Operation**: Runs in a loop, allowing multiple operations until the user chooses to exit.

## How to Use
### Prerequisites
- Python 3.x installed on your system.

### Running the Application
- **Save the code**: Save the provided Python code into a file named `contact_book.py` (or any other `.py` extension).
- **Open a terminal/command prompt**: Navigate to the directory where you saved `contact_book.py`.
- **Run the script**: Execute the command:

```
python contact_book.py
```
### Interacting with the App
Upon running, you will see the main menu:

```
--- Simple Contact Book Menu ---
1. Add a new contact
2. Look up a contact
3. List all contacts
4. Delete a contact
5. Exit
Enter your choice (1-5):
```
 
- **To Add a New Contact (Option 1):**
 - Enter `1 `and press Enter.
 - Follow the prompts to enter the contact's name and phone number.
 - A confirmation message will be displayed.
- **To Look Up a Contact (Option 2):**
 - Enter `2 `and press Enter.
 - Enter the name of the contact you wish to find.
 - The app will display the contact's phone number or indicate if the contact is not found.
- **To List All Contacts (Option 3):**
 - Enter `3 `and press Enter.
 - The app will display all contacts stored in the book, or a message if the book is empty.
- **To Delete a Contact (Option 4):**
 - Enter `4 `and press Enter.
 - The app will first list current contacts for reference.
 - Enter the name of the contact you wish to delete.
 - A confirmation message will be displayed if successful, or a "not found" message if the contact doesn't exist.
- **To Exit the App (Option 5):**
 - Enter `5 `and press Enter.
 - The app will print a goodbye message and terminate.
- **Invalid Choice:** If you enter any number or text that is not a valid menu option, the app will prompt you to try again.

## Code Structure
The application's logic is contained within a single Python script (`contact_book.py`) and is structured as follows:
- `contacts = {}`: An empty Python dictionary initialized at the beginning. This `dictionary `is the core data structure, storing `name: phone_number` pairs.
- `while True:` **loop**: The primary loop that keeps the application running, continuously presenting the menu and processing user input until an explicit exit command.
- **Menu Display:** `print()` statements inside the loop present the user with the available options.
- **User Input:** `input()` captures the user's menu choice.
- **Conditional Logic** (`if/elif/else`):
 - `if choice == '1':` Handles adding a contact. It takes `name `and `phone_number` input and adds them to the `contacts `dictionary using `contacts[name] = phone_number`.
 - `elif choice == '2':` Handles looking up a contact. It takes a `name `as input and uses the `in `operator (`if name in contacts:`) to check for the key's existence before attempting to retrieve and print its value (`contacts[name]`).
 - `elif choice == '3':` Handles listing all contacts. It checks if the `contacts `dictionary is empty (`len(contacts) == 0` or `if not contacts:`). If not empty, it iterates through all key-value pairs using `for name, number in contacts.items():` and prints them.
 - `elif choice == '4':` Handles deleting a contact. It first checks if the dictionary is empty. If not, it prompts for a name to delete, checks if the name exists using `in`, and then uses `del contacts[name_to_delete]` to remove the entry. Provides feedback for success or if the contact is not found.
 - `elif choice == '5':` Handles exiting the app. It prints a goodbye message and uses `break `to terminate the `while `loop.
 - `else:` Catches invalid menu choices.

##  Key Concepts Demonstrated
This project effectively utilizes and reinforces the following fundamental Python programming concepts:
- **Data Structures**: Extensive use of Dictionaries (`dict`) for storing and managing key-value pairs (contacts).
 - Dictionary methods like `.items()`.
 - Dictionary operations like adding/updating (`dict[key] = value`), accessing (`dict[key]`), and deleting (`del dict[key]`).
 - Checking for key existence using the `in `operator.
- **Variables**: Storing names, phone numbers, user choices, and the `contacts` dictionary.
- **Input/Output**: Using `input()` for user interaction and `print()` for displaying information.
- **Logic & Control Flow:**
 - `while `**Loop**: For the continuous operation of the application.
 - `if/elif/else` **Statements**: For decision-making based on user menu choices and dictionary conditions.
 - `for `**Loop**: For iterating through dictionary items to display all contacts.
 - `break `**Keyword**: For gracefully exiting the main application loop.
- **String Formatting**: Using f-strings (`f"..."`) for clear and dynamic output messages.