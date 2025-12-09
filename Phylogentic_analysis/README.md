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

## 3. Recombination prediction and removal
Run Genealogies Unbiased By recomBinations In Nucleotide Sequences [nickjcroucher/gubbins](https://github.com/nickjcroucher/gubbins) on core genome alignment to detect and mask recombination regions
#### Easy install
```markdown
conda install gubbins
```
#### Run Gubbins
```markdown
run_gubbins.py --prefix gubbins_out --threads 12 /path_to_file/core_alignment.fasta
```
## 4. Maximum-likelihood tree construction
