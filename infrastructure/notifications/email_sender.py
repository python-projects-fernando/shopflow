from domain.interfaces import INotificationSender

class EmailSender(INotificationSender):
    def send_confirmation(self, email: str, order_id: str) -> None:
        # In production, integrate with SMTP or a service like SendGrid
        print(f"[EMAIL] Sent to {email}: Order {order_id} confirmed!")