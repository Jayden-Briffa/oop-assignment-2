from Ticket import Ticket, Priority, Status
from Technician import Technician


class FeatureRequest(Ticket):
    def __init__(
        self,
        ticket_id: int,
        priority: Priority,
        status: Status,
        title: str,
        description: str,
        technician: Technician,
    ):
        super().__init__(
            ticket_id, priority, status, title, description, technician
        )

    @classmethod
    def validateStatus(cls, status: str) -> bool:
        pass

    def approve(self) -> bool:
        pass

    def getTicketDetails(self) -> bool:
        pass
