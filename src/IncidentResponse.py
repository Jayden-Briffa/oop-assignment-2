from Ticket import FieldDetails, Priority, Status, Ticket
from Technician import Technician
from enum import Enum


class IncidentType(Enum):
    CYBER_SECURITY = "Cyber Security"
    SERVICE_OUTAGE = "Service Outage"


class IncidentResponse(Ticket):
    def __init__(
        self,
        id: int,
        priority: Priority,
        title: str,
        description: str,
        assignedTechnician: Technician,
        incidentType: IncidentType,
    ):
        super().__init__(
            id,
            priority,
            title,
            description,
            assignedTechnician,
        )
        self._incidentType = incidentType

    def getIncidentType(self) -> IncidentType:
        return self._incidentType

    def _validateIncidentType(self, incidentType: IncidentType | str) -> None:
        if isinstance(incidentType, IncidentType):
            return

        try:
            IncidentType(incidentType)
        except ValueError:
            raise ValueError(f"Invalid incident type '{incidentType}'") from None

    # Returns field details appended with incidentType configuration
    def getFieldDetails(self):
        return {
            **super().getFieldDetails(),
            "incidentType": FieldDetails(
                name="incidentType",
                prompt="Incident type",
                isInitializedByUser=True,
                validator=self._validateIncidentType,
                transformer=IncidentType,
                choices=IncidentType,
            ),
        }

    # Appends incident type to ticket details
    def getTicketDetails(self) -> str:
        ticketStr = super().getTicketDetails()
        ticketStr += f"\nIncident Type: {self._incidentType}"
        return ticketStr
