# Cows and Bulls
# Optimized

import random

def main():
	num = []
	while(len(num) < 4):
		gen_num = random.randint(1,9)
		works = True
		for used_num in range(0,len(num)):
			if(gen_num == num[used_num]):
				works = False
		if(works):
			num.append(gen_num)
	won = False
	while(won == False):
		guess = list(raw_input("Guess?\n>>> "))
		bulls = 0
		cows = 0
		# Check for bulls
		for cur_num in range(0,4):
			guess[cur_num] = int(guess[cur_num])
			if(guess[cur_num] == num[cur_num]):
				cows += 1
			for check_num in range(0,4):
				if(cur_num != check_num):
					if(guess[cur_num] == num[check_num]):
						bulls += 1
						break
		print(str(bulls) + " bulls")
		print(str(cows) + " cows") 
		if(guess == num):
			won = True
	print("You won!")
				

if(__name__ == "__main__"):
	main()
