students = {}
fail_set = set()
pass_students = []

# task 1
n = int(input("How many students' data do you want to enter: "))
# task 2
for i in range(n):
    name = input(f"\nEnter name of student {i+1}: ")
    roll = int(input("Enter roll number: "))
    marks = float(input("Enter marks: "))
    # task 3
    students[roll] = {
        "name" : name,
        "marks" : marks
    }
    
    #task 5
    if marks < 50:
        fail_set.add(roll)
    else:
        pass_students.append(name)

# task 4
 # show student info based on user - input roll number   
search_roll = int(input("\nEnter the roll number of the students you want to search: "))

if search_roll in students:
    print(f"Name: {students[search_roll]['name']}, Marks: {students[search_roll]['marks']}")
else:
    print("No students found with this roll number")

for key in sorted(students):
    print(key, ":", students[key])

# task 6
# show aveage marks of all students
total_marks = 0

for info in students.values():
    total_marks += info['marks']

average = total_marks // len(students)
print(f"\nAverage marks of all students : {average}")



# task 5
# show roll numbers of students who scored below 50
print("\nRoll numbers of students who scored below 50: ", fail_set)

# show names of students who passed
print("\nNames of students who passed (scored 50 or more): ",pass_students)

# find the student with the highest marks
highest_roll= None
highest_marks = - 1

for roll, info in students.items():
    if info['marks'] > highest_marks:
        highest_marks = info['marks']
        highest_roll = roll

# show the to scorer
top_student = students[highest_roll]
print(f"\nTop scorer: {top_student['name']} (Roll: {highest_roll}) got {top_student['marks']} marks.")