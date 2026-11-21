import pytest
from Ticket import Ticket, Priority, Status
from Technician import Technician
from TicketManager import TicketManager, TicketType


def testCreateTicket(dummyTicketManager, dummyData):
    initialCount = len(dummyData)
    expectedId = dummyTicketManager._lastId + 1

    newTicket = dummyTicketManager.createTicket(
        TicketType.NONE,
        {
            "id": expectedId,
            "priority": Priority.HIGH,
            "title": "Test Ticket",
            "description": "This is a test ticket.",
            "assignedTechnician": "Test Technician",
        },
    )

    assert newTicket.getId() == expectedId
    assert len(dummyTicketManager._loadedTickets) == initialCount + 1
    assert dummyTicketManager._lastId == expectedId
    assert (
        dummyTicketManager._loadedTickets[newTicket.getId()].getTitle() == "Test Ticket"
    )


def testGetTicketById(dummyTicketManager):
    foundTicket = dummyTicketManager.getTicketById(2)
    assert foundTicket.getId() == 2


def testGetAllTickets(dummyTicketManager, dummyData):
    allTickets = dummyTicketManager.getAllTickets()

    assert allTickets == dummyData


def testUpdateTicketStatus(dummyTicketManager):
    ticketId = 1
    dummyTicketManager.updateTicketField(ticketId, "status", Status.TO_DO)

    assert dummyTicketManager.getTicketById(ticketId).getStatus() is Status.TO_DO


def testUpdateTicketPriority(dummyTicketManager):
    ticketId = 1
    dummyTicketManager.updateTicketField(ticketId, "priority", Priority.LOW)

    assert dummyTicketManager.getTicketById(ticketId).getPriority() is Priority.LOW


def testUpdateTicketAssignedTechnician(dummyTicketManager):
    ticketId = 1
    technician = Technician("Technician1")
    dummyTicketManager.updateTicketField(ticketId, "assignedTechnician", technician)

    assert (
        dummyTicketManager.getTicketById(ticketId).getAssignedTechnician() == technician
    )


def testCreateTicketInEmptyManagerGetsIdOne():
    emptyTicketManager = TicketManager(loadedTickets={}, lastId=0)

    newTicket = emptyTicketManager.createTicket(
        TicketType.NONE,
        {
            "id": 1,
            "priority": Priority.HIGH,
            "title": "First Ticket",
            "description": "This is the first ticket.",
            "assignedTechnician": "Test Technician",
        },
    )

    assert newTicket.getId() == 1
    assert list(emptyTicketManager._loadedTickets.keys()) == [1]
    assert emptyTicketManager._lastId == 1
