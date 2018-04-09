# calculate for all orthologs
./calc_for_gene.sh Yp1 10000000
./calc_for_gene.sh lilli 10000
./calc_for_gene.sh gpp 10000

./calc_for_gene.sh CheA87a 10000
./calc_for_gene.sh CG15894 10000
./calc_for_gene.sh se 10000
./calc_for_gene.sh VhaM9.7-a 10000
./calc_for_gene.sh Nlg1 30000
./calc_for_gene.sh gammaTub37C 100000
./calc_for_gene.sh sunn 10000

./calc_for_gene.sh CG34222 100000
./calc_for_gene.sh CG31805 50000
./calc_for_gene.sh CG6652 100000
./calc_for_gene.sh Eglp1 100000
./calc_for_gene.sh CG17005 100000
./calc_for_gene.sh prd 100000
./calc_for_gene.sh gom 100000
./calc_for_gene.sh CG2990 1000
./calc_for_gene.sh CG15522 10000
./calc_for_gene.sh Mal-A6 10000



# calculate one ortholog in certain species
pyGenomeTracks --tracks track/w1118.forward.10000.ini --region 2R:19979242-19984895  --width 40 --height 40 --dpi 100 --outFileName svg/CG8654.w1118.svg

pyGenomeTracks --tracks track/dgri.forward.10000.ini --region scaffold_15110:16717000-16725000  --width 40 --height 40 --dpi 100 --outFileName svg/CG30438.dgri.svg

