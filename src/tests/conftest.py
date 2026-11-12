import pytest
from Ticket import Priority, Status, Ticket
from FeatureRequest import FeatureRequest
from IncidentResponse import IncidentResponse, IncidentType
from TicketManager import TicketManager
import userInterface

import tests.helpers as helpers


@pytest.fixture
def dummyData():
    return {
        1: IncidentResponse(
            1,
            Priority.HIGH,
            Status.IN_PROGRESS,
            "Cannot access account",
            "User is unable to sign in.",
            "Alex",
            IncidentType.CYBER_SECURITY,
        ),
        2: FeatureRequest(
            2,
            Priority.MEDIUM,
            Status.NEEDS_APPROVAL,
            "Add export option",
            "Add CSV export to reports.",
            "Sam",
        ),
        3: Ticket(
            3,
            Priority.LOW,
            Status.TO_DO,
            "Update help text",
            "Clarify the password reset instructions.",
            "Jordan",
        ),
    }


@pytest.fixture
def dummyTicketManager(dummyData):
    ticketManager = TicketManager(loadedTickets=dummyData, lastId=max(dummyData.keys()))

    return ticketManager


# Block acknowledgeToContinue from disrupting tests
@pytest.fixture(autouse=True)
def mockOutputErrorForAllTests(monkeypatch):
    monkeypatch.setattr(userInterface, "outputError", helpers.mockOutputError)
