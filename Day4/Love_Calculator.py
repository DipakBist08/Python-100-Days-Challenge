import random
Love_calculator=random.randint(1,100)
if Love_calculator<=25:
    print(f"It's complicated to Express your Love: {Love_calculator}")
elif Love_calculator<=50:
    print(f"There is a chance to fall in love:{Love_calculator}")
elif Love_calculator<=75:
    print(f"You have a chance if you express:{Love_calculator}")
elif Love_calculator>75:
    print(f"You Guys are already in Love:{Love_calculator}")
else:
    print("Invalid Information!! !")