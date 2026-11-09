import userInterface
import controllers as controllers
from TicketManager import TicketManager
from Ticket import Ticket
import userInterface

ticketManager = TicketManager()

while True:
    try:
        bannerBuffer = "-" * 2
        userInterface.output(
            bannerBuffer,
            "TYPE 'abort' AT ANY TIME TO ABORT THE CURRENT OPERATION",
            bannerBuffer,
        )

        bannerBuffer = "=" * 5
        mainMenuChoices = {
            "Create a new ticket": lambda: controllers.createTicket(ticketManager),
            "Update an existing ticket": lambda: controllers.updateTicket(
                ticketManager
            ),
            "View a ticket": lambda: controllers.viewTicket(ticketManager),
            "View all tickets": lambda: controllers.viewAllTickets(ticketManager),
        }

        userChoice = userInterface.executeMenu("Home", mainMenuChoices)

        controllers.saveTickets(ticketManager)

    except userInterface.UserAbortException:
        userInterface.output("Operation aborted by the user.")
        userInterface.acknowledgeToContinue()

    except Exception as e:
        userInterface.outputError(f"An unexpected error occurred: {str(e)}")
