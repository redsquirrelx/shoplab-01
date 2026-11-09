from shoplab.domain.models import Order
from shoplab.infrastructure.console_notifier import ConsoleNotifier


def send_via_bridge(order: Order, message: str) -> None:
    ConsoleNotifier().send(order, message)
