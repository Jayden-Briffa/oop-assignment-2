from IncidentResponse import IncidentResponse, IncidentType
from Ticket import Priority, Status


def testGetTicketDetailsReturnsTicketDetailsString():
    ticket = IncidentResponse(
        1,
        Priority.HIGH,
        "Cannot access account",
        "User is unable to sign in.",
        "Alex",
        IncidentType.CYBER_SECURITY,
    )

    details = ticket.getTicketDetails()

    assert isinstance(details, str)
    assert "Cannot access account" in details
    assert "Incident Type: IncidentType.CYBER_SECURITY" in details
