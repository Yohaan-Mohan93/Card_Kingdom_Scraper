from dataclasses import dataclass


@dataclass
class CkMtgCard:
    name: str
    type: str
    set: str
    rarity: str
    nm_price: float
    ex_price: float
    vg_price: float
    g_price: float

    def to_string(self):
        return (self.name + "|" + self.type + "|" + self.set + "|" + self.rarity + "|"
                + self.nm_price + "|" + self.ex_price + "|" + self.vg_price + self.g_price)


@dataclass
class CkCardPlacement:
    name: str
    set: str
    place_in_page: int
    page_number: int
