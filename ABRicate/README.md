
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
--db plasmidfinder for plasmid detection

## Screening assemblies againt own database
create a newfolder within abricate db directory 


Add multifasta files of genes to be screened

1. Insertion sequence 
2. FbsB variants
3. Bca variants 
4. Bac variants

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
DATABASE  SEQUENCES  DBTYPE  DATE
IS        5          nucl    2025-Dec-10

Run abricate with new db (--db IS) 

