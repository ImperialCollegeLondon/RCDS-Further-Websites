# First

<!-- TODO: Add front matter with title, description, icon, and status: new
     See: https://squidfunk.github.io/mkdocs-material/reference/#setting-the-page-status -->

Get DinoSoft installed and run your first analysis in under five minutes.

<!-- TODO: Convert the prerequisites below into an admonition: !!! note "Prerequisites"
     See: https://squidfunk.github.io/mkdocs-material/reference/admonitions/ -->

Prerequisites: You need Python 3.10 or later. Check your version with
`python --version`.

## 1. Install DinoSoft

```bash
pip install -e .
```

<!-- TODO: Convert the venv instructions below into a collapsible admonition:
     ??? tip "Using a virtual environment (recommended)"
     See: https://squidfunk.github.io/mkdocs-material/reference/admonitions/#collapsible-blocks -->

If you prefer to use a virtual environment (recommended):

```bash
python -m venv .venv
source .venv/bin/activate  # On Windows, use .venv\Scripts\activate
pip install -e .
```

<!-- TODO: Add code annotations to the above snippet using the (1)! syntax
     to annotate the Windows alternative
     See: https://squidfunk.github.io/mkdocs-material/reference/code-blocks/#adding-annotations -->

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

<!-- TODO: Add code annotations to explain what each line does
     See: https://squidfunk.github.io/mkdocs-material/reference/code-blocks/#adding-annotations -->

```python
from dinosoft import load_sample_data, diet_summary

data = load_sample_data()  # Loads the built-in dataset of 7 dinosaur species
print(diet_summary(data))  # Returns {'herbivore': 3, 'carnivore': 3, 'omnivore': 1}
```

## Done!

You now have DinoSoft installed with the sample dataset loaded. Head to the
[Tutorial](tutorial.md) to learn what you can do with it.

<!-- TODO: Convert the troubleshooting note below into an admonition:
     !!! question "Something not working?" -->

Something not working? Make sure you are in the project root directory
(where `pyproject.toml` is) before running `pip install -e .`
