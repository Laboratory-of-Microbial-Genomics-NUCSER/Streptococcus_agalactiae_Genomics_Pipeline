# Phylogentic analysis pipelines
This repository contains scripts and resources used for phylogenetic reconstruction of Streptococcus agalactiae ST7 Ia genomes as described in the manuscript.
## 1. Genome annotation 
Annotate multiple genome assemblies with rapid prokaryotic genome annotation: [tseemann/prokka](https://github.com/tseemann/prokka)
#### Place [run_prokka.sh](run_prokka.sh) and assembly files in a single directory and simply run 
```markdown 
./run_prokka.sh
```


make it executable if not
```markdown
chmod +x run_prokka.sh
```

## 2. Core genome alignment
Use annotated GFF files from Prokka to generate core genome alignment with the pan genome pipeline [sanger-pathogens/Roary](https://github.com/sanger-pathogens/Roary)

#### First collect all gff files by running [collect_gff.sh](collect_gff.sh) from the same directory 
```markdown 
./collect_gff.sh
```
#### Next, simply place [run_roary.sh](run_roary.sh) along with gff files and run 
```markdown 
./run_roary.sh
```
#### Output
core_gene_alignment.aln : concatenated core genome alignment

gene_presence_absence.csv 
: pan-genome matrix

## 3. Recombination prediction and removal
Run Genealogies Unbiased By recomBinations In Nucleotide Sequences [nickjcroucher/gubbins](https://github.com/nickjcroucher/gubbins) on core genome alignment to detect and mask recombination regions
#### Easy install
```markdown
conda install gubbins
```
#### Run Gubbins
```markdown
run_gubbins.py --prefix gubbins_out --threads 12 /path_to_file/core_gene_alignment.aln
```

#### Output
gubbins_out_core_gene_alignment.filtered_polymorphic_sites.fasta

gubbins_out_recombination_predictions.gff
## 4. Maximum-likelihood tree construction
Perform phylogenetic reconstruction using  [ RAxML v.8](https://github.com/stamatak/standard-RAxML)
#### 4.1. First remove gubbins predicted recombination regions from the concantated core genome alignmnt 

#### script: [remove_recombination.py](remove_recombination.py) 

#### Usage
```markdown
python remove_recombination.py \
    -i gubbins_out.recombination_predictions.gff core_gene_alignment.aln \
    -o recombination_removed_core_genome_alignment.fasta
```
#### 4.2. Run RAxML

#### Easy install
```markdown
conda install -c bioconda raxml
```
#### Usage 

```markdown
raxmlHPC-PTHREADS -T 12   -s /path_to_file/recombination_removed_core_alignment.fasta   -m GTRGAMMA    -p 12345 -x 12345 -# 1000 -f a   -n name_RAxML_out_GTRGAMMA_1000
```
-T: Threads


-s: Input alignment file


-m: Model


-#: Bootstrap replicates 


-n: Output name


**Note:** If directly using  gubbins output of recombination removed SNP-only alignment with non variable sites removed "gubbins_out_filtered_polymorphic_sites.fasta" ascertainment-bias-corrected model (ASC_GTRGAMMA) with Lewis correction for ascertainment bias (--asc-corr=lewis) must be used.

#### Usage
```markdown
raxmlHPC-PTHREADS -T 12   -s /path_to_file/gubbins_out_filtered_polymorphic_sites.fasta   -m ASC_GTRGAMMA --asc-corr=lewis   -p 12345 -x 12345 -# 1000 -f a   -n name_RAxML_out_GTRGAMMA_1000_asc
```
#### 4.3. Visualize and annotate
Upload the RaxMl output "RAxML_bipartitions.name" in figtree/itol/microreact to visualize final ML tree with bootstrap support values added to internal nodes.
## 5. Time scaled phylogeny 
Use Bayesian Evolutionary Analysis by Sampling Trees [(BEAST)](https://github.com/beast-dev/beast-mcmc?tab=readme-ov-file), a cross-platform program for Bayesian analysis of molecular sequences using MCMC

Follow [BEAST.COMMUNITY](https://beast.community/installing) for installing BEAST and associated software packages needed for time scaled phylogenetic analyis

Here is the tutorial for running BEAST 

[ First_tutorial](https://beast.community/first_tutorial) 

[Second tutorial](https://beast.community/second_tutorial)
