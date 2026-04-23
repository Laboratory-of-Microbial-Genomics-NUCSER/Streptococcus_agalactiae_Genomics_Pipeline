# 1. CRISPR1 Typing
## Identify CRISPR arrays
Identify CRISPR arrays and associated Cas proteins in your assemblies with [CRISPRCasFinder](https://github.com/dcouvin/CRISPRCasFinder)

#### Easy install
Get the source codes [tar.gz file](https://github.com/dcouvin/CRISPRCasFinder/releases/tag/release-4.3.2) and unzip it
```markdown
conda env create -f ccf.environment.yml -n crisprcasfinder
```
```markdown
conda activate crisprcasfinder
```

#### **Usage on multiple assembly files**
```markdown
cd /path_to_/CRISPRCasFinder-release-4.3.2
```
```markdown
for file path_to_assemblies/*.fna; do     echo ">>> Running CRISPRCasFinder on $file";     perl CRISPRCasFinder.pl -in "$file" -cas -keep; done
```

## 2. Processing 
Convert filtered spacers into presence absence matrix.

| Genome | Spacer1 | Spacer2 | ... |
|--------|---------|---------|-----|
| G1     | 0       | 1       | ... |
| G2     | 1       | 1       | ... |
| G3     | 1       | 0       | ... |

- Rows = genomes
- Columns = spacers
- Values = 0 or 1

## 3. Clustering 
Compute pairwise similarity and generate UPGMA tree based on CRISPR spacer presence/absence matrix using Jaccard distance.
```console
Jaccard distance = 1 - No. of shared spacers/ No. of total spacers
```

#### **Dependencies**
Install requirements with either pip or conda:

Using pip:

```markdown
pip install pandas scipy
```

Using conda:

```markdown
conda install pandas scipy
```
#### **Script**
- Download file: [crispr_upgma_tree.py](crispr_upgma_tree.py)


#### **Usage**

##### Run in Linux / macOS / Windows terminal
```markdown
python3 crispr_upgma_tree.py -i path/to/spacer_matrix.csv -o CRISPR_UPGMA_tree.newick --sep ","
```
#### **Output**
NEWICK formatted UPGMA tree (tree scale in jaccard distance 0-1)

CRISPR1 UPGMA tree for S. agalactiae ST7 Ia isolates[CRISPR_UPGMA_tree.newick](CRISPR_UPGMA_tree.newick)

Annotate the tree with metadata (DR, isolation source, country, year, ST, serotype, etc)