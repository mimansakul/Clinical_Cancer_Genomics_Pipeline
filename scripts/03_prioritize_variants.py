import pandas as pd
from pathlib import Path

maf = pd.read_csv(
    "data/maf/01d89297-2636-4115-bfcf-993e9523401e.wxs.aliquot_ensemble_masked.maf",
    sep="\t",
    comment="#",
    low_memory=False
)

Path("results/prioritization").mkdir(parents=True, exist_ok=True)

# Keep HIGH and MODERATE impact variants
priority = maf[
    maf["IMPACT"].isin(["HIGH", "MODERATE"])
].copy()

# Remove synonymous (silent) mutations
priority = priority[
    priority["Variant_Classification"] != "Silent"
]

# Select clinically useful columns
priority = priority[
    [
        "Hugo_Symbol",
        "Chromosome",
        "Start_Position",
        "Variant_Classification",
        "Variant_Type",
        "HGVSc",
        "HGVSp_Short",
        "IMPACT",
        "COSMIC",
        "CLIN_SIG",
        "Tumor_Sample_Barcode"
    ]
]

priority.to_csv(
    "results/prioritization/high_priority_variants.csv",
    index=False
)

print("High-priority variants:", len(priority))
print(priority.head(10))
