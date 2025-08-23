"""Tests for the DinoSoft package."""

from dinosoft import (
    Dinosaur,
    DietType,
    hunger_factor,
    diet_summary,
    biggest_eaters,
    load_sample_data,
)
from dinosoft.analysis import filter_by_diet


def test_load_sample_data():
    data = load_sample_data()
    assert len(data) == 7
    assert data[0].name == "Triceratops"


def test_hunger_factor():
    dino = Dinosaur("Rex", DietType.CARNIVORE, food_kg_per_day=230)
    assert hunger_factor(dino) == 230.0


def test_hunger_factor_zero():
    dino = Dinosaur("Tiny", DietType.HERBIVORE, food_kg_per_day=0)
    assert hunger_factor(dino) == 0.0


def test_diet_summary():
    data = load_sample_data()
    summary = diet_summary(data)
    assert summary["herbivore"] == 3
    assert summary["carnivore"] == 3
    assert summary["omnivore"] == 1


def test_biggest_eaters():
    data = load_sample_data()
    top = biggest_eaters(data, n=2)
    assert len(top) == 2
    assert top[0].name == "Brachiosaurus"
    assert top[1].name == "Tyrannosaurus"


def test_filter_by_diet():
    data = load_sample_data()
    herbs = filter_by_diet(data, DietType.HERBIVORE)
    assert len(herbs) == 3
    assert all(d.diet == DietType.HERBIVORE for d in herbs)


def test_food_ratio():
    dino = Dinosaur("Stego", DietType.HERBIVORE, weight_kg=3500, food_kg_per_day=70)
    assert round(dino.food_ratio(), 3) == 0.02


def test_food_ratio_zero_weight():
    dino = Dinosaur("Unknown", DietType.OMNIVORE, weight_kg=0, food_kg_per_day=10)
    assert dino.food_ratio() == 0.0
