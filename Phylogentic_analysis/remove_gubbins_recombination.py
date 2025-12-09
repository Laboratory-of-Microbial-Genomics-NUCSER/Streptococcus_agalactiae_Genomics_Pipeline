from Bio import AlignIO
import numpy as np

alignment_file = "core_gene_alignment128.aln"
gff_file = "gubbins_out.recombination_predictions.gff"
output_file = "recombination_removed_core_alignment128.aln"

recomb_pos = set()
with open(gff_file) as gff:
    for line in gff:
        if line.startswith("#"):
            continue
        parts = line.strip().split("\t")
        if len(parts) < 5:
            continue
        start = int(parts[3]) - 1
        end = int(parts[4])
        recomb_pos.update(range(start, end))

alignment = AlignIO.read(alignment_file, "fasta")
alignment_length = alignment.get_alignment_length()

all_positions = np.arange(alignment_length)
keep_positions = [i for i in all_positions if i not in recomb_pos]

from Bio.Align import MultipleSeqAlignment
from Bio.SeqRecord import SeqRecord
from Bio.Seq import Seq

new_alignment = MultipleSeqAlignment([])

for record in alignment:
    new_seq = ''.join(record.seq[i] for i in keep_positions)
    new_record = SeqRecord(Seq(new_seq), id=record.id, description="")
    new_alignment.append(new_record)

AlignIO.write(new_alignment, output_file, "fasta")
print(f"Recombination-removed alignment saved to: {output_file}")

