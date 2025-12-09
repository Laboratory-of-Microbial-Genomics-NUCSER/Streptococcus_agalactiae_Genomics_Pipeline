# Streptococcus_agalactiae_Host_adaptation_paper
This repository contains the scripts and data used in the manuscript described below.
# Manucript Title
*authors list
### Data Availability  
The raw sequence data generated in this project is submitted to the SRA () and the genome assemblies are made available through the NCBI Bioproject ()
### Citation
xxxxx
### Abstract
xxxxx
# Pipelines
## 1. S. agalactiae typing schemes
#### 1. MLST
Perform in silico MLST to assign sequence type (STs) with [tseeman/mlst](https://github.com/tseemann/mlst)

Easy install
```markdown
% conda install -c conda-forge -c bioconda  mlst
```
Open your directory with all fasta/fna/fa files and just run 
```markdown
mlst --scheme sagalactiae --csv *.fasta > mlst_sagalactiae.csv
```

#### 2. Serotyping
Perform in silico capsular polysaccharide sequence based serotyping to assign serotype with [swainechen/GBS-SBG](https://github.com/swainechen/GBS-SBG)

Clone the git repo
```markdown
git clone https://github.com/swainechen/GBS-SBG
```
Serotype calling on multiple genome assemblies

```markdown
for file in /path_to_assembly_files/*fasta; do  perl GBS-SBG.pl "$file" -name "$(basename "$file".fasta)" -best >> serotype.txt; done
```

Refer [kaholt/srst2](https://github.com/katholt/srst2) for short read serotype calling
#### 3. Surafce protein and penicilin binding protein based typing 
For surface protein typing (alpha variants, hvga, pili, and serine rich repeats) and penicilin binding protein based typing follow [GBS-Typer-sanger-nf](https://github.com/sanger-bentley-group/GBS-Typer-sanger-nf) pipeline. 
#### 4. Prophage integrase typing 
For prophage integrase based typing on S. agalactiae assemblies follow [chcrestani/GBS_prophage_integrase_typing](https://github.com/chcrestani/GBS_prophage_integrase_typing) 
#### 5. Insertion sequence elements
To type S. agalactiae genomes based on IS elements see section 

#### 6. CRISPR1 typing 
To perform CRISPR1 typing from WGS data
- See: [CRISPR1 Typing README](CRISPR1%20Typing/README.md)

## 2. Screening for ARGs, virulence genes and plasmids
## 3. Phylogentic analysis


## 4. Pan genome analysis and metabolic estimation with anvi'o
#### a. Pan genome analysis
#### b. Metabolic estimation


## 5. Genome Wide Association Study
#### a. 
#### b. Visualization
Create an interactive Manhattan plot and hover over the points to view the genetic variants (SNPs and indels) that are associated with the host group. Find the scripts and data here: [GWAS — SNPs and indels](./GWAS/SNPs%20and%20indels/)


FTGFG


### Acknowledgements and fundings
