import random

secret = random.randrange(0, 100)
print(secret)
guess = 0
tries = 0
while guess != secret:
    guess = int(input("make a guess between 1 to 100: "))
    tries = tries + 1
    if guess > secret:
        print('that is too high !!')
    elif guess < secret:
        print('that is too low !!')
    else:
        print('You got it !!')
print('You took', tries, 'tries')