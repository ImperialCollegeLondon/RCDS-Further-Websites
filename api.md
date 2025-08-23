# API 

The DinoSoft public API. All classes
and functions listed here are importable from the top-level `dinosoft`
package unless otherwise noted.

## Models

### DietType

Classification of dinosaur dietary habits.

Members:

- `HERBIVORE` — Plant-eating dinosaurs
- `CARNIVORE` — Meat-eating dinosaurs
- `OMNIVORE` — Dinosaurs that ate both plants and animals

```python
from dinosoft import DietType

DietType.HERBIVORE.value  # 'herbivore'
```

### Dinosaur

Represents a single dinosaur species and its dietary profile.

Parameters:

- `name` (str) — The species name, e.g. `"Triceratops"`
- `diet` (DietType) — The dietary classification
- `food_sources` (list[str]) — A list of primary food sources
- `weight_kg` (float) — Estimated adult body weight in kilograms
- `food_kg_per_day` (float) — Estimated daily food intake in kilograms

<!-- TODO: Writing out docstrings manually like the above is tedious and
     will go out of date as the code changes. Instead, use the mkdocstrings
     plugin to auto-generate the reference from your Python docstrings.

     1. Install it:
        pip install 'mkdocstrings[python]'

     2. Add it to mkdocs.yml under plugins:
        plugins:
          - search
          - mkdocstrings:
              handlers:
                python:
                  options:
                    show_source: true
                    show_root_heading: true
                    heading_level: 3
                    docstring_style: google

     3. Then replace the content above with:

        ## Models

        ::: dinosoft.models

     The ::: syntax tells mkdocstrings to pull docstrings directly from
     your Python source. It will render classes, functions, parameters,
     return types, and examples automatically.

     See: https://mkdocstrings.github.io/  
     -->

## Analysis

### hunger_factor(dino)

Calculate the Hunger Factor for a dinosaur.

<!-- TODO: Use autodocstrings for this section too! -->

## Data

### load_sample_data()

Load the built-in sample dataset of seven dinosaur species.

<!-- TODO: Use autodocstrings for this section too! -->