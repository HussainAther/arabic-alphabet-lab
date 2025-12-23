from __future__ import annotations

from dataclasses import dataclass
from typing import Any, Dict, Optional, Literal

from .load_data import load_letters

JoiningType = Literal["DUAL", "RIGHT", "NONE"]


def is_arabic_letter(ch: str) -> bool:
    if not isinstance(ch, str) or len(ch) != 1:
        return False
    return ch in load_letters()


def get_letter_record(ch: str) -> Dict[str, Any]:
    """
    Return the raw record for a given Arabic letter.

    Raises:
        ValueError: if ch is not a single Arabic letter we know about.
    """
    if not isinstance(ch, str) or len(ch) != 1:
        raise ValueError(f"Expected a single character, got: {ch!r}")
    letters = load_letters()
    if ch not in letters:
        raise ValueError(f"Unknown Arabic letter: {ch!r}")
    return letters[ch]


def _normalize_joining(value: Optional[str]) -> JoiningType:
    if value is None:
        return "NONE"
    v = value.strip().upper()
    if v in ("DUAL", "RIGHT", "NONE"):
        return v  # type: ignore[return-value]
    # future-proof: if data has something unexpected, keep failure explicit
    raise ValueError(f"Invalid joining type in data: {value!r}")


@dataclass(frozen=True, slots=True)
class Letter:
    """
    Structured representation of an Arabic letter (base character).

    This is not a shaper; it's a programmable, inspectable model of the script.
    """
    char: str

    def __post_init__(self) -> None:
        if not isinstance(self.char, str) or len(self.char) != 1:
            raise ValueError(f"Letter expects a single character, got: {self.char!r}")
        if not is_arabic_letter(self.char):
            raise ValueError(f"Unknown Arabic letter: {self.char!r}")

    @property
    def record(self) -> Dict[str, Any]:
        return get_letter_record(self.char)

    @property
    def name(self) -> str:
        return str(self.record.get("name", ""))

    @property
    def codepoint(self) -> str:
        # stored like "U+0642"
        return str(self.record.get("codepoint", ""))

    @property
    def joining(self) -> JoiningType:
        return _normalize_joining(self.record.get("joining"))

    @property
    def can_connect_left(self) -> bool:
        """
        Can this letter connect to the letter on its left (i.e., have a joining stroke
        to the previous letter in Arabic writing direction)?
        """
        # DUAL letters connect on both sides
        return self.joining == "DUAL"

    @property
    def can_connect_right(self) -> bool:
        """
        Can this letter connect to the letter on its right (i.e., connect forward to next letter)?
        """
        # RIGHT and DUAL both connect to the next letter
        return self.joining in ("DUAL", "RIGHT")

    def __str__(self) -> str:
        return self.char

