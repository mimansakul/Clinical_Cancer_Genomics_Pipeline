import pandas as pd
from pathlib import Path

maf_file = "data/maf/01d89297-2636-4115-bfcf-993e9523401e.wxs.aliquot_ensemble_masked.maf"

df = pd.read_csv(
    maf_file,
    sep="\t",
    comment="#",
    low_memory=False
)

print("\n========== BASIC QC ==========\n")

print("Number of variants :", len(df))
print("Number of genes    :", df["Hugo_Symbol"].nunique())
print("Sample            :", df["Tumor_Sample_Barcode"].iloc[0])

print("\nVariant Classes\n")
print(df["Variant_Classification"].value_counts())

print("\nVariant Types\n")
print(df["Variant_Type"].value_counts())

print("\nImpact\n")
print(df["IMPACT"].value_counts())

Path("results/qc").mkdir(parents=True, exist_ok=True)

df["Variant_Classification"].value_counts().to_csv(
    "results/qc/variant_classification.csv"
)

df["Variant_Type"].value_counts().to_csv(
    "results/qc/variant_type.csv"
)

df["IMPACT"].value_counts().to_csv(
    "results/qc/impact_summary.csv"
)

gene_summary = (
    df.groupby("Hugo_Symbol")
      .size()
      .reset_index(name="Mutation_Count")
      .sort_values("Mutation_Count", ascending=False)
)

gene_summary.to_csv(
    "results/qc/gene_summary.csv",
    index=False
)

print("\nQC completed successfully.")
