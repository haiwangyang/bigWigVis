from __future__ import print_function, division
from shared_info import get_lines, SharedInfo
import pandas

""" get ortholog information
Convert IDs if neccessary DyakG_ => YOgnYA
"""

def convert_to_YOgn(gid):
    """ input DyakG_009556
        output YOgnYA09556
    """
    if gid.startswith("D") and "G_" in gid:
        DxxxG, five_digits = gid.split("_0")
        XX = DxxxG[1:3].upper()
        return("YOgn" + XX + five_digits)
    else:
        return(gid)

def convert_to_dxxx(s):
    """ input w1118
        output dmel
    """
    if s == "w1118":
        return("dmel")
    elif s == "oreR":
        return("dmel")
    elif s == "dgriG1":
        return("dgri")
    else:
        return(s)

class OrthologInfo():
    """ OrthologInfo Object """
    def __init__(self):
        self.lines = get_lines("ortholog/orth_8490.txt")
        self.ortho_table = pandas.read_table("ortholog/orth_8490.txt", sep="\t")
        self.ortho_dct = self.get_ortho_dct()

    def get_ortho_dct(self):
        """ get ortho dict """
        si = SharedInfo()
        dct = dict()
        for index, row in self.ortho_table.iterrows():
            symbol = row['symbol']
            if not symbol in dct.keys():
                dct[symbol] = dict()
            for s in si.species:
                dxxx = convert_to_dxxx(s)
                dct[symbol][s] = convert_to_YOgn(row[dxxx])
        return(dct)

def main():
    o = OrthologInfo()

if __name__ == '__main__':
    main()



