# generate exon.gtf
module load ucsc/360
for i in gtf/*.gtf; do
    echo $i
    ii=${i/.gtf/.exon.gtf}
    iii=`echo $i | sed 's#gtf#genepred#g'`
    iv=`echo $i | sed 's#gtf#bed#g'`
    cat $i | awk '$3=="exon"' >$ii
    gtfToGenePred $ii $iii
    genePredToBed $iii $iv
    rm $ii
    rm $iii
done

