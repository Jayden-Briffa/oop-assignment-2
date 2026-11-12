import pytest
from Ticket import Priority, Status, Ticket
import tests.helpers as helpers


def testValidatePriorityValid():
    ticket = helpers.generateTestTicket()
    msg = ticket.validatePriority(Priority.HIGH)

    assert msg is None, f"Expected no error for valid priority, got: {msg}"


def testValidatePriorityInvalid():
    ticket = helpers.generateTestTicket()
    msg = ticket.validatePriority("InvalidPriority")

    assert msg is not None, "Expected an error for invalid priority, got None"


def testUpdatePriority():
    ticket = helpers.generateTestTicket()
    ticket.updatePriority(Priority.MEDIUM)

    assert (
        ticket.priority.value == "Medium"
    ), f"Expected priority to be 'Medium', got: {ticket.priority}"


def testValidateStatusValid():
    ticket = helpers.generateTestTicket()
    msg = ticket.validateStatus(Status.IN_PROGRESS)

    assert msg is None, f"Expected no error for valid status, got: {msg}"


def testValidateStatusInvalid():
    ticket = helpers.generateTestTicket()
    msg = ticket.validateStatus("InvalidStatus")

    assert msg is not None, "Expected an error for invalid status, got None"


def testUpdateStatus():
    ticket = helpers.generateTestTicket()
    ticket.updateStatus(Status.COMPLETED)

    assert (
        ticket.status.value == "Completed"
    ), f"Expected status to be 'Completed', got: {ticket.status}"


def testStatusDefaultsToToDo():
    ticket = Ticket(
        1, Priority.HIGH, Status.TO_DO, "Test Ticket", "Description", "Test Technician"
    )

    assert ticket.status is Status.TO_DO


def testAssignTechnician():
    ticket = helpers.generateTestTicket()
    ticket.assignTechnician("New Technician")

    assert (
        ticket.assignedTechnician == "New Technician"
    ), f"Expected assigned technician to be 'New Technician', got: {ticket.assignedTechnician}"


def testGetId():
    ticket = helpers.generateTestTicket()
    ticket_id = ticket.getId()

    assert ticket_id == 1, f"Expected ticket ID to be 1, got: {ticket_id}"
