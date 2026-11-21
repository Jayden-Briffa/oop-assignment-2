from Ticket import FieldDetails, Ticket, Priority, Status
from Technician import Technician


class FeatureRequest(Ticket):
    def __init__(
        self,
        ticketId: int,
        priority: Priority,
        title: str,
        description: str,
        technician: Technician,
        approved: bool = False,
    ):
        self._approved = approved
        super().__init__(ticketId, priority, title, description, technician)
        self._status = Status.NEEDS_APPROVAL

    def approve(self) -> bool:
        self._approved = True
        return self._approved

    def getApproved(self) -> bool:
        return self._approved

    def getTicketDetails(self) -> str:
        ticketStr = super().getTicketDetails()
        ticketStr += f"\nApproved: {self._approved}"

        return ticketStr
