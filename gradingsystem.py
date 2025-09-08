def grading_system(marks):
    if marks>=90:
        grade="A"
    elif marks>=75:
        grade="B"
    elif marks>=60:
        grade="C"
    elif marks>=40:
        grade="D"
    else:
        grade="F"
    return grade
marks=int(input("Enter your marks:"))
print("your grade is:",grading_system(marks))
