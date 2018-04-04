
# cluster 1
for i in `cat cluster/cluster1.symbol`; do echo "p3 generate_pyGenomeTracks_cmd.py $i 10000 | bash"; done >batch.cmd.sh
swarm -f batch.cmd.sh

for i in `cat cluster/cluster1.symbol`; do echo "p3 merge_pdf.py $i"; done >batch.cmd.sh
swarm -f batch.cmd.sh

# pyGenomeTracks --tracks track/w1118.forward.10000000.ini --region X:10053794-10055564 --width 10 --height 40 --dpi 100 --outFileName svg/Yp1.w1118.svg

# pyGenomeTracks --tracks track/w1118.forward.10000.ini --region X:12917477-12950422 --width 10 --height 40 --dpi 100 --outFileName svg/fne.w1118.svg


# p3 generate_pyGenomeTracks_cmd.py Yp1 10000000

# p3 generate_pyGenomeTracks_cmd.py CG11029 10000
# p3 merge_pdf.py CG11029
# inkscape --export-pdf=pdf/CG11029.merged.pdf svg/CG11029.merged.svg

