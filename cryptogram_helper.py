"""This file handles the book keeping of a crytpogram."""
import re

SOLVED = "\033[92m"
NOT_SOLVED = "\033[0m"


def get_message():
    """Get the message contents from a file."""
    message = None
    while not message:
        message_location = input("Input the message file: ")
        try:
            with open(message_location) as input_file:
                message = input_file.read()
        except FileNotFoundError:
            print(f"{message_location} not found")
    print(message)
    return message


def show_message(message):
    """Keep adding new substitutions until the message is solved."""
    mapped = {}
    quit = False
    while len(mapped) < 26 and not quit:
        substitution = input(
            "Enter a letter and replacement of the form 'A>E' or hit 'Q' to quit: "
        ).upper()
        if substitution == "Q":
            quit = True
        mapping = re.match("^([a-zA-Z])>([a-zA-Z])$", substitution)
        if mapping:
            if mapping[2] in mapped.values():
                print(f"Skipping mapping: {mapping[2]} already mapped.")
            else:
                print(mapped.values())
                mapped[mapping[1]] = mapping[2]
                replacement = f"{SOLVED}{mapping[1]}{NOT_SOLVED}"
                message = message.replace(mapping[1], replacement)
        translated_message = message.translate(
            message.maketrans(
                "".join([x[0] for x in mapped.items()]),
                "".join([x[1] for x in mapped.items()]),
            )
        )
        print(translated_message)
        print(mapped)


if __name__ == "__main__":
    message = get_message()
    show_message(message)
