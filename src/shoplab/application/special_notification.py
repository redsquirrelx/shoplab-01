from shoplab.domain.models import Order
from shoplab.infrastructure.console_notifier import ConsoleNotifier


def send_special_confirmation(order: Order) -> None:
    ConsoleNotifier().send(order, f"Special handling for {order.order_id}")
