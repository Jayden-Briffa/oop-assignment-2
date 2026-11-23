# Ticket Management System

This repository contains a command-line ticket management system written in
Python. It supports creating, viewing, updating, and approving tickets,
including feature requests and incident responses.

## Usage

From the repository root, create and activate a virtual environment and
install the dependencies:

```bash
cd src
python -m venv .venv
source .venv/bin/activate       # macOS/Linux
# .venv\Scripts\activate        # Windows
python -m pip install -r requirements.txt
```

Alternatively, with uv:

```bash
cd src
uv venv
source .venv/bin/activate       # macOS/Linux
# .venv\Scripts\activate        # Windows
uv pip install -r requirements.txt
```

Start the interactive application from the `src` directory:

```bash
python main.py
```

The application loads sample tickets and displays a menu with options to perform CRUD operations on Tickets
Prompts accept either the displayed menu number or the full menu option. Type
`abort` during an operation to cancel it.

## Testing

Install the project dependencies as described above, then run the test suite
from the `src` directory:

```bash
pytest
```

Pytest is configured in [`src/pytest.ini`](src/pytest.ini) to add `src` to the
Python path and discover tests in [`src/tests`](src/tests).

## Repository structure

```text
repo/
├── README.md
└── src/
    ├── main.py                 # Application entry point
    ├── controllers.py          # Menu actions and application workflows
    ├── userInterface.py        # Input, menus, and console output
    ├── Ticket.py               # Ticket model, fields, validation, and enums
    ├── FeatureRequest.py       # Feature-request ticket type
    ├── IncidentResponse.py     # Incident-response ticket type
    ├── Technician.py           # Technician value object
    ├── TicketManager.py        # Ticket creation, lookup, and updates
    ├── UserAbortException.py   # User cancellation exception
    ├── helpers.py              # Shared test/application helpers
    ├── requirements.txt        # Runtime and test dependencies
    ├── pytest.ini              # Pytest configuration
    └── tests/                  # Automated tests for models and workflows
```

`TicketManager` stores tickets in memory, while `controllers.py` coordinates those models
with the interactive UI.

## Code formatting

The dependencies include Black for formatting. To check or format the Python
source from `src`, run:

```bash
black --check .
black .
```