from Ticket import FieldDetails, Priority, Status, Ticket
from Technician import Technician
from enum import Enum


class IncidentType(Enum):
    CYBER_SECURITY = "Cyber Security"
    SERVICE_OUTAGE = "Service Outage"


class IncidentResponse(Ticket):
    def __init__(
        self,
        ticketId: int,
        priority: Priority,
        title: str,
        description: str,
        technician: Technician,
        incidentType: IncidentType,
    ):
        super().__init__(
            ticketId,
            priority,
            title,
            description,
            technician,
        )
        self._incidentType = incidentType

    def getIncidentType(self) -> IncidentType:
        return self._incidentType

    def validateIncidentType(self, incidentType: IncidentType | str) -> None:
        if isinstance(incidentType, IncidentType):
            return

        try:
            IncidentType(incidentType)
        except ValueError:
            raise ValueError(f"Invalid incident type '{incidentType}'") from None

    def getFieldDetails(self):
        return {
            **super().getFieldDetails(),
            "incidentType": FieldDetails(
                name="incidentType",
                prompt="Incident type",
                isInitializedByUser=True,
                validator=self.validateIncidentType,
                transformer=IncidentType,
                choices=IncidentType,
            ),
        }

    def getTicketDetails(self) -> str:
        ticketStr = super().getTicketDetails()
        ticketStr += f"\nIncident Type: {self._incidentType}"
        return ticketStr
