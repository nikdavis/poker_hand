from operator import itemgetter
from itertools import groupby
from card_parser import *
from collections import Counter

class Hand(object):
  def __init__(self, ranks, suits):
    self.ranks = ranks
    self.suits = suits
    self.hands = []
    self._remaining_cards = None
    self._pair_ranks = {  'one': None,
                          'two': None,
                          'three': None,
                          'four': None
                        }
    # Calculate the things
    self._of_a_kind()

  def has_straight(self):
    ranks_sorted = sorted(self.ranks)
    if 14 in ranks_sorted:
      ranks_sorted.append(1) # Account for Ace low only in straights!
      ranks_sorted = sorted(ranks_sorted)
    run = 0
    for i in range(1, len(ranks_sorted)):
      if (ranks_sorted[i] - ranks_sorted[i-1]) == 1:
        run += 1
    return run == 4

    return 5 in [len(run) for run in arr_of_runs] # 5 sequential cards

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
    elif pair_count == 2:
      self._pair_ranks["two"]  = pair_ranks

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

  def calc_rank(self):
    hand = None
    if(self.has_straight_flush()):
      hand = StraightFlush(hands)
    elif(self.has_four_kind()):
      hand = FourKind(self._pair_ranks["four"])
    elif(self.has_full_house()):
      hand = FullHouse(self._pair_ranks["three"])
    elif(self.has_flush()):
      hand = Flush(self.ranks)
    elif(self.has_straight()):
      hand = Straight(self.ranks)
    elif(self.has_three_kind()):
      hand = 3
    elif(self.has_two_pair()):
      hand = 2
    elif(self.has_pair()):
      hand = 1
    return hand












