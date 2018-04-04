# bigWigVis
Visualize bigWig files of RNA-seq data (supported by pyGenomeTracks)<br>
<br>
# Tutorial
In bigWigVis/bigWigVis folder<br>
<br>
(1) put gtf files in gtf<br>
(2) generate bed files based on gtf<br>
./generate_bed_from_gtf.sh<br>
<br>
(3) generate track files for each species<br>
./generate_track_for_species.sh<br>
<br>
(4) modify track files (i.e., color, title, and etc)<br>
./modify_track_for_species.py<br>
<br>
(5) test pyGenomeTrack command<br>
    ./test_pyGenomeTracks.sh<br>
<br>
(6) generate generate_track cmd (to run the cmd add "| bash")<br>
python3 generate_pyGenomeTracks_cmd.py fne<br>
<br>
output:<br>
pyGenomeTracks --tracks track/w1118.forward.1.ini --region X:12917477-12950422 --outFileName pdf/fne.w1118.pdf
<br>pyGenomeTracks --tracks track/dyak.forward.1.ini --region X:7091984-7114301 --outFileName pdf/fne.dyak.pdf
<br>pyGenomeTracks --tracks track/dana.forward.1.ini --region scaffold_13117:3764945-3768676 --outFileName pdf/fne.dana.pdf
<br>pyGenomeTracks --tracks track/dpse.reverse.1.ini --region XL_group3a:1588940-1593108 --outFileName pdf/fne.dpse.pdf
<br>pyGenomeTracks --tracks track/dper.forward.1.ini --region scaffold_52:225704-234294 --outFileName pdf/fne.dper.pdf
<br>pyGenomeTracks --tracks track/dwil.forward.1.ini --region scf2_1100000004909:4977862-4983033 --outFileName pdf/fne.dwil.pdf
<br>pyGenomeTracks --tracks track/dmoj.forward.1.ini --region scaffold_6328:147017-151370 --outFileName pdf/fne.dmoj.pdf
<br>pyGenomeTracks --tracks track/dvir.reverse.1.ini --region scaffold_12928:4482025-4510194 --outFileName pdf/fne.dvir.pdf
<br>pyGenomeTracks --tracks track/dgri.reverse.1.ini --region scaffold_14853:1129804-1139248 --outFileName pdf/fne.dgri.pdf
<br>
(7) merge 
