import math
def paint_calc(height,width,cover):
    area= height*width
    no_of_can=math.ceil(area/cover)
    print(f"You will need {no_of_can} cans of paint.")

input_height = int(input("Enter Height of Wall: "))
input_Width = int(input("Enter Width of Wall: "))
coverage=5
paint_calc(height=input_height,width=input_Width,cover=coverage)