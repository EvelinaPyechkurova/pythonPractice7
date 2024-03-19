# output.py

def output_to_console(text):
    """
    Outputs the given text to the console.

    Parameters:
    - text: The text to be printed.
    """
    print(text)

def write_to_file_builtin(filepath, text):
    """
    Writes the given text to a file.txt using Python's built-in capabilities.

    Parameters:
    - filepath: The path to the file.txt where the text will be written.
    - text: The text to write to the file.txt.
    """
    with open(filepath, 'w') as file:
        file.write(text)