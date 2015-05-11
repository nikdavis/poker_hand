from ranked_hand import *

def test_equivalence_between_parent_child():
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
  high, low  = OnePair([14, 14], [9, 5, 2]), OnePair([14, 14], [9, 3, 2])
  assert high > low
  assert high != low
  assert high == high

def test_two_pair_decided_on_high_pair():
  high, low  = TwoPair([[14, 14], [9, 9]], [8]), TwoPair([[12, 12], [9, 9]], [2])
  assert high > low
  assert high != low
  assert high == high

def test_two_pair_decided_on_low_pair():
  high, low  = TwoPair([[14, 14], [9, 9]], [8]), TwoPair([[14, 14], [8, 8]], [2])
  assert high > low
  assert high != low
  assert high == high

def test_three_kind_decided_on_three_kind():
  high, low  = ThreeKind([14, 14, 14], [8, 4]), ThreeKind([10, 10, 10], [9, 2])
  assert high > low
  assert high != low






