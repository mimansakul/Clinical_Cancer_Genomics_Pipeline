import pandas as pd

maf = pd.read_csv(
    "results/prioritization/high_priority_variants.csv"
)

with open("gene_panels/cancer_driver_genes.txt") as f:
    drivers = {line.strip() for line in f}

driver_variants = maf[
    maf["Hugo_Symbol"].isin(drivers)
]

driver_variants.to_csv(
    "results/prioritization/driver_gene_variants.csv",
    index=False
)

print(driver_variants[
    ["Hugo_Symbol",
     "HGVSp_Short",
     "Variant_Classification",
     "IMPACT"]
])
