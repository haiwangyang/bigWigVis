from __future__ import print_function, division
from shared_info import get_lines, SharedInfo

""" modify track ini file
(1) make color correct for YO annotation
(2) make color correct for sex (female:red; male:blue)
(3) number of bin => 1
(4) make title shorter, e.g., title = w1118_f_ac.forward => title = w1118_f_ac
"""

class Track():
    """  object """
    def __init__(self, species, strandness):
        self.species = species
        self.strandness = strandness
        self.filepath = "track/" + self.species + "." + self.strandness + ".ini"
        self.lines = get_lines(self.filepath)
        self.mlines = self.get_modified_lines()

    def get_modified_lines(self):
        """ modify track files """
        mlines = []
        sex = ""
        for line in self.lines:
            if line.startswith("color = darkblue"):
                mlines.append(line.replace("darkblue","darkgreen"))
            elif line.startswith("title"):
                if "forward" in line:
                    mlines.append(line.replace(".forward", "(+)"))
                elif "reverse" in line:
                    mlines.append(line.replace(".reverse", "(-)"))
                else:
                    mlines.append(line)
            elif line.startswith("file=bw"):
                sex = line.split("_")[1]
                mlines.append(line)
            elif line.startswith("color = #666666"):
                if sex == "f":
                    mlines.append(line.replace("#666666", "red"))
                elif sex == "m":
                    mlines.append(line.replace("#666666", "blue"))
                else:
                    mlines.append(line)
            else:
                mlines.append(line)
        return(mlines)

    def print_mlines(self):
        with open(self.filepath.replace(".ini", ".1.ini"), "w") as f:
            for mline in self.mlines:
                f.write(mline)
        print(self.filepath.replace(".ini", ".1.ini") + " file generated")

def main():
    si = SharedInfo()

    for s in si.species:
        for d in si.strandness: # call it direction to avoid confusion for "s"
            t = Track(s, d)
            t.print_mlines()

if __name__ == '__main__':
    main()

