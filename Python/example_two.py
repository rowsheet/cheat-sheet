def example_function():
    print("THIS IS AN EXAMPLE FUNCTION")

"""
Don't worrie too much about what this means, this is just the "python" way
of setting the entry point of the file. When you run this python file
as is (versus including it from another file), it will run this protion.
"""
if __name__ == "__main__":
    print("TESTING")
    example_function()
