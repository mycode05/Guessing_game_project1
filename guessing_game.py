#Python project1--GUESSING Game

import random
#guess() is a function 
def guess(num):
    ran_num = random.randint(1,num)
    #to loop until the user gives right answer
    key = 0
    while key != ran_num:
        key = int(input(f"Guess a number between 1 and {num}: "))
        if 1<key<num:
            print(key)
            if key < ran_num:
                print('Try again.Too low.')
            elif key > ran_num:
                print('Try again.Too high.')
        else:
            print(f"Please, enter number between 1 and {num} only.")

    print(f'Congratulations,You have guessed the number {ran_num} correctly.')

#user input
number=int(input("Enter the number: "))
guess(number)
