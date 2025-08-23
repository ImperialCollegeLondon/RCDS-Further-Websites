"""Data models for DinoSoft."""

from __future__ import annotations

from dataclasses import dataclass, field
from enum import Enum


class DietType(Enum):
    """Classification of dinosaur dietary habits.

    Attributes:
        HERBIVORE: Plant-eating dinosaurs.
        CARNIVORE: Meat-eating dinosaurs.
        OMNIVORE: Dinosaurs that ate both plants and animals.
    """

    HERBIVORE = "herbivore"
    CARNIVORE = "carnivore"
    OMNIVORE = "omnivore"


@dataclass
class Dinosaur:
    """Represents a single dinosaur species and its dietary profile.

    Parameters:
        name: The species name, e.g. ``"Triceratops"``.
        diet: The dietary classification.
        food_sources: A list of primary food sources.
        weight_kg: Estimated adult body weight in kilograms.
        food_kg_per_day: Estimated daily food intake in kilograms.

    Example::

        >>> from dinosoft import Dinosaur, DietType
        >>> rex = Dinosaur(
        ...     name="Tyrannosaurus",
        ...     diet=DietType.CARNIVORE,
        ...     food_sources=["Triceratops", "Edmontosaurus"],
        ...     weight_kg=8000,
        ...     food_kg_per_day=230,
        ... )
        >>> rex.name
        'Tyrannosaurus'
    """

    name: str
    diet: DietType
    food_sources: list[str] = field(default_factory=list)
    weight_kg: float = 0.0
    food_kg_per_day: float = 0.0

    def food_ratio(self) -> float:
        """Return daily food intake as a proportion of body weight.

        Returns:
            The ratio of ``food_kg_per_day`` to ``weight_kg``.
            Returns ``0.0`` if ``weight_kg`` is zero.

        Example::

            >>> dino = Dinosaur("Stego", DietType.HERBIVORE, weight_kg=3500, food_kg_per_day=70)
            >>> round(dino.food_ratio(), 3)
            0.02
        """
        if self.weight_kg == 0:
            return 0.0
        return self.food_kg_per_day / self.weight_kg
