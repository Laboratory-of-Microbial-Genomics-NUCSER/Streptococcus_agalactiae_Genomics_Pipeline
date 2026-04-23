import argparse
import pandas as pd
from scipy.spatial.distance import pdist
from scipy.cluster.hierarchy import linkage, to_tree


def parse_args():
    parser = argparse.ArgumentParser(
        description=(
            "Construct a UPGMA tree from a CRISPR spacer presence/absence matrix "
            "using Jaccard distance and write it as a Newick file."
        )
    )
    parser.add_argument(
        "-i", "--input",
        required=True,
        help="Path to spacer presence/absence matrix (CSV/TSV). Rows = genomes, columns = spacers."
    )
    parser.add_argument(
        "-o", "--output",
        required=True,
        help="Output Newick tree file path."
    )
    parser.add_argument(
        "--sep",
        default=",",
        help="Column separator for input file (default: ','). Use '\\t' for TSV."
    )
    return parser.parse_args()


def get_newick(node, newick="", parentdist=0.0, leaf_names=None):
    """
    Recursively generate Newick string from a SciPy ClusterNode.

    Parameters
    ----------
    node : scipy.cluster.hierarchy.ClusterNode
        Current node in the tree.
    newick : str
        Partial Newick string (built backwards).
    parentdist : float
        Distance from this node to its parent.
    leaf_names : list of str
        Names of the leaves (genome labels), indexed by node.id.

    Returns
    -------
    str
        Newick-formatted string for this subtree.
    """
    if node.is_leaf():
        # branch length from this node to its parent
        branch_length = parentdist - node.dist
        return f"{leaf_names[node.id]}:{branch_length:.6f}{newick}"
    else:
        if len(newick) > 0:
            # close subtree and add branch length to parent
            newick = f"):{parentdist - node.dist:.6f}{newick}"
        else:
            # root: close tree with semicolon later
            newick = ");"
        # recurse on children
        newick = get_newick(node.get_left(), newick, node.dist, leaf_names)
        newick = get_newick(node.get_right(), f",{newick}", node.dist, leaf_names)
        newick = f"({newick}"
        return newick


def main():
    args = parse_args()

    # Load CRISPR spacer presence/absence matrix
    sep = "\t" if args.sep == "\\t" else args.sep
    mat = pd.read_csv(args.input, sep=sep, index_col=0)

    # Ensure values are numeric 0/1 (important!)
    mat = mat.apply(pd.to_numeric, errors="coerce").fillna(0).astype(int)

    print("Matrix shape (genomes × spacers):", mat.shape)

    # 2. Compute Jaccard distance between genomes
    # pdist works on rows → each row is a genome
    dist_jaccard = pdist(mat.values, metric="jaccard")

    # 3. UPGMA hierarchical clustering (average linkage)
    Z = linkage(dist_jaccard, method="average")  

    # 4. Convert SciPy linkage tree to Newick string
    tree = to_tree(Z, rd=False)
    leaf_names = list(mat.index)
    newick_str = get_newick(tree, leaf_names=leaf_names)

    # 5. Write Newick tree to file
    with open(args.output, "w") as f:
        f.write(newick_str + "\n")

    print("Newick tree written to:")
    print(args.output)


if __name__ == "__main__":
    main()

