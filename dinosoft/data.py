"""Built-in sample data for DinoSoft."""

from __future__ import annotations

from dinosoft.models import Dinosaur, DietType


def load_sample_data() -> list[Dinosaur]:
    """Load the built-in sample dataset of seven dinosaur species.

    The dataset is drawn from the DinoDiet project and
    represents a selection of well-known species from the late
    Cretaceous period.

    Returns:
        A list of seven :class:`~dinosoft.models.Dinosaur` instances.

    Example::

        >>> from dinosoft import load_sample_data
        >>> data = load_sample_data()
        >>> len(data)
        7
        >>> data[0].name
        'Triceratops'
    """
    return [
        Dinosaur(
            name="Triceratops",
            diet=DietType.HERBIVORE,
            food_sources=["Ferns", "cycads", "horsetails"],
            weight_kg=8000,
            food_kg_per_day=200,
        ),
        Dinosaur(
            name="Tyrannosaurus",
            diet=DietType.CARNIVORE,
            food_sources=["Triceratops", "Edmontosaurus"],
            weight_kg=8000,
            food_kg_per_day=230,
        ),
        Dinosaur(
            name="Stegosaurus",
            diet=DietType.HERBIVORE,
            food_sources=["Ferns", "mosses", "cycads"],
            weight_kg=3500,
            food_kg_per_day=70,
        ),
        Dinosaur(
            name="Velociraptor",
            diet=DietType.CARNIVORE,
            food_sources=["Small herbivorous dinosaurs"],
            weight_kg=15,
            food_kg_per_day=2,
        ),
        Dinosaur(
            name="Brachiosaurus",
            diet=DietType.HERBIVORE,
            food_sources=["High tree foliage", "conifers"],
            weight_kg=56000,
            food_kg_per_day=400,
        ),
        Dinosaur(
            name="Spinosaurus",
            diet=DietType.CARNIVORE,
            food_sources=["Fish", "small to medium-sized dinosaurs"],
            weight_kg=7000,
            food_kg_per_day=100,
        ),
        Dinosaur(
            name="Oviraptor",
            diet=DietType.OMNIVORE,
            food_sources=["Eggs", "plants", "small animals"],
            weight_kg=40,
            food_kg_per_day=3,
        ),
    ]
