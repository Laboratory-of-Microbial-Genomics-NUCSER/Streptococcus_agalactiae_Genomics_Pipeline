# *Streptococcus agalactiae* genome analysis pipeline
This repository contains the scripts and data used in the manuscript described below.
# Manucript Title
*authors list
### Data Availability  
The raw sequence data generated in this project is submitted to the SRA () and the genome assemblies are made available through the NCBI Bioproject ()
### Citation
xxxxx
### Abstract
xxxxx
### Acknowledgements and funding

# Pipelines
## 1. *S. agalactiae* typing schemes
#### 1.1. MLST
Perform in silico MLST to assign sequence type (STs) with [tseeman/mlst](https://github.com/tseemann/mlst)

Easy install
```markdown
conda install -c conda-forge -c bioconda  mlst
```
Open your directory with all fasta/fna/fa files and just run 
```markdown
mlst --scheme sagalactiae --csv *.fasta > mlst_sagalactiae.csv
```

#### 1.2. Serotyping
Perform in silico capsular polysaccharide sequence based serotyping to assign serotype using [swainechen/GBS-SBG](https://github.com/swainechen/GBS-SBG)

Clone the git repo
```markdown
git clone https://github.com/swainechen/GBS-SBG
```
Serotype calling on multiple genome assemblies

```markdown
for file in /path_to_assembly_files/*fasta; do  perl GBS-SBG.pl "$file" -name "$(basename "$file".fasta)" -best >> serotype.txt; done
```

Refer [kaholt/srst2](https://github.com/katholt/srst2) for short read serotype calling
#### 1.3. Surafce protein and penicilin binding protein based typing 
For surface protein typing (alpha variants, hvga, pili, and serine rich repeats) and penicilin binding protein based typing follow [GBS-Typer-sanger-nf](https://github.com/sanger-bentley-group/GBS-Typer-sanger-nf) pipeline. 
#### 1.4. Prophage integrase typing 
For prophage integrase based typing on *S. agalactiae* assemblies follow [chcrestani/GBS_prophage_integrase_typing](https://github.com/chcrestani/GBS_prophage_integrase_typing) 
#### 1.5. Insertion sequence elements
To type *S. agalactiae* genomes based on IS elements
- See section : [ABRicate README](ABRicate/README.md)

#### 1.6. CRISPR1 typing 
To perform CRISPR1 typing from WGS data
- See: [CRISPR1 Typing README](CRISPR1%20Typing/README.md)

## 2. Screening for ARGs, virulence genes and plasmids
Mass screenng of resistance genes, virulence genes, and plasmids using [tseemann/abricate](https://github.com/tseemann/abricate)

- See section: [ABRicate README](ABRicate/README.md)

## 3. Phylogentic analysis
a. Genome annotation 

b. Core genome alignment

c. Recombination prediction and filtering

d. Phylogentic reconstruction

e. Time scaled phylogeny

- see section: [Phylogentic_analysis README](Phylogentic_analysis/README.md)

## 4. Pan genome analysis and metabolic estimation with anvi'o
a. Pan genome analysis with anvio

b. Quantfication of genome openess

c. COG functional enrichment

d. Metabolic estimation and enrichement with anvio
- see section [Pangenome_analysis README](Pangenome_analysis/README.md)



## 5. Genome Wide Association Study
#### 5.1. GWAS pipeline
See section [Genome_Wide_Association_Study_GWAS](Genome_Wide_Association_Study_GWAS/Genome_Wide_Association_Study/README.md)
: This pipeline enables the identification of genetic variants—including k-mers, SNPs, and indels—that are significantly associated with host groups or other phenotypic traits.
#### 5.2. Visualization
See section [GWAS_Interactive_Manhattan_Plotting](Genome_Wide_Association_Study_GWAS/GWAS_Interactive_Manhattan_Plotting/README.md) to reproduce the interactive Manhattan plot used to visualize genetic variants (Kmers, SNPs and indels) of *S. agalactiae* ST-7 Ia that were significantly associated with the host group in this study. 


