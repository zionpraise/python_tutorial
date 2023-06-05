import random
number = [1,2,3,4,5,6,7,8,9,10,11]
first_card = random.choice(number)
second_card = random.choice(number)
sum = first_card + second_card

if sum < 21:
    print("Do you want to take a new card..." "\n")
elif sum > 21:
    print("You're out of the game " "\n")
else:
    print("You win" "\n")
print(sum)
