# Importing the necessary module
from random import randint

# Creating the random number
rand_int = randint(1, 100)

# Creating the desired number range
number_range = range(1, 101)

def validation(num: str) -> bool:
    '''
    This is a function that takes an input from the user and validates if it is an integer and if it is within the range

    INPUTS: Any input from the user (int, float, string) in string form
    OUTPUTS: Boolean value
                - True = The value is an integer
                - False = The value is not an integer OR an integer has bene inputted but is not within 1 and 100 inclusive
    '''

    # Try, except loop to catch ValueErrors (eg the use has inputted a string)
    try:
        # Checking if the number can be convereted to an integer
        num = int(num)
        
        # Logical to catch if an integer has been inputted, but is not within 1 to 100 inclusive
        if num not in number_range:
            print("You have given an integer that is outside the range! Please enter an integer between 1 and 100.")
            return False
        
        else:
            return True
        

    except ValueError:
        print("You have given an invalid input! Please give an integer.")

        return False
    
    
    
def determine_position(num: int) -> bool:
    '''
    This is a function the determins the position of a guessed number and prints a message saying higher, lower, or correct

    INPUTS: An integer within the hardcoded number range
    OUTPUTS: Printing statement + boolean, False if incorrect guess
                                           True if correct guess
    '''

    # Series of logicals to see where the number is
    if num < rand_int:
        print("You have guessed too low! Try again.")
        return False

    elif num > rand_int:
        print("You ahve guessed too high! Try again.")
        return False
    
    else:
        print("Congratulations! You have guessed the random integer correctly!")
        return True

    

# Loop that runs indefinately until a correct guess
while True:
    # Asking for user unput and validating it
    guessed_int = input("Guess the random integer: ")
    validate_guess = validation(guessed_int)

    # Logical to see if the user inputted something that can be accepted
    if validate_guess == True:
        guessed_int = int(guessed_int)

        # Determining if the correct number is guessed
        correct_number = determine_position(guessed_int)

        if correct_number == True:
            break