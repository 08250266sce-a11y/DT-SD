print()
student1_id = (66)
student2_id = (80)
unique_value = (student1_id + student2_id) % 10
print(f"Unique value generated: {unique_value}")
students = {}
while True:
    name = input("Enter student name (or type 'exit' to stop): ")
    if name.lower() == "exit":
        break
    if name == "":
        print("Warning: Blank name entered. Skipping...")
        continue
    students[name] = 0 
print("Registered Students:")
for student in students.keys():
    print(student)
for student in students.keys():
    print(f"Quiz for {student}:")
    score = 0
    ans1 = int(input(f"Q1: What is {unique_value} + 2 = "))
    if ans1 == unique_value + 2:
        score += 1
    ans2 = int(input(f"Q2: What is {unique_value} * 3 =  "))
    if ans2 == unique_value * 3:
        score += 1
    ans3 = int(input(f"Q3: What is {unique_value} + 5 = "))
    if ans3 == unique_value + 5:
        score += 1
    students[student] = score
    if score == 3:
        performance = "Excellent"
    elif score == 2:
        performance = "Good"
    elif score == 1:
        performance = "Needs Improvement"
    else:
        performance = "Poor"
    eligible = "Eligible for Certificate" if score >= 2 else "Not Eligible"
    if score == 0:
        print(" Warning: Score is 0! You need to study harder!")
print()