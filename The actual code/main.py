import random

def main():
   value = random.randint(1, 20)

   print('Guess the number: ')
   user_guess = input()

   if(value == user_guess):
        print('You are correct! Bet you can\'t do it again.')
   else:
        print('Wrong. Try again')

if __name__ == "__main__":
    main()