from __future__ import print_function, division
from ortholog_info import OrthologInfo
from shared_info import SharedInfo
from gtf_info import GtfInfo
import sys

gene = sys.argv[1]

# shared info
si = SharedInfo()

# ortholog info
o = OrthologInfo()
ortho_dct = o.ortho_dct[gene]

for species in si.species:
    g = GtfInfo(species)
    YOID = ortho_dct[species]
    gid2range = g.gid2range[YOID]
    scaffold = list(gid2range.keys())[0]
    info = gid2range[scaffold]
    start = info['min']
    end = info['max']
    strand = info['strand']
    if strand == "+":
        direction = "forward"
    elif strand == "-":
        direction = "reverse"

    print("pyGenomeTracks --tracks track/" + species + "." + direction + ".1.ini --region " + scaffold + ":" + str(start) + "-" + str(end) + " --outFileName pdf/" + gene + "." + species + ".pdf")


