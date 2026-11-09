from shoplab.billing import charge
from shoplab.domain.models import Order
from shoplab.domain.notifications import send_confirmation
from shoplab.infrastructure.console_notifier import ConsoleNotifier
from shoplab.inventory import available_stock
from shoplab.orders import create_order


def process_order(order: Order) -> tuple[bool, int]:
    before = available_stock(order.sku)
    if not create_order(order):
        return False, before
    receipt = charge(order)
    send_confirmation(order, ConsoleNotifier())
    return True, receipt.amount
