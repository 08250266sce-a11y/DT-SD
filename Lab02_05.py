print()  # Print a blank line for spacing

# Store last two digits of student IDs
student1_id = (66)
student2_id = (80)

# Generate a unique value using modulo operation
unique_value = (student1_id + student2_id) % 10
print(f"Unique value generated: {unique_value}")  # Display unique value

students = {}  # Dictionary to store student names and scores

# Loop to take student names continuously
while True:
    # Take input from user
    name = input("Enter student name (or type 'exit' to stop): ")
    
    # Check if user wants to exit
    if name.lower() == "exit":
        break
    
    # Check for empty input
    if name == "":
        print("Warning: Blank name entered. Skipping...")
        continue
    
    # Add student with initial score 0
    students[name] = 0 

# Display registered students
print("Registered Students:")
for student in students.keys():
    print(student)

# Loop through each student for quiz
for student in students.keys():
    print(f"Quiz for {student}:")
    score = 0  # Initialize score
    
    # Question 1
    ans1 = int(input(f"Q1: What is {unique_value} + 2 = "))
    if ans1 == unique_value + 2:
        score += 1
    
    # Question 2
    ans2 = int(input(f"Q2: What is {unique_value} * 3 =  "))
    if ans2 == unique_value * 3:
        score += 1
    
    # Question 3
    ans3 = int(input(f"Q3: What is {unique_value} + 5 = "))
    if ans3 == unique_value + 5:
        score += 1
    
    # Store score in dictionary
    students[student] = score
    
    # Determine performance level
    if score == 3:
        performance = "Excellent"
    elif score == 2:
        performance = "Good"
    elif score == 1:
        performance = "Needs Improvement"
    else:
        performance = "Poor"
    
    # Check certificate eligibility
    eligible = "Eligible for Certificate" if score >= 2 else "Not Eligible"
    
    # Warning for zero score
    if score == 0:
        print(" Warning: Score is 0! You need to study harder!")
    
    # Display results
    print(f"Score: {score}")
    print(f"Performance Level: {performance}")
    print(f"Certificate Status: {eligible}")
    
    # Print star pattern based on score
    print("Stars Pattern:")
    if score > 0:
        for i in range(score):
            print("*" * (i + 1))
    else:
        print("")  

print()  # Final blank line