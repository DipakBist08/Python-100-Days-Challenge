Fruits_List = ["Apple", "Banana", "Cheery", "Mango", "Papiya", "Cheery", "Orange"]
Vegetable_List = ["Lady Finger", "Cucumber", "Carrot"]
#To print out whole List

#print(Fruits_List)
#Append-Adds an element to the end of Fruits_List.
Fruits_List.append("Berry")
print(Fruits_List)

#count():- It Returns number of elements with the specified value. or counts how many same elements on the list.
Count_Element = Fruits_List.count("Cheery")
print(Count_Element)

#Copy():- it will make copy of Fruits_List
New_List = Fruits_List.copy()
print(f"It's Copy-New List:{New_List}")

#sort():- It will sort the list elements ascending or Descending order.
Fruits_List.reverse()
print(f"It's Sorted List: {Fruits_List}")

#index():- Returns the index of specific given element or it returns index of first element.
Index = Fruits_List.index("Cheery")
print(Index)
Last_Element = Fruits_List[-1]
print(Last_Element)

#insert():- It adds the value at specific position
Fruits_List.insert(0, "PineApple")

print(f"After Added PineApple at oth Element:\n {Fruits_List[0]}")
print(Fruits_List)

#extend():- adds the element to the lsit or extend the current list
Fruits_List.extend(Vegetable_List)
print(f"Combined List of Fruits_List and Vegetable_List: {Fruits_List}")

#pop():- It will remove the element from the lsit of specified positon.
Fruits_List.pop(1)
print(f"Removed First Element:{Fruits_List}")

#remove:- Removes the frist element with specified value
Fruits_List.remove(f"RemovedBanana From Fruits_List:{Fruits_List}")
print(Fruits_List)

#Clear:- It Removes all the elements from Fruit_List
Fruits_List.clear()
print(f"Cleared the List:{Fruits_List}")
