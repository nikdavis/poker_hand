from functools import total_ordering


@total_ordering
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



@total_ordering
class HighCard(RankedHand):
  def __init__(self, remaining_cards):
    super(HighCard, self).__init__(remaining_cards)
    self._rank = 0

  def __eq__(self, other):
    if self.rank() != other.rank():
      return super(HighCard, self).__eq__(other)
    return self.compare_high_cards(other) == 0

  def __lt__(self, other):
    if self.rank() != other.rank():
      return super(HighCard, self).__lt__(other)
    return self.compare_high_cards(other) == -1


@total_ordering
class OnePair(RankedHand):
  def __init__(self, pair_cards, remaining_cards):
    super(OnePair, self).__init__(remaining_cards)
    self._rank = 1
    self._pair_cards = pair_cards
    self._remaining_cards = remaining_cards

  def pair_cards(self):
    return self._pair_cards

  def __eq__(self, other):
    if self.rank() != other.rank():
      return super(OnePair, self).__eq__(other)
    return self.pair_cards() == other.pair_cards() and self.compare_high_cards(other) == 0

  def __lt__(self, other):
    if self.rank() != other.rank():
      return super(OnePair, self).__lt__(other)
    return self.pair_cards()[0] < other.pair_cards()[0] or (self.pair_cards() == other.pair_cards() and self.compare_high_cards(other) == -1)



@total_ordering
class TwoPair(RankedHand):
  def __init__(self, arr_of_pair_cards, remaining_cards):
    super(TwoPair, self).__init__(remaining_cards)
    self._rank = 2
    if arr_of_pair_cards[0][0] > arr_of_pair_cards[1][0]:
      self._high_pair = arr_of_pair_cards[0]
      self._low_pair = arr_of_pair_cards[1]
    else:
      self._high_pair = arr_of_pair_cards[1]
      self._low_pair = arr_of_pair_cards[0]
    self._remaining_cards = remaining_cards

  def high_pair(self):
    return self._high_pair

  def low_pair(self):
    return self._low_pair

  def __eq__(self, other):
    if self.rank() != other.rank():
      return super(TwoPair, self).__eq__(other)
    return self.high_pair() == other.high_pair() and self.low_pair() == other.low_pair() and self.compare_high_cards(other) == 0

  def __lt__(self, other):
    if self.rank() != other.rank():
      return super(TwoPair, self).__lt__(other)
    if self.high_pair()[0] < other.high_pair()[0]:
      return True
    elif(self.high_pair() == other.high_pair() and self.low_pair()[0] < other.low_pair()[0]):
      return True
    elif(self.high_pair() == other.high_pair() and self.low_pair() == other.low_pair() and self.compare_high_cards(other) == -1):
      return True
    return False



@total_ordering
class ThreeKind(RankedHand):
  def __init__(self, three_kind_cards, remaining_cards):
    super(ThreeKind, self).__init__(remaining_cards)
    self._rank = 3
    self._three_kind_cards = three_kind_cards
    self._remaining_cards = remaining_cards

  def three_kind(self):
    return self._three_kind_cards

  def __eq__(self, other):
    if self.rank() != other.rank():
      return super(ThreeKind, self).__eq__(other)
    return False # Can't be equal

  def __lt__(self, other):
    if self.rank() != other.rank():
      return super(ThreeKind, self).__lt__(other)
    if self.three_kind()[0] < other.three_kind()[0]:
      print self.three_kind()[0] < other.three_kind()[0]
      return True
    elif(self.three_kind() == other.three_kind() and self.compare_high_cards(other) == -1):
      return True
    return False
















