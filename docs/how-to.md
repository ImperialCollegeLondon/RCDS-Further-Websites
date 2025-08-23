---
title: How-to Guides
description: Task-oriented guides for common DinoSoft operations
icon: material/tools
---

# :material-tools: How-to Guides

Practical, goal-oriented guides for specific tasks. Each guide assumes
you have DinoSoft [installed](quickstart.md) and are familiar with the
[basics](tutorial.md).

---

## Add your own dinosaurs

Create custom `Dinosaur` instances and mix them with the sample data:

```python
from dinosoft import Dinosaur, DietType, load_sample_data, biggest_eaters

my_dino = Dinosaur(
    name="Parasaurolophus",
    diet=DietType.HERBIVORE,
    food_sources=["Leaves", "twigs", "pine needles"],
    weight_kg=2500,
    food_kg_per_day=60,
)

all_dinos = load_sample_data() + [my_dino]  # (1)!
print(biggest_eaters(all_dinos, n=4))
```

1. You can combine lists freely — all analysis functions accept
   any `#!python list[Dinosaur]`.

!!! warning

    Make sure `weight_kg` and `food_kg_per_day` are non-negative.
    Negative values will raise a `ValueError` in `hunger_factor()`.

---

## Compare two diet groups

To compare herbivores and carnivores side by side:

```python
from dinosoft import load_sample_data, DietType
from dinosoft.analysis import filter_by_diet

data = load_sample_data()
herbs = filter_by_diet(data, DietType.HERBIVORE)
carns = filter_by_diet(data, DietType.CARNIVORE)

avg_herb = sum(d.food_kg_per_day for d in herbs) / len(herbs)
avg_carn = sum(d.food_kg_per_day for d in carns) / len(carns)

print(f"Avg herbivore intake: {avg_herb:.0f} kg/day")  # (1)!
print(f"Avg carnivore intake: {avg_carn:.0f} kg/day")
```

1. Herbivores average ~223 kg/day vs ~111 kg/day for carnivores in the
   sample data.

---

## Run the test suite

=== "With pytest"

    ```bash
    pip install -e ".[dev]"
    python -m pytest tests/ -v
    ```

=== "Without pytest"

    ```bash
    python -m doctest dinosoft/models.py -v
    python -m doctest dinosoft/analysis.py -v
    ```

!!! tip

    All public functions include doctests. You can run them individually
    to verify a specific module.

---

## Handle errors gracefully

The `hunger_factor` function raises a `ValueError` for negative intake
values. Here is how to handle it:

```python
from dinosoft import Dinosaur, DietType, hunger_factor

dino = Dinosaur("Bad Data", DietType.OMNIVORE, food_kg_per_day=-5)

try:
    hf = hunger_factor(dino)
except ValueError as e:
    print(f"Caught error: {e}")  # (1)!
```

1. Prints: `Caught error: food_kg_per_day must be non-negative, got -5`

---

## Build the documentation site

This documentation site is built with [Material for MkDocs](https://squidfunk.github.io/mkdocs-material/).

=== "Serve locally"

    ```bash
    pip install mkdocs-material
    mkdocs serve  # (1)!
    ```

    1. Opens a live preview at `http://127.0.0.1:8000`

=== "Build static site"

    ```bash
    mkdocs build
    ```

    The output is written to the `site/` directory.

=== "Deploy to GitHub Pages"

    ```bash
    mkdocs gh-deploy
    ```

    Or use the GitHub Actions workflow for automatic deployment on push.

---

## Export data to CSV

DinoSoft doesn't include an export function, but you can easily write one
using the standard library:

```python
import csv
from dinosoft import load_sample_data

data = load_sample_data()

with open("dino_data.csv", "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["Name", "Diet", "Weight (kg)", "Food (kg/day)"])  # (1)!
    for dino in data:
        writer.writerow([
            dino.name,
            dino.diet.value,
            dino.weight_kg,
            dino.food_kg_per_day,
        ])
```

1. This creates a CSV compatible with the R analysis workflow described
   in the DinoDiet project README.
