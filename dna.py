def DNA_strand(dna):
    dictionary = {"A": "T", "T": "A", "C": "G", "G": "C"}
    return "".join(dictionary.get(ch, ch) for ch in dna)  # type: ignore


def DNA_strand_alternative(dna):
    return dna.translate(str.maketrans("ATCG", "TAGC"))


def test_DNA_strand():
    assert DNA_strand("ATTGC") == "TAACG"


def test_DNA_strand_alternative():
    assert DNA_strand_alternative("ATTGCAATGGGCAC") == "TAACGTTACCCGTG"
