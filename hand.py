from operator import itemgetter
from itertools import groupby
from card_parser import *
from collections import Counter
from ranked_hand import *

class Hand(object):
  def __init__(self, ranks, suits):
    self.ranks = ranks
    self.suits = suits
    self.best_hand = None
    self._remaining_cards = None
    self._pair_ranks = {  'one': None,
                          'two': None,
                          'three': None,
                          'four': None
                        }
    # Calculate the things
    self._of_a_kind()
    self._calc_rank()

  def has_straight(self):
    run = 0
    run_w_low_ace = 0
    ranks_sorted = sorted(self.ranks)
    if 14 in ranks_sorted:
      ranks_w_low_ace = list(self.ranks) # Account for Ace low only in straights!
      ranks_w_low_ace.append(1)
      ranks_w_low_ace.remove(14)
      print ranks_w_low_ace
      ranks_sorted_w_low_ace = sorted(ranks_w_low_ace)
      for i in range(1, len(ranks_sorted_w_low_ace)):
        if (ranks_sorted_w_low_ace[i] - ranks_sorted_w_low_ace[i-1]) == 1:
          run_w_low_ace += 1
    print ranks_sorted
    for i in range(1, len(ranks_sorted)):
      if (ranks_sorted[i] - ranks_sorted[i-1]) == 1:
        run += 1
    return run == 4 or run_w_low_ace == 4

  def has_flush(self):
    return len(set(self.suits)) == 1

  def _of_a_kind(self):
    """Returns a hash of k -> v, where key is rank and v is frequency"""
    counts = Counter(self.ranks)
    pair_count = 0
    pair_ranks = []
    for k, v in counts.iteritems():
      if v == 2:
        pair_count += 1
        pair_ranks.append(k)
      if v == 3:
        self._pair_ranks["three"] = k
      if v == 4:
        self._pair_ranks["four"] = k
    if pair_count == 1:
      self._pair_ranks["one"]  = pair_ranks[0]
      self._remaining_cards = [card for card in self.ranks if card not in pair_ranks]
    elif pair_count == 2:
      self._pair_ranks["two"]  = pair_ranks
      self._remaining_cards = [card for card in self.ranks if card not in pair_ranks]

  # Should be called after has_two_pair, so we don't need to worry about multiple pairs
  def has_pair(self):
    return self._pair_ranks["one"] != None

  def has_two_pair(self):
    return self._pair_ranks["two"] != None

  def has_three_kind(self):
    return self._pair_ranks["three"] != None

  def has_four_kind(self):
    return self._pair_ranks["four"] != None

  def has_full_house(self):
    return self.has_pair() and self.has_three_kind()

  def has_straight_flush(self):
    return self.has_straight() and self.has_flush()

  # Not used in this example
  def has_royal_flush(self):
    # Check for king to avoid ace low straight mistruth
    has_king_and_ace = 13 in self.ranks and 14 in self.ranks
    return has_king_and_ace and self.has_straight_flush()

  def _calc_rank(self):
    hand = None
    if(self.has_royal_flush()):
      hand = RoyalFlush()
    elif(self.has_straight_flush()):
      hand = StraightFlush(list(self.ranks))
    elif(self.has_four_kind()):
      hand = FourKind(self._pair_ranks["four"])
    elif(self.has_full_house()):
      hand = FullHouse(self._pair_ranks["three"])
    elif(self.has_flush()):
      hand = Flush(list(self.ranks))
    elif(self.has_straight()):
      hand = Straight(list(self.ranks))
    elif(self.has_three_kind()):
      hand = ThreeKind(self._pair_ranks["three"])
    elif(self.has_two_pair()):
      hand = TwoPair(self._pair_ranks["two"], list(self._remaining_cards))
    elif(self.has_pair()):
      hand = OnePair(self._pair_ranks["one"], list(self._remaining_cards))
    else:
      hand = HighCard(list(self.ranks))
    self.best_hand = hand












