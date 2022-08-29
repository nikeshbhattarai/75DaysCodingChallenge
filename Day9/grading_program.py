student_scores = {
    "Harry": 81,
    "Ron": 78,
    "Hermione": 99,
    "Draco": 74,
    "Neville": 62
} 

student = {}

for key, value in student_scores.items():
    if value > 90:
        student[key] = "Outstanding"
    elif value > 80:
        student[key] = "Exceeds Expectations"
    elif value > 70:
        student[key] = "Acceptable"
    else:
        student[key] = "Fail"
    
print(student)