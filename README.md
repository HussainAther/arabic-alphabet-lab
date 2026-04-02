# Arabic Alphabet Lab

> Arabic as a programmable system — not just a script.

Arabic Alphabet Lab is a lightweight Python library that models the Arabic writing system as structured, programmable data. It encodes letters, their properties, and the rules that govern how they connect, enabling analysis, transformation, and computational experimentation with Arabic text.

---

## ✨ Motivation

Arabic script is not just a set of characters — it is a *dynamic system*:

- Letters change shape depending on position
- Characters connect conditionally
- Diacritics modify meaning and pronunciation
- Visual structure carries linguistic information

This project treats Arabic as a **computational object**, making it easier to:

- Build language tools
- Explore script logic
- Prototype educational or visualization systems
- Study writing systems programmatically

---

## 🧠 Core Idea

Each Arabic letter is represented as structured data:

```json
{
  "ق": {
    "name": "QAF",
    "codepoint": "U+0642",
    "joining": "DUAL",
    "group": "ARABIC",
    "notes": ["descender", "two dots above"]
  }
}
````

This allows us to reason about:

* Joining behavior (`RIGHT`, `DUAL`, etc.)
* Structural features
* Groupings and classifications
* Rendering logic (future direction)

---

## 📦 Features

* 📚 Structured dataset of Arabic letters (`letters.json`)
* 🔤 Explicit modeling of **joining behavior**
* 🧩 Designed for composability and extension
* 🧪 Test-ready with `pytest`
* 🧼 Linting via `ruff`

---

## 🗂️ Project Structure

```
arabic-alphabet-lab/
├── src/
│   ├── arabic_alphabet_lab/
│   │   └── ... (core logic - WIP/extendable)
│   └── data/
│       └── letters.json   # canonical letter definitions
├── tests/
│   └── test_graphemes.py
├── pyproject.toml
└── README.md
```

---

## 🚀 Getting Started

### Install (dev mode)

```bash
pip install -e .
```

### Install dev dependencies

```bash
pip install -e .[dev]
```

---

## 🧪 Run Tests

```bash
pytest
```

---

## 🔍 Example Use Cases

This library is designed as a foundation for:

* Arabic text rendering engines
* Educational tools for learning Arabic script
* Linguistic analysis pipelines
* NLP preprocessing for Arabic
* XR / visualization systems (e.g., interactive script exploration)

---

## 🧩 Design Philosophy

* **Data-first**: Language is encoded as structured data
* **Composable**: Build higher-level logic on top of primitives
* **Minimal core**: Avoid over-engineering; enable experimentation
* **Extensible**: Add diacritics, ligatures, morphology, etc.

---

## 🔮 Future Directions

* Diacritic system modeling (harakat)
* Positional glyph generation (initial/medial/final forms)
* Ligature handling (e.g., lam-alef)
* Rendering pipelines
* Integration with visualization / XR systems
* Graph-based representation of script structure

---

## 🤝 Contributing

Contributions are welcome — especially:

* Expanding letter metadata
* Adding grapheme logic
* Building transformation utilities
* Writing educational examples

---

## 📜 License

MIT License

---

## 👤 Author

Hussain Ather

