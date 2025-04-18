num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

print("select an operation: 1.(+),2.(-),3.(*),4.(/)")

choice = input("Your choice (1/2/3/4): ") 


if choice == '1':
   result = num1 + num2
   print("Result = ",result)

elif choice == '2':
   result = num1 - num2
   print("Result = ",result)

elif choice == '3':
   result = num1 * num2
   print("Result = ",result)

elif choice == '4':
   if num2!= 0:
    result = num1 / num2
    print("Result = ",result)
   else:
      print("Division by zero is not allowed!")

else:
   print("Invalid option!")