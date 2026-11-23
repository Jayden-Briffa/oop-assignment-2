| Test suite | Purpose | Requirements verified |
| --- | --- | --- |
| [`test_Ticket.py`](../repo/src/tests/test_Ticket.py) | Verifies ticket validation, default values, field updates, technician assignment, and identifier access. | 2, 3, 4, 5, 7, 8 |
| [`test_FeatureRequest.py`](../repo/src/tests/test_FeatureRequest.py) | Verifies feature-request approval behaviour and the rules governing status changes before and after approval. | 3, 4, 7, 8 |
| [`test_IncidentResponse.py`](../repo/src/tests/test_IncidentResponse.py) | Verifies that incident-response tickets return readable details including their incident type. | 3, 6, 8 |
| [`test_TicketManager.py`](../repo/src/tests/test_TicketManager.py) | Verifies ticket creation, identifier allocation, retrieval, collection access, and ticket-field updates. | 1, 2, 4, 5, 6 |
| [`test_controllers.py`](../repo/src/tests/test_controllers.py) | Verifies controller workflows for creating, updating, approving, and viewing tickets, including the manual controller checks MaCT1–MaCT5. | 1, 2, 3, 4, 5, 6, 7, 8 |
