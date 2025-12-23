from __future__ import annotations

import json
from functools import lru_cache
from importlib.resources import files
from typing import Any, Dict


def _read_json(rel_path: str) -> Dict[str, Any]:
    data_path = files("arabic_alphabet_lab").joinpath(rel_path)
    with data_path.open("r", encoding="utf-8") as f:
        return json.load(f)


@lru_cache(maxsize=1)
def load_letters() -> Dict[str, Dict[str, Any]]:
    """
    Load letters.json as a mapping: { "ق": { ... }, ... }.
    Cached for speed and to avoid repeated IO.
    """
    return _read_json("data/letters.json")


@lru_cache(maxsize=1)
def load_diacritics() -> Dict[str, Dict[str, Any]]:
    """
    Load diacritics.json as a mapping: { "َ": { ... }, ... }.
    Cached for speed and to avoid repeated IO.
    """
    return _read_json("data/diacritics.json")

