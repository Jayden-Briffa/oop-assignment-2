from Ticket import Priority, Status, Ticket
from FeatureRequest import FeatureRequest


# Accepts 2 tickets as Ticket or dict and raises assertion errors if they don't have the same values for all attributes provided by expectedTicket
def assertTicketHasSameValues(
    actualTicket: dict | Ticket, expectedTicket: dict | Ticket
):
    assert actualTicket is not None, (
        f"Expected a ticket object, but actual was None. Expected={expectedTicket!r}, actual={actualTicket!r}"
    )

    privateAttributeNames = {
        "id": "_id",
        "priority": "_priority",
        "status": "_status",
        "title": "_title",
        "description": "_description",
        "assignedTechnician": "_assignedTechnician",
        "approved": "_approved",
        "incidentType": "_incidentType",
    }

    def normalizeTicketValues(values):
        return {
            privateAttributeNames.get(name, name): value
            for name, value in values.items()
        }

    actualValues = (
        normalizeTicketValues(actualTicket)
        if isinstance(actualTicket, dict)
        else vars(actualTicket)
    )
    expectedValues = (
        normalizeTicketValues(expectedTicket)
        if isinstance(expectedTicket, dict)
        else vars(expectedTicket)
    )

    for key, value in expectedValues.items():
        assert actualValues.get(key) == value, (
            f"Ticket mismatch: expected {key}={value!r}, actual={actualValues.get(key)!r}"
        )


# Retrieves the next answer on each execution
# Must be monkeypatched to the appropriate input function for any test that requires user input
def mockGetUserInputFactory(answers):
    # compatible with original "prompt" and "default" function parameters, but it doesn't need to use them
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


# Construct an expected ticket and a list of dummy inputs based on an inputted dict[str, list | str] (ticketFieldName -> value(s)).
# Values in expectedTicketInputs which are not lists are added to expectedTicket, but not userInputs.
# The value for the expectedTicket[field] is the last list item, unless the last input is confirmation.
# Expects a dict of ticketFieldName -> listOfInputs.
# Returns a tuple of expectedTicket and userInputs.
def constructExpectedTicketAndUserInputs(
    expectedTicketInputs: dict[str, list[str] | str],
) -> tuple[dict, list[str]]:
    def resolveEnumInput(rawInput, enumType):
        if isinstance(rawInput, enumType):
            return rawInput

        if isinstance(rawInput, str):
            for enumValue in enumType:
                if rawInput.strip().lower() in {
                    enumValue.name.lower(),
                    enumValue.value.lower(),
                }:
                    return enumValue

        return rawInput

    def resolveExpectedValue(key: str, rawValue):
        if key == "id" and isinstance(rawValue, str) and rawValue.isdigit():
            return int(rawValue)
        if key == "priority":
            return resolveEnumInput(rawValue, Priority)
        if key == "status":
            return resolveEnumInput(rawValue, Status)
        return rawValue

    def formatUserInput(userInput):
        if isinstance(userInput, (Priority, Status)):
            return userInput.value
        return userInput

    expectedTicket = {}
    userInputs = []

    for key, value in expectedTicketInputs.items():
        if isinstance(value, list):
            userInputs.extend(formatUserInput(userInput) for userInput in value)
            expectedValue = value[-1]

            if len(value) > 1 and expectedValue == "yes":
                expectedValue = value[-2]
        else:
            expectedValue = value

        if key != "_":
            expectedTicket[key] = resolveExpectedValue(key, expectedValue)

    return expectedTicket, userInputs


def generateTestTicket():
    return Ticket(
        1,
        Priority.HIGH,
        "Test Ticket",
        "This is a test ticket.",
        "Test Technician",
    )


def generateTestFeatureRequest():
    return FeatureRequest(
        1,
        Priority.HIGH,
        "Test Feature",
        "Description",
        "Test Technician",
    )
