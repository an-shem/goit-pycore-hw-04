def parse_input(user_input):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args


def add_contact(args, contacts):
    if len(args) == 2:
        name, phone = args
    else:
        return "To add a phone number, you need to enter a command in the format:'add username phone'"
    if name in contacts:
        return "User with that name already exists."
    contacts[name] = phone
    return "Contact added."


def change_contact(args, contacts):
    if len(args) == 2:
        name, phone = args
    else:
        return (
            "To change a user's phone number, you need to enter a "
            "command in the following format:'change username phone'"
        )
    if name not in contacts:
        return "User with this name not found."
    contacts[name] = phone
    return "Contact updated."


def show_phone(args, contacts):
    if len(args) == 1:
        [name] = args
    else:
        return "To get a phone number, you need to enter a command in the format:'phone username'"
    if name not in contacts:
        return "User with this name not found."
    return contacts[name]


def show_all(contacts):
    return str(contacts)


def main():
    contacts = {}
    print("Welcome to the assistant bot!")
    while True:
        user_input = input("Enter a command: ")
        command, *args = parse_input(user_input)

        if command in ["close", "exit"]:
            print("Good bye!")
            break
        elif command == "hello":
            print("How can I help you?")
        elif command == "add":
            print(add_contact(args, contacts))
        elif command == "change":
            print(change_contact(args, contacts))
        elif command == "phone":
            print(show_phone(args, contacts))
        elif command == "all":
            print(show_all(contacts))
        else:
            print("Invalid command.")


if __name__ == "__main__":
    main()
