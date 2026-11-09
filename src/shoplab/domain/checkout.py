from shoplab.domain.models import Order
from shoplab.domain.ports import Notifier
from shoplab.infrastructure.console_notifier import ConsoleNotifier


def send_special_confirmation(order: Order, notifier: Notifier | None = None) -> None:
    notifier = notifier or ConsoleNotifier()
    notifier.send(order, f"Special handling for {order.order_id}")
