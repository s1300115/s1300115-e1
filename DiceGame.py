import random as r
from time import sleep

print("What is your name?")
name = input("> ")
print(f"Hello, {name}!")

sleep(1)

print("Rolling dice...")
dices = [r.randint(1,6) for i in range(2)]
sleep(0.5)

for i in range(1,3):
    print(f"Die {i}: {dices[i-1]}")
else:
    num = sum(dices)
    print(f"Total value: {num}")

print("You won") if num > 7 else print("You lose")