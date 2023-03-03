import random as r

names = ['Carl','John','Maya','Broski','Charles','Lemon','Tiger']

students_dict = {name : r.randint(1,100) for name in names}

passed_students = {name: score for name,score in students_dict.items() if score >= 60}

print(students_dict)
print(passed_students)