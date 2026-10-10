import numpy as np

rng = np.random.default_rng(11)
marks = rng.integers(10, 101, size=(10, 5))
print("Marks (rows are students, columns are subjects):\n", marks)

student_totals = np.sum(marks, axis=1)
student_averages = np.mean(marks, axis=1)
subject_averages = np.mean(marks, axis=0)

best_student = np.argmax(student_averages)
pass_mask = student_averages >= 50
passed_students = np.sum(pass_mask)
results = np.where(pass_mask, "Pass", "Fail")

print("Student totals:", student_totals)
print("Student averages:", student_averages)
print("Subject averages:", subject_averages)
print("Student with highest average:", best_student + 1)
print("Highest average:", student_averages[best_student])
print("Students with average at least 50:", passed_students)
print("Pass/Fail results:", results)
