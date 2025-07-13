# dictionary to store student information
student = {}

# Get user input
name = input("Enter your name: ")
age = int(input("Enter your age: "))
passed = input("Have you passed? (yes/no): ").lower()== 'yes'

# input favorite subjects and format
fav_sub = input("Enter your favorite subject (comma separated): ").lower().split(',')
subjects = [sub.strip() for sub in fav_sub] # remove extra spaces

# input birthday as a tuple
dob = tuple(map(int, input("Enter your date of birth (YYY MM DD): ").split()))

# store all data in dictionary
student.update({
    "name" : name,
    "age" : age,
    "passed" : passed,
    "subject" : subjects,
    "dob" : dob
})

# check if 'math' is in favorite subjects
if "math" in subjects:
    print("Math Lover!")
else:
    print("Try Math Once!")

# output full student summary
print(f"\nStudent Summary:")
print(f"Name: {name}")
print(f"Birthday: {dob}, Year of Birth: {dob[0]}")
print(f"Age: {age}")
print(f"Passed: {passed}")
print(f"Favorite Subjects: {subjects}")

# access individual dictionary values
print("\nData from dictionary:")
print("Name", student["name"])
print("Age", student["age"])
print("Subject",student["subject"])

# optional: compare with friend's subjects using set
friend_subjects = input("Enter your friend's favorite subjects (comma separated): ").lower().split(",")
friend_subjects = [sub.strip() for sub in friend_subjects]
common_subjects = set(subjects) & set(friend_subjects)

# print common subjects
print(f"\ncommon subjects with friend: {common_subjects}")