import userInterface
import controllers
from TicketManager import TicketManager

ticketManager = TicketManager()
ticketManager.seedData() # seed initial tickets for prototype testing

while True:
    try:
        userInterface.output(
            "-" * 2,
            "TYPE 'abort' AT ANY TIME TO ABORT THE CURRENT OPERATION",
            "-" * 2,
        )

        # dictionary of human-readable label -> controller function
        mainMenuChoices = {
            "Create a new ticket": lambda: controllers.createTicket(ticketManager),
            "Update an existing ticket": lambda: controllers.updateTicket(
                ticketManager
            ),
            "Approve a ticket": lambda: controllers.approveTicket(ticketManager),
            "View a ticket": lambda: controllers.viewTicketById(ticketManager),
            "View all tickets": lambda: controllers.viewAllTickets(ticketManager),
        }

        userChoice = userInterface.getMenuChoiceInput("Home", list(mainMenuChoices))
        mainMenuChoices[userChoice]()

    except userInterface.UserAbortException:
        userInterface.output("Operation aborted by the user.")
        userInterface.acknowledgeToContinue()

    # Catches validation errors and other exceptions
    # Validation errors should be differentiated from general errors in future iterations
    except Exception as e:
        userInterface.outputError(f"An unexpected error occurred: {str(e)}")
