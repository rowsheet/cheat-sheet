def example_function():
    print("THIS IS AN EXAMPLE FUNCTION")

def read_antibiotics_file_and_print():
    """
    Open the file. Note: this assumes the filename and that it exits. If the
    file doesn't exist, this will cause an error.
    """
    with open("antibiotics.csv") as antibiotics_file:
        """
        Read the file contents.
        """
        file_contents = antibiotics_file.read()
        """
        Collect an array of the lines by taking all of the file contents and
        splitting by a new-line charachter (aka "carage return")
        """
        lines = file_contents.split("\n")
        """
        Go through each line.
        """
        for line in lines:
            """
            Print the line to the screen.
            """
            print(line) + ("ANOTHER LINE")

"""
Don't worrie too much about what this means, this is just the "python" way
of setting the entry point of the file. When you run this python file
as is (versus including it from another file), it will run this protion.
"""
if __name__ == "__main__":
    print("TESTING")
    example_function()
    read_antibiotics_file_and_print()
