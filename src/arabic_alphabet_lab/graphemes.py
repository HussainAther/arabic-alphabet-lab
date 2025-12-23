from __future__ import annotations

from typing import List

from .diacritics import is_diacritic


def graphemes(text: str) -> List[str]:
    """
    Segment Arabic-script text into "grapheme clusters" where each cluster is:
      - one base character (letter or other non-diacritic)
      - followed by zero or more diacritics

    Examples:
      "قُرْآن" -> ["قُ", "رْ", "آ", "ن"]
      "السَّلَام" -> ["ا", "ل", "سَّ", "لَ", "ا", "م"]
    """
    if text is None:
        raise ValueError("text cannot be None")

    clusters: List[str] = []
    current = ""

    for ch in text:
        if is_diacritic(ch):
            # attach diacritics to the current base if it exists
            if current:
                current += ch
            else:
                # leading diacritic: keep as its own cluster to avoid dropping info
                clusters.append(ch)
            continue

        # new base char starts a new cluster
        if current:
            clusters.append(current)
        current = ch

    if current:
        clusters.append(current)

    return clusters

