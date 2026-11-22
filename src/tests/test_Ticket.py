import pytest
from Ticket import Priority, Status, Ticket
import tests.helpers as helpers


def testValidatePriorityValid():
    validator = helpers.generateTestTicket().getFieldDetails()["priority"].validator

    assert validator(Priority.HIGH) is None


def testValidatePriorityInvalid():
    validator = helpers.generateTestTicket().getFieldDetails()["priority"].validator

    with pytest.raises(ValueError):
        validator("InvalidPriority")


def testValidateTitleUpper():
    validator = helpers.generateTestTicket().getFieldDetails()["title"].validator

    assert validator("a" * 50) is None


def testValidateTitleLower():
    validator = helpers.generateTestTicket().getFieldDetails()["title"].validator

    assert validator("abc") is None


def testValidateTitleInvalidUpper():
    validator = helpers.generateTestTicket().getFieldDetails()["title"].validator

    with pytest.raises(ValueError):
        validator("a" * 51)


def testValidateTitleInvalidLower():
    validator = helpers.generateTestTicket().getFieldDetails()["title"].validator

    with pytest.raises(ValueError):
        validator("ab")


def testUpdatePriority():
    ticket = helpers.generateTestTicket()
    ticket.updateField("priority", Priority.MEDIUM)

    assert (
        ticket.getPriority().value == "Medium"
    ), f"Expected priority to be 'Medium', got: {ticket.getPriority()}"


def testValidateStatusValid():
    validator = helpers.generateTestTicket().getFieldDetails()["status"].validator

    assert validator(Status.IN_PROGRESS) is None


def testValidateStatusInvalid():
    validator = helpers.generateTestTicket().getFieldDetails()["status"].validator

    with pytest.raises(ValueError):
        validator("InvalidStatus")


def testUpdateStatus():
    ticket = helpers.generateTestTicket()
    ticket.updateField("status", Status.COMPLETED)

    assert (
        ticket.getStatus().value == "Completed"
    ), f"Expected status to be 'Completed', got: {ticket.getStatus()}"


def testStatusDefaultsToToDo():
    ticket = Ticket(
        1,
        Priority.HIGH,
        "Test Ticket",
        "D" "escription",
        "Test Technician",
    )

    assert ticket.getStatus() is Status.TO_DO


def testAssignTechnician():
    ticket = helpers.generateTestTicket()
    ticket.updateField("assignedTechnician", "New Technician")

    assert (
        ticket.getAssignedTechnician() == "New Technician"
    ), f"Expected assigned technician to be 'New Technician', got: {ticket.getAssignedTechnician()}"


def testGetId():
    ticket = helpers.generateTestTicket()
    ticketId = ticket.getId()

    assert ticketId == 1, f"Expected ticket ID to be 1, got: {ticketId}"
