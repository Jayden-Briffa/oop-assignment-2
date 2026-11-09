from Ticket import Priority, Status, Ticket


# Accepts 2 tickets as Ticket or dict and raises assertion errors if they don't have the same values for al attributes
def assertTicketHasSameValues(
    actualTicket: dict | Ticket, expectedTicket: dict | Ticket
):
    if type(expectedTicket) == dict:
        expectedTicket = Ticket(**expectedTicket)

    if type(actualTicket) == dict:
        actualTicket = Ticket(**actualTicket)

    assert actualTicket is not None, (
        f"Expected a ticket object, but actual was None.\n"
        f"expected={expectedTicket!r}\n"
        f"actual={actualTicket!r}"
    )
    assert vars(actualTicket) == vars(expectedTicket), (
        f"Ticket mismatch:\n"
        f"expected={vars(expectedTicket)!r}\n"
        f"actual={vars(actualTicket)!r}"
    )


# Must be monkeypatched to the appropriate input function for any test that requires user input
def mockGetUserInputFactory(answers):
    # Make the mock getUserInput compatible with original "prompt" and "default" function parameters, but it doesn't need to use them
    def mockGetUserInput(prompt="", default="", format=True):
        answer = next(answers)
        if format:
            return answer.strip().lower()

        return answer

    return mockGetUserInput


def mockOutputTicket(ticket: Ticket, pressEnter=True):
    return ticket


def mockOutputTicketsByCategory(ticketsByCategory: dict[str, Ticket]):
    return ticketsByCategory


def mockOutputError(msg: str):
    print(f"ERROR: {msg}")


# Construct an expected ticket and a list of dummy inputs based on an inputted dict[str, list | str]
# Values in expectedTicketInputs which are strings instead of lists are added to expectedNewTicket, but not userInputs
# Where confirmation is required for an action (ie, the answer is "yes"), the second to-last value in the list is added to expectedNewTicket (as "yes" will be the last input in the list)
# Expects a dict of ticketFieldName -> listOfInputs
# Returns a tuple of expectedTicket and userInputs
def constructExpectedTicketAndUserInputs(
    expectedTicketInputs: dict[str, list[str] | str],
) -> tuple[Ticket, list[str]]:
    pass

    # return expectedTicket, userInputs


def generateTestTicket():
    return Ticket(
        1,
        Priority.HIGH,
        "Test Ticket",
        "This is a test ticket.",
        "Test Technician",
        Status.IN_PROGRESS,
    )
