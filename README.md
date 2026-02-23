<!--DinoDiet Readme starts below-->

# DinoDiet

**Principal Investigator:** Dr. Geller[^1]

## Project Description

This project[^1] aims to analyse the dietary habits of dinosaurs during 
the late Cretaceous period. We will be focusing on the differences
between herbivorous and carnivorous dinosaurs.

> [!NOTE]
> The project will include data collection, analysis, and visualisation of the findings.

## Sections

- [Data Collection](#data-collection)
- [Data Analysis](#data-analysis)
- [Data Visualisation](#data-visualisation)
- [Conclusion](#conclusion)

A simple plan for progressing through the technical stages of the project
is shown below:

```mermaid
flowchart LR
  Collection --> Analysis --> Visualisation
                 Analysis --> Conclusion
```

### Data Collection

We will be gathering data from various sources, including fossil records,
scientific literature, and online databases. We've listed some key sources
below, check them out!

1. [Paleobiology Database](https://paleobiodb.org)
2. [The Fossil Forum](https://www.thefossilforum.com/)
4. [Research articles from the Journal of Vertebrate Paleontology](https://www.tandfonline.com/toc/ujvp20/current)

### Data Analysis

The data will be analysed using statistical methods to identify patterns
and trends in the dietary habits of dinosaurs. We will be comparing the
diets of herbivorous and carnivorous dinosaurs to understand their food
preferences and ecological roles.

We will be using Python for our data analysis. Here is a sample
of how we will load the library in Python:

```python
import dinosoft # Load the necessary lib
```

### Data Visualisation

We will create graphs and charts to visualise the findings from our analysis.
This will help us better understand the relationships between different dinosaur
species and their diets. For instance, we will include visualisations such as pie
charts for proportions of herbivorous and carnivorous dinosaurs, and bar graphs
for the comparison of average body sizes.

> [!WARNING]
> Dinosaur images may be frightening.

An example of a dinosaur image we will use for reference in our
visualisations can be found below:

![Public Domain Dinosaur Image](https://www.publicdomainpictures.net/pictures/10000/nahled/dinosaur-background-20851282041923qTUN.jpg)

### Conclusion

The goal of this project is to gain a deeper understanding of the dietary habits
of dinosaurs during the late Cretaceous period. The findings from this research
could provide insights into the evolution and ecology of these fascinating creatures
and potentially reveal new information about their extinction event.

<details>
  
  <summary>Further Info</summary>

For more information about dinosaurs and their diet, visit the American Museum of
Natural History's website at https://www.amnh.org/
</details>
  
## Contributor Reference

### Hunger Factor :chart_with_upwards_trend:

Hunger Factor

The Hunger Factor (HF) is an important metric in our work. We calculate it
with the following equation:

$HF = \sqrt(Food Eaten^2)$

### DinoSoft Bugs :bug:

When calculating large HF scores for dinosaurs, the DinoSoft software may crash.
Please reboot your machine with <kbd>Ctrl</kbd> + <kbd>Alt</kbd> + <kbd>Delete</kbd>.

### Dino Diets :t-rex:

DinoSoft

You can find the documentation for the DinoSoft software at dinosoft/README.md

Dino Diets

For reference, here is a summary of the diets and primary food sources
of some well-known dinosaur species:

| Dinosaur Species | Diet      | Primary Food Sources |
|------------------|-----------|-------------------------------|
| Triceratops      | Herbivore | Ferns, cycads, and horsetails |
| Tyrannosaurus    | Carnivore | Triceratops, Edmontosaurus |
| Stegosaurus      | Herbivore | Ferns, mosses, and cycads |
| Velociraptor     | Carnivore | Small herbivorous dinosaurs |
| Brachiosaurus    | Herbivore | High tree foliage, such as conifers |
| Spinosaurus      | Carnivore | Fish, small to medium-sized dinosaurs |
| Oviraptor        | Omnivore  | Eggs, plants, small animals |

More widely, we estimate the following distribution of dinosaur diets:

```mermaid
pie title Dino Diet Distribution
    "Herbivore" : 65
    "Carnivore" : 25
    "Omnivore" : 10
```

## Roadmap

To track the progress of the project, we will be using this roadmap:

- [ ] Data Collection
  - [X] Collect data from fossil records
  - [ ] Collect data from scientific literature
  - [X] Collect data from online databases
- [ ] Data Analysis
  - [ ] Clean and preprocess the data
  - [ ] Perform statistical analysis
  - [ ] Identify patterns and trends
- [ ] Data Visualisation
  - [ ] Create graphs and charts
  - [ ] Integrate visualisations in the report
- [ ] Conclusion
  - [ ] Summarise findings
  - [ ] Discuss implications for dinosaur evolution and ecology
  - [ ] Suggest future research directions


[^1]: This is a fictional research project undertaken by a fictional principal investigator. For educational purposes only.
