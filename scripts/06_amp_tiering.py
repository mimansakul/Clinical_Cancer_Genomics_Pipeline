import pandas as pd
from pathlib import Path

df = pd.read_csv("results/evidence/clinical_evidence.csv")

def assign_amp_tier(row):

    gene = row["Hugo_Symbol"]

    impact = row["IMPACT"]

    cosmic = row["COSMIC_Status"]

    if gene in ["TP53", "PIK3CA"] and cosmic == "Present":
        return "Tier II - Potential Clinical Significance"

    elif impact == "HIGH":
        return "Tier III - Variant of Unknown Clinical Significance"

    else:
        return "Tier III - Variant of Unknown Clinical Significance"

df["AMP_Tier"] = df.apply(assign_amp_tier, axis=1)

Path("results/amp").mkdir(parents=True, exist_ok=True)

df.to_csv(
    "results/amp/amp_classification.csv",
    index=False
)

print(df[[
    "Hugo_Symbol",
    "HGVSp_Short",
    "AMP_Tier"
]])
