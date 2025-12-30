# Genome-Wide Association Study (GWAS)
This folder contains the data and scripts used to visualize the Genome-Wide Association Study (GWAS) results generated for *Streptococcus agalactiae* ST-7 Ia isolates in this study. 

## SNPs and indels


### Visualize interactive Manhattan plot 
#### Dependencies
- Python 3.10+
- pandas
- numpy
- plotly
- biopython

Install with:
```python
pip install pandas numpy plotly biopython
```
#### Files
- [pyseer_results_coresnp_fdr_annotation.txt](../GWAS_Interactive_Manhattan_Plotting/SNPs%20and%20indels/Data/pyseer_results_coresnp_fdr_annotation.txt)
- [pyseer_results_indels_fdr_annotation.txt](../GWAS_Interactive_Manhattan_Plotting/SNPs%20and%20indels/Data/pyseer_results_indels_fdr_annotation.txt)                                          
- [ref_NZ_CP012419.gb](../GWAS_Interactive_Manhattan_Plotting/SNPs%20and%20indels/Data/ref_NZ_CP012419.gb)  
- [snp_indels_interactive_manhattan_plot.py](../GWAS_Interactive_Manhattan_Plotting/SNPs%20and%20indels/Scripts/snp_indels_interactive_manhattan_plot.py)

**Note:** Keep all files together — the script gets lonely otherwise!
#### Usage
navigate to the folder containing the script and data files, then run:
`````python
python snp_indels_interactive_manhattan_plot.py
`````

hover over the points to view the signifcant SNPs that are associated with the host group and map to genes
## Kmers
### Visualize interactive Manhattan plots
#### Dependencies
- Python 3.10+
- pandas
- numpy
- plotly

Install with:
```python
pip install pandas numpy plotly
```
#### Files
- [kmer_results_fdr_with_blast_gene_clinicalclade.csv](../GWAS_Interactive_Manhattan_Plotting/Kmers/Data/kmer_results_fdr_with_blast_gene_clinicalclade.csv)
- [kmer_results_fdr_with_blast_gene_aquaticclade1.csv](../GWAS_Interactive_Manhattan_Plotting/Kmers/Data/kmer_results_fdr_with_blast_gene_aquaticclade1.csv)
- [kmer_results_fdr_with_blast_gene_aquaticclade2.csv](../GWAS_Interactive_Manhattan_Plotting/Kmers/Data/kmer_results_fdr_with_blast_gene_aquaticclade2.csv)
- [kmers_interactive_manhattan_plot_clinicalclade.py](../GWAS_Interactive_Manhattan_Plotting/Kmers/Scripts/kmers_interactive_manhattan_plot_clinicalclade.py)
- [kmers_interactive_manhattan_plot_aquaticclade1.py](../GWAS_Interactive_Manhattan_Plotting/Kmers/Scripts/kmers_interactive_manhattan_plot_aquaticclade1.py)
- [kmers_interactive_manhattan_plot_aquaticclade2.py](../GWAS_Interactive_Manhattan_Plotting/Kmers/Scripts/kmers_interactive_manhattan_plot_aquaticclade2.py)

**Note:** Again. Dont breakapart the files — the script will start crying!
#### Usage
navigate to the folder containing the script and data files, then run it for all three references from each of the clades:
`````python
python kmers_interactive_manhattan_plot_clinicalclade.py
`````
`````python
python kmers_interactive_manhattan_plot_aquaticclade1.py
`````
`````python
python kmers_interactive_manhattan_plot_aquaticclade2.py
`````

Hover over the points to view the significant indels that are associated with the host group and those which map to genes.