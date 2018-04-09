# bigWigVis README
## why to use bigWigVis?
It is difficult to visualize and compare in one figure the expression of orthologs in different species, tissues, and sexes. IGV or UCSC can do the job, but so much manual works are required, considering that different species share different genome tracks and a shared y-axis is needed for different tissues/sexes. I developed bigWigVis to make it easy to visualize ortholog expression in species/tissues/sexes by just one command.<br> 
## what is bigWigVis?
The bigWigVis is to visualize bigWig files for RNA-seq data, it is a combination of python (supported by pyGenomeTracks package) and bash scripts. 
* generate_bed_from_gtf.sh
pyGenomeTracks will need a bed file (not gtf/gff3) to draw annotations in certain genomic region, and I generate such bed file from gtf annotation.  To make the problem simple, each species will just have one bed file, rather than many bed files for different genomic regions.
* generate_track_for_species.sh

## 
<br>
## Tutorial
In bigWigVis/bigWigVis folder<br>
<br>
* put gtf files in gtf
FlyBase annotations are available:<br>
ftp://ftp.flybase.net/releases/FB2017_03<br>
Updated annotations are available:<br>
https://doi.org/10.6084/m9.figshare.6042005.v1<br>
<br>
* generate bed files based on gtf
./generate_bed_from_gtf.sh<br>
<br>
* generate track files for each species
./generate_track_for_species.sh<br>
<br>
* modify track files (i.e., color, title, and etc)
./modify_track_for_species.py<br>
<br>
* given gene and y-axis-max generate pyGenomeTracks cmd
run cmd to generate svgs for each ortholog<br>
merge the svgs into one<br>
./calc_for_gene.sh CG34222 100000<br>
<br>
* the merged svg can be viewed or edited in Adobe Illustrator
![alt text](https://s3.us-east-2.amazonaws.com/haiwangyang.com/image/Yp1.png)
![alt text](https://s3.us-east-2.amazonaws.com/haiwangyang.com/image/sunn.png)
