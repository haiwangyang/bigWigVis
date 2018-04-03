#!/bin/bash
# generate track ini files for pyGenomeTracks
# eaches species and direction will have one track ini file 
# tissues of the bw are sorted by sex-biased expression, except the whole body (wb)
for s in `cat species/species.list`; do 
    for d in `echo forward reverse`; do
        echo -ne "make_tracks_file --trackFiles bed/${s}.YO.bed "
        
        for t in `cat tissue/tissue.list`; do
            ls bw/${s}*${t}*${d}.bw | tr -s '\n' ' '
        
        done
        echo -ne " -o track/${s}.${d}.ini\n"
    done
done


