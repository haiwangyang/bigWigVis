# bigWigVis README
## why to use bigWigVis?
It is difficult to visualize and compare in one figure the expression of orthologs in different species, tissues, and sexes. IGV or UCSC can do the job, but so much manual works are required, considering that different species share different genome tracks and a shared y-axis is needed for different tissues/sexes. I developed bigWigVis to make it easy to visualize ortholog expression in species/tissues/sexes by just one command.<br> 
## what is bigWigVis?
The bigWigVis is to visualize bigWig files for RNA-seq data, it is a combination of python (supported by pyGenomeTracks package) and bash scripts. 
* **shared_info.py**<br>
A python script that collect information needed for multiple downstream scripts, such as commonly used functions and possible options for species/tissues/strandness.   
* **generate_bed_from_gtf.sh**<br>
The pyGenomeTracks will need a bed file (not gtf/gff3) to draw annotations in certain genomic region, and I generate such bed file from gtf annotation.  To make the problem simple, each species will just have one bed file, rather than many bed files for different genomic regions.
* **generate_track_for_species.sh**<br>
The pyGenomeTracks will also need a track file to know the style and format of the vector figures (such as svg). It uses the make_tracks_file command to do the job.  I wrote a bash script to generate make_tracks_file commands, which further generate template track.ini files.  We call these track.ini files template, because all parameters in the track.ini are default and to achieve custermized illustration, a lot of them need to be modified.
* **modify_track_for_species.py**<br>
I wrote the python script to modify the template track.ini generated in the previous step.  In the track.ini, titles, fonts, and colors of tracks are custormized for my project. For instance, red and blue barplots are used to denote female and male samples respectively. I also generated different versions of y-axis-max, so that in future I can use the right one for certain gene. For instance, Yp1 is a highly expressed gene (y-axis-max=10000000) while CG2990 is a lowly expressed gene (y-axis-max = 1000).
* **generate_pyGenomeTracks_cmd.py**<br>
Now bed and track.ini are generated from previous steps. I wrote the python script to generate pyGenomeTracks command, given a gene name (e.g., Yp1) and correct y-axis-max (e.g., 10000000). It will fetch the scaffold, strand, and position of the given gene by another script (**ortholog_info.py**).  It also generate summary of strandness of orthologs each of the nine species.


## folders in bigWigVis/bigWigVis

## Tutorial
In bigWigVis/bigWigVis folder
* **put gtf files in gtf**<br>
FlyBase annotations are available:<br>
ftp://ftp.flybase.net/releases/FB2017_03<br>
Updated annotations are available:<br>
https://doi.org/10.6084/m9.figshare.6042005.v1<br>

* **generate bed files based on gtf**<br>
./generate_bed_from_gtf.sh<br>

* **generate track files for each species**<br>
./generate_track_for_species.sh<br>

* **modify track files (i.e., color, title, and etc)**<br>
./modify_track_for_species.py<br>

* **given gene and y-axis-max generate pyGenomeTracks cmd**<br>
run cmd to generate svgs for each ortholog<br>
merge the svgs into one<br>
./calc_for_gene.sh CG34222 100000<br>

* **the merged svg can be viewed or edited in Adobe Illustrator**<br>
![alt text](https://s3.us-east-2.amazonaws.com/haiwangyang.com/image/Yp1.png)
![alt text](https://s3.us-east-2.amazonaws.com/haiwangyang.com/image/sunn.png)
