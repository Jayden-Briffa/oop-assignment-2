import pytest
from Ticket import Priority, Status, Ticket
from FeatureRequest import FeatureRequest
from IncidentResponse import IncidentResponse, IncidentType
from TicketManager import TicketManager
import userInterface

import tests.helpers as helpers


@pytest.fixture
def dummyData():
    incidentResponse = IncidentResponse.__new__(IncidentResponse)
    setattr(incidentResponse, "_id", 1)
    setattr(incidentResponse, "_priority", Priority.HIGH)
    setattr(incidentResponse, "_status", Status.IN_PROGRESS)
    setattr(incidentResponse, "_title", "Cannot access account")
    setattr(incidentResponse, "_description", "User is unable to sign in.")
    setattr(incidentResponse, "_assignedTechnician", "Alex")
    setattr(incidentResponse, "_incidentType", IncidentType.CYBER_SECURITY)

    featureRequest = FeatureRequest.__new__(FeatureRequest)
    setattr(featureRequest, "_id", 2)
    setattr(featureRequest, "_priority", Priority.MEDIUM)
    setattr(featureRequest, "_status", Status.NEEDS_APPROVAL)
    setattr(featureRequest, "_title", "Add export option")
    setattr(featureRequest, "_description", "Add CSV export to reports.")
    setattr(featureRequest, "_assignedTechnician", "Sam")
    setattr(featureRequest, "_approved", False)

    ticket = Ticket.__new__(Ticket)
    setattr(ticket, "_id", 3)
    setattr(ticket, "_priority", Priority.LOW)
    setattr(ticket, "_status", Status.TO_DO)
    setattr(ticket, "_title", "Update help text")
    setattr(ticket, "_description", "Clarify the password reset instructions.")
    setattr(ticket, "_assignedTechnician", "Jordan")

    return {1: incidentResponse, 2: featureRequest, 3: ticket}


@pytest.fixture
def dummyTicketManager(dummyData):
    ticketManager = TicketManager(loadedTickets=dummyData, lastId=max(dummyData.keys()))

    return ticketManager


# Block acknowledgeToContinue from disrupting tests
@pytest.fixture(autouse=True)
def mockOutputErrorForAllTests(monkeypatch):
    monkeypatch.setattr(userInterface, "outputError", helpers.mockOutputError)
