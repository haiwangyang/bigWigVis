g=$1
y=$2
p3 generate_pyGenomeTracks_cmd.py $g $y | bash
p3 merge_pdf.py $g
