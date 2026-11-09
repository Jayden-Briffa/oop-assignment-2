import pytest
from Ticket import Ticket, Priority, Status
from Technician import Technician

def testCreateTicket(dummyTicketManager, dummyData):
    newId = dummyTicketManager.createTicket(
        "Test Ticket", "This is a test ticket.", "Test Technician", "High"
    )

    assert newId == len(dummyData) + 1
    assert len(dummyTicketManager._loadedTickets) == len(dummyData) + 1
    assert dummyTicketManager._lastId == max(dummyData.keys()) + 1
    assert dummyTicketManager._loadedTickets[dummyTicketManager._lastId].name == "Test Ticket"

def testGetTicketById(dummyTicketManager):
    foundTicket = dummyTicketManager.getTicketById(2) 
    assert foundTicket.id == 2

def testGetAllTickets(dummyTicketManager, dummyData):
    allTickets = dummyTicketManager.getAllTickets()

    assert allTickets == dummyData

def testUpdateTicketStatus(dummyTicketManager):
    ticketId = 1
    dummyTicketManager.updateTicketStatus(ticketId, Status.TO_DO)

    assert dummyTicketManager.getTicketById(ticketId).status is Status.TO_DO

def testUpdateTicketPriority(dummyTicketManager):
    ticketId = 1
    dummyTicketManager.updateTicketPriority(ticketId, Priority.LOW)

    assert dummyTicketManager.getTicketById(ticketId).priority is Priority.LOW

def testUpdateTicketAssignedTechnician(dummyTicketManager):
    ticketId = 1
    technician = Technician("Technician1")
    dummyTicketManager.updateTicketAssignedTechnician(ticketId, technician)

    assert dummyTicketManager.getTicketById(ticketId).assignedTechnician is technician
