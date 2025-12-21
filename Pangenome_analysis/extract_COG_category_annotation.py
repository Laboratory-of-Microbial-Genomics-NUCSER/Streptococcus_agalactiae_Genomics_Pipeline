import os
import argparse
from collections import defaultdict

# Argument parsing
parser = argparse.ArgumentParser(
    description="Build a STAMP-ready COG category table from eggNOG-mapper outputs"
)

parser.add_argument(
    "-i", "--input",
    required=True,
    help="Path to folder containing eggNOG-mapper outputs (.emapper.annotations or .tabular)"
)

parser.add_argument(
    "-o", "--output",
    default="COG_categories.tsv",
    help="Output table (default: COG_categories.tsv)"
)

args = parser.parse_args()

INPUT_DIR = os.path.abspath(args.input)

if not os.path.isdir(INPUT_DIR):
    raise FileNotFoundError(f"Input directory not found: {INPUT_DIR}")

# Data containers
genomes = []
cog_counts = defaultdict(lambda: defaultdict(int))

# accepted eggNOG output extensions
VALID_EXT = (".emapper.annotations", ".tabular")

# Parse eggNOG outputs
for fname in os.listdir(INPUT_DIR):
    if not fname.endswith(VALID_EXT):
        continue

    genome = fname
    for ext in VALID_EXT:
        genome = genome.replace(ext, "")
    genomes.append(genome)

    filepath = os.path.join(INPUT_DIR, fname)

    with open(filepath, "r", encoding="utf-8") as f:
        for line in f:
            if line.startswith("#"):
                continue

            parts = line.rstrip("\n").split("\t")
            if len(parts) < 7 or parts[6] == "-":
                continue

            # split comma-separated blocks, then split multi-letter COGs
            for block in parts[6].split(","):
                for cog in block:
                    cog_counts[cog][genome] += 1

genomes = sorted(set(genomes))

with open(args.output, "w", encoding="utf-8") as out:
    out.write("COG_Category\t" + "\t".join(genomes) + "\n")
    for cog in sorted(cog_counts.keys()):
        out.write(cog)
        for g in genomes:
            out.write("\t" + str(cog_counts[cog].get(g, 0)))
        out.write("\n")

print("DONE!")
print(f"COG categories extracted and written to: {args.output}")

