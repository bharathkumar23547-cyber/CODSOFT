import random

print("=" * 35)
print("     ROCK PAPER SCISSORS")
print("=" * 35)
choices=["rock","paper","scissors"]

user_choice=input("enter rock,paper,or scissors:").lower()

computer_choice=random.choice(choices)

print("\n your choice:",user_choice)
print("computer choice:",computer_choice)
if user_choice==computer_choice:
    print("result:it's a Tie!")
elif (user_choice=="rock" and computer_choice=="scissors")or\
     (user_choice=="paper" and computer_choice=="rock")or\
     (user_choice=="scissors" and computer_choice=="paper"):
    print("result: you win!")
elif user_choice in choices:
    print("result:computer wins:")
else:
    print("Invalid choice!")
print("\n Thank you for playing Rock paper scissors!")
