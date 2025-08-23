---
title: DinoSoft
description: A Python library for analysing dinosaur dietary habits
icon: material/egg
---

# :material-egg: DinoSoft

**DinoSoft** is a small Python library for loading, analysing, and visualising dinosaur dietary data from the late Cretaceous period. It is the software component of the DinoDiet research project.

---

<div class="grid cards" markdown>

-   :material-clock-fast:{ .lg .middle } **Get started in 5 minutes**

    ---

    Install DinoSoft and run your first analysis with just a few commands

    [:octicons-arrow-right-24: Quickstart](quickstart.md)

-   :material-school:{ .lg .middle } **Learn the basics**

    ---

    A guided tutorial that walks you through the core features step by step

    [:octicons-arrow-right-24: Tutorial](tutorial.md)

-   :material-tools:{ .lg .middle } **Solve a problem**

    ---

    Task-oriented guides for common things you might want to do

    [:octicons-arrow-right-24: How-to Guides](how-to.md)

-   :material-head-lightbulb:{ .lg .middle } **Understand the concepts**

    ---

    Learn about the Hunger Factor, food ratios, and the DinoDiet methodology

    [:octicons-arrow-right-24: Explanation](explanation.md)

-   :material-book-open-variant:{ .lg .middle } **API Reference**

    ---

    Exhaustive technical details for every class and function

    [:octicons-arrow-right-24: Reference](reference/api.md)

-   :material-flask:{ .lg .middle } **Examples & Templates**

    ---

    Copy-pasteable snippets and a full starter project

    [:octicons-arrow-right-24: Examples](examples.md)

</div>

## Quick overview

```python
from dinosoft import load_sample_data, diet_summary, biggest_eaters

data = load_sample_data()
print(diet_summary(data))       # {'herbivore': 3, 'carnivore': 3, 'omnivore': 1}
print(biggest_eaters(data, 1))  # [Dinosaur(name='Brachiosaurus', ...)]
```

!!! info "About the DinoDiet project"

    This is a fictional research project created for
    educational purposes as part of an Imperial College London
    RCDS workshop on software documentation.
