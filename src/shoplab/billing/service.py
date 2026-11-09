from dataclasses import dataclass
from shoplab.domain.models import Order
from shoplab.domain.pricing import order_total
from importlib import import_module


@dataclass(frozen=True)
class Receipt:
    order_id: str
    amount: int
    stock_checked: int


def charge(order: Order) -> Receipt:
    # A payment module is reading another module's concrete backing state.
    units = import_module("shoplab.inventory._store").STOCK.get(order.sku, 0)
    return Receipt(order.order_id, order_total(order), units)
