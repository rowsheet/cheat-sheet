class Antibiotic:
    name = ""
    klass = ""
    atc_code = ""
    category = ""
    eml = False

    def __init__(self, name, klass, atc_code, category, eml):
        self.name = name
        self.klass = klass
        self.atc_code = atc_code
        self.category = category
        self.eml = eml

    def print(self):
        print("name: " + self.name)
        print("\tclass:     " + self.klass)
        print("\tatc_code:  " + self.atc_code)
        print("\tcategory:  " + self.category)
        print("\teml:       " + str(self.eml))

def load_antibiotics():
    with open("antibiotics.csv") as antibiotics_file:
        file_contents = antibiotics_file.read()
        lines = file_contents.split("\n")
        antibiotics_list = []
        for line in lines:
            try:
                vals = line.split(",")
                name = vals[0]
                klass = vals[1]
                atc_code = vals[2]
                category = vals[3]
                eml = vals[4]
                antibiotic = Antibiotic(name, klass, atc_code, category, eml)
                antibiotics_list.append(antibiotic)
            except Exception as ex:
                pass
        for antibiotic in antibiotics_list:
            antibiotic.print()

"""
Don't worrie too much about what this means, this is just the "python" way
of setting the entry point of the file. When you run this python file
as is (versus including it from another file), it will run this protion.
"""
if __name__ == "__main__":
    load_antibiotics()
