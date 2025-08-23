# Some Code

<!-- TODO: Add front matter with title, description, and icon -->

<!-- TODO: Add title attributes to code blocks: ```python title="filename.py"
     See: https://squidfunk.github.io/mkdocs-material/reference/code-blocks/#adding-a-title -->

<!-- TODO: Wrap each "Output" section in a collapsible admonition:
     ??? success "Output"
     This lets readers expand only the outputs they want to check -->

Small, self-contained code snippets demonstrating individual features.
Each can be copied and run directly.

## Load and print all species

```python
from dinosoft import load_sample_data

for dino in load_sample_data():
    print(f"{dino.name} ({dino.diet.value})")
```

Output:

```
Triceratops (herbivore)
Tyrannosaurus (carnivore)
Stegosaurus (herbivore)
Velociraptor (carnivore)
Brachiosaurus (herbivore)
Spinosaurus (carnivore)
Oviraptor (omnivore)
```

## Hunger Factor for all species

```python
from dinosoft import load_sample_data, hunger_factor

for dino in load_sample_data():
    print(f"{dino.name:16s}  HF = {hunger_factor(dino):6.1f}")
```

Output:

```
Triceratops       HF =  200.0
Tyrannosaurus     HF =  230.0
Stegosaurus       HF =   70.0
Velociraptor      HF =    2.0
Brachiosaurus     HF =  400.0
Spinosaurus       HF =  100.0
Oviraptor         HF =    3.0
```

## Diet pie chart with matplotlib

```python
import matplotlib.pyplot as plt
from dinosoft import load_sample_data, diet_summary

summary = diet_summary(load_sample_data())

# Green for herbivore, red for carnivore, orange for omnivore
plt.pie(
    summary.values(),
    labels=[k.title() for k in summary.keys()],
    autopct="%1.0f%%",
    colors=["#4caf50", "#f44336", "#ff9800"],
)
plt.title("Diet Distribution")
plt.savefig("diet_pie.png")
```

<!-- TODO: Add a code annotation on the colors line explaining the colour choices -->

<!-- TODO: Convert the note below into an admonition: !!! note -->

Note: This example requires `matplotlib` which is not included in
DinoSoft's dependencies. Install it with `pip install matplotlib`.

## Sort by food ratio

```python
from dinosoft import load_sample_data

data = load_sample_data()
by_ratio = sorted(data, key=lambda d: d.food_ratio(), reverse=True)

for dino in by_ratio:
    print(f"{dino.name:16s}  {dino.food_ratio():.4f}")
```

Output:

```
Velociraptor      0.1333
Oviraptor         0.0750
Tyrannosaurus     0.0288
Triceratops       0.0250
Stegosaurus       0.0200
Spinosaurus       0.0143
Brachiosaurus     0.0071
```

## Create a custom species

```python
from dinosoft import Dinosaur, DietType, hunger_factor

ankylosaurus = Dinosaur(
    name="Ankylosaurus",
    diet=DietType.HERBIVORE,
    food_sources=["Low-growing plants", "ferns"],
    weight_kg=6000,
    food_kg_per_day=150,
)

print(f"Name:    {ankylosaurus.name}")
print(f"HF:      {hunger_factor(ankylosaurus)}")
print(f"Ratio:   {ankylosaurus.food_ratio():.4f}")
```

Output:

```
Name:    Ankylosaurus
HF:      150.0
Ratio:   0.0250
```

## Export to JSON

```python
import json
from dinosoft import load_sample_data

data = load_sample_data()

records = [
    {
        "name": d.name,
        "diet": d.diet.value,
        "weight_kg": d.weight_kg,
        "food_kg_per_day": d.food_kg_per_day,
        "food_sources": d.food_sources,
    }
    for d in data
]

print(json.dumps(records, indent=2))
```

## Compare two specific dinosaurs

```python
from dinosoft import load_sample_data, hunger_factor

data = {d.name: d for d in load_sample_data()}

rex = data["Tyrannosaurus"]
brach = data["Brachiosaurus"]

print(f"{'':20s} {'T-Rex':>10s} {'Brachio':>10s}")
print(f"{'Weight (kg)':20s} {rex.weight_kg:10,.0f} {brach.weight_kg:10,.0f}")
print(f"{'Food (kg/day)':20s} {rex.food_kg_per_day:10,.0f} {brach.food_kg_per_day:10,.0f}")
print(f"{'Hunger Factor':20s} {hunger_factor(rex):10.1f} {hunger_factor(brach):10.1f}")
print(f"{'Food ratio':20s} {rex.food_ratio():10.4f} {brach.food_ratio():10.4f}")
```

Output:

```
                          T-Rex    Brachio
Weight (kg)               8,000     56,000
Food (kg/day)               230        400
Hunger Factor             230.0      400.0
Food ratio               0.0288     0.0071
```
