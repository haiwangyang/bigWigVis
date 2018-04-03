# bigWigVis
Visualize bigWig files of RNA-seq data (supported by pyGenomeTracks)<br>
<br>
# Tutorial
In bigWigVis/bigWigVis folder<br>
<br>
(1) put gtf files in gtf<br>
<br>
(2) generate bed files based on gtf<br>
<br>
    ./generate_bed_from_gtf.sh<br>
<br>
(3) generate track files for each species<br>
<br>
    ./generate_track_for_species.sh<br>
<br>
(4) modify track files (i.e., color, title, and etc)<br>
<br>
./modify_track_for_species.py<br>
<br>
(4) test pyGenomeTrack command<br>
<br>
    ./test_pyGenomeTracks.sh<br>
<br>
