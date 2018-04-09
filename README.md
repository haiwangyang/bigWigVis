# bigWigVis README
## why to use bigWigVis?
It is difficult to visualize and compare in one figure the expression of orthologs in different species, tissues, and sexes. IGV or UCSC can do the job, but so much manual works are required, considering that different species share different genome tracks and a shared y-axis is needed for different tissues/sexes. I developed bigWigVis to make it easy to visualize ortholog expression in species/tissues/sexes by just one command.<br> 
## what is bigWigVis?
The bigWigVis is to visualize bigWig files for RNA-seq data (supported by pyGenomeTracks)

## 
<br>
## Tutorial
In bigWigVis/bigWigVis folder<br>
<br>
(1) put gtf files in gtf<br>
FlyBase annotations are available:<br>
ftp://ftp.flybase.net/releases/FB2017_03<br>
Updated annotations are available:<br>
https://doi.org/10.6084/m9.figshare.6042005.v1<br>
<br>
(2) generate bed files based on gtf<br>
./generate_bed_from_gtf.sh<br>
<br>
(3) generate track files for each species<br>
./generate_track_for_species.sh<br>
<br>
(4) modify track files (i.e., color, title, and etc)<br>
./modify_track_for_species.py<br>
<br>
(5) given gene and y-axis-max generate pyGenomeTracks cmd<br>
run cmd to generate svgs for each ortholog<br>
merge the svgs into one<br>
./calc_for_gene.sh CG34222 100000<br>
<br>
(6) the merged svg can be viewed or edited in Adobe Illustrator<br>
![alt text](https://s3.us-east-2.amazonaws.com/haiwangyang.com/image/Yp1.png)
![alt text](https://s3.us-east-2.amazonaws.com/haiwangyang.com/image/sunn.png)
