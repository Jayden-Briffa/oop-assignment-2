from Ticket import Ticket
from TicketManager import TicketManager
from prompt_toolkit import prompt
from typing import Callable
from UserAbortException import UserAbortException


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


def _getMenuInput(title, choices: list[str], defaultInput="") -> str | None:
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

    return normalisedChoice


# Provides default choice functionality and validates the user's input against the provided choices
# Once a valid choice is found, the option's callback function is executed
def executeMenu(title, choices: dict[str, Callable], defaultChoice="") -> str:
    defaultInput = ""
    options = list(choices.keys())
    if defaultChoice != "":
        # Derive the default input index from the default choice string
        for i, choice in enumerate(options):
            if choice.lower() == defaultChoice.lower():
                defaultInput = str(i)
                break

    # Ask for user input until a valid choice is made, or return the default choice if provided
    while True:
        normalisedIndex = _getMenuInput(title, choices, defaultInput=defaultInput)
        if normalisedIndex != "":
            chosenOption = options[int(normalisedIndex)]
            choices[
                chosenOption
            ]()  # Execute the callback function for the selected option

        if defaultChoice != "":
            choices[
                defaultChoice
            ]()  # Execute the callback function for the default option

        outputError(
            f"Invalid menu input. You must enter numbers (0-{len(choices) - 1}) or the full phrase"
        )


# Outputs the string representation of a ticekt as returned by the Ticket class's getTicket() method
def outputTicket(ticket: Ticket, pressEnter=True):

    print()

    ticketOutput = ticket.getTicket()
    print(ticketOutput)

    if pressEnter:
        acknowledgeToContinue()


def outputError(msg: str):
    bannerBuffer = "!"
    print(bannerBuffer, "ERROR:", msg, bannerBuffer)

    acknowledgeToContinue()

def output(*args):
    print(*args)


class UserInterface:
    def executeMenu(self, title: str, choices: dict[str, Callable]):
        pass

    def getMenuChoices(self, title: str, choices: list[str]) -> None:
        pass

    def printTicketSummary(self, ticket: Ticket) -> None:
        pass

    def printTicketDetails(self, ticket: Ticket) -> None:
        pass

    def getUserInput(self, prompt_text: str) -> None:
        pass

    def getMenuInput(self, title: str, choices: list[str]):
        pass

    def output(self, message: str) -> None:
        pass

    def errorOutput(self, message: str) -> None:
        pass

    def acknowledgeToContinue(self) -> None:
        pass