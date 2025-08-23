"""Analysis functions for DinoSoft."""

from __future__ import annotations

import math
from collections import Counter

from dinosoft.models import Dinosaur, DietType


def hunger_factor(dino: Dinosaur) -> float:
    """Calculate the Hunger Factor (HF) for a dinosaur.

    The Hunger Factor is defined as::

        HF = sqrt(food_kg_per_day ** 2)

    which simplifies to the absolute value of daily food intake,
    but is kept in this form for compatibility with the original
    DinoDiet paper (Geller, 2024).

    Parameters:
        dino: A :class:`~dinosoft.models.Dinosaur` instance.

    Returns:
        The Hunger Factor score (always non-negative).

    Raises:
        ValueError: If ``food_kg_per_day`` is negative.

    Example::

        >>> from dinosoft import Dinosaur, DietType, hunger_factor
        >>> rex = Dinosaur("T-Rex", DietType.CARNIVORE, food_kg_per_day=230)
        >>> hunger_factor(rex)
        230.0
    """
    if dino.food_kg_per_day < 0:
        raise ValueError(
            f"food_kg_per_day must be non-negative, got {dino.food_kg_per_day}"
        )
    return math.sqrt(dino.food_kg_per_day**2)


def diet_summary(dinosaurs: list[Dinosaur]) -> dict[str, int]:
    """Count how many dinosaurs fall into each diet category.

    Parameters:
        dinosaurs: A list of :class:`~dinosoft.models.Dinosaur` instances.

    Returns:
        A dictionary mapping diet names (e.g. ``"herbivore"``) to counts.

    Example::

        >>> from dinosoft import load_sample_data, diet_summary
        >>> data = load_sample_data()
        >>> summary = diet_summary(data)
        >>> summary["herbivore"]
        3
    """
    counts: Counter[str] = Counter()
    for dino in dinosaurs:
        counts[dino.diet.value] += 1
    return dict(counts)


def biggest_eaters(
    dinosaurs: list[Dinosaur], n: int = 3
) -> list[Dinosaur]:
    """Return the *n* dinosaurs with the highest daily food intake.

    Parameters:
        dinosaurs: A list of :class:`~dinosoft.models.Dinosaur` instances.
        n: How many to return.  Defaults to ``3``.

    Returns:
        A list of up to *n* dinosaurs sorted by ``food_kg_per_day``
        in descending order.

    Example::

        >>> from dinosoft import load_sample_data, biggest_eaters
        >>> top = biggest_eaters(load_sample_data(), n=2)
        >>> [d.name for d in top]
        ['Brachiosaurus', 'Tyrannosaurus']
    """
    ranked = sorted(dinosaurs, key=lambda d: d.food_kg_per_day, reverse=True)
    return ranked[:n]


def filter_by_diet(
    dinosaurs: list[Dinosaur], diet: DietType
) -> list[Dinosaur]:
    """Return only those dinosaurs matching a given diet type.

    Parameters:
        dinosaurs: A list of :class:`~dinosoft.models.Dinosaur` instances.
        diet: The :class:`~dinosoft.models.DietType` to filter on.

    Returns:
        A filtered list of dinosaurs.

    Example::

        >>> from dinosoft import load_sample_data, DietType
        >>> from dinosoft.analysis import filter_by_diet
        >>> herbs = filter_by_diet(load_sample_data(), DietType.HERBIVORE)
        >>> len(herbs)
        3
    """
    return [d for d in dinosaurs if d.diet == diet]
