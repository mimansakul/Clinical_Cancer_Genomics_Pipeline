library(TCGAbiolinks)

query <- GDCquery(
    project = "TCGA-BRCA",
    data.category = "Simple Nucleotide Variation",
    data.type = "Masked Somatic Mutation",
    workflow.type = "Aliquot Ensemble Somatic Variant Merging and Masking",
    access = "open"
)

GDCdownload(query)

maf <- GDCprepare(query)

write.csv(
    maf,
    "data/maf/TCGA_BRCA_MAF.csv",
    row.names = FALSE
)

cat("Download Finished\n")
