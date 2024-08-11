fruits_list = [
    "Apple", "Banana", "Mango", "Kiwi", "Orange", "Pineapple", "Grapes",
    "Strawberry", "Blueberry", "Raspberry", "Peach", "Plum", "Cherry",
    "Watermelon", "Cantaloupe", "Honeydew", "Papaya", "Pomegranate", "Avocado",
    "Fig", "Date", "Dragon Fruit", "Lychee", "Grapefruit", "Tangerine",
    "Nectarine", "Apricot", "Guava", "Passion Fruit", "Persimmon", "Coconut"
]

input_fruit_name = input("Check Fruit is in List: ")
if input_fruit_name in fruits_list:
    print(f"{input_fruit_name} is in stock.")

else:
    print(f"{input_fruit_name} is out of stock!!")
