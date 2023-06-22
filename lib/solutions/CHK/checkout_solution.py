from typing import NamedTuple, Callable


class IllegalItem(Exception):
    pass


class SKU(NamedTuple):
    name: str
    price: int


class SpecialOffer(NamedTuple):
    name: str
    applicable_sku: SKU
    should_apply: Callable[[list[SKU]], bool]
    skus_to_remove: list[SKU]
    reduced_price: int


A = SKU("A", 50)
B = SKU("B", 30)
C = SKU("C", 20)
D = SKU("D", 15)

SKU_TO_ITEMS = {
    "A": A,
    "B": B,
    "C": C,
    "D": D,
}

SPECIAL_OFFERS = [
    SpecialOffer(
        name="3A for 130",
        applicable_sku=A,
        should_apply=lambda skus: skus.count(A) == 3,
        skus_to_remove=[A, A, A],
        reduced_price=130,
    ),
    SpecialOffer(
        name="2B for 45",
        applicable_sku=B,
        should_apply=lambda skus: skus.count(B) == 2,
        skus_to_remove=[B, B],
        reduced_price=45,
    )
]


def parse_skus(skus: str) -> list[SKU]:
    """Takes a comma seperated str representing the basket and returns a list of SKUs

    Raises:
        IllegalItem if item is not known to the shop
    """
    sku_objects = []
    for sku_str in skus.split(","):
        if sku_str not in SKU_TO_ITEMS:
            raise IllegalItem
        sku_objects.append(SKU_TO_ITEMS[sku_str])
    return sku_objects


def remove_skus_in_offer_from_remaining_basket(offer: SpecialOffer, current_basket: list[SKU]) -> list[SKU]:
    remove_skus = offer.skus_to_remove
    for item in remove_skus:
        basket_items.fin


# noinspection PyUnusedLocal
# skus = unicode string
def checkout(skus: str) -> int:
    try:
        basket_items = parse_skus(skus)
    except IllegalItem:
        return -1

    total_checkout_value = 0

    # First apply offers (first assume offer applies once?)
    for offer in SPECIAL_OFFERS:
        if offer.should_apply:
            total_checkout_value += offer.reduced_price
            basket_items = remove_skus_in_offer_from_remaining_basket(offer, basket_items)

    # Go through remaining items after offers have been applied
    for item in basket_items:
        total_checkout_value += item.price

    return total_checkout_value




