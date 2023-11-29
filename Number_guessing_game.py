from random import randint

EASY_LEVEL_TURN = 10
HARD_LEVEL_TURN = 5


def check_answer(guess, answer, turns):
  """checks answer against guess.Returns the number of turns remmaning"""
  if guess > answer:
    print("Too high")
    return turns - 1
  elif guess < answer:
    print("Too low")
    return turns - 1
  else:
    print(f"You got it! The answer is {answer}.")


def set_difficulty():
  level = input("choose the difficulty.Type 'easy' or 'hard': ")
  if level == "easy":

    return EASY_LEVEL_TURN
  else:
    return HARD_LEVEL_TURN


def game():
  print("Welcome to the guessing the number game")
  print("I'm thinking of a number between 1 and 100.: ")
  answer = randint(1, 100)
  print(f"Passst,the correct answer is {answer}")
  turns = set_difficulty()
  print(f"You have {turns} attempts remaining to guess the number.")
  guess = 0
  while guess != answer:
    guess = int(input("Make a guess:"))
    turns = check_answer(guess, answer,turns)
    if turns==0:
      print("You've run out of guesses,you lose.")
      return


game()
