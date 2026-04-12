#   CS-467 Project: Top-N Music Genre Classification Neural Network Project
#   Program: Main Program
#   Date: 04-12-2026
#   Programmer: Kelsey Shanks

def program_desc():
    """
    Displays information describing program
    """

    print("Welcome to Top-N Music Genre CNN!\n")
    print("This program is able to identify the following genres:\n"
          "\t1. Option 1\n\t2. Option 2\n\t3. Option 3\n\t4. Option 4\n\t5. Option 5\n"
          "\t6. Option 6\n\t7. Option 7\n\t8. Option 8\n\t9. Option 9\n\t10. Option 10\n")
    print("If provided a .wav audio file, this program will identify any of the above genres "
          "if they are exhibited in the audio file.\n")
    return

def validate_f_input(f_input: str): # TO-DO: Write checks for file type and extension!
    """
    Validates user input
    Return: BOOL - True if valid, False if invalid
    """

    #if f_input is .wav: True
    #else: False

    return True

def prompt_user():
    """
    Displays prompt to user for input
    Return: f_name (STR) - Holds file path to .wav audio file
    """

    while True:
        f_path = input("Please type the file path of the .wav audio file to examine: ")
        if validate_f_input():
            return f_path
        else:
            print("\nFile is not a .wav audio file. Please try again.\n")

def main():
    """
    Main Function - Executes main program of project and calls functions
    """

    #   Display Info: (To-Do PR1 - April 24)
    program_desc()

    #   Display Prompt: (To-Do PR1 - April 24)
    prompt_user()

    #   User Input: (To-Do PR1 - April 24)

    #   Call Pipeline: (To-Do PR2 - May 10)

    #   Get Result from Pipeline: (To-Do PR2 - May 10)

    #   Call CNN: (To-Do PR2 - May 10)

    #   Get Result from CNN: (To-Do PR2 - May 10)

    #   Sort Results (To-DO PR3 - May 24)

    #   Print Results: (To-Do PR1 - April 24) -> Edit for PR 3/4 - May 24/June 2

    return