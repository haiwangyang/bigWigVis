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
ortho_dct = o.ortho_dct["Yp1"]

for species in si.species:
    print(species)
    g = GtfInfo(species)
    YOID = ortho_dct[species]
    gid2range = g.gid2range[YOID]
    print(gid2range)

