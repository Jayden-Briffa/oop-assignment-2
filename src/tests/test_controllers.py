import tests.helpers as helpers
import userInterface
import controllers
from Ticket import Status, Priority, Ticket
from typing import Callable
from TicketManager import TicketType


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
        "_": [TicketType.NONE],
        "title": ["Additional ticket"],
        "priority": [Priority.HIGH.value],
        "status": Status.TO_DO,
        "assignedTechnician": ["Jamie"],
    }

    expectedTicket = setupMonkeyPatchInputs(monkeypatch, expectedNewTicketInputs)
    actualTicket = executeCreateUpdateTestCase(
        dummyTicketManager, expectedTicket, controllers.createTicket
    )
    assert actualTicket.id == expectedTicket["id"]

    assert (
        type(actualTicket) == Ticket
    ), "Expected new created ticket to be of type: Ticket"


def testUpdateTicketPriority(monkeypatch, dummyTicketManager):
    previousTicketState = dummyTicketManager._loadedTickets[3]
    expectedTicketInputs = {
        "id": ["3"],
        "_": ["Priority"],
        "title": previousTicketState.title,
        "description": previousTicketState.description,
        "priority": [Priority.HIGH.value],
        "status": previousTicketState.status,
        "assignedTechnician": previousTicketState.assignedTechnician,
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
        "title": previousTicketState.title,
        "description": previousTicketState.description,
        "priority": previousTicketState.priority,
        "status": [Status.IN_PROGRESS],
        "assignedTechnician": previousTicketState.assignedTechnician,
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
        "title": previousTicketState.title,
        "description": previousTicketState.description,
        "priority": previousTicketState.priority,
        "status": previousTicketState.status,
        "assignedTechnician": "Jamie",
    }

    expectedTicket = setupMonkeyPatchInputs(monkeypatch, expectedTicketInputs)
    executeCreateUpdateTestCase(
        dummyTicketManager, expectedTicket, controllers.updateTicket
    )


def testUpdateFeatureRequestApproval(monkeypatch, dummyTicketManager):
    expectedTicketInputs = {"id": ["2", "yes"], "approved": True}

    setupMonkeyPatchInputs(monkeypatch, expectedTicketInputs)

    newTicketState = dummyTicketManager._loadedTickets[2]
    assert newTicketState.approved


def testViewTaskById(monkeypatch, dummyTicketManager):
    expectedTicketInputs = {"id": ["2"]}

    setupMonkeyPatchInputs(monkeypatch, expectedTicketInputs)

    foundTicket = controllers.viewTicketById(dummyTicketManager)
    expectedTicket = dummyTicketManager._loadedTickets[2]
    assert foundTicket.id == expectedTicket.id


def testViewAllTasks(monkeypatch, dummyTicketManager):
    foundTickets = controllers.viewAllTickets(dummyTicketManager)
    expectedTickets = dummyTicketManager._loadedTickets

    assert len(foundTickets) == len(expectedTickets)
    assert foundTickets.keys() == expectedTickets.keys()
