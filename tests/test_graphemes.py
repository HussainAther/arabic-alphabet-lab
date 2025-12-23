from arabic_alphabet_lab import graphemes


def test_graphemes_simple_word():
    assert graphemes("سلام") == ["س", "ل", "ا", "م"]


def test_graphemes_with_harakat_and_sukun():
    # قُرْآن  => ق + damma, ر + sukun, آ, ن
    assert graphemes("قُرْآن") == ["قُ", "رْ", "آ", "ن"]


def test_graphemes_whitespace_and_punct():
    assert graphemes("سلام، عالم") == ["س", "ل", "ا", "م", "،", " ", "ع", "ا", "ل", "م"]


def test_graphemes_leading_diacritic_not_dropped():
    assert graphemes("َا") == ["َ", "ا"]

