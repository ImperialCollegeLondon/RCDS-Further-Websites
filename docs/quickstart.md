---
title: Quickstart
description: Get DinoSoft up and running in under 5 minutes
icon: material/rocket-launch
status: new
---

# :material-rocket-launch: Quickstart

Get DinoSoft installed and run your first analysis in under five minutes.

!!! note "Prerequisites"

    You need **Python 3.10** or later. Check your version with:

    ```bash
    python --version
    ```

## 1. Install DinoSoft

```bash
pip install -e .
```

??? tip "Using a virtual environment (recommended)"

    ```bash
    python -m venv .venv
    source .venv/bin/activate  # (1)!
    pip install -e .
    ```

    1.  On Windows, use `.venv\Scripts\activate` instead.

## 2. Run the demo

```bash
python -m dinosoft
```

You should see output like this:

```
==================================================
  DinoSoft  -  Dinosaur Dietary Analysis
==================================================

Diet breakdown:
  carnivore     3
  herbivore     3
  omnivore      1

Top 3 biggest eaters (kg/day):
  Brachiosaurus        400 kg/day  (HF=400.0)
  Tyrannosaurus        230 kg/day  (HF=230.0)
  Triceratops          200 kg/day  (HF=200.0)
```

## 3. Try it in Python

```python
from dinosoft import load_sample_data, diet_summary

data = load_sample_data()  # (1)!
print(diet_summary(data))  # (2)!
```

1.  Loads the built-in dataset of 7 dinosaur species.
2.  Returns `#!python {'herbivore': 3, 'carnivore': 3, 'omnivore': 1}`.

## :material-check-all: Done!

You now have DinoSoft installed with the sample dataset loaded. Head to the [Tutorial](tutorial.md) to learn what you can do with it.

---

!!! question "Something not working?"

    Make sure you are in the project root directory (where `pyproject.toml` is)
    before running `pip install -e .`
