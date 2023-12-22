# PersonalAssistant

## Overview

This project implements an advanced console-based assistant bot featuring an enhanced data management system through custom classes and improved error handling. The assistant supports various functionalities, including contact management, birthday reminders and notes management.

The user interface is implemented in the form of a command line and is based on text messages and commands that the user enters from the keyboard. The assistant interacts with the user in a loop, presenting options to choose a command and processing it until the user enters an `exit` command.

## Features

-   **Advanced Error Handling**: Utilizes the `input_error` decorator for robust error management across different commands.
-   **Enhanced Data Management**: Introduces classes like `AddressBook` and `Record` for efficient contact management.
-   **Birthday Management**: Ability to add, store, and display contact birthdays.
-   **Contact Management**: Add, change, find, and delete contact information with ease.
-   **Notes Management**: Add, change, find, and delete notes with ease.
-   **Tags Management**: Add and find tags with ease.
-   **Persistence**: Save and restore address book data from disk using serialization, ensuring data is not lost between sessions.

## Getting Started

To interact with the assistant, run the `main.py` file. The assistant supports a range of commands to manage contacts and their information:

-   `hello`: Greet the bot.
-   `add [name]`: Add a new contact with a name. It provides next optional inputs step-by-step: `Enter phone number`, `Enter birthday`, `Enter address`, `Enter email`
-   `change [name]`: Change an existing contact. It provides optional inputs step-by-step to add or change information
-   `delete [name]`: Remove a contact from an address book
-   `all`: Display all saved contacts
-   `add-phone [name]`: Add a phone number to a contact phone list
-   `change-phone [name]`: Change a phone number in a contact phone list
-   `remove-phone [name]`: Remove a phone number in a contact phone list
-   `phone [name]`: Retrieve the contact information
-   `add-address [name]`: Add an address to a contact
-   `change-address [name]`: Change an address of a contact
-   `remove-address [name]`: Remove an address from a contact
-   `add-email [name]`: Add e-mail to a contact
-   `change-email [name]`: Change e-mail of a contact
-   `remove-email [name]`: Remove e-mail from a contact
-   `add-birthday [name]`: Add birthday for a contact
-   `change-birthday [name]`: Change birthday of a contact
-   `remove-birthday [name]`: Remove birthday from a contact.
-   `birthdays`: Show birthdays occurring in the upcoming week.
-   `add-note [name]`: Add a note for a contact
-   `change-note [name]`: Change a note of a contact
-   `change-note-title [name]`: Change a note title of a contact
-   `remove-note [name]`: Remove a note from a contact.
-   `find-note [name]`: Find a note of a contact
-   `add-tag [name]`: Add a tag for a note
-   `find-tag [name]`: Find a tag of notes
-   `close` or `exit`: Exit the application.

To see a demonstration of these functionalities, run the `demo.test.py` script.

## Testing

Run `demo.test.py` to execute a series of automated actions demonstrating the bot's capabilities. This includes creating contacts, adding phone numbers, managing birthdays, and showcasing persistence features.

## Additional Notes

-   The project's error handling system ensures a user-friendly experience, gracefully managing incorrect inputs and providing clear instructions.
-   Data validation includes checks for correct phone number formats and valid date inputs for birthdays.
-   The application saves data to disk upon exit and retrieves it upon startup, ensuring data persistence.
