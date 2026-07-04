import pandas as pd
from pathlib import Path

df = pd.read_csv("results/evidence/evidence_table.csv")

interpretations = []

for _, row in df.iterrows():

    gene = row["Gene"]

    if gene == "TP53":
        summary = (
            "TP53 is a well-established tumor suppressor gene. "
            "The detected nonsense variant is predicted to truncate the protein. "
            "Further interpretation requires correlation with tumor type, "
            "clinical findings, and additional evidence."
        )

    elif gene == "PIK3CA":
        summary = (
            "PIK3CA is a frequently altered oncogene in breast cancer. "
            "The detected missense variant warrants review using curated "
            "clinical knowledgebases and disease-specific evidence."
        )

    else:
        summary = (
            "Clinical significance requires additional review."
        )

    interpretations.append(summary)

df["Clinical_Interpretation"] = interpretations

Path("results/report").mkdir(parents=True, exist_ok=True)

df.to_csv(
    "results/report/clinical_interpretation.csv",
    index=False
)

print(df[[
    "Gene",
    "Protein_Change",
    "AMP_Tier",
    "Clinical_Interpretation"
]])
