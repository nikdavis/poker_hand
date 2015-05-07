from hand import *
from card_parser import *

def test_exhasts():
  assert isinstance(Hand,type)

def test_can_detect_ace_low_straight():
  hand = Hand(CardParser("2H 3D 5S 4C AD").dict())
  assert hand.has_straight() == True

def test_can_detect_true_straight():
  hand = Hand(CardParser("2H 3D 5S 4C 6D").dict())
  assert hand.has_straight() == True

def test_can_detect_false_straight():
  hand = Hand(CardParser("2H 3D 5S 8C AD").dict())
  assert hand.has_straight() == False

def test_can_detect_flush():
  hand = Hand(CardParser("2H 3H 5H 8H AH").dict())
  assert hand.has_flush() == True

def test_can_detect_false_flush():
  hand = Hand(CardParser("2H 3D 5S 8C AD").dict())
  assert hand.has_flush() == False

def test_can_detect_pairs():
  hand = Hand(CardParser("2H 2D 5S 8C AD").dict())
  assert hand.has_pair() == True

def test_can_detect_false_pairs():
  hand = Hand(CardParser("2H 9D 5S 8C AD").dict())
  assert hand.has_pair() == False

def test_can_detect_three_kind():
  hand = Hand(CardParser("AH AD AS 8C 2D").dict())
  assert hand.has_three_kind() == True

def test_can_detect_false_three_kind():
  hand = Hand(CardParser("AH 2D AS AC AD").dict())
  assert hand.has_three_kind() == False

def test_can_detect_four_kind():
  hand = Hand(CardParser("AH 2D AS AC AD").dict())
  assert hand.has_four_kind() == True

def test_can_detect_false_four_kind():
  hand = Hand(CardParser("2H 2D 2S 8C AD").dict())
  assert hand.has_four_kind() == False