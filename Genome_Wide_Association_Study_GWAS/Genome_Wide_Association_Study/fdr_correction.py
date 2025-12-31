import argparse
import pandas as pd
from statsmodels.stats.multitest import multipletests


def main():
    parser = argparse.ArgumentParser(
        description="Apply Benjamini–Hochberg FDR correction to pyseer GWAS results"
    )
    parser.add_argument(
        "-i", "--input",
        required=True,
        help="Input pyseer results file (tab-delimited)"
    )
    parser.add_argument(
        "-o", "--output",
        required=True,
        help="Output file with FDR-corrected p-values"
    )
    parser.add_argument(
        "--pcol",
        default="lrt-pvalue",
        help="Column name containing raw p-values (default: lrt-pvalue)"
    )
    parser.add_argument(
        "--fdr-col",
        default="lrt-pval-FDR",
        help="Name of output column for FDR-corrected p-values"
    )

    args = parser.parse_args()

    # Load pyseer results
    df = pd.read_csv(args.input, sep="\t")

    if args.pcol not in df.columns:
        raise ValueError(f"P-value column '{args.pcol}' not found in input file")

    # Apply Benjamini–Hochberg FDR correction
    df[args.fdr_col] = multipletests(
        df[args.pcol],
        method="fdr_bh"
    )[1]

    # Save output
    df.to_csv(args.output, sep="\t", index=False)
    print(f"✅ Done! FDR-corrected results saved to: {args.output}")


if __name__ == "__main__":
    main()

