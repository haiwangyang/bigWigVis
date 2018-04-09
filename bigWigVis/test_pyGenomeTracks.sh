
# cluster 1
for i in `cat cluster/cluster1.symbol`; do echo "p3 generate_pyGenomeTracks_cmd.py $i 10000 | bash"; done >batch.cmd.sh
swarm -f batch.cmd.sh

for i in `cat cluster/cluster1.symbol`; do echo "p3 merge_pdf.py $i"; done >batch.cmd.sh
swarm -f batch.cmd.sh

# pyGenomeTracks --tracks track/w1118.forward.10000000.ini --region X:10053794-10055564 --width 10 --height 40 --dpi 100 --outFileName svg/Yp1.w1118.svg

# pyGenomeTracks --tracks track/w1118.forward.10000.ini --region X:12917477-12950422 --width 10 --height 40 --dpi 100 --outFileName svg/fne.w1118.svg

# context example 1 in dmel
pyGenomeTracks --tracks track/w1118.forward.10000.ini --region 2R:19979242-19984895  --width 40 --height 40 --dpi 100 --outFileName svg/CG8654.w1118.svg

# context example 2 in dgri
pyGenomeTracks --tracks track/dgri.forward.10000.ini --region scaffold_15110:16717000-16725000  --width 40 --height 40 --dpi 100 --outFileName svg/CG30438.dgri.svg


./calc_for_gene.sh Yp1 10000000
./calc_for_gene.sh lilli 10000
./calc_for_gene.sh gpp 10000

# go dpse opposite dper
./calc_for_gene.sh CheA87a 10000
./calc_for_gene.sh CG15894 10000
./calc_for_gene.sh se 10000
./calc_for_gene.sh VhaM9.7-a 10000
./calc_for_gene.sh Nlg1 30000
./calc_for_gene.sh gammaTub37C 100000
./calc_for_gene.sh sunn 10000

# testis even
./calc_for_gene.sh CG34222 100000
./calc_for_gene.sh CG31805 50000
./calc_for_gene.sh CG6652 100000
./calc_for_gene.sh Eglp1 100000 &
./calc_for_gene.sh CG17005 100000 &
./calc_for_gene.sh prd 100000 &
./calc_for_gene.sh gom 100000 &

p3 generate_pyGenomeTracks_cmd.py CG2990 1000 | bash
p3 merge_pdf.py CG2990

p3 generate_pyGenomeTracks_cmd.py CG15522 10000 | bash
p3 merge_pdf.py CG15522


p3 generate_pyGenomeTracks_cmd.py Mal-A6 10000 | bash
p3 merge_pdf.py Mal-A6





# p3 generate_pyGenomeTracks_cmd.py CG11029 10000
# p3 merge_pdf.py CG11029
# inkscape --export-pdf=pdf/CG11029.merged.pdf svg/CG11029.merged.svg

