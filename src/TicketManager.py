from enum import Enum

from Ticket import Priority, Status, Ticket
from FeatureRequest import FeatureRequest
from IncidentResponse import IncidentResponse, IncidentType


class TicketType(Enum):
    NONE = ("None", Ticket)
    FEATURE_REQUEST = ("Feature Request", FeatureRequest)
    INCIDENT_RESPONSE = ("Incident Response", IncidentResponse)

    @classmethod
    def choices(cls):
        return [e.label() for e in cls]

    def label(self):
        return self.value[0]

    def cls(self):
        return self.value[1]


class TicketManager:
    def __init__(self, loadedTickets: dict[int, Ticket] | None = None, lastId: int = 0):
        self._loadedTickets = {} if loadedTickets is None else loadedTickets
        self._lastId = lastId

    def createTicket(
        self,
        ticketType: TicketType,
        ticketKwargs: dict,
    ) -> Ticket:
        nextId = self._lastId + 1

        ticketKwargs = {**ticketKwargs, "id": nextId}
        newTicket = ticketType.cls()(**ticketKwargs)
        self._loadedTickets[nextId] = newTicket

        self._lastId = nextId
        return newTicket

    def updateTicketField(self, ticketId: int, field: str, value) -> None:
        foundTicket = self.getTicketById(ticketId)
        if not foundTicket:
            raise ValueError(f"There is no ticket with id {ticketId}")

        foundTicket.updateField(field, value)
        return foundTicket

    def approveTicket(self, ticketId: int) -> None:
        foundTicket = self.getTicketById(ticketId)
        if not foundTicket:
            raise ValueError(f"There is no ticket with id {ticketId}")

        foundTicket.approve()
        return foundTicket

    def getTicketById(self, ticketId: int) -> Ticket | None:
        return self._loadedTickets.get(ticketId)

    def getAllTickets(self) -> dict[int, Ticket]:
        return self._loadedTickets

    def seedData(self) -> None:
        incidentResponse = IncidentResponse(
            id=1,
            priority=Priority.HIGH,
            title="Cannot access account",
            description="User is unable to sign in.",
            assignedTechnician="Alex",
            incidentType=IncidentType.CYBER_SECURITY,
        )
        featureRequest = FeatureRequest(
            id=2,
            priority=Priority.MEDIUM,
            title="Add export option",
            description="Add CSV export to reports.",
            assignedTechnician="Sam",
        )
        ticket = Ticket(
            id=3,
            priority=Priority.LOW,
            title="Update help text",
            description="Clarify the password reset instructions.",
            assignedTechnician="Jordan",
        )

        incidentResponse.updateField("status", Status.IN_PROGRESS)
        self._loadedTickets = {
            incidentResponse.getId(): incidentResponse,
            featureRequest.getId(): featureRequest,
            ticket.getId(): ticket,
        }
        self._lastId = ticket.getId()
