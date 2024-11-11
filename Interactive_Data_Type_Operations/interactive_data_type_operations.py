# Prompt the user to choose a data type to perform operations on
print("Choose a data type to perform operations on:")
print("1. Strings")
print("2. Numbers")
print("3. Booleans")
print("4. Additional Data Types (List, Tuple, Dictionary)")

# Get the user's choice and store it in a variable
choice = input("Enter the number of your choice (1-4): ")

# If the user chooses Strings (choice == '1'):
if choice == '1':
    # Declare a string variable, e.g., sentence = "Learning Python is fun!"
    text = "Working with strings is fun!"

    # Extract and print a substring, such as the word "Python" from the sentence.
    extracted_word = text[13:20]

    # Convert the entire sentence to uppercase and print it.
    uppercase_text = text.upper()

    # Replace a word in the sentence (e.g., replace "fun" with "awesome") and print the modified sentence.
    replaced_text = text.replace("fun", "interesting")

    print(f"Original text is: {text}")
    print(f"An extracted word from the original text: {extracted_word}")
    print(f"Original text converted in uppercase: {uppercase_text}")
    print(f"Word 'fun' replaced with 'interesting': {replaced_text}")

# If the user chooses Numbers (choice == '2'):
elif choice == '2':
    # Prompt the user to input two numbers, e.g., num1 and num2.
    first_number = float(input())
    second_number = float(input())

    # Perform and print the results of addition, subtraction, multiplication, and division.
    addition = first_number + second_number
    subtraction = first_number - second_number
    multiplication = first_number * second_number

    # Handle division by zero (e.g., print an error message if num2 is zero).
    division = 0
    second_number_is_zero = False
    if second_number == 0:
        second_number_is_zero = True
    else:
        division = first_number / second_number

    # Perform a power operation, raising num1 to the power of num2, and print the result.
    power_operation = first_number ** second_number

    print(f"Sum of the two numbers: {addition}")
    print(f"Difference of the two numbers: {subtraction}")
    print(f"Product of the two numbers: {multiplication}")
    if second_number == 0:
        print("It is not possible to divide by zero!")
    else:
        print(f"Division of the two numbers: {division}")

# If the user chooses Booleans (choice == '3'):
elif choice == '3':
    # Declare two boolean variables, e.g., is_python_fun = True, is_sunny = False.
    programming_with_python_is_fun = True
    i_do_not_like_chocolate = False

    # Perform and print the results of logical operations: AND, OR, NOT.
    if programming_with_python_is_fun and i_do_not_like_chocolate:
        print("I love both programming but not chocolate.")
    elif programming_with_python_is_fun and not i_do_not_like_chocolate:
        print("I love both programming and chocolate.")
    elif not programming_with_python_is_fun and i_do_not_like_chocolate:
        print("It is not true that I do not like programming with Python and chocolate!")

    # Perform and print the results of comparison operations (e.g., 10 > 5 and 5 == 5).
    comparison = 10 > 5
    print(f"Is 10 > 5: {comparison}")
    comparison = 5 == 5
    print(f"Is 5 == 5: {comparison}")

# If the user chooses Additional Data Types (choice == '4'):
elif choice == '4':
    # ### List Operations ###
    # Create a list with mixed data types (e.g., numbers, strings, booleans).
    created_list = [1, 3, "Python", True]
    print(f"Created list is: {created_list}")

    # Append a new element to the list and print the updated list.
    created_list.append(["hello", "there"])
    print(f"List with words 'hello' and 'there' was added. Updated list is: {created_list}")

    # Access and print the 4th element in the list.
    fourth_element = created_list[4]
    print(f"Fourth element of the updated list is: {fourth_element}")
    print()

    # ### Tuple Operations ###
    # Create a tuple with some string elements (e.g., fruits).
    created_tuple = ("Programming", 7, True, {"type": "tuple"})
    print(f"Created tuple is: {created_tuple}")

    # Print the length of the tuple.
    tuple_length = len(created_tuple)
    print(f"Length of tuple is: {tuple_length}")

    # Try to modify one element in the tuple and handle the resulting TypeError.
    print("Modification of tuple's elements is not possible. "
          "Otherwise following error will be raised:\nTypeError: 'tuple' object does not support item assignment")
    print()

    # ### Dictionary Operations ###
    # Create a dictionary with some key-value pairs (e.g., name, age, city).
    created_dictionary = {"Name": "Iveta", "Interests": "Programming, Sports and Reading", "Favourite color": "Green"}
    print(f"Created dictionary is: {created_dictionary}")

    # Access and print the value for one of the keys (e.g., "age").
    interests = created_dictionary["Interests"]
    print(f"Added key 'Interests' in the dictionary with following values: {interests}")

    # Add a new key-value pair to the dictionary and print the updated dictionary.
    created_dictionary["Last visited place"] = "Malta"
    print(f"Last visited place was {created_dictionary['Last visited place']}")

# If the user enters an invalid choice:
else:
    # Print an error message indicating an invalid selection.
    print("Choice is invalid. Please make a valid selection.")
