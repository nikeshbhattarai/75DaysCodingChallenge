students_scores = input("Input a list of student scores.").split()
print(students_scores)
for n in range(0, len(students_scores)):
    students_scores[n] = int(students_scores[n])

max_score = 0
for scores in students_scores:
    if scores > max_score:
        max_score = scores

print(max_score)