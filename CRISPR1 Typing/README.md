## CRISPR1 Typing
1..Identify CRISPR arrays and associated Cas proteins in your assemblies with [CRISPRCasFinder](https://github.com/dcouvin/CRISPRCasFinder)

Easy install
```markdown
conda env create -f ccf.environment.yml -n crisprcasfinder
```
Usage on multiple assembly files
```markdown
for file path_to_assemblies/*.fna; do     echo ">>> Running CRISPRCasFinder on $file";     perl CRISPRCasFinder.pl -in "$file" -cas -keep; done
```

2.. Filter CRISPR1 arrays with evidence level 4 and CRISPR1 arrays with cas association and DR conservation for evidence level <4. Convert to presence absence matrix.

CRISPR1 spacers presence/absence matrix for S. agalactiae ST7 Ia isolates
- Link: [CRISPR1_spacers_filtered.xlsx](CRISPR1_spacers_filtered.xlsx)
- Link: [CRISPR1_spacer_matrix.csv](CRISPR1_spacer_matrix.csv)

3.. Compute pairwise similarity and generate UPGMA tree based on CRISPR spacer presence/absence matrix using Jaccard distance.
```console
Jaccard distance = 1 - No. of shared spacers/ No. of total spacers
```
##### Input format (.csv)
| Genome | Spacer1 | Spacer2 | ... |
|--------|---------|---------|-----|
| G1     | 1       | 0       | ... |
| G2     | 1       | 1       | ... |
| G3     | 0       | 1       | ... |

- Rows = genomes
- Columns = spacers
- Values = 0 or 1
#### **Script**


#### 🚀 **Usage**

##### Run in Linux / macOS / Windows terminal
```bash
python3 crispr_upgma_tree.py -i spacermatrix.csv -o CRISPR_UPGMA_tree.newick --sep ","
