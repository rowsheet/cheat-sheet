#!/usr/bin/python3

class Deniro:
    title = ""
    year = ""
    score = ""

    def __init__(self, title=title, year=year, score=score):
        self.title = self
        self.year = year
        self.score = score

    def print(self):
        print("""title: %s
    year:  %s
    score: %s""" % (
        self.title,
        self.year,
        self.score))
    
def load_deniro():
    with open("deniro.csv") as deniro_file:
        file_contents = deniro_file.read()
        lines = file_contents.split("\n")
        deniro_list = []
        for line in lines:
            try:
                vals = line.split(",")
                title = vals[0]
                year = vals[2]
                score = vals[4]
                deniromovie = DeniroMovie(
                    title=title,
                    year=year,
                    score=score)
                deniro_list.append(deniro)
"""
Dude I cant get this thing to run. Whats the deal with the error.
Its something to do with this last thing you told me not to worry
about on example_four. Let me know or change it up.
"""
    
if __name__ == "__main__":
    load_deniro()
