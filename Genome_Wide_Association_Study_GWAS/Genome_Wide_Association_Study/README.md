# Genome-Wide Association Study (GWAS) 
This folder contains tools and scripts to perform Genome-Wide Association Studies (GWAS) for identifying genetic markers (SNPs, Indels, and K-mers) associated with phenotypic traits, and mapping them to genes.

## SNPs
#### Extract SNPS
Extract SNPs like a boss with snippy. A bigshoutout to Torsten Seemann for making bioinformatics a little less painful.

Install Snippy; 
The easy way
```markdown
conda install -c conda-forge -c bioconda -c defaults snippy
```

Try other ways https://github.com/tseemann/snippy

```markdown
snippy-multi /path_to_/input.tab --ref /path_to_/reference.fna --cpus 4 > runme.sh
```
```markdown
sh ./runme.sh
```
#### GWAS with Pyseer


```markdown
pyseer   --vcf /path_to_/core.vcf   --phenotypes /path_to_/phenotype.txt   --no-distances   > pyseer_results_snp.txt
```

**Note:** Here, we used --no-distances option only beacuse the dataset consisted of isolates forming two deeply separated phylogenetic clades consistent with the trait being used for GWAS, rendering distance-based population structure correction uninformative.

⚠️ **Important:** This setting is not recommended for general GWAS analysis. For datasets with subtle population structure, it is strongly recommended to account for relatedness using a linear mixed model (LMM) (--lmm ) with an appropriate kinship or distance matrix to control for population stratification and reduce false-positive associations.
## Indels
First, lets compress all VCF files per isolate
```markdown
for vcf in */snps.vcf; do
    bgzip -c "$vcf" > "${vcf}.gz"
    tabix -p vcf "${vcf}.gz"
done
```
Merge the compressed individual VCFs
```markdown
bcftools merge */snps.vcf.gz -O z -o merged.all.vcf.gz
bcftools index merged.vcf.gz
```
Extract the indels
```markdown
bcftools view -v indels -Oz -o merged.indels.vcf.gz merged.vcf.gz

bcftools index merged.indels.vcf.gz
```
Decompose multiallelic sites into separate lines
```markdown
bcftools norm -m -any -Oz -o merged.indels.decomposed.vcf.gz merged.indels.vcf.gz

bcftools index merged.indels.decomposed.vcf.gz
```
Simplify the format - GWAS compatible
```markdown
bcftools annotate -x ^FORMAT/GT -Oz -o indelsdecomposed.vcf.gz merged.indels.decomposed.vcf.gz
bcftools index indelsdecomposed.vcf.gz
```
#### GWAS with Pyseer


```markdown
pyseer   --vcf /path_to_/indelsdecomposed.vcf   --phenotypes /path_to_/phenotype.txt   --no-distances   > pyseer_results_snp.txt
```
**Note:** Here, we used --no-distances option only beacuse the dataset consisted of isolates forming two deeply separated phylogenetic clades consistent with the trait being used for GWAS, rendering distance-based population structure correction uninformative.

⚠️ **Important:** This setting is not recommended for general GWAS analysis. For datasets with subtle population structure, it is strongly recommended to account for relatedness using a linear mixed model (LMM) (--lmm ) with an appropriate kinship or distance matrix to control for population stratification and reduce false-positive associations.

## Kmers

```markdown
unitig-caller --call \
  --refs /home/user1/miniconda3/GWAS/refs.txt \
  --pyseer \
  --threads 12 \
  --out unitigs
```
lets stop being smart for once and just zip the file

```markdown
gzip unitigs.pyseer
```
run pyseer on your zipped file
```markdown
pyseer --phenotypes /home/user1/miniconda3/GWAS/phenotype.txt \
       --kmers /home/user1/miniconda3/GWAS/unitigs.pyseer.gz \
       --no-distances \
       --cpu 12 \
       > kmer_results.txt
```

**Note:** Here, we used --no-distances option only beacuse the dataset consisted of isolates forming two deeply separated phylogenetic clades consistent with the trait being used for GWAS, rendering distance-based population structure correction uninformative.

⚠️ **Important:** This setting is not recommended for general GWAS analysis. For datasets with subtle population structure, it is strongly recommended to account for relatedness using a linear mixed model (LMM) (--lmm ) with an appropriate kinship or distance matrix to control for population stratification and reduce false-positive associations.