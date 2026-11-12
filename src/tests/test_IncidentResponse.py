from IncidentResponse import IncidentResponse, IncidentType
from Ticket import Priority, Status
import tests.helpers as helpers


def testGetTicketDetailsReturnsTicketAsDict():
    ticket = IncidentResponse(
        1,
        Priority.HIGH,
        Status.IN_PROGRESS,
        "Cannot access account",
        "User is unable to sign in.",
        "Alex",
        IncidentType.CYBER_SECURITY,
    )

    details = ticket.getTicketDetails()

    assert isinstance(details, dict)
    expected_ticket_details = {
        "id": 1,
        "priority": Priority.HIGH,
        "status": Status.IN_PROGRESS,
        "title": "Cannot access account",
        "description": "User is unable to sign in.",
        "assignedTechnician": "Alex",
        "incidentType": IncidentType.CYBER_SECURITY,
    }

    helpers.assertTicketHasSameValues(expected_ticket_details, details)
