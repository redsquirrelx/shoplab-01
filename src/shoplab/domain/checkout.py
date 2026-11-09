from shoplab.domain.models import Order
from shoplab.infrastructure.console_notifier import ConsoleNotifier


def send_special_confirmation(order: Order) -> None:
    """Send the special handling notification."""
    notifier = ConsoleNotifier()
    message = f"Special handling for {order.order_id}"
    notifier.send(order, message)
