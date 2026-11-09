import pytest
from Ticket import Priority, Status, Ticket
from TicketManager import TicketManager
import userInterface

import helpers as helpers


@pytest.fixture
def dummyData():
    return {
        1: Ticket(
            1,
            Priority.HIGH,
            "Cannot access account",
            "User is unable to sign in.",
            "Alex",
            Status.IN_PROGRESS,
        ),
        2: Ticket(
            2,
            Priority.MEDIUM,
            "Add export option",
            "Add CSV export to reports.",
            "Sam",
            Status.NEEDS_APPROVAL,
        ),
        3: Ticket(
            3,
            Priority.LOW,
            "Update help text",
            "Clarify the password reset instructions.",
            "Jordan",
            Status.TO_DO,
        ),
    }


@pytest.fixture
def dummyTicketManager(dummyData):
    ticketManager = TicketManager(loadedTickets=dummyData, lastId=max(dummyData.keys()))
    ticketManager.saveTickets()

    return ticketManager


# Block acknowledgeToContinue from disrupting tests
@pytest.fixture(autouse=True)
def mockOutputErrorForAllTests(monkeypatch):
    monkeypatch.setattr(userInterface, "outputError", helpers.mockOutputError)
