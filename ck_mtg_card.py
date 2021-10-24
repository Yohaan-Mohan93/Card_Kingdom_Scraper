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
                + str(self.nm_price) + "|" + str(self.ex_price) + "|" + str(self.vg_price) + str(self.g_price))


@dataclass
class CkCardPlacement:
    name: str
    set: str
    place_in_page: int
    page_number: int

    def to_string(self):
        return self.name + "|" + self.set + "|" + str(self.place_in_page) + "|" + str(self.page_number)