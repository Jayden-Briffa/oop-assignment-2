from Ticket import Ticket, Priority, Status
from Technician import Technician


class TicketManager:
    def __init__(self, loadedTickets: dict[int, Ticket] = {}, lastId=0):
        self._loadedTickets = loadedTickets
        self._lastId = lastId

    def getNextId(self) -> int:
        pass

    def createTicket(
        self,
        priority: Priority,
        status: Status,
        title: str,
        description: str,
        technician: Technician,
    ) -> int:
        pass

    def getTicketById(self, ticket_id: int) -> Ticket:
        pass

    def getAllTickets(self) -> dict[int, Ticket]:
        pass

    def updateTicketStatus(self, ticket_id: int, status: Status) -> None:
        pass

    def updateTicketPriority(self, ticket_id: int, priority: Priority) -> None:
        pass

    def updateTicketAssignedTechnician(
        self, ticket_id: int, technician: Technician
    ) -> None:
        pass
