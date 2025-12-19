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

### Quantification of genome openness

Genome openness can be quantified by computing pangenome rarefaction curves and estimating Heaps’ Law parameters, which indicate whether a pangenome is open or closed by modeling the rate at which new gene clusters are identified with the sequential addition of genomes. This analysis can be  performed using the anvi’o program *anvi-compute-rarefaction-curves* [tutorials](https://merenlab.org/2016/11/08/pangenomics-v2/#calculating-rarefaction-curves-and-heaps-law-parameters)

**Note:** The *anvi-compute-rarefaction-curves* function is only available in *anvio-dev* the developmental version of anvio 

Follow [anvio.org/install/linux/dev](https://anvio.org/install/linux/dev/) for installing the anvio's developmental version.

#### Usage
Once installed activate anvio-dev environment
```markdown
conda activate anvio-dev
```
Move a copy of PAN-db file created with anvio-8 into a new directory and migrate the PAN-db to the anvi’o development schema (DB v21) using anvi-migrate

```markdown
anvi-migrate   --migrate-safely   /path/to/PAN.db
```
Now run
```markdown
anvi-compute-rarefaction-curves   -p /path/to/S_agalactiae-PAN.db   -O Sagalactiae_rarefaction   --iterations 100
```

#### Output
        
Number of genomes found ..........................: 128                             
Number of iterations to run .........................: 100                             
Heaps' Law parameters estimated ..............: K=1658.5266, alpha=0.1221                           
Rarefaction curves ..........................................: Sagalactiae_rarefaction-rarefaction-curves.svg



## 2. Metabolic estimation and enrichment analysis

Here is the fully reproducible interactive metabolic completeness matrix of *S. agalactiae* ST7 Ia genomes used in this study


Here is the fully reproducible interactive pan genome of *S. agalactiae* ST7 Ia genomes used in this study 

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