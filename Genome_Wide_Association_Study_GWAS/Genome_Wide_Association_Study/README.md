# Genome-Wide Association Study (GWAS) 
This folder contains tools and scripts to perform Genome-Wide Association Studies (GWAS) for identifying genetic markers (SNPs, Indels, and K-mers) associated with phenotypic traits, and mapping them to genes.

## SNPs
#### Extract SNPS
Extract SNPs with [TorstenSeemann/Snippy](https://github.com/tseemann/snippy). Huge shoutout to Torsten Seemann for making bioinformatics a little less painful.

Install Snippy; 
The easiest way
```markdown
conda install -c conda-forge -c bioconda -c defaults snippy
```

Generate a multi-sample Snippy run script using snippy-multi. 

The input.tab file is a tab-delimited text file with two columns: sample name and path to the assembly FASTA file.
```markdown
snippy-multi /path_to_/input.tab --ref /path_to_/reference.fna --cpus 4 > runme.sh
```

execute 
```markdown
sh ./runme.sh
```
run Pyseer



```markdown
pyseer   --vcf /path_to_/core.vcf   --phenotypes /path_to_/phenotype.txt   --no-distances   > pyseer_results_snp.txt
```

phenotype.txt is a two-column, tab-delimited file specifying the phenotype matrix (0 or 1).

**Note:** Here, we used --no-distances option only beacuse the dataset consisted of isolates forming two deeply separated phylogenetic clades consistent with the trait being used for GWAS, rendering distance-based population structure correction uninformative.

⚠️ **Important:** This setting is not recommended for general GWAS analysis. For datasets with subtle population structure, it is strongly recommended to account for relatedness using a linear mixed model (--lmm ) with an appropriate kinship or distance matrix to control for population stratification and reduce false-positive associations.
## Indels
First, lets compress all snippy VCF files per isolate
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
run pyseer


```markdown
pyseer   --vcf /path_to_/indelsdecomposed.vcf   --phenotypes /path_to_/phenotype.txt   --no-distances   > pyseer_results_snp.txt
```
**Note:** Here, we used --no-distances option only beacuse the dataset consisted of isolates forming two deeply separated phylogenetic clades consistent with the trait being used for GWAS, rendering distance-based population structure correction uninformative.

⚠️ **Important:** This setting is not recommended for general GWAS analysis. For datasets with subtle population structure, it is strongly recommended to account for relatedness using a linear mixed model (--lmm ) with an appropriate kinship or distance matrix to control for population stratification and reduce false-positive associations.

## Kmers
Extract unitigs from your assemblies  with [unitig-caller](https://github.com/bacpop/unitig-caller) 

easy install
```markdown
conda install unitig-caller
```
usage

refs.txt is a plain text file containing paths to genome assemblies (one per line).
```markdown
unitig-caller --call \
  --refs /path_to/refs.txt \
  --pyseer \
  --threads 12 \
  --out unitigs
```
lets stop being smart for once and just zip the file

```markdown
gzip unitigs
```
run pyseer on your zipped file
```markdown
pyseer --phenotypes /path_to/phenotype.txt \
       --kmers /path_to/unitigs.pyseer.gz \
       --no-distances \
       --cpu 12 \
       > kmer_results.txt
```

**Note:** Here, we used --no-distances option only beacuse the dataset consisted of isolates forming two deeply separated phylogenetic clades consistent with the trait being used for GWAS, rendering distance-based population structure correction uninformative.

⚠️ **Important:** This setting is not recommended for general GWAS analysis. For datasets with subtle population structure, it is strongly recommended to account for relatedness using a linear mixed model (--lmm ) with an appropriate kinship or distance matrix to control for population stratification and reduce false-positive associations.

## Multiple testing and FDR correction of GWAS p-values
To control for multiple testing in GWAS results, correct the raw p-values from pyseer using the Benjamini–Hochberg false discovery rate (FDR) procedure. This step reduces false-positive associations while retaining statistical power.

**Script** [fdr_correction.py](fdr_correction.py)

**Dependencies**
```markdown
pip install pandas statsmodels
```

**Usage**
```markdown
python fdr_correction.py \
  -i /path_to/pyseer_results.txt \
  -o results_with_FDR.txt \
  --pcol lrt-pvalue
```

**--pcol** defines the p-value column name in your GWAS output file — because not all babies cry the same way.

Adjusted p-values are reported in the column **lrt-pval-FDR** in the output file.