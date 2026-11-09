# bannerBuffer = "-" * 3
# category = task.category if task.category != "" else "<no output>"
# description = task.description if task.description != "" else "<no description>"
# deadline = task.deadline if task.deadline != "" else "<no deadline>"

# print(bannerBuffer, task.name, f"(#{task.id})", bannerBuffer)
# print(f"- Category: {category}")
# print(f"- Status: {task.status}")
# print(description)
# print(f"[ Deadline: {deadline} ]")


from enum import Enum

from Technician import Technician


class Priority(
    Enum,
):
    LOW = "Low"
    MEDIUM = "Medium"
    HIGH = "High"


class Status(
    Enum,
):
    NEEDS_APPROVAL = "Needs Approval"
    TO_DO = "To Do"
    IN_PROGRESS = "In Progress"
    COMPLETED = "Completed"


class Ticket:
    def __init__(
        self,
        id: int,
        priority: Priority,
        status: Status,
        title: str,
        description: str,
        assignedTechnician: Technician,
    ):
        self.id = id
        self.priority = priority
        self.status = status
        self.title = title
        self.description = description
        self.assignedTechnician = assignedTechnician

    @classmethod
    def validatePriority(cls, priority: str) -> str | None:
        pass

    @classmethod
    def validateStatus(cls, status: str) -> str | None:
        pass

    def updatePriority(self, priority: Priority) -> bool:
        pass

    def updateStatus(self, status: Status) -> bool:
        pass

    def assignTechnician(self, technician: Technician) -> bool:
        pass

    def getTicketSummary(self) -> str:
        pass

    def getTicketDetails(self) -> str:
        pass

    def getId(self) -> int:
        pass
