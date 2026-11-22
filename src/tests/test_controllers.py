import tests.helpers as helpers
import userInterface
import controllers
from Ticket import Status, Priority, Ticket
from TicketManager import TicketType
from typing import Callable


def setupMonkeyPatchInputs(monkeypatch, expectedTicketInputs):
    expectedTicket, userInputs = helpers.constructExpectedTicketAndUserInputs(
        expectedTicketInputs
    )

    monkeypatch.setattr(userInterface, "outputTicket", helpers.mockOutputTicket)
    monkeypatch.setattr(
        userInterface, "getUserInput", helpers.mockGetUserInputFactory(iter(userInputs))
    )

    return expectedTicket


def executeCreateUpdateTestCase(dummyTicketManager, expectedTicket, callback: Callable):
    outputtedNewTicket = callback(dummyTicketManager)
    helpers.assertTicketHasSameValues(outputtedNewTicket, expectedTicket)

    actualNewTicket = dummyTicketManager._loadedTickets[expectedTicket["id"]]
    helpers.assertTicketHasSameValues(actualNewTicket, expectedTicket)

    return actualNewTicket


def testCreateTicketStandard(monkeypatch, dummyTicketManager):
    expectedNewTicketInputs = {
        "id": 4,
        "_": [TicketType.NONE.label()],
        "title": ["additional ticket"],
        "description": ["additional description"],
        "priority": [Priority.HIGH.value],
        "assignedTechnician": ["jamie"],
    }

    expectedTicket = setupMonkeyPatchInputs(monkeypatch, expectedNewTicketInputs)
    actualTicket = executeCreateUpdateTestCase(
        dummyTicketManager, expectedTicket, controllers.createTicket
    )
    assert actualTicket.getId() == expectedTicket["id"]

    assert (
        type(actualTicket) == Ticket
    ), "Expected new created ticket to be of type: Ticket"


def testUpdateTicketPriority(monkeypatch, dummyTicketManager):
    previousTicketState = dummyTicketManager._loadedTickets[3]
    expectedTicketInputs = {
        "id": ["3"],
        "_": ["Priority"],
        "title": previousTicketState.getTitle(),
        "description": previousTicketState.getDescription(),
        "priority": [Priority.HIGH.value],
        "status": previousTicketState.getStatus(),
        "assignedTechnician": previousTicketState.getAssignedTechnician(),
    }

    expectedTicket = setupMonkeyPatchInputs(monkeypatch, expectedTicketInputs)
    executeCreateUpdateTestCase(
        dummyTicketManager, expectedTicket, controllers.updateTicket
    )


def testUpdateTicketStatus(monkeypatch, dummyTicketManager):
    previousTicketState = dummyTicketManager._loadedTickets[3]
    expectedTicketInputs = {
        "id": ["3"],
        "_": ["Status"],
        "title": previousTicketState.getTitle(),
        "description": previousTicketState.getDescription(),
        "priority": previousTicketState.getPriority(),
        "status": [Status.IN_PROGRESS],
        "assignedTechnician": previousTicketState.getAssignedTechnician(),
    }

    expectedTicket = setupMonkeyPatchInputs(monkeypatch, expectedTicketInputs)
    executeCreateUpdateTestCase(
        dummyTicketManager, expectedTicket, controllers.updateTicket
    )


def testUpdateTicketTechnician(monkeypatch, dummyTicketManager):
    previousTicketState = dummyTicketManager._loadedTickets[3]
    expectedTicketInputs = {
        "id": ["3"],
        "_": ["Assigned technician"],
        "title": previousTicketState.getTitle(),
        "description": previousTicketState.getDescription(),
        "priority": previousTicketState.getPriority(),
        "status": previousTicketState.getStatus(),
        "assignedTechnician": ["jamie"],
    }

    expectedTicket = setupMonkeyPatchInputs(monkeypatch, expectedTicketInputs)
    executeCreateUpdateTestCase(
        dummyTicketManager, expectedTicket, controllers.updateTicket
    )


def testApproveTicket(monkeypatch, dummyTicketManager):
    expectedTicketInputs = {"id": ["2", "yes"], "approved": True}

    expectedTicket = setupMonkeyPatchInputs(monkeypatch, expectedTicketInputs)

    newTicketState = controllers.approveTicket(dummyTicketManager)

    helpers.assertTicketHasSameValues(newTicketState, expectedTicket)


def testViewTaskById(monkeypatch, dummyTicketManager):
    expectedTicketInputs = {"id": ["2"]}

    setupMonkeyPatchInputs(monkeypatch, expectedTicketInputs)

    foundTicket = controllers.viewTicketById(dummyTicketManager)
    expectedTicket = dummyTicketManager._loadedTickets[2]
    assert foundTicket.getId() == expectedTicket.getId()


def testViewAllTasks(monkeypatch, dummyTicketManager):
    monkeypatch.setattr(
        userInterface,
        "getUserInput",
        helpers.mockGetUserInputFactory(iter([""])),
    )

    foundTickets = controllers.viewAllTickets(dummyTicketManager)
    expectedTickets = dummyTicketManager._loadedTickets

    assert len(foundTickets) == len(expectedTickets)
    assert foundTickets.keys() == expectedTickets.keys()
