from Ticket import Priority, Status, Ticket
from Technician import Technician
from enum import Enum


class IncidentType(Enum):
    CYBER_SECURITY = "Cybers Security"
    SERVICE_OUTAGE = "Service Outage"


class IncidentResponse(Ticket):
    def __init__(
        self,
        ticket_id: int,
        priority: Priority,
        status: Status,
        title: str,
        description: str,
        technician: Technician,
        incidentType: IncidentType,
    ):
        super().__init__(
            ticket_id,
            priority,
            status,
            title,
            description,
            technician,
        )
        self.incidentType = incidentType

    def getTicketDetails(self) -> str:
        pass
