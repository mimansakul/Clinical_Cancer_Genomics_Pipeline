import pandas as pd
from pathlib import Path

# Load AMP-classified variants
df = pd.read_csv("results/amp/amp_classification.csv")

# Build an educational evidence summary
evidence = []

for _, row in df.iterrows():

    notes = []

    if row["COSMIC_Status"] == "Present":
        notes.append("Reported in COSMIC")

    if row["ClinVar_Status"] != "Not Reported":
        notes.append("ClinVar annotation available")

    if row["Hugo_Symbol"] == "TP53":
        notes.append("Well-established tumor suppressor gene")

    if row["Hugo_Symbol"] == "PIK3CA":
        notes.append("Established oncogene in breast cancer")

    evidence.append({
        "Gene": row["Hugo_Symbol"],
        "Protein_Change": row["HGVSp_Short"],
        "Variant": row["Variant_Classification"],
        "Impact": row["IMPACT"],
        "COSMIC": row["COSMIC_Status"],
        "ClinVar": row["ClinVar_Status"],
        "AMP_Tier": row["AMP_Tier"],
        "Evidence_Summary": "; ".join(notes)
    })

evidence_df = pd.DataFrame(evidence)

Path("results/evidence").mkdir(parents=True, exist_ok=True)

evidence_df.to_csv(
    "results/evidence/evidence_table.csv",
    index=False
)

print("\n===== Clinical Evidence Table =====\n")
print(evidence_df)
