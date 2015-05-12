from ranked_hand import *

def test_compare_between_child_child():
  high_card = HighCard([14, 10, 9, 5, 2])
  one_pair = OnePair([9, 9], [14, 10, 2])
  another_pair = OnePair([9, 9], [14, 10, 2])
  assert high_card < one_pair
  assert one_pair == another_pair

def test_function_high_card_comparison():
  high_card_hands  = HighCard([14, 10, 9, 5, 2]), HighCard([14, 10, 9, 3, 2])
  assert high_card_hands[0].compare_high_cards(high_card_hands[1]) == 1
  assert high_card_hands[1].compare_high_cards(high_card_hands[0]) == -1
  assert high_card_hands[0].compare_high_cards(high_card_hands[0]) == 0

def test_high_card():
  high, low  = HighCard([14, 10, 9, 5, 2]), HighCard([14, 10, 9, 3, 2])
  assert high > low
  assert (high < low) == False
  assert (high == low) == False
  assert high == high

def test_pair_decided_on_high_card():
  high, low  = OnePair(14, [9, 5, 2]), OnePair(14, [9, 3, 2])
  assert high > low
  assert high != low
  assert high == high

def test_two_pair_decided_on_high_pair():
  high, low  = TwoPair([14, 9], [8]), TwoPair([14, 9], [2])
  assert high > low
  assert high != low
  assert high == high

def test_two_pair_decided_on_low_pair():
  high, low  = TwoPair([14, 9], [8]), TwoPair([14, 8], [2])
  assert high > low
  assert high != low
  assert high == high

def test_three_kind_decided_on_three_kind():
  high, low  = ThreeKind(14), ThreeKind(10)
  assert high > low
  assert high != low

def test_straight_decided_straight():
  high, low  = Straight([14, 13, 12, 11, 10]), Straight([9, 8, 7, 6, 5])
  assert high.straight_rank == 14
  assert low.straight_rank == 9
  assert high > low
  assert high != low

def test_straight_ace_low():
  high, low  = Straight([14, 13, 12, 11, 10]), Straight([5, 4, 3, 2, 14])
  assert high.straight_rank == 14
  assert low.straight_rank == 5
  assert high > low
  assert high != low
  assert high == high

def test_flush():
  high, low  = Straight([14, 13, 2, 10, 10]), Straight([5, 4, 3, 2, 14])
  assert high > low
  assert high != low
  assert high == high

def test_full_house():
  high, low  = FullHouse(12), FullHouse(3),
  assert high > low
  assert high != low

def test_full_house():
  high, low  = FourKind(12), FourKind(3),
  assert high > low
  assert high != low

def test_straight_flush():
  high, low = StraightFlush([14, 13, 12, 11, 10]), StraightFlush([11, 10, 9, 8, 7]),
  high_no_flush = Straight([14, 13, 12, 11, 10])
  assert high > low
  assert high != low

def test_straight_flush_against_straight():
  high, low = StraightFlush([14, 13, 12, 11, 10]), Straight([14, 13, 12, 11, 10]),
  assert high > low
  assert high != low



