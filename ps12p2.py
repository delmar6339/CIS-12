def display_students_info(names, scores):
    print("Student Names and Exam Scores:")
    for i in range(len(names)):
        print(f"{names[i]}: {scores[i]}")
student_names = ["Konnor", "Bacevic", "Del Mar", "Junior", "God"]
exam_scores = [99, 88, 90, 65, 10]
display_students_info(student_names, exam_scores)