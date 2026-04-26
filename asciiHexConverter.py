class Converter:
    @staticmethod
    def to_ascii(h):
        return bytes.fromhex(h).decode()

    @staticmethod
    def to_hex(s):
        return s.encode().hex()


def test_converter_to_hex():
    assert Converter.to_hex("Look mom, no hands") == "4c6f6f6b206d6f6d2c206e6f2068616e6473"


def test_converter_to_ascii():
    assert Converter.to_ascii("4c6f6f6b206d6f6d2c206e6f2068616e6473") == "Look mom, no hands"
