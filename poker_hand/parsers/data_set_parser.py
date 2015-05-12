from poker_hand.parsers import card_parser

class DataSetParser:
  SUIT = {1: "heart", 2: "spade", 3: "diamond", 4: "club"}
  def parse_line(self, line):
    nums = line.rstrip().split(",")
    # they use ace -> 1, otherwise the same as our rank
    ranks = [int(rank) if rank != "1" else 14 for rank in nums[1::2]]
    suits = [self.SUIT[int(suit_num)] for suit_num in nums[:10:2]]
    rank = int(nums[-1])
    return ranks, suits, rank
