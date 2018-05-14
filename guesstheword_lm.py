import random

words = ["cat", "dog", "bird", "fish", "mouse"]
hint1 = ["paws" ,"paws", "beak", "water", "cheese"]
hint2 = ["meow", "bark", "feathers", "gills", "squeak"]

number = random.randint(0,4)
secretword = words[number]
guess = ""
counter = 0

while True:
    print("Guess the secret word!")
    print("Type 'hint1', 'hint2', 'length', 'first letter', 'last letter' or 'give up' for help.")
    guess = input()

    if guess == secretword:
        print("You got it!")
        break
    elif guess == "hint1":
        print(hint1[number])
    elif guess == "hint2":
        print(hint2[number])
    elif guess == "first letter":
        print(secretword[0])
    elif guess == "last letter":
        print(secretword[-1])
    elif guess== "length":
        print(len(secretword))
    elif guess == "give up":
        print("The secret word was " + secretword)
        break
