from shoplab.inventory import stock_engine


def available_stock(sku: str) -> int:
    return stock_engine.read(sku)


def reserve_stock(sku: str, count: int) -> bool:
    return stock_engine.decrement(sku, count)
