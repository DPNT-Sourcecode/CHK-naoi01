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
E = SKU("E", 40)

SKU_STR_TO_ITEMS = {
    "A": A,
    "B": B,
    "C": C,
    "D": D,
    "E": E,
}

SPECIAL_OFFERS = [
    # This is better than "3A for 130" so apply this first
    SpecialOffer(
        name="5A for 200",
        applicable_sku=A,
        should_apply=lambda skus: skus.count(A) >= 5,
        skus_to_remove=[A, A, A, A, A],
        reduced_price=200,
    ),
    SpecialOffer(
        name="3A for 130",
        applicable_sku=A,
        should_apply=lambda skus: skus.count(A) >= 3 and skus.count(A) < 5,
        skus_to_remove=[A, A, A],
        reduced_price=130,
    ),
    SpecialOffer(
        name="2B for 45",
        applicable_sku=B,
        should_apply=lambda skus: skus.count(B) >= 2,
        skus_to_remove=[B, B],
        reduced_price=45,
    ),
    SpecialOffer(
        name="2E get one B free",
        applicable_sku=E,
        should_apply=lambda skus: skus.count(E) >= 2 and skus.count(B) >= 1,
        skus_to_remove=[E, E, B],
        reduced_price=80,
    )
]


def parse_skus(skus: str) -> list[SKU]:
    """Takes a unicode str representing the basket and returns a list of SKUs

    Examples:
        >>> parse_skus("AAAA")
        ... [A, A, A, A]

    Raises:
        IllegalItem if item is not known to the shop
    """
    sku_objects = []
    for sku_str in list(skus):
        if sku_str not in SKU_STR_TO_ITEMS:
            raise IllegalItem
        sku_objects.append(SKU_STR_TO_ITEMS[sku_str])
    return sku_objects


def remove_skus_in_offer_from_remaining_basket(offer: SpecialOffer, current_basket: list[SKU]) -> list[SKU]:
    remove_skus = offer.skus_to_remove
    for item in remove_skus:
        # value error shouldn't be raised as we have already checked offer applies
        index_of_item = current_basket.index(item)
        current_basket.pop(index_of_item)
    return current_basket


def basket_contains_applicable_offers(current_basket: list[SKU]) -> bool:
    for offer in SPECIAL_OFFERS:
        if offer.should_apply(current_basket):
            return True

    return False


# skus = unicode string
def checkout(skus: str) -> int:
    try:
        basket_items = parse_skus(skus)
    except IllegalItem:
        return -1

    total_checkout_value = 0

    # First apply offers (which could be applicable multiple times)
    while basket_contains_applicable_offers(basket_items):
        for offer in SPECIAL_OFFERS:
            if offer.should_apply(basket_items):
                total_checkout_value += offer.reduced_price
                basket_items = remove_skus_in_offer_from_remaining_basket(offer, basket_items)

    # Go through remaining items after offers have been applied
    for item in basket_items:
        total_checkout_value += item.price

    return total_checkout_value


