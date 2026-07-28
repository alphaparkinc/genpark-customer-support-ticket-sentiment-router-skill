from client import SupportTicketRouterClient

def main():
    client = SupportTicketRouterClient()
    res = client.route_ticket(ticket_text='System is DOWN! Emergency!')
    print(f"Result for priority: {res['priority']}")

if __name__ == "__main__":
    main()
