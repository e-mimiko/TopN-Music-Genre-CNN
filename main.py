#   CS-467 Project: Top-N Music Genre Classification Neural Network Project
#   Program: Main Program
#   Date: 04-12-2026
#   Programmer: Kelsey Shanks

def program_desc() -> None:
    """
    Displays information describing program
    """

    print("Welcome to Top-N Music Genre CNN!\n"
          "This program is able to identify the following genres:\n"
          "\t1. Classical\n\t2. Country\n\t3. Disco\n\t4. HipHop\n\t5. Jazz\n"
          "\t6. Rock\n\t7. Blues\n\t8. Reggae\n\t9. Pop\n\t10. Metal\n"
          "If provided a .wav audio file, this program will identify any of the above genres "
          "if they are exhibited in the audio file.\n")
    return


def validate_f_input(f_input: str) -> bool:  # TO-DO: Write checks for file type and extension!
    """
    Validates user input
    Return: BOOL - True if valid, False if invalid
    """

    # if f_input is .wav: True
    # else: False

    return True


def prompt_user() -> str:
    """
    Displays prompt to user for input
    Return: f_name (STR) - Holds file path to .wav audio file
    """

    while True:
        f_path = input("Please type the file path of the .wav audio file to examine: ")
        if validate_f_input(f_path):
            return f_path
        else:
            print("\nFile is not a .wav audio file. Please try again.\n")


def display_genres(g_dict: dict[str, float]) -> None:
    """
    Displays genres from provided dictionary
    Parameter: g_dict (DICT) - holds genres and accuracy metric
    """

    print("Here are the genres detected with the percent confidence in the genre's presence:")
    for genre, metric in g_dict.items():
        if metric > 0.0:
            print(genre + ": " + str(metric) + "%")

    return


def main():
    """
    Main Function - Executes main program of project and calls functions
    """
    g_dict = {
        "Classical": 0.0,
        "Country": 0.0,
        "Disco": 0.0,
        "HipHop": 0.0,
        "Jazz": 0.0,
        "Rock": 0.0,
        "Blues": 0.0,
        "Reggae": 0.0,
        "Pop": 0.0,
        "Metal": 0.0,
    }

    #   Display Info: (To-Do PR1 - April 24)
    program_desc()

    #   Display Prompt: (To-Do PR1 - April 24)
    wav_file = prompt_user()

    #   User Input: (To-Do PR1 - April 24)

    #   Call Pipeline: (To-Do PR2 - May 10)

    #   Get Result from Pipeline: (To-Do PR2 - May 10)

    #   Call CNN: (To-Do PR2 - May 10)

    #   Get Result from CNN: (To-Do PR2 - May 10)

    #   Sort Results (To-DO PR3 - May 24)

    #   Print Results: (To-Do PR1 - April 24) -> Edit for PR 3/4 - May 24/June 2
    display_genres(g_dict)

    return