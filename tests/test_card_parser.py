from poker_hand.parsers.card_parser import CardParser

def test_exhasts():
  assert isinstance(CardParser,type)

def test_can_parse():
  parser = CardParser("2H 3D 5S 9C KD")
  assert parser.ranks() == [2, 3, 5, 9, 13]
  assert parser.suits() == ["heart", "diamond", "spade", "club", "diamond"]

