
class Player():

  def __init__(self,name):
    self.name = name
    self.cards = []

  def __str__(self):
    return f'Player {self.name} has {len(self.cards)} cards'
  
  def play_card(self):
    return self.cards.pop(0)
  
  def can_declare_war(self):
    return len(self.cards) >= 10

  def add_cards(self,cards):
    if type(cards) == type([]):
      self.cards.extend(cards)
    else:
      self.cards.append(cards)
  
  def hasCards(self):
    return len(self.cards) > 0

  def play_war(self):
    war_cards = []
    for n in range(10):
      war_cards.append(self.play_card())
    return war_cards