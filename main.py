import random
from pyfiglet import Figlet
from time import sleep
import os

allowedGames = {
	# "Difficulty":(start, end, tries)
	1:(1, 10, 5, "Easy"),
	2:(1, 100, 10, "Normal"),
	3:(1, 1000, 15, "Hard"),
	4:(1, 10000, 20, "Insane")
}

def Check(match, toMatch):
	if toMatch == match:
		return 0
	elif toMatch<match:
		return 1
	else:
		return -1

def takeInput():
	try:
		inputChoice = int(input(("Your Choice? ")))
		return inputChoice
	except ValueError:
		return "Integer required!!"

def introPrint():
	print("+"*50)
	f = Figlet(font='5lineoblique')
	print(f.renderText('Can You Guess?'))
	print("+"*50)
	print()


def levelDescription(difficulty = 1):
	level = allowedGames[difficulty]
	start = level[0]
	end = level[1]
	life = level[2]
	text = level[3]

	print(f"Loading level {text} .......")
	sleep(5)
	print()
	print(f"Description")
	print("-"*80)
	print(f"I am going to choose any number from {start} to {end} and you need to guess that number.")
	print("If you guessed the right one, you will land on the next level.")
	print("Else I will provide you with some hints to guess the right.")
	print(f"Remember you have only {life} lifes.\n")
	print("-"*80)
	input("Press [Enter] to start: ")
	print()

	return (start, end, life)

def main():
	os.system('cls')
	introPrint()
	START_LEVEL = 1
	while True:
		Start, End, Life = levelDescription(difficulty=START_LEVEL)
		COMPUTER_CHOICE = random.randint(Start, End)
		for l in range(Life, 0, -1):
			print()
			print(f'Life: {l}')
			print()
			USER_CHOICE = takeInput()
			if USER_CHOICE == "Integer required!!":
				print("Integer required!!\nTry Again")
				continue
			result = Check(match=COMPUTER_CHOICE, toMatch=USER_CHOICE)
			if result == 0:
				print('+'+'='*14+'+')
				print("+ Level Passed +")
				print('+'+'='*14+'+')
				sleep(1)
				print()
				START_LEVEL+=1
				break
			elif result == -1:
				print("Try with SMALLER numbers")
				print()
			elif result == 1:
				print("Try with LARGER number")
				print()
		else:
			print("Sorry! You failed to pass this level")
			print(f"The number was {COMPUTER_CHOICE}")
			print('+'+'-'*13+'+')
			print("+ Game Over!! +")
			print('+'+'-'*13+'+')
			break




if __name__ == '__main__':
	main()
	
