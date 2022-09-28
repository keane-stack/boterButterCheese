import random
from bke import start, MLAgent, EvaluationAgent, is_winner, opponent, train_and_plot, can_win

class MyAgent(MLAgent):
    def evaluate(self, board):
        if is_winner(board, self.symbol):
            reward = 1
        elif is_winner(board, opponent[self.symbol]):
            reward = -1
        else:
            reward = 0
        return reward

class RandomAgent(EvaluationAgent):
  def evaluate(self, board, my_symbol, opponent_symbol):
    getal = 1 
    if can_win(board, opponent_symbol):
      getal = getal = 1000
    return getal
  
  


menu_options = {
    1: 'Speel tegen een ander persoon',
    2: 'Tegen een domme tegenstander spelen',
    3: 'De tegenstander trainen en plotten',
    4: 'Tegen een slimme tegenstander spelen',
}

def print_menu():
    for key in menu_options.keys():
        print (key, '--', menu_options[key] )

def vsPlayer():
  start()

def option2():
  randomAgent = RandomAgent()
  start(player_x=randomAgent)


def option3():
     print('Handle option \'De tegenstander trainen en plotten\'')


def option4():
     print('\Tegen een slimme tegenstander spelen\'')



    

def trainAndPlot():
  random.seed(1)
  my_agent = MyAgent()
  random_agent = RandomAgent()
   
  train_and_plot(
      agent=my_agent,
      validation_agent=random_agent,
      iterations=50,
      trainings=100,
      validations=1000)





    
print_menu()

option = int(input('Kies een optie: '))

if option == 1:
   vsPlayer()
elif option == 2:
    option2()
elif option == 3:
    option3()
elif option == 4:
    option4()
else:
    print('Geen optie kies een nummer tussen de 1 en 4.')