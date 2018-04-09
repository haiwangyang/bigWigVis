from __future__ import print_function, division
from ortholog_info import OrthologInfo
from shared_info import SharedInfo, get_A2B
from gtf_info import GtfInfo
import sys

gene = sys.argv[1]
maxexp = sys.argv[2]

# shared info
si = SharedInfo()

# ortholog info
o = OrthologInfo()
ortho_dct = o.ortho_dct[gene]

with open("strandness/" + gene + ".txt", "w") as f:
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
        f.write("\t".join([species, YOID, strand]) + "\n")
        print("pyGenomeTracks --tracks track/" + species + "." + direction + "." + maxexp + ".ini --region " + scaffold + ":" + str(start) + "-" + str(end) + " --width 10 --height 40 --dpi 100 --outFileName svg/" + gene + "." + species + ".svg")
    
    
