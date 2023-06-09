import random as r

print("Rolling dice...")
dices = [r.randint(1,6) for i in range(2)]

for i in range(1,3):
    print(f"Die {i}: {dices[i-1]}")
else:
    print(f"Total value: {sum(dices)}")