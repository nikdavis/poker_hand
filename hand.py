from operator import itemgetter
from itertools import groupby
from card_parser import *
from collections import Counter

class Hand(object):
  def __init__(self, ranks, suits):
    """Expect CardParser dict of one hand"""
    self.ranks = ranks
    self.suits = suits
    self.hands = []

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

  def of_a_kind(self):
    """Returns a hash of any matches of a kind e.g. [], [2], or [2,3] for full house."""
    counts = Counter(self.ranks)
    print(counts)
    return counts

  # Should be called after has_two_pair, so we don't need to worry about multiple pairs
  def has_pair(self):
    counts = self.of_a_kind()
    rank = None
    for k, v in counts.iteritems():
      if v == 2:
        rank = k
    # save max rank later
    return rank != None

  def has_two_pair(self):
    counts = self.of_a_kind()
    ranks = []
    pair_count = 0
    for k, v in counts.iteritems():
      if v == 2:
        ranks.append(k)
        pair_count += 1
    return pair_count == 2

  def has_three_kind(self):
    counts = self.of_a_kind()
    rank = None
    for k, v in counts.iteritems():
      if v == 3:
        rank = k
    # save max rank later
    return rank != None

  def has_four_kind(self):
    counts = self.of_a_kind()
    rank = None
    for k, v in counts.iteritems():
      if v == 4:
        rank = k
    # save max rank later
    return rank != None

  def has_full_house(self):
    return self.has_pair() and self.has_three_kind()

  # Will be run after royal flush, so no need to check
  def has_straight_flush(self):
    return self.has_straight() and self.has_flush()

  def has_royal_flush(self):
    # Check for king to avoid ace low straight mistruth
    has_king_and_ace = 13 in self.ranks and 14 in self.ranks
    print has_king_and_ace
    print self.has_straight()
    print self.has_flush()
    return has_king_and_ace and self.has_straight_flush()

  def set_rank(self):
    if(self.has_royal_flush()):
      self.rank = 9
    elif(self.has_straight_flush()):
      self.rank = 8
    elif(self.has_four_kind()):
      self.rank = 7
    elif(self.has_full_house()):
      self.rank = 6
    elif(self.has_flush()):
      self.rank = 5
    elif(self.has_straight()):
      self.rank = 4
    elif(self.has_three_kind()):
      self.rank = 3
    elif(self.has_two_pair()):
      self.rank = 2
    elif(self.has_pair()):
      self.rank = 1











