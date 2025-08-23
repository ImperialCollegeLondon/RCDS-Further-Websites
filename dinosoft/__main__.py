"""Command-line entry point for DinoSoft.

Run with::

    python -m dinosoft
"""

from dinosoft import (
    load_sample_data,
    diet_summary,
    biggest_eaters,
    hunger_factor,
)


def main() -> None:
    """Print a quick summary of the sample dinosaur dataset."""
    data = load_sample_data()

    print("=" * 50)
    print("  DinoDiet  -  Dinosaur Dietary Analysis")
    print("=" * 50)
    print()

    # Diet breakdown
    summary = diet_summary(data)
    print("Diet breakdown:")
    for diet, count in sorted(summary.items()):
        print(f"  {diet:12s}  {count}")
    print()

    # Biggest eaters
    print("Top 3 biggest eaters (kg/day):")
    for dino in biggest_eaters(data, n=3):
        hf = hunger_factor(dino)
        print(f"  {dino.name:16s}  {dino.food_kg_per_day:6.0f} kg/day  (HF={hf:.1f})")
    print()

    # Full table
    print(f"{'Species':16s} {'Diet':12s} {'Weight (kg)':>11s} {'Food (kg/d)':>11s} {'Ratio':>7s}")
    print("-" * 60)
    for dino in data:
        ratio = dino.food_ratio()
        print(
            f"{dino.name:16s} {dino.diet.value:12s} {dino.weight_kg:11,.0f} "
            f"{dino.food_kg_per_day:11,.0f} {ratio:7.4f}"
        )


if __name__ == "__main__":
    main()
