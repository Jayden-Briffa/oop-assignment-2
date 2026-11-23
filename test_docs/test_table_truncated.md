
## Ticket (`test_Ticket.py`)

| Id | Description | Test type | Expected result | Requirements |
| --- | --- | --- | --- | --- |
| TK1 | Accept a valid priority | Normal | The priority validator returns `None` | 7 |
| TK2 | Reject an invalid priority | Invalid | The priority validator raises `ValueError` | 7 |
| TK3 | Update a ticket priority | Normal | `getPriority().value` is `"Medium"` | 4, 8 |
| TK4 | Accept a valid status | Normal | The status validator returns `None` | 7 |
| TK5 | Reject an invalid status | Invalid | The status validator raises `ValueError` | 7 |
| TK6 | Update a ticket status | Normal | `getStatus().value` is `"Completed"` | 4, 8 |
| TK7 | Preserve the To Do status | Normal | `getStatus()` is `Status.TO_DO` | 3, 8 |
| TK8 | Assign a technician | Normal | `getAssignedTechnician()` is `"New Technician"` | 5, 8 |
| TK9 | Get a ticket id | Normal | `getId()` returns `1` | 2, 8 |
| TK10 | Accept a title at the upper length boundary | Boundary | The title validator returns `None` | 7, 8 |
| TK11 | Accept a title at the lower length boundary | Boundary | The title validator returns `None` | 7, 8 |
| TK12 | Reject a title above the upper length boundary | Invalid/ Boundary | The title validator raises `ValueError` | 7, 8 |
| TK13 | Reject a title below the lower length boundary | Invalid/ Boundary | The title validator raises `ValueError` | 7, 8 |

## FeatureRequest (`test_FeatureRequest.py`)

| Id | Description | Test type | Expected result | Requirements |
| --- | --- | --- | --- | --- |
| FR1 | Preserve the Needs Approval status | Normal | `getStatus()` is `Status.NEEDS_APPROVAL` | 3, 8 |
| FR2 | Allow a status change after approval | Normal | `validateStatus()` returns `None` | 3, 4, 8 |
| FR3 | Reject a status change before approval | Invalid | `validateStatus()` raises `ValueError` | 3, 7, 8 |

## IncidentResponse (`test_IncidentResponse.py`)

| Id | Description | Test type | Expected result | Requirements |
| --- | --- | --- | --- | --- |
| IR1 | Return incident ticket details | Normal | `getTicketDetails()` returns a string containing the title and `"Incident Type: IncidentType.CYBER_SECURITY"` | 3, 6, 8 |

## TicketManager (`test_TicketManager.py`)

| Id | Description | Test type | Expected result | Requirements |
| --- | --- | --- | --- | --- |
| TM1 | Create a ticket | Normal | New id is `4`; four tickets are loaded; `_lastId` is `4`; the new title is `"Test Ticket"` | 1, 2 |
| TM2 | Get a ticket by id | Normal | The returned ticket id is `2` | 2, 6 |
| TM3 | Get all tickets | Normal | The returned tickets equal the fixture data | 6 |
| TM4 | Update ticket status | Normal | Ticket `1` has status `Status.TO_DO` | 4 |
| TM5 | Update ticket priority | Normal | Ticket `1` has priority `Priority.LOW` | 4 |
| TM6 | Update assigned technician | Normal | Ticket `1` has that `Technician` object assigned | 5 |
| TM7 | Create the first ticket in an empty manager | Boundary | New id is `1`; the only loaded ticket has id `1`; `_lastId` is `1` | 1, 2 |

## Controllers (`test_controllers.py`)

| Id | Description | Test type | Expected result | Requirements |
| --- | --- | --- | --- | --- |
| CT1 | Create a standard ticket | Normal | Ticket `4` is returned and stored as a `Ticket` with the supplied values | 1, 2, 3, 7, 8 |
| CT2 | Update ticket priority | Normal | Ticket `3` has High priority and unchanged remaining fields; returned and stored tickets match | 4, 7 |
| CT3 | Update ticket status | Normal | Ticket `3` has In Progress status and unchanged remaining fields; returned and stored tickets match | 4, 7 |
| CT4 | Update assigned technician | Normal | Ticket `3` has technician `"jamie"` and unchanged remaining fields; returned and stored tickets match | 5, 7 |
| CT5 | Approve a feature request | Normal | Ticket `2` is approved and the returned and stored tickets match | 3, 4, 7, 8 |
| CT6 | View a ticket by id | Normal | The returned ticket has id `2` | 2, 6, 7 |
| CT7 | View all tickets | Normal | All three tickets are returned with the same keys as the manager | 6 |
| MaCT1 | Create a FeatureRequest | Normal | Ticket is created | 1, 2 |
| MaCT2 | Update an IncidentResponse status | Normal | Ticket `2` is updated | 4 |
| MaCT3 | View a ticket | Normal | The returned ticket has id `2` and is readable | 2, 6 |
| MaCT4 | View all tickets | Normal | All tickets are returned with limited detail and are readable | 6 |
| MaCT5 | Ticket approval does not show any non-approvable tickets | Normal | Only approvable tickets are shown | 3 |
