from dataclasses import dataclass

@dataclass
class ScgMtgCard:
    id : int
    name : str
    type : str
    set : str
    rarity : str
    nm_price : float
    card_text : str

    def to_string(self):
        return (str(self.id) +'|' + self.name + "|" + self.type + "|" + self.set + "|" + self.rarity + "|"
                + str(self.nm_price) + "|" + "|" + self.card_text)