# given a gene and y-axis-max
g=$1
y=$2

# generate genome-track svg for each ortholog
python3 generate_pyGenomeTracks_cmd.py $g $y | bash

# merge svg files
python3 merge_svg.py $g
