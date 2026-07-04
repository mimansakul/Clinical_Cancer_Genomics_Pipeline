import pandas as pd
from pathlib import Path

variants = pd.read_csv(
    "results/prioritization/driver_gene_variants.csv"
)

def clinvar_status(x):
    if pd.isna(x) or x == "":
        return "Not Reported"
    return x

def cosmic_status(x):
    if pd.isna(x) or x == "":
        return "Absent"
    return "Present"

variants["ClinVar_Status"] = variants["CLIN_SIG"].apply(clinvar_status)
variants["COSMIC_Status"] = variants["COSMIC"].apply(cosmic_status)

Path("results/evidence").mkdir(
    parents=True,
    exist_ok=True
)

variants.to_csv(
    "results/evidence/clinical_evidence.csv",
    index=False
)

print(
    variants[
        [
            "Hugo_Symbol",
            "HGVSp_Short",
            "ClinVar_Status",
            "COSMIC_Status"
        ]
    ]
)
