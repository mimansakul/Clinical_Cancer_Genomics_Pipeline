library(TCGAbiolinks)

maf <- getMC3MAF()

write.csv(
    maf,
    file = "data/maf/MC3_PUBLIC_MAF.csv",
    row.names = FALSE
)

cat("MC3 download completed!\n")
