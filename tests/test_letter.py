import pytest

from arabic_alphabet_lab import Letter, get_letter_record, is_arabic_letter


def test_is_arabic_letter_true():
    assert is_arabic_letter("ق") is True
    assert is_arabic_letter("ا") is True


def test_is_arabic_letter_false():
    assert is_arabic_letter("A") is False
    assert is_arabic_letter(" ") is False
    assert is_arabic_letter("") is False
    assert is_arabic_letter("سلام") is False


def test_get_letter_record():
    rec = get_letter_record("ق")
    assert rec["name"] == "QAF"
    assert rec["codepoint"].startswith("U+")


def test_letter_properties():
    qaf = Letter("ق")
    assert qaf.name == "QAF"
    assert qaf.joining == "DUAL"
    assert qaf.can_connect_left is True
    assert qaf.can_connect_right is True

    alef = Letter("ا")
    assert alef.name == "ALEF"
    assert alef.joining == "RIGHT"
    assert alef.can_connect_left is False
    assert alef.can_connect_right is True


def test_letter_validation():
    with pytest.raises(ValueError):
        Letter("A")
    with pytest.raises(ValueError):
        Letter("")
    with pytest.raises(ValueError):
        Letter("سلام")

