# bigWigVis README
## Why to use bigWigVis?
It is difficult to visualize and compare in one figure the expression of orthologs in different species, tissues, and sexes. IGV or UCSC can do the job, but so much manual works are required, considering that different species share different genome tracks and a shared y-axis is needed for different tissues/sexes. I developed bigWigVis to make it easy to visualize ortholog expression in species/tissues/sexes by just one command.<br> 
## What is bigWigVis?
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
Now bed and track.ini are generated from previous steps. I wrote the python script to generate pyGenomeTracks command, given a gene name (e.g., Yp1) and correct y-axis-max (e.g., 10000000). It will fetch the scaffold, strand, and position of the given gene by another script (**gtf_info.py**). It will fetch the all orthologs of the same gene by another script (**ortholog_info.py**). When running, the script will generate individual svg for each species' ortholog, as well as a summary of strandness of orthologs each of the nine species.
* **merge_svg.py**<br>
Now svg files of different species' orthologs are available. I wrote the python script (based on svgutils.compose package) to merge all svg of the same gene together into one svg figure.
* **calc_for_gene.sh**<br>
A bash script to run **generate_pyGenomeTracks_cmd** and **merge_svg**, given a gene name and y-axis-max.

## What are the folders in bigWigVis?
* All scripts and data folders are under bigWigVis/bigWigVis<br>
* gtf/<br>
Original annotation in gtf format<br>
FlyBase annotations are available:<br>
ftp://ftp.flybase.net/releases/FB2017_03<br>
Updated annotations are available:<br>
https://doi.org/10.6084/m9.figshare.6042005.v1<br>
* genepred/<br>
Intermediate folder to convert gtf to genepred to bed
* bed/<br>
Final annotation in bed format
* bw/<br>
BigWig files of samples<br>
The data are available at https://doi.org/10.6084/m9.figshare.6041888.v1
* ortholog/<br>
It contains ortholog matrix in the file orth_8490.txt, so that I can connect gene symbol to gene id for any of the nine species.
* species/<br>
It contains species list under study in the file species.list.
* tissues/<br>
It contains tissue list under study in the file tissue.list
* expression/<br>
It contains max normalized read count (from DESeq2) in all tissues of D. melanogaster in the file dmel_max_expression.txt. It can help guess what y-axis-max need to be used for a certain gene.
* cluster/<br>
It contains kmean cluster information for sex-biased expression of orthologs in the file heatmap.sb15.txt.
* track/<br>
It contains template and final version of track.ini files needed for pyGenomeTracks.
* cmd/<br>
It contains command lines for commonly calculated genes
* svg/<br>
It contains individual and merged version of svg files.
* pdf/<br>
It contains individual and merged version of pdf files, which act as alternative format as svg.
* strandness/<br>
It contains summary of strandness for all orthologs for certain gene

## How to use bigWigVis?
In bigWigVis/bigWigVis folder
* **put data in correct folders**<br>
Required folders: gtf/, bw/, species/, tissue/, strandness/, and ortholog/<br> 
Optional folders: expression/ and cluster/<br>

* **generate bed files based on gtf**<br>
./generate_bed_from_gtf.sh<br>

* **generate track files for each species**<br>
./generate_track_for_species.sh<br>

* **modify track files (i.e., color, title, and etc)**<br>
./modify_track_for_species.py<br>

* **given gene and y-axis-max generate merged svg for all orthologs**<br>
./calc_for_gene.sh CG34222 100000<br>

* **the merged svg can be viewed or edited in Adobe Illustrator, such as**<br>
![alt text](https://s3.us-east-2.amazonaws.com/haiwangyang.com/image/Yp1.png)
![alt text](https://s3.us-east-2.amazonaws.com/haiwangyang.com/image/sunn.png)
