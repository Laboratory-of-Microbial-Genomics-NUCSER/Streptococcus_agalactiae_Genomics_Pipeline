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

()

3.. 