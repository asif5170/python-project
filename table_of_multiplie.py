# Table of Multiplie
while True:
    print("1.Multiplie")
    print("2. Exit")
    choice = input("Enter Your choice 1 - 2: ")
    if choice == '1':
       n = int(input("Enter Multiplie Number: "))
       for i in range(1, 11):
           print(f"{n} x {i} = {n * i}")

    elif choice == '2':
        print("Programme is Closed")
        break
    else:
        print("Enter Valid Option!")
        