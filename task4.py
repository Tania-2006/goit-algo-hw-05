def input_error(func):
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except KeyError:
            return "This name is not in contacts. Please try again."
        except ValueError:
            return "Give me name and phone please."
        except IndexError:
            return "Enter user name."
    return inner


contacts = {}

@input_error
def add_contact(args):
    name, phone = args.split()
    contacts[name] = phone
    return "Contact added."

@input_error
def get_phone(args):
    name = args.strip()
    if not name:
        raise IndexError
    phone = contacts[name]
    return f"{name}: {phone}"

@input_error
def show_all(args=None):
    if not contacts:
        return "No contacts saved."
    result = ""
    for name, phone in contacts.items():
        result += f"{name}: {phone}\n"
    return result.strip()

def main():
    commands = {
        "add": add_contact,
        "phone": get_phone,
        "all": show_all,
        "exit": lambda args=None: "Goodbye!",
        "close": lambda args=None: "Goodbye!",
        "bye": lambda args=None: "Goodbye!",
    }

    while True:
        user_input = input("Enter a command: ").strip()
        if not user_input:
            continue
        parts = user_input.split(' ', 1)
        command = parts[0].lower()
        args = parts[1] if len(parts) > 1 else ""

        if command in commands:
            result = commands[command](args)
            print(result)
            if result == "Goodbye!":
                break
        else:
            print("Unknown command. Try again.")

if __name__ == "__main__":
    main()

