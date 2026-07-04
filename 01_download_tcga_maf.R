library(TCGAbiolinks)

query <- GDCquery(
  project = "TCGA-BRCA",
  data.category = "Simple Nucleotide Variation",
  data.type = "Masked Somatic Mutation",
  access = "open",
  workflow.type = "Aliquot Ensemble Somatic Variant Merging and Masking"
)

GDCdownload(query)

maf <- GDCprepare(query)

write.csv(
  maf,
  file = "data/maf/TCGA_BRCA_MAF.csv",
  row.names = FALSE
)
