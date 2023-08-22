student_heights = input("Input a list of student heights ").split()
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])

total_sum = 0
for height in student_heights:
  total_sum += height
print(total_sum)

total_count = 0
for count in student_heights:
  total_count += 1
print(total_count)

average = round(total_sum / total_count)
print(average)
