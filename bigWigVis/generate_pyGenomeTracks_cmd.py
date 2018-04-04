from __future__ import print_function, division
from ortholog_info import OrthologInfo
from shared_info import SharedInfo
from gtf_info import GtfInfo
from shared_info import get_A2B
import sys

gene = sys.argv[1]
maxexp = sys.argv[2]

# alternatively we can assign maxexp by maxnrc
### max normalized read counts of gene in all dmel samples
#gene2maxnrc = get_A2B("expression/dmel_max_expression.txt")

#def get_maxexp(maxnrc):
#    if maxnrc <1000:
#        return(1000)
#    elif maxnrc < 100000:
#        return(10000)
#    else
#        return(1000000)

#maxexp = gene2maxnrc(gene2maxnrc[gene])

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

    print("pyGenomeTracks --tracks track/" + species + "." + direction + "." + maxexp + ".ini --region " + scaffold + ":" + str(start) + "-" + str(end) + " --width 10 --height 40 --dpi 100 --outFileName svg/" + gene + "." + species + ".svg")


