import pandas as pd
from pathlib import Path
from datetime import datetime

# -----------------------------
# Load Results
# -----------------------------
clinical = pd.read_csv("results/report/clinical_interpretation.csv")
evidence = pd.read_csv("results/evidence/evidence_table.csv")

Path("reports/final").mkdir(parents=True, exist_ok=True)

report = []

# ==========================================================
# HEADER
# ==========================================================

report.append("# Clinical Cancer Genomics Interpretation Report\n")
report.append(f"**Generated:** {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")

# ==========================================================
# SAMPLE INFORMATION
# ==========================================================

report.append("## 1. Sample Information\n")

report.append("| Parameter | Value |")
report.append("|----------|-------|")
report.append("| Dataset | TCGA Breast Invasive Carcinoma (TCGA-BRCA) |")
report.append("| Sample Type | Primary Tumor |")
report.append("| Sequencing | Whole Exome Sequencing (WXS) |")
report.append("| Data Source | Genomic Data Commons (GDC) |")
report.append("| Sample ID | TCGA-BH-A18H-01A-11D-A12B-09 |\n")

# ==========================================================
# QC
# ==========================================================

report.append("## 2. Quality Control Summary\n")

report.append("| Metric | Value |")
report.append("|-------|------:|")
report.append("| Total Variants | 48 |")
report.append("| Prioritized Variants | 36 |")
report.append("| Driver Variants | 2 |")
report.append("| Missense Mutations | 31 |")
report.append("| Nonsense Mutations | 3 |")
report.append("| Frameshift Deletions | 1 |")
report.append("| Splice Site Variants | 1 |")
report.append("| SNPs | 47 |")
report.append("| Deletions | 1 |\n")

# ==========================================================
# DRIVER VARIANTS
# ==========================================================

# Load driver variants

driver = pd.read_csv("results/prioritization/driver_gene_variants.csv")

report.append("## 3. Driver Variant Summary\n")

report.append("| Gene | HGVS.c | HGVS.p | Chromosome | Classification | AMP Tier |")
report.append("|------|--------|--------|------------|----------------|----------|")

for _, row in driver.iterrows():

    amp = evidence.loc[
        evidence["Gene"] == row["Hugo_Symbol"],
        "AMP_Tier"
    ].values[0]

    report.append(
        f"| {row['Hugo_Symbol']} | "
        f"{row['HGVSc']} | "
        f"{row['HGVSp_Short']} | "
        f"{row['Chromosome']}:{row['Start_Position']} | "
        f"{row['Variant_Classification']} | "
        f"{amp} |"
    )

report.append("")

# ==========================================================
# EVIDENCE
# ==========================================================

report.append("## 4. Clinical Evidence Summary\n")

report.append("| Gene | COSMIC | ClinVar | Evidence Summary |")
report.append("|------|---------|----------|-----------------|")

for _, row in evidence.iterrows():
    report.append(
        f"| {row['Gene']} | "
        f"{row['COSMIC']} | "
        f"{row['ClinVar']} | "
        f"{row['Evidence_Summary']} |"
    )

report.append("")

# ==========================================================
# INTERPRETATION
# ==========================================================

report.append("## 5. Clinical Interpretation\n")

for _, row in clinical.iterrows():

    report.append(f"### {row['Gene']}")

    report.append(f"- **Protein Change:** {row['Protein_Change']}")

    report.append(f"- **AMP Tier:** {row['AMP_Tier']}")

    report.append(f"- **Interpretation:** {row['Clinical_Interpretation']}\n")

# ==========================================================
# WORKFLOW
# ==========================================================

report.append("## 6. Analysis Workflow\n")

report.append("""

TCGA BRCA MAF
│
▼
MAF Parsing
│
▼
Quality Control
│
▼
Variant Prioritization
│
▼
Driver Gene Detection
│
▼
Clinical Evidence Integration
│
▼
Educational AMP/ASCO/CAP Tiering
│
▼
Clinical Interpretation
│
▼
Automated Report Generation

""")


# ==========================================================
# Software and Reference Information
# ==========================================================

report.append("## 7. Software and Reference Information\n")

report.append("- Python 3.x")
report.append("- pandas")
report.append("- Linux (Ubuntu/WSL2)")
report.append("- Reference Genome: GRCh38")
report.append("- Input Format: GDC Masked Somatic Mutation (MAF)")
report.append("")


# ==========================================================
# LIMITATIONS
# ==========================================================

report.append("## 8. Limitations\n")

limitations = [
    "Educational workflow using publicly available TCGA research data.",
    "AMP tier assignments are simplified educational demonstrations and not clinical-grade classifications.",
    "Clinical significance depends on tumor type, clinical context, and expert molecular pathology review.",
    "BAM/CRAM review in IGV was not performed for this demonstration dataset.",
    "No therapeutic recommendations are generated by this pipeline."
]

for item in limitations:
    report.append(f"- {item}")

report.append("")


# ==========================================================
# Generated Output Files
# ==========================================================

report.append("## 9. Generated Output Files\n")

outputs = [
    "results/qc/",
    "results/prioritization/",
    "results/evidence/",
    "results/amp/",
    "results/report/",
    "reports/final/"
]

for folder in outputs:
    report.append(f"- {folder}")

report.append("")
# ==========================================================
# DISCLAIMER
# ==========================================================

report.append("## 10. Disclaimer\n")

report.append(
"This report was generated from publicly available TCGA research data and "
"demonstrates a bioinformatics workflow for somatic variant prioritization and "
"educational AMP-style reporting. It is not intended for clinical diagnosis, "
"treatment selection, or patient management."
)

report.append("")

# ==========================================================
# REFERENCES
# ==========================================================

report.append("## 11. References\n")

report.append("1. Li MM et al. *Standards and Guidelines for the Interpretation and Reporting of Sequence Variants in Cancer.* Journal of Molecular Diagnostics, 2017.")  # :contentReference[oaicite:0]{index=0}

report.append("2. Genomic Data Commons (GDC).")

report.append("3. COSMIC Cancer Mutation Database.")

report.append("4. TCGA Breast Invasive Carcinoma (TCGA-BRCA).")

# ==========================================================
# WRITE REPORT
# ==========================================================

with open(
    "reports/final/Clinical_Genomics_Report.md",
    "w",
    encoding="utf-8"
) as f:
    f.write("\n".join(report))

print("Clinical report generated successfully.")
