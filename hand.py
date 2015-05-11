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
    rank_sorted = sorted(self.ranks)
    if 14 in rank_sorted:
      rank_sorted.append(1) # Account for Ace low only in straights!
      rank_sorted = sorted(rank_sorted)
    arr_of_runs = []
    for k, g in groupby(enumerate(rank_sorted), lambda (i,x):i-x):
        arr_of_runs.append(map(itemgetter(1), g))
    print arr_of_runs
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
    print (self._pair_ranks)

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
    print has_king_and_ace
    print self.has_straight()
    print self.has_flush()
    return has_king_and_ace and self.has_straight_flush()

  def calc_rank(self):
    hand = None
    if(self.has_straight_flush()):
      hand = 8
    elif(self.has_four_kind()):
      rank = 7
    elif(self.has_full_house()):
      rank = 6
    elif(self.has_flush()):
      rank = 5
    elif(self.has_straight()):
      rank = 4
    elif(self.has_three_kind()):
      rank = 3
    elif(self.has_two_pair()):
      rank = 2
    elif(self.has_pair()):
      rank = 1
    return rank












