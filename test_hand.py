from hand import *
from card_parser import *

def test_exhasts():
  assert isinstance(Hand,type)

def test_can_detect_ace_low_straight():
  cards = "2H 3D 5S 4C AD"
  parser = CardParser(cards)
  hand = Hand(parser.ranks(), parser.suits())
  assert hand.has_straight() == True


def test_can_detect_straight():
  cards = "2H 3D 5S 4C 6D"
  parser = CardParser(cards)
  hand = Hand(parser.ranks(), parser.suits())
  assert hand.has_straight() == True

def test_can_detect_false_straight():
  cards = "2H 3D 5S 8C AD"
  parser = CardParser(cards)
  hand = Hand(parser.ranks(), parser.suits())
  assert hand.has_straight() == False

def test_can_detect_flush():
  cards = "2H 3H 5H 8H AH"
  parser = CardParser(cards)
  hand = Hand(parser.ranks(), parser.suits())
  assert hand.has_flush() == True

def test_can_detect_false_flush():
  cards = "2H 3D 5S 8C AD"
  parser = CardParser(cards)
  hand = Hand(parser.ranks(), parser.suits())
  assert hand.has_flush() == False

def test_can_detect_pair():
  cards = "2H 2D 5S 8C AD"
  parser = CardParser(cards)
  hand = Hand(parser.ranks(), parser.suits())
  assert hand.has_pair() == True

def test_can_detect_false_pair():
  cards = "2H 9D 5S 8C AD"
  parser = CardParser(cards)
  hand = Hand(parser.ranks(), parser.suits())
  assert hand.has_pair() == False

def test_can_detect_two_pair():
  cards = "2H 2D 9S 9C AD"
  parser = CardParser(cards)
  hand = Hand(parser.ranks(), parser.suits())
  assert hand.has_pair() == True

def test_can_detect_false_two_pair():
  cards = "2H 9D 5S 8C AD"
  parser = CardParser(cards)
  hand = Hand(parser.ranks(), parser.suits())
  assert hand.has_pair() == False

def test_can_detect_three_kind():
  cards = "AH AD AS 8C 2D"
  parser = CardParser(cards)
  hand = Hand(parser.ranks(), parser.suits())
  assert hand.has_three_kind() == True

def test_can_detect_false_three_kind():
  cards = "AH 2D AS AC AD"
  parser = CardParser(cards)
  hand = Hand(parser.ranks(), parser.suits())
  assert hand.has_three_kind() == False

def test_can_detect_four_kind():
  cards = "AH 2D AS AC AD"
  parser = CardParser(cards)
  hand = Hand(parser.ranks(), parser.suits())
  assert hand.has_four_kind() == True

def test_can_detect_false_four_kind():
  cards = "2H 2D 2S 8C AD"
  parser = CardParser(cards)
  hand = Hand(parser.ranks(), parser.suits())
  assert hand.has_four_kind() == False

def test_can_detect_straight_flush():
  cards = "8H 9H TH JH QH"
  parser = CardParser(cards)
  hand = Hand(parser.ranks(), parser.suits())
  assert hand.has_four_kind() == False

def test_can_detect_false_straight_flush():
  cards = "2H 3D 5S 4C 6D"
  parser = CardParser(cards)
  hand = Hand(parser.ranks(), parser.suits())
  assert hand.has_four_kind() == False

def test_can_detect_royal_flush():
  cards = "TD JD QD KD AD"
  parser = CardParser(cards)
  hand = Hand(parser.ranks(), parser.suits())
  assert hand.has_four_kind() == False

def test_can_detect_false_royal_flush():
  cards = "TD JD QD KD AH"
  parser = CardParser(cards)
  hand = Hand(parser.ranks(), parser.suits())
  assert hand.has_four_kind() == False


