# Test table

The automated tests are in `repo/src/tests`.

Shared setup from `conftest.py` provides `dummyTicketManager`, a
`TicketManager` containing three tickets with `_lastId` set to `3`:

- `1`: `IncidentResponse`, High, In Progress, “Cannot access account”, technician “Alex”, type Cyber Security
- `2`: `FeatureRequest`, Medium, Needs Approval, “Add export option”, technician “Sam”
- `3`: `Ticket`, Low, To Do, “Update help text”, technician “Jordan”

`userInterface.outputError` is mocked for every test. Controller tests also
mock user input and ticket output where required.

The `Requirements` column uses the requirement numbers from
[`requirements.md`](../requirements.md).

## Ticket (`test_Ticket.py`)

| Id | Description | Set up | Data | Test type | Expected result | Requirements | Prerequisites |
| --- | --- | --- | --- | --- | --- | --- | --- |
| TK1 | Accept a valid priority | Generate a test ticket | `Priority.HIGH` | Normal | The priority validator returns `None` | 7 | N/A |
| TK2 | Reject an invalid priority | Generate a test ticket | `"InvalidPriority"` | Invalid | The priority validator raises `ValueError` | 7 | N/A |
| TK3 | Update a ticket priority | Generate a test ticket | Update `priority` to `Priority.MEDIUM` | Normal | `getPriority().value` is `"Medium"` | 4, 8 | N/A |
| TK4 | Accept a valid status | Generate a test ticket | `Status.IN_PROGRESS` | Normal | The status validator returns `None` | 7 | N/A |
| TK5 | Reject an invalid status | Generate a test ticket | `"InvalidStatus"` | Invalid | The status validator raises `ValueError` | 7 | N/A |
| TK6 | Update a ticket status | Generate a test ticket | Update `status` to `Status.COMPLETED` | Normal | `getStatus().value` is `"Completed"` | 4, 8 | N/A |
| TK7 | Preserve the To Do status | Construct a `Ticket` directly | id `1`, priority High, status `Status.TO_DO`, title `"Test Ticket"`, description `"Description"`, technician `"Test Technician"` | Normal | `getStatus()` is `Status.TO_DO` | 3, 8 | N/A |
| TK8 | Assign a technician | Generate a test ticket | Update `assignedTechnician` to `"New Technician"` | Normal | `getAssignedTechnician()` is `"New Technician"` | 5, 8 | N/A |
| TK9 | Get a ticket id | Generate a test ticket | N/A | Normal | `getId()` returns `1` | 2, 8 | N/A |
| TK10 | Accept a title at the upper length boundary | Generate a test ticket | A title containing 50 characters | Boundary | The title validator returns `None` | 7, 8 | N/A |
| TK11 | Accept a title at the lower length boundary | Generate a test ticket | A title containing 3 characters | Boundary | The title validator returns `None` | 7, 8 | N/A |
| TK12 | Reject a title above the upper length boundary | Generate a test ticket | A title containing 51 characters | Invalid/ Boundary | The title validator raises `ValueError` | 7, 8 | N/A |
| TK13 | Reject a title below the lower length boundary | Generate a test ticket | A title containing 2 characters | Invalid/ Boundary | The title validator raises `ValueError` | 7, 8 | N/A |

## FeatureRequest (`test_FeatureRequest.py`)

| Id | Description | Set up | Data | Test type | Expected result | Requirements | Prerequisites |
| --- | --- | --- | --- | --- | --- | --- | --- |
| FR1 | Preserve the Needs Approval status | Construct a `FeatureRequest` directly | id `1`, priority High, status `Status.NEEDS_APPROVAL`, title `"Test Feature"`, description `"Description"`, technician `"Test Technician"` | Normal | `getStatus()` is `Status.NEEDS_APPROVAL` | 3, 8 | N/A |
| FR2 | Allow a status change after approval | Generate a test feature request and call `approve()` | Validate change to `Status.TO_DO` | Normal | `validateStatus()` returns `None` | 3, 4, 8 | FR1 |
| FR3 | Reject a status change before approval | Generate a test feature request without approving it | Validate change to `Status.TO_DO` | Invalid | `validateStatus()` raises `ValueError` | 3, 7, 8 | FR1 |

## IncidentResponse (`test_IncidentResponse.py`)

| Id | Description | Set up | Data | Test type | Expected result | Requirements | Prerequisites |
| --- | --- | --- | --- | --- | --- | --- | --- |
| IR1 | Return incident ticket details | Construct an `IncidentResponse` | id `1`, priority High, status In Progress, title `"Cannot access account"`, description `"User is unable to sign in."`, technician `"Alex"`, type `IncidentType.CYBER_SECURITY` | Normal | `getTicketDetails()` returns a string containing the title and `"Incident Type: IncidentType.CYBER_SECURITY"` | 3, 6, 8 | N/A |

## TicketManager (`test_TicketManager.py`)

| Id | Description | Set up | Data | Test type | Expected result | Requirements | Prerequisites |
| --- | --- | --- | --- | --- | --- | --- | --- |
| TM1 | Create a ticket | Use `dummyTicketManager` with three loaded tickets | Type `TicketType.NONE`; High; To Do; title `"Test Ticket"`; description `"This is a test ticket."`; technician `"Test Technician"` | Normal | New id is `4`; four tickets are loaded; `_lastId` is `4`; the new title is `"Test Ticket"` | 1, 2 | N/A |
| TM2 | Get a ticket by id | Use `dummyTicketManager` | id `2` | Normal | The returned ticket id is `2` | 2, 6 | N/A |
| TM3 | Get all tickets | Use `dummyTicketManager` | N/A | Normal | The returned tickets equal the fixture data | 6 | N/A |
| TM4 | Update ticket status | Use `dummyTicketManager` | id `1`; status `Status.TO_DO` | Normal | Ticket `1` has status `Status.TO_DO` | 4 | TM2 |
| TM5 | Update ticket priority | Use `dummyTicketManager` | id `1`; priority `Priority.LOW` | Normal | Ticket `1` has priority `Priority.LOW` | 4 | TM2 |
| TM6 | Update assigned technician | Use `dummyTicketManager` | id `1`; `Technician("Technician1")` | Normal | Ticket `1` has that `Technician` object assigned | 5 | TM2 |
| TM7 | Create the first ticket in an empty manager | Construct `TicketManager(loadedTickets={}, lastId=0)` | Type `TicketType.NONE`; High; To Do; title `"First Ticket"`; description `"This is the first ticket."`; technician `"Test Technician"` | Boundary | New id is `1`; the only loaded ticket has id `1`; `_lastId` is `1` | 1, 2 | TM1 |

## Controllers (`test_controllers.py`)

| Id | Description | Set up | Data | Test type | Expected result | Requirements | Prerequisites |
| --- | --- | --- | --- | --- | --- | --- | --- |
| CT1 | Create a standard ticket | Use `dummyTicketManager`; mock prompts and output | Type `Ticket`; title `"additional ticket"`; description `"additional description"`; priority High; status To Do; technician `"jamie"` | Normal | Ticket `4` is returned and stored as a `Ticket` with the supplied values | 1, 2, 3, 7, 8 | TM1 |
| CT2 | Update ticket priority | Use `dummyTicketManager`; select ticket `3`; mock prompts and output | Field `Priority`; priority High; all other fields retain their current values | Normal | Ticket `3` has High priority and unchanged remaining fields; returned and stored tickets match | 4, 7 | TM5 |
| CT3 | Update ticket status | Use `dummyTicketManager`; select ticket `3`; mock prompts and output | Field `Status`; status In Progress; all other fields retain their current values | Normal | Ticket `3` has In Progress status and unchanged remaining fields; returned and stored tickets match | 4, 7 | TM4 |
| CT4 | Update assigned technician | Use `dummyTicketManager`; select ticket `3`; mock prompts and output | Field `Assigned technician`; technician `"jamie"`; all other fields retain their current values | Normal | Ticket `3` has technician `"jamie"` and unchanged remaining fields; returned and stored tickets match | 5, 7 | TM6 |
| CT5 | Approve a feature request | Use `dummyTicketManager`; select ticket `2`; mock confirmation `"yes"` | id `2`; approval confirmation `yes` | Normal | Ticket `2` is approved and the returned and stored tickets match | 3, 4, 7, 8 | FR2 |
| CT6 | View a ticket by id | Use `dummyTicketManager`; mock input and output | id `2` | Normal | The returned ticket has id `2` | 2, 6, 7 | TM2 |
| CT7 | View all tickets | Use `dummyTicketManager` | N/A | Normal | All three tickets are returned with the same keys as the manager | 6 | TM3 |
| MaCT1 | Create a FeatureRequest | None |  | Normal | Ticket is created | 1, 2 | N/A |
| MaCT2 | Update an IncidentResponse status | None | id `2`; new status `Completed` | Normal | Ticket `2` is updated | 4 | FR2 |
| MaCT3 | View a ticket | None | id `2` | Normal | The returned ticket has id `2` and is readable | 2, 6 | TM2 |
| MaCT4 | View all tickets | None | N/A | Normal | All tickets are returned with limited detail and are readable | 6 | TM3 |
| MaCT5 | Ticket approval does not show any non-approvable tickets | None | N/A | Normal | Only approvable tickets are shown | 3 | FR2 |
