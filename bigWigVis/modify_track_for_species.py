from __future__ import print_function, division
from shared_info import get_lines, SharedInfo

""" modify track ini file
(1) make color correct for YO annotation
(2) make color correct for sex (female:red; male:blue)
(3) number of bin => 1
(4) make title shorter, e.g., title = w1118_f_ac.forward => title = w1118_f_ac
"""

def replace(line, a, b):
    """ 
    if line starts with string a, then
    replace string a with string b in line
    """
    mline = line
    if line.startswith(a):
        mline = line.replace(a,b)
    return(mline)

class Track():
    """ Track object """
    def __init__(self, species, strandness, maxexp):
        self.species = species
        self.strandness = strandness
        self.maxexp = maxexp
        self.filepath = "track/" + self.species + "." + self.strandness + ".ini"
        self.lines = get_lines(self.filepath)
        self.mlines = self.get_modified_lines()
        
    def get_modified_lines(self):
        """ modify track files """
        mlines = []
        sex = ""
        for line in self.lines:
            if line.startswith("#fontsize=20"):
                mlines.append(line.replace("#fontsize=20","fontsize=5"))
            elif line.startswith("fontsize = 10"):
                mlines.append(line.replace("fontsize=10","fontsize=30"))
            elif line.startswith("#line width = 0.5"):
                mlines.append(line.replace("#line width = 0.5","line width = 5"))

            elif line.startswith("labels = off"):
                mlines.append(line.replace("labels = off","labels = on"))

            elif line.startswith("color = darkblue"):
                mlines.append(line.replace("color = darkblue","color = grey"))

            elif line.startswith("#style = flybase"):
                mlines.append(line.replace("#style = flybase", "style = flybase"))

            elif line.startswith("title"):
                mlines.append(line.replace("title", "#title"))
                #if "forward" in line:
                #    mlines.append(line.replace(".forward", "(+)"))
                #elif "reverse" in line:
                #    mlines.append(line.replace(".reverse", "(-)"))
                #else:
                #    mlines.append(line)

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
            elif line.startswith("show data range = yes"):
                mlines.append(line.replace("show data range = yes", "show data range = no"))

            elif line.startswith("#max_value = auto"):
                mlines.append(line.replace("#max_value = auto", "max_value = " + self.maxexp))
            
            elif line.startswith("number of bins = 500"):
                mlines.append(line.replace("number of bins = 500", "number of bins = 500"))
            
            else:
                mlines.append(line)
        return(mlines)

    def print_mlines(self):
        with open(self.filepath.replace(".ini", "." + self.maxexp + ".ini"), "w") as f:
            for mline in self.mlines:
                f.write(mline)
        print(self.filepath.replace(".ini", "." + self.maxexp + ".ini") + " file generated")

def main():
    si = SharedInfo()

    for s in si.species:
        for d in si.strandness: # call it direction to avoid confusion for "s"
            for m in ['1000', '2000', '3000', '4000', '5000', '6000', '7000', '8000', '9000', '10000', '20000', '30000', '40000', '50000', '60000', '70000', '80000', '90000', '100000', '1000000', '10000000']: # maxexp for bigWig track
                t = Track(s, d, m)
                t.print_mlines()

if __name__ == '__main__':
    main()

