from shoplab.domain.models import Order
from importlib import import_module


def send_special_confirmation(order: Order) -> None:
    notifier = import_module("shoplab.infrastructure.console_notifier").ConsoleNotifier()
    notifier.send(order, f"Special handling for {order.order_id}")
