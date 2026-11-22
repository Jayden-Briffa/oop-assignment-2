from Ticket import FieldDetails, Ticket, Priority, Status
from Technician import Technician


class FeatureRequest(Ticket):
    def __init__(
        self,
        id: int,
        priority: Priority,
        title: str,
        description: str,
        assignedTechnician: Technician,
        approved: bool = False,
    ):
        self._approved = approved
        super().__init__(id, priority, title, description, assignedTechnician)
        self._status = Status.NEEDS_APPROVAL

    def approve(self) -> bool:
        self._approved = True
        return self._approved

    def getApproved(self) -> bool:
        return self._approved

    def validateStatus(self, status: str | Status) -> None:
        super().validateStatus(status)

        if self._approved is not True:
            raise ValueError(
                "Invalid status: feature requests must be approved before their status can change"
            )

    def getFieldDetails(self) -> dict[str, FieldDetails]:
        fieldDetails = super().getFieldDetails()
        fieldDetails["status"] = FieldDetails(
            "status",
            "Status",
            False,
            True,
            self.validateStatus,
            Status,
            Status,
        )
        return fieldDetails

    def getTicketDetails(self) -> str:
        ticketStr = super().getTicketDetails()
        ticketStr += f"\nApproved: {self._approved}"

        return ticketStr
