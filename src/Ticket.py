# bannerBuffer = "-" * 3
# category = task.category if task.category != "" else "<no output>"
# description = task.description if task.description != "" else "<no description>"
# deadline = task.deadline if task.deadline != "" else "<no deadline>"

# print(bannerBuffer, task.name, f"(#{task.id})", bannerBuffer)
# print(f"- Category: {category}")
# print(f"- Status: {task.status}")
# print(description)
# print(f"[ Deadline: {deadline} ]")

from dataclasses import dataclass
from enum import Enum
from typing import Any, Callable

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


@dataclass
class FieldDetails:
    name: str
    prompt: str
    isInitializedByUser: bool = False
    isMutable: bool = False
    validator: Callable[[Any], None | str] = lambda x: None
    transformer: Callable[[Any], Any] = lambda x: x
    choices: type[Enum] | None = None


class Ticket:
    def __init__(
        self,
        id: int,
        priority: Priority,
        title: str,
        description: str,
        assignedTechnician: Technician,
    ):
        self._id = id
        self._priority = self._validateAndTransformField("priority", priority)
        self._status = Status.TO_DO
        self._title = self._validateAndTransformField("title", title)
        self._description = description
        self._assignedTechnician = self._validateAndTransformField(
            "assignedTechnician", assignedTechnician
        )

    def _validateAndTransformField(self, field: str, value: Any) -> Any:
        fieldDetails = self.getFieldDetails()[field]
        validationError = fieldDetails.validator(value)
        if validationError is not None:
            raise ValueError(validationError)

        return fieldDetails.transformer(value)

    def _validateTitle(self, title: str) -> None:
        if not isinstance(title, str):
            raise TypeError(f"Invalid title '{title}': title must be a string")

        if not (3 <= len(title) and len(title) <= 50):
            raise ValueError(
                f"Invalid title '{title}': title must be between 3 and 50 characters long (inclusive)"
            )

    def _validatePriority(self, priority: str | Priority) -> None:
        if isinstance(priority, Priority):
            return

        if isinstance(priority, str):
            Priority(priority)
            return

        raise TypeError(
            f"Invalid priority '{priority}': priority must be a Priority, or string of:"
            + ", ".join([p.value for p in Priority])
        )

    def _validateStatus(self, status: str) -> None:
        if isinstance(status, Status):
            return

        if isinstance(status, str):
            Status(status)
            return

        raise TypeError(
            f"Invalid status '{status}': status must be a Status, or string of:"
            + ", ".join([s.value for s in Status])
        )

    def _validateTechnician(self, technician: str) -> None:
        if not isinstance(technician, str):
            return f"Invalid assignedTechnician '{technician}': assignedTechnician must be a string"

        return None

    def _transformTechnician(self, technician: str) -> Technician:
        return Technician(technician)

    def getFieldDetails(self) -> dict[str, FieldDetails]:
        return {
            "title": FieldDetails("title", "Title", True, False, self._validateTitle),
            "description": FieldDetails("description", "Description", True),
            "priority": FieldDetails(
                "priority",
                "Priority",
                True,
                True,
                self._validatePriority,
                Priority,
                Priority,
            ),
            "status": FieldDetails(
                "status",
                "Status",
                False,
                True,
                self._validateStatus,
                Status,
                Status,
            ),
            "assignedTechnician": FieldDetails(
                "assignedTechnician",
                "Assigned technician",
                True,
                True,
                self._validateTechnician,
                self._transformTechnician,
            ),
        }

    def updateField(self, field: str, value) -> bool:
        if self.getFieldDetails()[field].isMutable:
            value = self._validateAndTransformField(field, value)
            setattr(self, "_" + field, value)
            return True

        raise ValueError("Field is not mutable")

    def getTicketSummary(self) -> str:
        return f"#{self._id}: {self._title} - {self._status} [Assigned: {self._assignedTechnician}]"

    def getTicketDetails(self) -> str:
        banner = "=" * 3 + f"#{self._id}: {self._title} " + "=" * 3
        description = f"Description: {self._description}"
        status = f"Status: {self._status}"
        priority = f"Priority: {self._priority}"
        assignedTechnician = f"Assigned: {self._assignedTechnician}"

        return "\n".join([banner, description, status, priority, assignedTechnician])

    def getId(self) -> int:
        return self._id

    def getPriority(self) -> Priority:
        return self._priority

    def getStatus(self) -> Status:
        return self._status

    def getTitle(self) -> str:
        return self._title

    def getDescription(self) -> str:
        return self._description

    def getAssignedTechnician(self) -> Technician:
        return self._assignedTechnician
