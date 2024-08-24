#Write a program that calculate the highest score from List of Student_score=[78,65,89,91,64,87]

Student_score = [78, 65, 89, 91, 64, 87]
max_score=Student_score[0]
for max_marks in Student_score:
    if max_marks>max_score:
        max_score=max_marks
print(f"Highest score is :{max_score}")

#max is python function to print maximum marks form the list.
print(max(Student_score))

