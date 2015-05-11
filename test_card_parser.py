from card_parser import *

def test_exhasts():
  assert isinstance(CardParser,type)

def test_ranks_live():
  assert CardParser.rank("2") < CardParser.rank("3")

def test_can_parse():
  parser = CardParser("2H 3D 5S 9C KD")
  print parser.suits()
  assert parser.suits() == ["heart", "diamond", "spade", "club", "diamond"]

