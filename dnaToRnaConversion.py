def dna_to_rna(dna):
    return dna.translate(str.maketrans("GCAT", "GCAU"))


def dna_to_rna_alternative(dna):
    return dna.replace("T", "U")


print(dna_to_rna("GAAGTTCTAG"))
print(dna_to_rna_alternative("GAAGTTCTAG"))
