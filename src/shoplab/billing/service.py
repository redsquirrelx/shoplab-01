from dataclasses import dataclass
from shoplab.domain.models import Order
from shoplab.domain.pricing import order_total
from shoplab.inventory import stock_for_billing


@dataclass(frozen=True)
class Receipt:
    order_id: str
    amount: int
    stock_checked: int


def charge(order: Order) -> Receipt:
    units = stock_for_billing(order.sku)
    return Receipt(order.order_id, order_total(order), units)
