import random
from Card import Card,suits,ranks

class Deck():

  def __init__(self):
    self.all_cards = []
    
    for suit in suits:
      for rank in ranks:
        self.all_cards.append(Card(suit,rank))

  def __len__(self):
    return len(self.all_cards)

  def print_cards(self):
    for card in self.all_cards:
      print(card)
  
  def shuffle(self):
    random.shuffle(self.all_cards)
  
  def deal_one(self):
    return self.all_cards.pop()