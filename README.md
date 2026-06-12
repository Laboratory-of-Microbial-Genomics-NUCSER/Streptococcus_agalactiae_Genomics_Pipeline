# *Streptococcus agalactiae* genome analysis pipeline
This repository contains the scripts and data used in the manuscript described below.
# Global phylogenomics of piscine and human associated *Streptococcus agalactiae* serotype Ia ST7 isolates reveals diversification and reductive evolution leading aquatic host adaptation
Rai Kodlamogaru Yajnesh¹, TG Sumithra², Sathiyaraj G³, Vijeth Vittal Naik⁴, Adwait Prashant Dighe¹, Pratik Shekhar Pangul¹, Rochelle Deanne Tauro⁴, Kattapuni Suresh Prithvisagar¹, S.R. Krupesha Sharma², Anusree VN², Anup Mandal³, Athina Papadopoulou⁵, David Ryder⁵, Chantelle Hooper⁵, David Bass⁵,⁶, Praveen Rai¹,⁷, Deekshit VK¹,⁷, Indrani Karunasagar⁸, Iddya Karunasagar⁸, Dharnappa Sannejal Akhila⁴,⁹*, Ballamoole Krishna Kumar¹,⁷*

¹Nitte (Deemed to be University), Department of Infectious Diseases and Microbial Genomics, Nitte University Centre for Science Education and Research (NUCSER), Paneer Campus, Deralakatte, Mangalore, Karnataka, 575018, India
²ICAR-Central Marine Fisheries Research Institute, Post Box No. 1603, Ernakulam,North P.O.  Kochi-682 018, Kerala, India
³Central Aquaculture Genetics, Pathology and food testing Laboratories, Rajiv Gandhi Centre for Aquaculture (RGCA), TTTAC, MPEDA, Sirkazhi, Mayiladuthurai- 609 109, Tamil Nadu, India.
⁴Nitte (Deemed to be University), Department of Food Safety and Nutrition, Nitte University Centre for Science Education and Research (NUCSER), Paneer Campus, Deralakatte, Mangalore, Karnataka, 575018, India
⁵The Centre for Environment, Fisheries and Aquaculture Science, Barrack Road, The Nothe, Weymouth, Dorset, DT4 8UB, UK
⁶Sustainable Aquaculture Futures, Biosciences, University of Exeter, Stocker Road Exeter, EX4 4QD, UK.
⁷Nitte (Deemed to be University), Department of Microbiology, KS Hegde Medical Academy, Deralakatte, Mangalore, Karnataka, 575018, India
⁸Nitte (Deemed to be University), FAO Reference Centre for Antimicrobial Resistance and Aquaculture Biosecurity, Deralakatte, Mangaluru, 575018, India
⁹Nitte (Deemed to be University), Department of Biochemistry, KS Hegde Medical Academy, Deralakatte, Mangalore, Karnataka, 575018, India

### Data Availability  
All raw sequencing reads and genome assemblies generated in this study have been submitted to the NCBI database under BioProject accession number PRJNA1469759.
### Citation
Pending
### Abstract
*Streptococcus agalactiae* ST7-Ia is an emerging aquaculture pathogen increasingly linked to streptococcosis worldwide. However, its evolutionary relationship with human isolates and zoonotic potential remain unclear. We analysed the genomes of 19 isolates recovered from streptococcosis outbreaks in Indian aquaculture between 2017-2022, together with 23,127 publicly available *S. agalactiae* genomes. All Indian isolates belonged to a single clonal ST7-Ia lineage. Recombination-filtered core-genome phylogeny of 128 global ST7-Ia genomes resolved ST7-Ia into two deeply separated clinical and aquatic host-associated lineages. Bayesian evolutionary analysis estimated the emergence of ST7-Ia around 1908.7 (95% HPD:1868-1933), with divergence of aquatic and clinical populations around 1942.2 (95% HPD:1908-1972) coinciding with aquaculture intensification. CRISPR1 spacer profiles mirrored this host-specific diversification with aquatic isolates showing progressive spacer loss.  Aquatic isolates showed loss of the *scpB–lmb* transposon and lacked AMR genes, whereas 31% of clinical isolates carried tetM within a Tn916-like integrative conjugative element (ICE). Pangenome analysis and association studies identified five host-associated genomic-islands, including an aquatic lineage-specific 74.1-kb ICE enriched in secretion systems, adhesins, and mobile genetic elements, together with lineage-specific loss-of-function mutations affecting transport, metabolism and regulatory pathways, indicating ongoing reductive evolution and aquatic niche specialization. Despite this, two recent invasive human isolates clustered within the aquatic lineage and retained aquatic-specific CRISPR profiles and genomic signatures, providing evidence of fish-to-human host transition. Overall, these findings indicate that ST7-Ia is undergoing host-adaptive genome remodeling associated with aquatic specialization while retaining zoonotic potential, underscoring the need for integrated genomic surveillance across aquaculture and clinical settings.
### Acknowledgement and funding
We gratefully acknowledge the financial support provided through Contract No. CEFAS24-29, “Contract for Services for Whole Genome Sequencing of *Streptococcus agalactiae* Serotypes in Indian Aquatic Systems,” under the Ocean Country Partnership Programme (OCPP) by Centre for Environment, Fisheries and Aquaculture Science (Cefas), United Kingdom. We also acknowledge Nitte (Deemed to be University) for providing the institutional support and computational infrastructure required for this study.



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


