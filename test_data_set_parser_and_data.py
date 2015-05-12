from data_set_parser import *
from hand import *

def test_line_parse():
  line = "1,9,1,12,1,10,1,11,1,13,8\n"
  parser = DataSetParser()
  ranks, suits, rank = parser.parse_line(line)
  assert [ranks, suits] == [[9, 12, 10, 11, 13], ["heart"] * 5]

def test_data_set():
  f = open("./poker_data.data", "r")
  parser = DataSetParser()
  i = 0
  for line in f:
    ranks, suits, rank = parser.parse_line(line)
    hand = Hand(ranks, suits)
    if rank != hand.best_hand.rank:
      print "line: %s" % i
      print line.rstrip()
      print ranks, suits, rank
    assert rank == hand.best_hand.rank
    i += 1
