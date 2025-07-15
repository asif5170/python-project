from datetime import datetime

password = "asif" # Diary password

def verify_password():
    user_pass = input("Enter diary password: ")
    if user_pass == password:
        print("Correct password.\n")
        return True
    else:
        print("Incorrect password! please enter a valid password.")
        return False
    
def write_diary():
    entry = input("Write Today Diary: ")
    time = datetime.now().strftime("%Y-%M-%D , %H:%M:%S") # Date and Time
    with open("asif_diary.txt", "a") as f:
        f.write(time + " - " + entry + "\n") # write with time
    print("Diary Append Successful.\n")

def read_diary():
    try:
        with open("asif_diary.txt", "r") as f:
            file = f.read()
        print("\nAll of your diary.\n")
        print(file)

        f.close()
            
    except FileNotFoundError:
        print("Diary is not found.write something before.\n")

# Main program
while True:
    print("\nPassword Protected Diary")
    print("1. Write a Diary.")
    print("2. Read the Diary.")
    print("3. Program Close..")

    choice = input("Your Choice(1/2/3): ")

    if choice == '1':
        if verify_password():
            write_diary()
    elif choice == '2':
        if verify_password():
            read_diary()
    elif choice == '3':
        print("Thank You. The Diary app is getting off.")
        break
    else:
        print("Wrong choice! Please press 1,2,or 3.\n")

