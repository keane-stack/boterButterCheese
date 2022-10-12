from bke import MLAgent, is_winner, opponent, train, load, start
 
 
class MyAgent(MLAgent):
    def evaluate(self, board):
        if is_winner(board, self.symbol):
            reward = 1
        elif is_winner(board, opponent[self.symbol]):
            reward = -1
        else:
            reward = 0
        return reward
    
 
my_agent = MyAgent()
my_agent = load('MyAgent_3000')
 
my_agent.learning = False
 
start(player_x=my_agent)















#import random
#from bke import start, MLAgent, EvaluationAgent, is_winner, opponent, train_and_plot, can_win, train, save, load 

#class MyAgent(MLAgent):
#    def evaluate(self, board):
 #       if is_winner(board, self.symbol):
  #          reward = 10
   #     elif is_winner(board, opponent[self.symbol]):
    #        reward = -1
     #   else:
      #      reward = 0
       # return reward

#class RandomAgent(EvaluationAgent):
 # def evaluate(self, board, my_symbol, opponent_symbol):
  #  getal = 1 
   # if can_win(board, opponent_symbol):
    #  getal = getal = 1000
    #return getal




#menu_options = {
 #   1: 'Speel tegen een ander persoon',
  #  2: 'Tegen een domme tegenstander spelen',
   # 3: 'De tegenstander trainen en plotten',
    #4: 'Tegen een slimme tegenstander spelen',
    
#}

#def print_menu():
 #   for key in menu_options.keys():
   #     print (key, '--', menu_options[key] )

#def vsPlayer():
#  start()

#def randomplayer():
  #randomAgent = RandomAgent()
  #start(player_x=randomAgent)


#def trainAndPlot():
# random_agent = RandomAgent()
 # start(player_x=randomAgent)


#def Option4():
 # my_agent = MyAgent()
 # my_agent = load('MyAgent_3000')
 # start(player_x=my_agent)



    

#def trainAndPlot():
  #random.seed(1)
 # my_agent = MyAgent()
# random_agent = RandomAgent()
   
  #train_and_plot(
  #    agent=my_agent,
  #    validation_agent=random_agent,
  #    iterations=50,
   #   trainings=100,
   #   validations=1000)





    
#print_menu()

#option = int(input('Kies een optie: '))

#if option == 1:
 #  vsPlayer()
#elif option == 2:
#    randomplayer()
#elif option == 3:
 #   trainAndPlot()
#elif option == 4:
#    Option4()
#else:
 #   print('Geen optie kies een nummer tussen de 1 en 4.')