import random

numbers = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]

squared_numbers = [num**2 for num in numbers]

print(squared_numbers)

result = [num for num in numbers if num%2 == 0]

print(result)

with open('file1.txt', 'r') as file1:
    items_file1 = file1.readlines()

with open('file2.txt', 'r') as file2:
    items_file2 = file2.readlines()

result = [int(item) for item in items_file1 if item in items_file2]
print(result)

names = ['Alex', 'Beth', 'Caroline', 'Dave', 'Eleanor', 'Freddie']

students_scores = {student:random.randint(1, 100) for student in names}
print(students_scores)

passed_students = {student:score for (student, score) in students_scores.items() if score >= 60}
print(passed_students)

sentence = "What is the Airspeed Velocity of an Unladen Swallow?"

result = {word:len(word) for word in sentence.split()}
print(result)
