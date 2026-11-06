name = input("student name: ")
math_marks = float(input("Math marks: "))
english_marks = float(input("English marks: "))
python_marks = float(input("Python marks: "))


if (0 <= math_marks <= 100) and (0 <= english_marks <= 100) and (0 <= python_marks <= 100):
    
    average_marks = (math_marks + english_marks + python_marks) / 3
    if 80 <= average_marks <= 100:
        grade = "A+"
    elif 70 <= average_marks <= 79:
        grade = "A"
    elif 60 <= average_marks <= 69:
        grade = "A-"
    elif 50 <= average_marks <= 59:
        grade = "B"
    elif 40 <= average_marks <= 49:
        grade = "C"
    else:
        grade = "F"


    print(f"\nStudent Name: {name}")
    print(f"Average Marks: {average_marks:.2f}")
    print(f"Final Grade: {grade}")

else:
    print("\nError: Invalid marks! Please enter marks between 0 and 100.")