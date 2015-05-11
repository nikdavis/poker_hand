class RankedHand(object):
  def __init__(self, remaining_cards):
    self._remaining_cards = remaining_cards
    self._rank = None

  def rank(self):
    return self._rank

  def remaining_cards(self):
    return self._remaining_cards

  # Returns 1 if self is higher, 0 if equal, -1 if self is lower
  def compare_high_cards(self, other):
    s_cards = reversed(sorted(self.remaining_cards()))
    o_cards = reversed(sorted(other.remaining_cards()))
    for card_pair in zip(s_cards, o_cards):
      print("Comparing %s and %s" % (str(card_pair[0]), str(card_pair[1])))
      if(card_pair[0] > card_pair[1]):
        return 1
      elif(card_pair[0] < card_pair[1]):
        return -1
    return 0

  def __eq__(self, other):
    return self.rank() == other.rank()

  def __lt__(self, other):
    return self.rank() < other.rank()

class HighCard(RankedHand):
  def __init__(self, remaining_cards):
    super(HighCard, self).__init__(remaining_cards)
    self._rank = 0

  def __eq__(self, other):
    if self.rank() != other.rank():
      return super(HighCard, self).__eq__(other)
    else:
      return self.compare_high_cards(other) == 0

  def __lt__(self, other):
    if self.rank() != other.rank():
      return super(HighCard, self).__lt__(other)
    else:
      return self.compare_high_cards(other) == -1

class OnePair(RankedHand):
  def __init__(self, pair_cards, remaining_cards):
    super(OnePair, self).__init__(remaining_cards)
    self._rank = 1
    self._pair_cards = pair_cards

  def pair_cards(self):
    return self._pair_cards

  def __eq__(self, other):
    if self.rank() != other.rank():
      return super(OnePair, self).__eq__(other)
    else:
      return self.pair_cards() == other.pair_cards() and self.compare_high_cards(other) == 0

  def __lt__(self, other):
    if self.rank() != other.rank():
      return super(OnePair, self).__lt__(other)
    else:
      return self.pair_cards() < other.pair_cards() or (self.pair_cards() == other.pair_cards() and self.compare_high_cards(other) == -1)

class TwoPair(RankedHand):
  def __init__(self, two_pair_ranks, remaining_card):
    super(TwoPair, self).__init__(remaining_card)
    self.two_pair_ranks = sorted(two_pair_ranks)

  def high_pair(self):
    return self.two_pair_ranks[1]

  def low_pair(self):
    return self.two_pair_ranks[0]

  def __eq__(self, other):
    if self.rank() != other.rank():
      return super(TwoPair, self).__eq__(other)
    else:
      return self.high_pair() == other.high_pair() and self.low_pair() == other.low_pair() and self.compare_high_cards(other) == 0

  def __lt__(self, other):
    if self.rank() != other.rank():
      return super(TwoPair, self).__lt__(other)
    if self.high_pair() < other.high_pair():
      return True
    elif(self.high_pair() == other.high_pair() and self.low_pair() < other.low_pair()):
      return True
    elif(self.high_pair() == other.high_pair() and self.low_pair() == other.low_pair() and self.compare_high_cards(other) == -1):
      return True
    else:
      return False

class ThreeKind(RankedHand):
  def __init__(self, three_kind_rank):
    self._rank = 3
    self.three_kind_rank = three_kind_rank

  def __eq__(self, other):
    if self.rank() != other.rank():
      return super(ThreeKind, self).__eq__(other)
    else:
      return False # Can't be equal

  def __lt__(self, other):
    if self.rank() != other.rank():
      return super(ThreeKind, self).__lt__(other)
    if self.three_kind_rank < other.three_kind_rank:
      return True
    elif(self.three_kind_rank == other.three_kind_rank and self.compare_high_cards(other) == -1):
      return True
    else:
      return False

class Straight(RankedHand):
  def __init__(self, all_cards):
    super(Straight, self).__init__(all_cards)
    self._rank = 4
    # Account for Ace low
    if 14 in all_cards and 2 in all_cards:
      tmp = all_cards
      tmp.remove(14)
      self._straight_rank = max(tmp)
    else:
      self._straight_rank = max(all_cards)

  def straight_rank(self):
    return self._straight_rank

  def __eq__(self, other):
    if self.rank() != other.rank():
      return super(Straight, self).__eq__(other)
    else:
      return self.straight_rank() == other.straight_rank()

  def __lt__(self, other):
    if self.rank() != other.rank():
      return super(Straight, self).__lt__(other)
    else:
      return self.straight_rank() < other.straight_rank()

class Flush(RankedHand):
  def __init__(self, all_cards):
    super(Flush, self).__init__(all_cards)
    self._rank = 5

  def __eq__(self, other):
    if self.rank() != other.rank():
      return super(Flush, self).__eq__(other)
    else:
      return self.compare_high_cards(other) == 0

  def __lt__(self, other):
    if self.rank() != other.rank():
      return super(Flush, self).__lt__(other)
    else:
      return self.compare_high_cards(other) == -1

class FullHouse(RankedHand):
  def __init__(self, three_kind_rank):
    super(FullHouse, self).__init__([])
    self.three_kind_rank = three_kind_rank

  def __eq__(self, other):
    if self.rank() != other.rank():
      return super(FullHouse, self).__eq__(other)
    else:
      return False # Can't be equal

  def __lt__(self, other):
    if self.rank() != other.rank():
      return super(FullHouse, self).__lt__(other)
    elif(self.three_kind_rank < other.three_kind_rank):
      return True
    else:
      return False

class FourKind(RankedHand):
  def __init__(self, four_kind_rank):
    self.four_kind_rank = four_kind_rank
    self._rank = 7

  def __eq__(self, other):
    if self.rank() != other.rank():
      return super(FourKind, self).__eq__(other)
    return False # Can't be equal

  def __lt__(self, other):
    if self.rank() != other.rank():
      return super(FourKind, self).__lt__(other)
    elif(self.four_kind_rank < other.four_kind_rank):
      return True
    else:
      return False

class StraightFlush(Straight):
  def __init__(self, all_cards):
    super(StraightFlush, self).__init__(all_cards)
    self._rank = 8







