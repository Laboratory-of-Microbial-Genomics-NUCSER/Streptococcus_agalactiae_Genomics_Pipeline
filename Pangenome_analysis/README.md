## Pan genome analysis and metabolic estimation with anvi'o
This repository contains scripts and resources used for pan genome analysis and metabolic estimation of Streptococcus agalactiae ST7 Ia genomes as described in the manuscript.

Refer  [anvi'o](https://anvio.org/) an open-source, community-driven analysis and visualization platform for microbial 'omics.

Follow [anvio_install](https://anvio.org/install) for installing anvi'o




### 1. Pan genome analysis 
Follow [pangenome_tutorial_anvio](https://merenlab.org/tutorials/vibrio-jasicida-pangenome/) for pan genome analysis on genome assemblies

Here is the fully reproducible interactive pan genome of Streptococcus agalactiae Ia genomes used in this study 

#### Download 
[GBS_ST7Ia_Pangenome.tar.xz](GBS_ST7Ia_Pangenome.tar.xz) 
#### Unzip
```markdown
tar -xf GBS_ST7Ia_Pangenome.tar.xz
```

#### Activate anvi'o
```markdown
conda activate anvio-8
```
#### Simply run
```markdown
anvi-display-pan -p GBS-PAN.db                  -g GBS-GENOMES.db

```
and you are done. The pan genome is ready. 