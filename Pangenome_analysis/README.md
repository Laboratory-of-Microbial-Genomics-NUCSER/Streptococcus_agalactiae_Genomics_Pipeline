# Pan genome analysis and metabolic estimation with anvi'o
This repository contains scripts and resources used for pan genome analysis and metabolic estimation of Streptococcus agalactiae ST7 Ia genomes as described in the manuscript.

Refer  [anvi'o](https://anvio.org/) an open-source, community-driven analysis and visualization platform for microbial 'omics.

Follow [anvio_install](https://anvio.org/install) for installing anvi'o




## 1. Pan genome analysis 

Here is the fully reproducible interactive pan genome of Streptococcus agalactiae ST7 Ia genomes used in this study 

#### Download 
[GBS_ST7Ia_Pangenome.tar.xz](GBS_ST7Ia_Pangenome.tar.xz) 
#### Unzip
```markdown
tar -xf GBS_ST7Ia_Pangenome.tar.xz
``` 
#### Move into the directory
```markdown
cd GBS_ST7Ia_Pangenome
```

#### Activate anvi'o
```markdown
conda activate anvio-8
```
#### Simply run
```markdown
anvi-display-pan -p S_agalactiae-PAN.db -g S_agalactiae-GENOMES.db
```
and you are done. The interactive pan genome is ready. 

Here is the summary file [S_agalactiae_gene_clusters_summary.txt.gz](S_agalactiae_gene_clusters_summary.txt.gz) 

Follow [pangenome_tutorial_anvio](https://merenlab.org/tutorials/vibrio-jasicida-pangenome/) to run pan genome analysis on your data

## 2. Metabolic estimation and enrichment analysis

Here is the fully reproducible interactive metabolic completeness matrix of Streptococcus agalactiae ST7 Ia genomes used in this study


Here is the fully reproducible interactive pan genome of Streptococcus agalactiae ST7 Ia genomes used in this study 

#### Download 
[GBS_ST7_Ia_Metabolism.tar.xz](GBS_ST7_Ia_Metabolism.tar.xz) 
#### Unzip
```markdown
tar -xf GBS_ST7_Ia_Metabolism.tar.xz
``` 
#### Move into the directory
```markdown
cd GBS_ST7_Ia_Metabolism
```

#### Activate anvi'o
```markdown
conda activate anvio-8
```



#### Simply run
```markdown
anvi-interactive -d GBS_metabolism-module_pathwise_completeness-MATRIX.txt -p modules_heatmap.db  --manual --title "GBS PATHWISE METABOLISM COMPLETENESS HEATMAP"

```
and you are done. The interactive metaboplic completness matrix is ready. 

Change pathwise to stepwise for stepwise completeness matrix

Follow [Metabolic_reconstruction_excerise](https://merenlab.org/tutorials/vibrio-jasicida-pangenome/) tutorial to perform metabolic estimation and enrichment analysis on your data