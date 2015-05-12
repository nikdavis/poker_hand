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
    "T": 10,
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
    self.cards = card_str.split(" ")

  def ranks(self):
    return [self.RANK[card[0]] for card in self.cards]

  def suits(self):
    return [self.SUIT[card[-1]] for card in self.cards]


