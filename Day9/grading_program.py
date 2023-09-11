student_scores = {
  "Harry": 81,
  "Ron": 78,
  "Hermione": 99, 
  "Draco": 74,
  "Neville": 62,
}

#TODO-1: Create an empty dictionary called student_grades.
student_grades = {}

#TODO-2: Write your code below to add the grades to student_grades.👇

for student in student_scores:
    if student_scores[student] >= 91:
        student_grades[student] = "A"
    elif student_scores[student] >= 81:
        student_grades[student] = "B"
    elif student_scores[student] >= 71:
        student_grades[student] = "C"
    elif student_scores[student] >= 61:
        student_grades[student] = "D"
    elif student_scores[student] >= 51:
        student_grades[student] = "E"
    else:
        student_grades[student] = "F"



    

# 🚨 Don't change the code below 👇
print(student_grades)