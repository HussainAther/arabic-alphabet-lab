from __future__ import annotations

from .load_data import load_diacritics


def is_diacritic(ch: str) -> bool:
    """
    True if `ch` is a known Arabic combining mark (harakat, sukun, shadda, etc.)
    from our diacritics.json.
    """
    if not isinstance(ch, str) or len(ch) != 1:
        return False
    return ch in load_diacritics()

