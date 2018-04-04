from __future__ import print_function, division
from shared_info import get_lines
import re

def get_id(others, tag):
    """ get id from gtf others field
        id could be geneid, refgeneid, ...
    """
    try:
        id = re.search(tag + ' "(.+?)"', others).group(1)
    except AttributeError:
        id = ""
    return id

class GtfInfo():
    """ GtfInfo Object """
    def __init__(self, species):
        self.linesYO = get_lines("gtf/" + species + ".YO.gtf")
        self.linesFB = get_lines("gtf/" + species + ".gtf")
        self.gid2range = self.get_gid2range()

    def get_gid2range(self):
        gid2range = dict()
        lines = self.linesYO + self.linesFB
        for line in lines:
            (scaffold, tag, feature, start, end, scoare, strand, dot, others) = line.rstrip().split("\t")
            this_gid = get_id(others, 'gene_id')
            start = int(start)
            end = int(end)
            if not this_gid in gid2range.keys():
                gid2range[this_gid] = dict()

            if not scaffold in gid2range[this_gid].keys():
                gid2range[this_gid][scaffold] = dict()
                gid2range[this_gid][scaffold]["strand"] = strand
                gid2range[this_gid][scaffold]["max"] = 0
                gid2range[this_gid][scaffold]["min"] = 99999999999999999

            if start < gid2range[this_gid][scaffold]["min"]:
                gid2range[this_gid][scaffold]["min"] = start
            if end > gid2range[this_gid][scaffold]["max"]:
                gid2range[this_gid][scaffold]["max"] = end
        return(gid2range)                


def main():
    g = GtfInfo("dyak")

if __name__ == '__main__':
    main()

