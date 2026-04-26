def dna_to_rna(dna):
    return dna.translate(str.maketrans("GCAT", "GCAU"))


def dna_to_rna_alternative(dna):
    return dna.replace("T", "U")


def test_dna_to_rna():
    assert dna_to_rna("GAAGTTCTAG") == "GAAGUUCUAG"


def test_dna_to_rna_alternative():
    assert dna_to_rna_alternative("GAAGTTCTAG") == "GAAGUUCUAG"
