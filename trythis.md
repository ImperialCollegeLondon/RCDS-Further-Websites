# Try This

<!-- TODO: Add front matter with title, description, and icon -->

On this page, we will build a small analysis of dinosaur diets together.
By the end, you will be able to load data, filter species, compute the
Hunger Factor, and compare dietary habits.

<!-- TODO: Convert this list into a task list with checkboxes using pymdownx.tasklist
     See: https://squidfunk.github.io/mkdocs-material/reference/lists/#using-task-lists -->

<!-- TODO: Wrap "What you will learn" in an admonition: !!! abstract "What you will learn" -->

What you will learn:

- Loading and inspecting the sample dataset
- Filtering dinosaurs by diet type
- Computing the Hunger Factor
- Ranking the biggest eaters
- Understanding food ratios

<!-- TODO: Convert to admonition: !!! note "Before you start" -->

Before you start, make sure you have completed the [Quickstart](quickstart.md)
and have DinoSoft installed.

## Step 1: Load the data

Let's start by loading the built-in sample dataset. Open a Python shell or
create a new script:

```python
from dinosoft import load_sample_data

data = load_sample_data()
print(f"Loaded {len(data)} dinosaurs")  # Prints: Loaded 7 dinosaurs
```

<!-- TODO: Replace the inline comments above with code annotations using (1)! syntax
     See: https://squidfunk.github.io/mkdocs-material/reference/code-blocks/#adding-annotations -->

We can inspect the first entry to see what a Dinosaur looks like:

```python
dino = data[0]
print(dino.name)          # Triceratops
print(dino.diet)          # DietType.HERBIVORE
print(dino.weight_kg)     # 8000
print(dino.food_sources)  # ['Ferns', 'cycads', 'horsetails']
```

<!-- TODO: Convert to admonition: !!! tip "Best practice" -->

Best practice: In a real project, you would load your data from a file or
database rather than using the built-in sample. See the
[How-to Guide on adding your own data](how-to.md#add-your-own-dinosaurs)
for details.

## Step 2: Explore the diet breakdown

Now let's see how the seven species divide across diet types:

```python
from dinosoft import diet_summary

summary = diet_summary(data)
print(summary)
```

This returns a dictionary:

```python
{'herbivore': 3, 'carnivore': 3, 'omnivore': 1}
```

The distribution across our sample matches the broader estimates from the
DinoDiet project: herbivores dominate, with carnivores second and omnivores
the rarest.

## Step 3: Filter by diet

Suppose we only want to work with the carnivores. We can use `filter_by_diet`:

```python
from dinosoft import DietType
from dinosoft.analysis import filter_by_diet

carnivores = filter_by_diet(data, DietType.CARNIVORE)

for dino in carnivores:
    print(f"{dino.name:16s} eats {', '.join(dino.food_sources)}")
```

Expected output:

```
Tyrannosaurus    eats Triceratops, Edmontosaurus
Velociraptor     eats Small herbivorous dinosaurs
Spinosaurus      eats Fish, small to medium-sized dinosaurs
```

## Step 4: Compute the Hunger Factor

The Hunger Factor (HF) is a key metric in the DinoDiet project. Let's
compute it for each carnivore:

```python
from dinosoft import hunger_factor

for dino in carnivores:
    hf = hunger_factor(dino)
    print(f"{dino.name}: HF = {hf}")
```

```
Tyrannosaurus: HF = 230.0
Velociraptor: HF = 2.0
Spinosaurus: HF = 100.0
```

<!-- TODO: Convert to admonition: !!! info "What does the Hunger Factor actually mean?"
     Also consider rendering the formula with pymdownx.arithmatex / MathJax: $\sqrt{x^2}$
     See: https://squidfunk.github.io/mkdocs-material/reference/math/ -->

The HF is simply the absolute daily food intake in kilograms. The
formula uses sqrt(x^2) for historical reasons. See the
[Explanation](explanation.md#the-hunger-factor) page for the full story.

## Step 5: Find the biggest eaters

Let's rank all dinosaurs (not just carnivores) by daily food intake:

```python
from dinosoft import biggest_eaters

top_3 = biggest_eaters(data, n=3)

for rank, dino in enumerate(top_3, 1):
    print(f"#{rank} {dino.name} — {dino.food_kg_per_day} kg/day")
```

```
#1 Brachiosaurus — 400 kg/day
#2 Tyrannosaurus — 230 kg/day
#3 Triceratops — 200 kg/day
```

Notice that herbivores dominate this ranking — large body size means
large food intake, regardless of diet type.

## Step 6: Compare food ratios

Raw intake doesn't tell the full story. A 56-tonne Brachiosaurus eating
400 kg/day is actually eating a smaller proportion of its body weight
than a 15 kg Velociraptor eating just 2 kg/day.

Let's compare using `food_ratio()`:

```python
for dino in data:
    ratio = dino.food_ratio()
    print(f"{dino.name:16s}  {ratio:.4f}  ({ratio*100:.1f}% of body weight)")
```

| Species | Daily intake | Body weight | Ratio |
| :--- | ---: | ---: | ---: |
| Triceratops | 200 kg | 8,000 kg | 2.5% |
| Tyrannosaurus | 230 kg | 8,000 kg | 2.9% |
| Stegosaurus | 70 kg | 3,500 kg | 2.0% |
| **Velociraptor** | **2 kg** | **15 kg** | **13.3%** |
| Brachiosaurus | 400 kg | 56,000 kg | 0.7% |
| Spinosaurus | 100 kg | 7,000 kg | 1.4% |
| Oviraptor | 3 kg | 40 kg | 7.5% |

<!-- TODO: Convert to admonition: !!! success "Key insight" -->

Key insight: Smaller dinosaurs have significantly higher food ratios.
Velociraptor eats 13.3% of its body weight daily — almost 20x the ratio
of Brachiosaurus.

## Congratulations!

<!-- TODO: Convert into a task list with checkboxes and add emoji: :material-party-popper: -->

You have successfully:

- Loaded the sample dataset
- Explored the diet breakdown
- Filtered species by diet type
- Computed the Hunger Factor
- Ranked the biggest eaters
- Compared food ratios across species

Next steps:

- Try the [How-to Guides](how-to.md) for specific tasks
- Read the [Explanation](explanation.md) to understand the methodology
- Browse the [API Reference](reference/api.md) for full technical details
