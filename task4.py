def input_error(func):
    def inner(contacts, args):
        try:
            return func(contacts, args)
        except KeyError:
            return "This name is not in contacts. Please try again."
        except ValueError:
            return "Give me name and phone please."
        except IndexError:
            return "Enter user name."
    return inner


@input_error
def add_contact(contacts, args):
    name, phone = args.split()
    contacts[name] = phone
    return "Contact added."


@input_error
def change_contact(contacts, args):
    name, phone = args.split()
    if name not in contacts:
        raise KeyError
    contacts[name] = phone
    return "Contact updated."


@input_error
def get_phone(contacts, args):
    name = args.strip()
    phone = contacts[name]  # Якщо name порожній або відсутній - буде KeyError
    return f"{name}: {phone}"


@input_error
def show_all(contacts, args=None):
    if not contacts:
        return "No contacts saved."
    result = ""
    for name, phone in contacts.items():
        result += f"{name}: {phone}\n"
    return result.strip()


def main():
    contacts = {}

    commands = {
        "add": add_contact,
        "change": change_contact,
        "phone": get_phone,
        "all": show_all,
        "exit": lambda contacts, args=None: "Goodbye!",
        "close": lambda contacts, args=None: "Goodbye!",
        "bye": lambda contacts, args=None: "Goodbye!",
    }

    while True:
        user_input = input("Enter a command: ").strip()
        if not user_input:
            continue
        parts = user_input.split(' ', 1)
        command = parts[0].lower()
        args = parts[1] if len(parts) > 1 else ""

        if command in commands:
            result = commands[command](contacts, args)
            print(result)
            if result == "Goodbye!":
                break
        else:
            print("Unknown command. Try again.")


if __name__ == "__main__":
    main()
