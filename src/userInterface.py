from Ticket import Ticket
from prompt_toolkit import prompt
from UserAbortException import UserAbortException

""" Handles user input and output operations """

# Remove case sensitivity
def formatAsUserInput(msg: str):
    return msg.strip().lower()


def getUserInput(msg: str, format=True, default=""):
    # Force a space after the prompt message if it doesn't already have one
    if len(msg) > 0 and msg[-1] != " ":
        msg += " "

    userInput = prompt(msg, default=default)
    if userInput == "abort":
        raise UserAbortException()

    if format:
        return formatAsUserInput(userInput)

    return userInput


def acknowledgeToContinue():
    getUserInput("\nPress enter to continue...")


# Always return the index of the user's choice, or an empty string if the input is invalid
def _normaliseMenuInput(userInput: str, choices: list[str]) -> str:
    for i, choice in enumerate(choices):
        castedI = str(i)
        if userInput == castedI or userInput == formatAsUserInput(choice):
            return castedI

    return ""


def _getMenuInput(title, choices: list[str], defaultInput="") -> tuple[str, str]:
    bannerBuffer = "=" * 5
    print(bannerBuffer, title, bannerBuffer)

    for i, choice in enumerate(choices):
        print(f"{i}. {choice}")

    userChoice = getUserInput(
        f"Enter your choice (0-{len(choices) - 1} or full phrase): ",
        format=True,
        default=defaultInput,
    )
    normalisedChoice = _normaliseMenuInput(userChoice, choices)

    return normalisedChoice, userChoice


# Provides default choice functionality and validates the user's input against the provided choices
# Returns the chosen option's text
def getMenuChoiceInput(title, choices: list[str], defaultChoice="") -> str:
    defaultInput = ""
    if defaultChoice != "":
        # Derive the default input index from the default choice string
        for i, choice in enumerate(choices):
            if choice.lower() == defaultChoice.lower():
                defaultInput = str(i)
                break

    # Ask for user input until a valid choice is made, or return the default choice if provided
    while True:
        normalisedIndex, userChoice = _getMenuInput(
            title, choices, defaultInput=defaultInput
        )
        if normalisedIndex.isdigit():
            return choices[int(normalisedIndex)]

        outputError(
            f"Invalid menu input: '{userChoice}'. You must enter numbers (0-{len(choices) - 1}) or the full phrase"
        )


# Outputs the ticket details.
def outputTicket(ticket: Ticket, pressEnter=True):

    print()

    ticketOutput = ticket.getTicketDetails()
    print(ticketOutput)

    if pressEnter:
        acknowledgeToContinue()


def outputError(msg: str):
    bannerBuffer = "!"
    print(bannerBuffer, "ERROR:", msg, bannerBuffer)

    acknowledgeToContinue()


def output(*args):
    print(*args)
