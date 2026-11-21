"""
Controllers handle high-level implementation logic. Each function calls the UI, validates with Ticket methods and uses TicketManager to perform CRUD operations safely
"""

import userInterface
from TicketManager import TicketType


def createTicket(ticketManager):
    selectedType = userInterface.getMenuChoiceInput("Type", TicketType.choices())
    ticketType = next(
        ticketType for ticketType in TicketType if ticketType.label() == selectedType
    )
    chosenType = ticketType.cls()
    fieldDetails = chosenType.__new__(chosenType).getFieldDetails()

    allUserInputs = {}
    for fieldLabel, field in fieldDetails.items():
        if not field.isInitializedByUser:
            continue

        promptStart = "Please enter the "
        if field.choices is not None:
            fieldChoices = [e.value for e in field.choices]
            userInput = userInterface.getMenuChoiceInput(
                promptStart + field.prompt, fieldChoices
            )
        else:
            userInput = userInterface.getUserInput(promptStart + field.prompt)

        allUserInputs[fieldLabel] = userInput

    createdTicket = ticketManager.createTicket(ticketType, allUserInputs)
    return createdTicket


def updateTicket(ticketManager):
    ticketId = int(userInterface.getUserInput("Enter ticket ID to update"))
    foundTicket = ticketManager.getTicketById(ticketId)
    if foundTicket is None:
        raise ValueError(f"There is no ticket with id {ticketId}")

    userInterface.output("Found ticket:", foundTicket)

    fieldDetails = foundTicket.getFieldDetails()
    mutableFields = {
        fieldLabel: field
        for fieldLabel, field in fieldDetails.items()
        if field.isMutable
    }
    immutableFields = {
        fieldLabel: field
        for fieldLabel, field in fieldDetails.items()
        if not field.isMutable
    }

    userInterface.output(
        "Immutable fields for this ticket:",
        ", ".join(field.prompt for field in immutableFields.values()),
    )
    fieldLabel = userInterface.getMenuChoiceInput(
        "Choose a field to update",
        [field.prompt for field in mutableFields.values()],
    )
    fieldLabel = next(
        label for label, field in mutableFields.items() if field.prompt == fieldLabel
    )
    fieldToUpdate = mutableFields[fieldLabel]

    if fieldToUpdate.choices is not None:
        newFieldValue = userInterface.getMenuChoiceInput(
            "Choose " + fieldToUpdate.prompt,
            [e.value for e in fieldToUpdate.choices],
        )
    else:
        newFieldValue = userInterface.getUserInput("Enter new value")

    newTicketState = ticketManager.updateTicketField(
        foundTicket.getId(), fieldLabel, newFieldValue
    )

    return foundTicket if newTicketState is None else newTicketState


def approveTicket(ticketManager):
    allTickets = ticketManager.getAllTickets()
    unapprovedTickets = [
        t for t in allTickets.values() if hasattr(t, "approved") and not t.approved
    ]

    userInterface.output("Unapproved tickets:")
    for t in unapprovedTickets:
        userInterface.output(t.getTicketSummary())

    ticketId = int(userInterface.getUserInput("Enter ticket ID to approve"))
    return ticketManager.approveTicket(ticketId)


def viewTicketById(ticketManager):
    ticketId = int(userInterface.getUserInput("Enter ticket ID"))
    foundTicket = ticketManager.getTicketById(ticketId)
    if foundTicket is None:
        raise ValueError(f"There is no ticket with id {ticketId}")

    userInterface.output(foundTicket.getTicketDetails())
    return foundTicket


def viewAllTickets(ticketManager):
    tickets = ticketManager.getAllTickets()
    for ticket in tickets.values():
        userInterface.output(ticket.getTicketSummary())

    return tickets
