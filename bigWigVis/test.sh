make_tracks_file --trackFiles bed/w1118.bed bed/w1118.YO.bed bw/w1118_f_wb.forward.bw bw/w1118_m_wb.forward.bw -o track/test.ini
pyGenomeTracks --tracks track/test.ini --region X:10,053,811-10,055,498 --outFileName pdf/test.pdf

