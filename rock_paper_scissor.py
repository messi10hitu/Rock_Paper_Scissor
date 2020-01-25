import random
print(" Hi every one this is my Rock Paper Scissor game")
print(" you just have to type Rock Paper Scissor")
print('           Plz enter ROCK  as Rock          ')
print('           Plz enter PAPER  as Paper          ')
print('           Plz enter SCISSOR  as Scissor          ')
x = ['Rock', 'Paper', 'Scissor']
while True:
    game = input("enter 'Q' or 'q' to: 'Quit'  or press Enter to start: ")
    if game == 'q' or game == 'Q':
        print("have a nice day")
        break
    user_input = input("enter the user input: ")
    print('enter the computer no:', end=" ")
    computer_input = random.choice(x)
    print(computer_input)
    if (user_input == 'Rock') and (computer_input == 'Scissor'):
        print('user win')
    elif(user_input == 'Paper') and (computer_input == 'Scissor'):
        print('computer win')
    elif (user_input == 'Paper') and (computer_input == 'Rock'):
        print('user win')
    elif (user_input == 'Scissor') and (computer_input == 'Paper'):
        print('user win')
    elif (user_input == 'Rock') and (computer_input == 'Rock'):
        print('Match Draw! Try again')
    elif (user_input == 'Paper') and (computer_input == 'Paper'):
        print('Match Draw! Try again')
    elif (user_input == 'Scissor') and (computer_input == 'Scissor'):
        print('Match Draw! Try again')
    else:
        print("computer win")

