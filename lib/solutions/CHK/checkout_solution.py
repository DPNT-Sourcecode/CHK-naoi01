from typing import NamedTuple

class IllegalItem(Exception):
    pass

class BasketItem(NamedTuple):
    name: str
    price: int


SKU_TO_ITEMS = {
    "A": BasketItem("A", 50),
    "B": BasketItem("B", 30),
    "C": BasketItem("C", 20),
    "D": BasketItem("D", 15),
}


def parse_skus(skus: str) -> list[BasketItem]:
    for sku in skus.split(","):
        if sku not in SKU_TO_ITEMS:
            raise IllegalItem
        


# noinspection PyUnusedLocal
# skus = unicode string
def checkout(skus: str) -> int:
    try:
        basket_items = parse_skus(skus)
    except IllegalItem:
        return -1



