"""DinoSoft - Analyse the dietary habits of dinosaurs.

A small Python library for loading, analysing, and visualising
dinosaur dietary data from the late Cretaceous period.
"""

from dinosoft.models import Dinosaur, DietType
from dinosoft.analysis import hunger_factor, diet_summary, biggest_eaters
from dinosoft.data import load_sample_data

__version__ = "0.5.0"
__all__ = [
    "Dinosaur",
    "DietType",
    "hunger_factor",
    "diet_summary",
    "biggest_eaters",
    "load_sample_data",
]
