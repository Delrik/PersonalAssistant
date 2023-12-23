command_descriptions = {
    # Contact Management
    "add": (
        "Add a new contact with a name. Step-by-step prompts for additional information like phone number, birthday, address, and email",
        "{name}",
    ),
    "change": (
        "Change an existing contact's details. Provides optional inputs step-by-step for modification",
        "{name}",
    ),
    "remove": ("Remove a contact from the address book", "{name}"),
    "all": ("Display all saved contacts", ""),
    "birthdays": ("Show birthdays occurring in the upcoming week", ""),
    # Phone Management
    "add-phone": ("Add a phone number to a contact's phone list", "{name}"),
    "change-phone": ("Change a phone number in a contact's phone list", "{name}"),
    "remove-phone": ("Remove a phone number from a contact's phone list", "{name}"),
    "phone": ("Retrieve the contact's phone numbers", "{name}"),
    # Address Management
    "add-address": ("Add an address to a contact", "{name}"),
    "change-address": ("Change an address of a contact", "{name}"),
    "remove-address": ("Remove an address from a contact", "{name}"),
    # Email Management
    "add-email": ("Add an email to a contact", "{name}"),
    "change-email": ("Change an email of a contact", "{name}"),
    "remove-email": ("Remove an email from a contact", "{name}"),
    # Birthday Management
    "add-birthday": ("Add a birthday to a contact", "{name}"),
    "change-birthday": ("Change the birthday of a contact", "{name}"),
    "remove-birthday": ("Remove the birthday from a contact", "{name}"),
    # Notes and Tags
    "add-note": ("Add a note to a contact", "{name}"),
    "change-note": ("Change a note of a contact", "{name}"),
    "change-note-title": ("Change the title of a note for a contact", "{name}"),
    "remove-note": ("Remove a note from a contact", "{name}"),
    "find-note": ("Find a note of a contact", "{name}"),
    "add-tag": ("Add a tag to a note of a contact", "{name}"),
    "find-tag": ("Find notes by tag", "{tag}"),
    # System Commands
    "hello": ("Greet the bot", ""),
    "close": ("Exit the application", ""),
}
