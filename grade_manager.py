import json

def average_score(scores):
    if not scores:
        return 0
    return sum(scores) / len(scores)

def grade(score):
    if score >= 70:
        return "A"
    elif score >= 60:
        return "B"
    elif score >= 50:
        return "C"
    else:
        return "F"

def load_students():
    try:
        with open("students.json", "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return []

def save_students(students):
    with open("students.json", "w") as file:
        json.dump(students, file)

def add_student(students, name, scores):
    name = name.strip().title()
    for student in students:
        if student["name"] == name:
            return False
    students.append({"name": name, "scores": scores})
    return True

def report_line(student):
    avg = average_score(student["scores"])
    return f"{student['name']}: average {avg:.1f}, grade {grade(avg)}"

def ranked(students):
    return sorted(
        students,
        key=lambda s: average_score(s["scores"]),
        reverse=True
    )

students = load_students()

while True:
    print("\n1. Add student")
    print("2. Show ranking")
    print("3. Quit")
    choice = input("Choose: ").strip()
    
    if choice == "1":
        name = input("Name: ")
        scores = []
        while True:
            text = input("Score (press Enter to finish): ").strip()
            if text == "":
                break
            try:
                scores.append(float(text))
            except ValueError:
                print("Please type a number.")
        if not scores:
            print("No scores entered. Student not added.")
        elif add_student(students, name, scores):
            save_students(students)
            print("Added.")
        else:
            print("That student already exists.")
       
    elif choice == "2":
        if not students:
            print("No students yet.")
        else:
            position = 1
            for student in ranked(students):
                print(f"{position}. {report_line(student)}")
                position = position + 1
    elif choice == "3":
        print("Goodbye!")
        break
    else:
        print("Please choose 1, 2 or 3.")