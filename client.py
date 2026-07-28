class SupportTicketRouterClient:
    def route_ticket(self, ticket_text: str) -> dict:
        return {
            "priority": 'CRITICAL_P0'
        }
