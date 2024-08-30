# import random
# start=int(input("enter the starting value:"))
# end=int(input("enter the ending value:"))
# while start>=end:
#     print("Please enter the value from low to high")
#     start=int(input("enter the starting value:"))
#     end=int(input("enter the ending value:"))
# genrandom=random.randint(start,end)
# print(f"guess the value between {start} and {end}, you have 5 attempts left")
# attempts=5
# while attempts >0:
#     guess=int(input("enter the guess: "))
#     attempts -=1
#     if guess < genrandom:
#         print(f"your guessed value is less than generated value. {attempts} attempts left to try again")
#     elif guess > genrandom:
#         print(f"your guessed value is more than generated value. {attempts} attempts left to try again")
#     else:
#         print("congratulations your guessed value is correct")
#         break
# else:
#     print(f"out of attempts the generated value is {genrandom}, try again")


import random
name=input("what is your name?")
print("good luck!",name)
words=["random","programming","dinesh","apple","zebra","jupiter","kitchen"]
genword=random.choice(words)
print("guess the characters")
guess=' '
attempts=5
while attempts > 0:
    failed=0
    for char in genword:
        if char in guess:
            print(char, end=" ")
        else:
            print("_")
            failed+=1
    if failed == 0:
        print ("You Win")
        print("The word is:",genword)
        break
    print()
    guesses=input("guess a character:")
    guess += guesses
    if guesses not in genword:
        attempts-=1
        print("wrong")
        print("you have", +attempts, 'attempts left')
        if attempts == 0:
            print(f"you have exceeded the attempts\nThe guess is '{genword}' try again")

