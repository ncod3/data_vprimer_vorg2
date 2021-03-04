#! /bin/sh

vcf="data_vprimer/YamV2_exam15.SNP_INDEL_hetero.vcf.gz"
ref="data_vprimer/TDr96_F1_v2_PseudoChromosome_01_17.fasta.gz"
target="chrom_17:3100000-3460000"
a_sample="DRS_015.all.rd.bam,DRS_098.all.rd.bam,DRS_253.all.rd.bam"
b_sample="DRS_013.all.rd.bam,DRS_080.all.rd.bam,DRS_099.all.rd.bam"

vprimer \
\
    -v $vcf \
    -r $ref \
    -T $target \
    -A $a_sample \
    -B $b_sample

