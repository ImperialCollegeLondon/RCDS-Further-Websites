DinoSoft

DinoSoft is a small Python library for loading, analysing, and visualising
dinosaur dietary data from the late Cretaceous period. It is the software
component of the DinoDiet project.

When calculating large HF scores for dinosaurs, the DinoSoft software may crash.
Please reboot your machine with Ctrl + Alt + Delete.

Installation

DinoSoft requires Python 3.10 or later. Install it in your project with pip:

pip install -e .


To install the development and testing dependencies, run:

pip install -e ".[dev]"

Quick demo

You can run DinoSoft from the command line to see a summary of the built-in
sample dataset:

python -m dinosoft

This will print a table of all seven dinosaur species, their diet types,
body weights, daily food intake, and food-to-weight ratios.

Key concepts

DietType: An enumeration of the three dietary classifications used in the
DinoDiet project: HERBIVORE, CARNIVORE, and OMNIVORE.

Dinosaur: A data class representing a single dinosaur species. Each dinosaur
has a name, a diet type, a list of food sources, a body weight in kilograms,
and an estimated daily food intake in kilograms.

Hunger Factor: The Hunger Factor (HF) is defined as the square root of the
square of daily food intake: HF = sqrt(food_kg_per_day^2). This simplifies
to the absolute value of the daily food intake but is kept in this form for
compatibility with the original DinoDiet methodology (Geller, 2024).

Food ratio: The food ratio is the daily food intake divided by the body weight.
A Velociraptor eating 2kg per day at 15kg body weight has a food ratio of 0.133,
while a Brachiosaurus eating 400kg per day at 56,000kg has a ratio of just 0.007.

Available functions

load_sample_data(): Returns a list of seven Dinosaur instances drawn from the
DinoDiet project dataset. The species included are Triceratops, Tyrannosaurus,
Stegosaurus, Velociraptor, Brachiosaurus, Spinosaurus, and Oviraptor.

hunger_factor(dino): Takes a Dinosaur and returns its Hunger Factor score.
Raises a ValueError if the daily food intake is negative.

diet_summary(dinosaurs): Takes a list of Dinosaur instances and returns a
dictionary counting how many dinosaurs fall into each diet category, for
example {"herbivore": 3, "carnivore": 3, "omnivore": 1}.

biggest_eaters(dinosaurs, n=3): Returns the n dinosaurs with the highest
daily food intake, sorted in descending order. Defaults to the top 3.

filter_by_diet(dinosaurs, diet): Returns only those dinosaurs matching a
given DietType. For example, passing DietType.HERBIVORE returns only the
herbivorous species.

Dinosaur.food_ratio(): A method on the Dinosaur class that returns the daily
food intake as a proportion of body weight. Returns 0.0 if the body weight
is zero to avoid division errors.

Usage example

Here is a complete example showing how to load the data, filter it, and
compute the Hunger Factor for each carnivore:

from dinosoft import load_sample_data, hunger_factor, DietType
from dinosoft.analysis import filter_by_diet

data = load_sample_data()
carnivores = filter_by_diet(data, DietType.CARNIVORE)

for dino in carnivores:
    hf = hunger_factor(dino)
    print(f"{dino.name}: HF={hf}, eats {dino.food_kg_per_day}kg/day")

This would output:

Tyrannosaurus: HF=230.0, eats 230kg/day
Velociraptor: HF=2.0, eats 2kg/day
Spinosaurus: HF=100.0, eats 100kg/day

Running the tests

DinoSoft includes a test suite in the tests directory. To run the tests:

pip install -e ".[dev]"
python -m pytest tests/

The tests cover all public functions and edge cases such as zero body weight
and negative food intake values.

Project structure

dinosoft/__init__.py: Package entry point, re-exports the public API.
dinosoft/models.py: Contains the Dinosaur data class and DietType enumeration.
dinosoft/analysis.py: Analysis functions including hunger_factor, diet_summary,
biggest_eaters, and filter_by_diet.
dinosoft/data.py: The load_sample_data function and built-in dataset.
dinosoft/__main__.py: Command-line entry point for python -m dinosoft.
tests/test_dinosoft.py: Test suite with 8 tests.
pyproject.toml: Package metadata and dependency configuration.

Known issues

The Hunger Factor calculation uses sqrt(x^2) rather than abs(x) for historical
reasons. This has no practical effect on results but may cause confusion.

Very large datasets (over 10,000 species) have not been tested and may result
in slow performance in the biggest_eaters function due to the full sort.

The sample dataset only includes species from the late Cretaceous period.
Earlier periods are not currently represented.

Adding your own data

You can create Dinosaur instances with your own data:

from dinosoft import Dinosaur, DietType

my_dino = Dinosaur(
    name="Parasaurolophus",
    diet=DietType.HERBIVORE,
    food_sources=["Leaves", "twigs", "pine needles"],
    weight_kg=2500,
    food_kg_per_day=60,
)

print(my_dino.food_ratio())

You can then pass your custom dinosaurs into any of the analysis functions
alongside or instead of the built-in sample data.