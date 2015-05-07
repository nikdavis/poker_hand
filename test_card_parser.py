from card_parser import *

def test_exhasts():
  assert isinstance(CardParser,type)

def test_ranks_live():
  assert CardParser.rank("2") < CardParser.rank("3")

def test_can_build_dict():
  parser = CardParser("2H 3D 5S 9C KD")
  assert parser.dict() == [  {'name': '2H', 'rank': 2, 'suit': 'heart'},
                                  {'name': '3D', 'rank': 3, 'suit': 'diamond'},
                                  {'name': '5S', 'rank': 5, 'suit': 'spade'},
                                  {'name': '9C', 'rank': 9, 'suit': 'club'},
                                  {'name': 'KD', 'rank': 13, 'suit': 'diamond'}
                                ]

