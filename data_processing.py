students = [
    {"name": "Ali", "age": 20, "marks": 85},
    {"name": "Ahmed", "age": 21, "marks": 78},
    {"name": "Sara", "age": 19, "marks": 92},
    {"name": "Ayesha", "age": 22, "marks": 88},
    {"name": "John", "age": 20, "marks": 75}
]

def summary_statistics(records):
    total_students = len(records)

    total_marks = sum(student["marks"] for student in records)

    average_marks = total_marks / total_students

    highest_marks = max(student["marks"] for student in records)

    lowest_marks = min(student["marks"] for student in records)

    return {
        "Total Students": total_students,
        "Average Marks": round(average_marks, 2),
        "Highest Marks": highest_marks,
        "Lowest Marks": lowest_marks
    }

def top_students(records):
    return [student for student in records if student["marks"] >= 80]

stats = summary_statistics(students)

print("\n===== SUMMARY STATISTICS =====")

for key, value in stats.items():
    print(f"{key}: {value}")

print("\n===== TOP STUDENTS =====")

for student in top_students(students):
    print(student)
