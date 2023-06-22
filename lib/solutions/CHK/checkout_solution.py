from typing import NamedTuple


class BasketItem(NamedTuple):
    name: str
    price: int

PRICES = [
    BasketItem("A", 50),
    BasketItem("B", 30),
    BasketItem("C", 20),
    BasketItem("D", 15),
]

def parse_skus(skus: str) -> list[BasketItem]:


# noinspection PyUnusedLocal
# skus = unicode string
def checkout(skus: str) -> int:
    basket_items = parse_skus(skus)


