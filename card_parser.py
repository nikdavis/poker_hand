class CardParser(object):
  RANK = {
    "2": 2,
    "3": 3,
    "4": 4,
    "5": 5,
    "6": 6,
    "7": 7,
    "8": 8,
    "9": 9,
    "10": 10,
    "J": 11,
    "Q": 12,
    "K": 13,
    "A": 14
  }

  SUIT = {
    "H": "heart",
    "D": "diamond",
    "C": "club",
    "S": "spade"
  }

  def __init__(self, card_str):
    """Takes one hands string, returns dict"""
    self.card_str = card_str

  @classmethod
  def rank(cls, card_num_str):
    return cls.RANK[card_num_str]

  @classmethod
  def suit(cls, card_suit_ltr):
    return cls.SUIT[card_suit_ltr]

  def dict(self):
    card_dict = []
    cards = self.card_str.split(" ")
    for card in cards:
      card_dict.append({"name": card, "rank": self.rank(card[0]), "suit": self.suit(card[-1])})
    return card_dict