# ITEC 204 - Laboratory Exercise 1
class IncidentTicket:

    # Constructor
    def __init__(self, incident_id, bot, description):
        self.incident_id = incident_id
        self.bot = bot
        self.description = description


class IncidentTicketManager:

    # Constructor
    def __init__(self):
        self.tickets = []

    # Add a new ticket
    def add_ticket(self):
        incident_id = input("Enter Incident ID: ")
        bot = input("Enter Bot: ")
        description = input("Enter Short Description: ")

        ticket = IncidentTicket(incident_id, bot, description)
        self.tickets.append(ticket)

        print("Ticket added successfully!")

    # Display all tickets
    def display_tickets(self):
        print("\n===== ACTIVE INCIDENT TICKETS =====")

        if len(self.tickets) == 0:
            print("No active incident tickets.")
        else:
            for ticket in self.tickets:
                print("Incident ID:", ticket.incident_id)
                print("Bot:", ticket.bot)
                print("Short Description:", ticket.description)
                print("--------------------------------")

    # Search ticket
    def search_ticket(self):
        search_id = input("Enter Incident ID to search: ")

        for ticket in self.tickets:
            if ticket.incident_id == search_id:
                print("\nTicket found!")
                print("Incident ID:", ticket.incident_id)
                print("Bot:", ticket.bot)
                print("Short Description:", ticket.description)
                return

        print("Ticket not found.")

    # Remove ticket
    def remove_ticket(self):
        remove_id = input("Enter Incident ID to remove: ")

        for ticket in self.tickets:
            if ticket.incident_id == remove_id:
                self.tickets.remove(ticket)
                print("Ticket removed successfully!")
                return

        print("Ticket not found.")

    # Count tickets
    def count_tickets(self):
        print("Total number of active tickets:", len(self.tickets))


# Create Incident Ticket Manager
manager = IncidentTicketManager()


# Sample tickets
manager.tickets.append(
    IncidentTicket("INC1392939", "BOT-Inventory",
                   "Failed to generate the daily report")
)

manager.tickets.append(
    IncidentTicket("INC1392940", "BOT-Email",
                   "Failed to send the scheduled notification")
)

manager.tickets.append(
    IncidentTicket("INC1392941", "BOT-DataSync",
                   "Encountered an error during data transfer")
)

manager.tickets.append(
    IncidentTicket("INC1392942", "BOT-Invoice",
                   "Failed to process an invoice")
)

manager.tickets.append(
    IncidentTicket("INC1392943", "BOT-Report",
                   "Failed to generate the weekly report")
)

manager.tickets.append(
    IncidentTicket("INC1392944", "BOT-FileTransfer",
                   "Failed to upload the required file")
)

manager.tickets.append(
    IncidentTicket("INC1392945", "BOT-DataEntry",
                   "Encountered an error while entering records")
)

manager.tickets.append(
    IncidentTicket("INC1392946", "BOT-Backup",
                   "Failed to complete the scheduled backup")
)

manager.tickets.append(
    IncidentTicket("INC1392947", "BOT-Validation",
                   "Failed to validate the submitted records")
)

manager.tickets.append(
    IncidentTicket("INC1392948", "BOT-Notification",
                   "Failed to send the system alert")
)


# Main Menu
while True:

    print("\n====================================")
    print("   INCIDENT TICKET MANAGER")
    print("====================================")
    print("1. Add New Incident Ticket")
    print("2. Display All Active Incident Tickets")
    print("3. Search for an Incident Ticket")
    print("4. Remove a Resolved ticket")
    print("5. Display Total Active Incident Tickets")
    print("6. Exit")
    print("====================================")

    choice = input("Enter your choice: ")

    if choice == "1":
        manager.add_ticket()

    elif choice == "2":
        manager.display_tickets()

    elif choice == "3":
        manager.search_ticket()

    elif choice == "4":
        manager.remove_ticket()

    elif choice == "5":
        manager.count_tickets()

    elif choice == "6":
        print("Thank you for using the Incident Ticket Manager!")
        break

    else:
        print("Invalid choice. Please try again.")
