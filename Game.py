from Deck import Deck
from Player import Player

class Game():

  def __init__(self):
    self.player1 = Player('one')
    self.player2 = Player('two')
    self.deck = Deck()
    self.deck.shuffle()
    self.deal_cards()

  def deal_cards(self):
    for x in range(len(self.deck) //2):
      self.player1.add_cards(self.deck.deal_one())  
      self.player2.add_cards(self.deck.deal_one())  

  def play(self):
    rounds = 0
    game_on = True

    
    while game_on:
      rounds += 1
      print(f'It is round {rounds}')

      #check if players still have cards

      if not self.player1.hasCards():
        print('game over, player 2 wins')
        game_on = False
        break
      if not self.player2.hasCards():
        print ('game over, player 1 wins')
        game_on = False
        break

      #Start new round
      player_one_played_cards = []
      player_one_played_cards.append(self.player1.play_card())

      player_two_played_cards = []
      player_two_played_cards.append(self.player2.play_card())

      at_war = True
      
      while at_war:
        p1_card = player_one_played_cards[-1]
        p2_card = player_two_played_cards[-1]

        if  p1_card.value > p2_card.value:
          self.player1.add_cards(player_one_played_cards)
          self.player1.add_cards(player_two_played_cards)
          at_war = False

        elif p2_card.value > p1_card.value:
          self.player2.add_cards(player_one_played_cards)
          self.player2.add_cards(player_two_played_cards)
          at_war = False

        else:
          print('War')

          if not self.player1.can_declare_war():
            print('Player 1 can not declare war')
            print('Player 2 wins')
            game_on = False
            break
          
          elif not self.player2.can_declare_war():
            print('Player 2 can not declare war')
            print('Player 1 wins')
            game_on = False
            break
          else:
            player_one_played_cards.extend(self.player1.play_war())
            player_two_played_cards.extend(self.player2.play_war())



          








