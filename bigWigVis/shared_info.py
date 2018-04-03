from __future__ import print_function, division

def get_lines(filepath):
    with open(filepath, 'r') as f:
        lines = f.readlines()
        return lines

def get_elements(filepath):
    with open(filepath, 'r') as f:
        lines = f.readlines()
        elements = list()
        for line in lines:
             elements.append(line.rstrip())
        return(elements)


class SharedInfo():
    """ SharedInfo object """
    def __init__(self):
        self.species = get_elements("species/species.list")
        self.tissue = get_elements("tissue/tissue.list")
        self.strandness = get_elements("strandness/strandness.list")

def main():
    si = SharedInfo()

if __name__ == '__main__':
    main()
