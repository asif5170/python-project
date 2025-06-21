# Total & Average
def calculate_total_and_average(marks):
    total = sum(marks)
    average = total / len(marks)
    return total, average

# Grade
def calculate_grade(average):
    if average >= 80:
        return "A"
    elif average >= 60:
        return "B"
    elif average >= 40:
        return "C"
    else:
        return "F"
    
# Print All Report
def print_and_save_report(file, name, marks):
    total, average = calculate_total_and_average(marks)
    grade = calculate_grade(average)

    # Screen Outpur
    print(f"Student Name: {name}")
    print(f"Total Marks: {total}")
    print(f"Average Marks: {average:.2f}")
    print(f"Grade: {grade}")
    print("------------------------------")

    # File Output
    file.write(f"Student Name: {name}\n")
    file.write(f"Total Marks: {total}\n")
    file.write(f"Average Marks: {average:.2f}\n")
    file.write(f"Grade: {grade}\n")
    file.write("--------------------------------")

# Main Function
def main():
    num_studens = int(input("How Many Studens?: "))

    # Creat/Open file to write
    with open("student_result.txt", "w") as file:
        for i in range(num_studens):
            name = input(f"\nEnter The Name Of Student {i + 1}: ")

            marks = []
            for j in range(3):
                mark = float(input(f"Enter Mark {j + 1} For {name}: "))
                marks.append(mark)

            print_and_save_report(file, name, marks)

    print("\nAll Result Have Been Saved To 'student_result.txt'.")
    file.close()

# Main function call
main()