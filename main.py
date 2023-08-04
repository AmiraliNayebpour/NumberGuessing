from colorama import Fore
from time import sleep
from random import randint


    
number = randint(99 , 999)

emptyList = ["_" , "_" , "_"]

numberStr = list(str(number))



print(Fore.BLUE + "Welcome to number Guessing game ")
sleep(1)
print(Fore.GREEN + "You need to find the best place for a 3 digit number _ _ _")
sleep(1)

tried_Times = 1



print(Fore.RED + "You have 6 chances to guess the number !!")
print(Fore.WHITE + "_ "*len(numberStr))

while tried_Times <= 6:
    num = input(Fore.YELLOW + f"Please enter the {tried_Times}'s digit : ")
    for i in range(3) :
        if num == numberStr[i] :
            emptyList[i] = num
    tried_Times+=1
    print(Fore.LIGHTBLUE_EX + " ".join(emptyList))
    if emptyList[0] != "_" and emptyList[1] != "_" and emptyList[2] != "_" :
        print(Fore.LIGHTGREEN_EX + "Congratulations!! you have guessed the number correctly!!!!")
        break
    elif tried_Times == 7:
        print(Fore.LIGHTMAGENTA_EX + "Nice Try ! you can try it later and catch the points!")
        print("The number that you haven't guessed was : " , " ".join(numberStr))


