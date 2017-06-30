## Full dataset for advanced user 

We provide two datasets for a total of 921 samples divided into a training set of 784 sample `genotyping_data_fullset_vcf_train.npy` and a test set of 137 samples in `genotyping_data_fullset_vcf_test.npy`.  
The whole dataset, contains **7,252,636** genetic variants from 22 autosomal chromosome pairs and sexual chromosomes (XX for women and XY for men) in a compressed **VCF format**.

**VCF format**  
The VCF files provided in the dataset section are in the VCF v4.2 standard; full specification is given [ here ](https://samtools.github.io/hts-specs/VCFv4.2.pdf).


~~~~~~~~
##fileformat=VCFv4.2
##FILTER=<ID=PASS,Description="All filters passed">
##fileDate=20170315
##source=PLINKv1.90
##contig=<ID=1,length=249240544>
##contig=<ID=2,length=243188368>
##contig=<ID=3,length=197962382>
...
##contig=<ID=21,length=48119741>
##contig=<ID=22,length=51244238>
##contig=<ID=X,length=155260479>
##contig=<ID=Y,length=28817459>
##INFO=<ID=PR,Number=0,Type=Flag,Description="Provisional reference allele, may
##FORMAT=<ID=GT,Number=1,Type=String,Description="Genotype">
#CHROM  POS ID  REF ALT QUAL  FILTER  INFO  FORMAT  sample_1  sample_2  sample_3  sample_4  sample_5
1 10177 rs367896724 A C . . PR  GT  0/0 0/1 1/0 1/1 ./.
~~~~~~~~

The file header consists of multiple lines starting with '#', which provide metadata on the VCF file (e.g. software that generated the file (PLINK), length of every chromosome).
The header is followed by actual genotypes. The example SNP listed above (ID: rs367896724) is on chromosome 1 at position 10177; its reference allele is A and the alternate allele is C. In the following columns, we can see that:

* Sample_1 is homozygous for the reference allele
* Sample_2 and sample_3 are heterozygous
* Sample_4 is homozygous for the alternate allele
* Sample_5 has missing information for this SNP

**Note** that the dataset has been filtered to only contains SNPs that:

* Have a minor allele frequency of at least 5% 
* Are not missing in more than 1% of individuals (except for chromosome Y)

