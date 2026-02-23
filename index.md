# DinoSoft

<!-- TODO: Add front matter with title, description, and icon
     See: https://squidfunk.github.io/mkdocs-material/reference/#setting-the-page-icon -->

<!-- TODO: Replace this bullet list with a grid of cards using attr_list + md_in_html
     See: https://squidfunk.github.io/mkdocs-material/reference/grids/ -->

DinoSoft is a small Python library for loading, analysing, and visualising
dinosaur dietary data from the late Cretaceous period. It is the software
component of the DinoDiet research project.

## Documentation sections

- Read more about our approach [here](about.md)

<!-- TODO: Once you have developed all of your sections, add a listing here with grid cards

https://squidfunk.github.io/mkdocs-material/reference/grids/#using-card-grids

<div class="grid cards" markdown>

-   :material-clock-fast:{ .lg .middle } **Get started in 5 minutes**

    ---

    Install DinoSoft and run your first analysis with just a few commands

    [:octicons-arrow-right-24: Quickstart](quickstart.md)

-->

## Quick overview

```python
from dinosoft import load_sample_data, diet_summary, biggest_eaters

data = load_sample_data()
print(diet_summary(data))       # {'herbivore': 3, 'carnivore': 3, 'omnivore': 1}
print(biggest_eaters(data, 1))  # [Dinosaur(name='Brachiosaurus', ...)]
```

<!-- TODO: Convert the note below into an admonition: !!! info "About the DinoDiet project"
     See: https://squidfunk.github.io/mkdocs-material/reference/admonitions/ -->

This is a fictional research project created for
educational purposes as part of an Imperial College London
RCDS workshop on software documentation.
