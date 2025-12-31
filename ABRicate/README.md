
## Screening for ARGs, virulence genes and plasmids
Mass screening of resistance genes, virulence genes and plasmids in multiple asssembly files using [tseeman/abricate](https://github.com/tseemann/abricate)
#### Easy install
```markdown
conda install -c conda-forge -c bioconda abricate
```
#### Usage for multiple assmembly files 
```markdown
abricate --db card /path_to_assemblyfiles/*.fasta>output_card.tab
```
--db resfinder for antimircobial resistance genes 

--db vfdb for virulence genes 

--db plasmidfinder for plasmid detection


Use --mincov and --minid options to change detection coverage and identity threshold 

Simplify output to an combined presence absence matrix
```markdown
abricate --summary output_card.tab > summary_card.csv
```

## Screening assemblies againt own database
create a new folder within abricate db directory 


Add multifasta files of genes to be screened

1. Insertion sequence  [IS_sequences](IS_sequences)
2. FbsB variants [FbsB_variant_sequences](FbsB_variant_sequences)
3. Bca variants [Bca_variant_sequences](Bca_variant_sequences)
4. Bac variants [Bac_variant_sequences](Bac_variant_sequences)

Note: These databases contains IS/ gene varaints only present in S. agalactiae ST7 Ia isolates used in this study

```markdown
makeblastdb -in sequences -dbtype nucl
```

```markdown
abricate --setupdb
```
```markdown
abricate --list
```
You will see 

DATABASE	SEQUENCES	DBTYPE	DATE


IS	        5	        nucl	2025-Dec-10


Run abricate with new db (--db IS) 

