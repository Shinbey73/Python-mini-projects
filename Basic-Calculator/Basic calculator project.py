"""
My Basic Calculator
14/2/2025

"""

print("\n +++++++ Welcome to my basic calculator ++++++\n")

def calculator():
    """
    Main function to run the basic calculator. It displays available operations,
    prompts the user for an operation and numbers, and then prints the result.
    The loop continues until the user selects Exit.
    """
    
    while True:
        operations = {
            1: ("Addition",addition),
            2: ("Subtraction", subtraction),
            3: ("Multiplication", multiplication),
            4: ("Division", division),
            5: ("Exit", None)
        }   
        #show the available operations
        print("\nOptions:")    
        for key, (value_name,value_func) in operations.items():
            print(f"Enter {key} for {value_name}")

        #prompt the user for an operation
        try:
            user_input = int(input("\nEnter your choice: "))

            if user_input not in operations.keys():
                raise ValueError
            
        except ValueError:
            print("\nInvalid input. Please try again\n")
            continue

        #exit the program
        if user_input == 5:
            print("\nExiting the program")
            break
        
        
        operations_name, operations_function = operations[user_input]
        
        #confirm the operation
        comfirm = input(f"\nYou chose {operations_name}.\nDo you want to perform {operations_name} operation? \nPlease enter 'y' for yes or 'n' for no: ").lower()
        
        #return to the main menu
        if comfirm == 'n':
            print("Returning to the main menu.\n")
            continue

        #prompt the user for numbers
        num1 = get_number()
        num2 = get_number()
        
        #perform the operation spesifically for division
        if user_input == 4:
            
            while True:
                try:
                    print(f"\nThe result is: {division(num1, num2)}\n")
                    break
                
                except ZeroDivisionError:
                    print("\nYou can't divide by zero. Please try again.\nEnter a non-zero number for divisor!\n")
                    num2 = get_number()
        
        #perform the operation for other operations
        try:
            result = operations_function(num1, num2)    
            print(f"\nThe result is: {result}\n")
        
        except Exception as Error:
            print(f"\nAn error occurred: {Error}\n")
            continue
                


def addition(num1, num2):
    return num1 + num2

def subtraction(num1, num2):
    return num1 - num2

def multiplication(num1, num2):
    return num1 * num2

def division(num1, num2):
    return num1 / num2


def get_number():
    while True:
        try:
            return float(input("\nEnter a number: "))
        except ValueError:
            print("Invalid input. Please try again")


if __name__ == "__main__":
    calculator()
      