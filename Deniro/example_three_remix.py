#!/usr/bin/python3
def example_function():
    print("Corona Virus Rules")

def read_deniro_file_and_print():
    with open("deniro.csv") as deniro_file:
        file_contents = deniro_file.read()
        lines = file_contents.split("\n")
        for line in lines:
            print(line + "\n")


if __name__ == "__main__":
    print("TESTING")
    example_funtion()
    read_deniro_file_and_print()

