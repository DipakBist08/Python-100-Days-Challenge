name1 = input("Enter Your Name: ")
name2 = input("Enter Your Loved One Name: ")
combined_string = name1+name2
lower_case_string=combined_string.lower()
t = lower_case_string.count("t")
r = lower_case_string.count("r")
u = lower_case_string.count("u")
e= lower_case_string.count("e")

true = t + r + u + e
l = lower_case_string.count("l")
o = lower_case_string.count("o")
v = lower_case_string.count("v")
e = lower_case_string.count("e")

love = l + o + v + e

love_score=int(str(true) + str(love))
# print(f"Your Love Score is:{love_score}")
if love_score <10 or love_score >90:
    print(f"Your Love Socre is {love_score}, You guys are perfect for each other")
elif love_score>=40 and love_score<=50:
    print(f"You Love Score is:{love_score}, You have change to be together")
else:
    print(f"Your Love Score is :{love_score} ") 
