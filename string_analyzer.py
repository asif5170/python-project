text = input("Enter a sentence: ")
# check for empty input
if len(text.split()) == 0:
    print("Please enter a valid sentence.")
    # length of the sentence
else:
    print("Length of the sentence: ", len(text))

    # First & last character
    print("First character: ", text[0])
    print("Last character: ", text[-1])

    # count of vowels
    vowels = "aeiouAEIOU"
    vowels_count = 0
    for char in text:
        if char in vowels:
            vowels_count += 1
    print("Number of vowels: ", vowels_count) 


    # Ask user for a word and count how many times it appears in the sentence
    word = input("Enter a word to count: ")
    count = text.count(word)
    print(f" '{word}' found {count} time(s)")

    # chack if 'python' is in the sentence
    if 'python' in text.lower():
        print("You like python!")

    # print 5 characters from the middle of the sentence
    middle = len(text) // 2
    slice_5 = text[middle:middle + 5]
    print("Middle 5 characters: ", slice_5)

    #Show lowercase and uppercase versions
    print("Lowercase version: ", text.lower())
    print("Uppercase version: ", text.upper())

    # Replace 'easy' with 'fun' if it exists
    # if "easy" in text.lower():
    #     replaced_text = text.replace("easy", "fun")
    #     print("Modified sentence: ", replaced_text)

    # Replace part of the sentence
    choice = input("Do you want to replace a part of the sentence? (yes/no): ").lower()
    if choice == "yes":
        old_part = input("Enter the part you want to replace: ")
        new_part = input("Enter the new part: ")
        modified = text.replace(old_part, new_part)
        print("Modified sentence: ", modified)


    print("Code completed successfully.")