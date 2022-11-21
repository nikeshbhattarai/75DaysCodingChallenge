student_heights = input("Input a list of student heights ").split()
print(student_heights)
print(len(student_heights))
for n in range(0, len(student_heights)):
    student_heights[n] = int(student_heights[n])

sum = 0
count = 0
for heights in student_heights:
    sum += heights
    count += 1

print("total: ", sum)
average_height = sum/count
print("The average height of the students is {:.2f}.".format(average_height))
print(f"The average height of the students is {average_height:.2f}.")
