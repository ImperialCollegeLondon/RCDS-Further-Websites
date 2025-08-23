---
title: Templates
description: Starter projects and production-ready patterns for DinoSoft
icon: material/package-variant
---

# :material-package-variant: Templates

Templates are fully functional project structures you can use as a
starting point for your own dinosaur dietary analysis, or as reference
material for best practices.

---

## Project structure

The recommended project layout when using DinoSoft:

```
my-dino-project/
├── .devcontainer/
│   └── devcontainer.json       # (1)!
├── dinosoft/
│   ├── __init__.py
│   ├── __main__.py
│   ├── models.py
│   ├── analysis.py
│   └── data.py
├── tests/
│   └── test_dinosoft.py        # (2)!
├── docs/                       # (3)!
│   ├── index.md
│   ├── quickstart.md
│   ├── tutorial.md
│   ├── how-to.md
│   ├── explanation.md
│   ├── examples.md
│   ├── templates.md
│   └── reference/
│       └── api.md
├── mkdocs.yml                  # (4)!
├── pyproject.toml
├── README.md
└── LICENSE
```

1. Pre-configures Codespaces to install all dependencies automatically.
2. Eight tests covering all public functions and edge cases.
3. This documentation site, following the seven-section model.
4. MkDocs Material configuration with tabs, search, code annotations, and more.

---

## Starter `mkdocs.yml`

A minimal but feature-rich configuration to get started:

```yaml title="mkdocs.yml"
site_name: My DinoSoft Project
theme:
  name: material
  palette:
    - scheme: default
      primary: green
      toggle:
        icon: material/brightness-7
        name: Switch to dark mode
    - scheme: slate
      primary: green
      toggle:
        icon: material/brightness-4
        name: Switch to light mode
  features:
    - navigation.tabs           # (1)!
    - navigation.top
    - content.code.copy         # (2)!
    - content.code.annotate     # (3)!
    - search.suggest

markdown_extensions:
  - admonition                  # (4)!
  - pymdownx.details
  - pymdownx.superfences:       # (5)!
      custom_fences:
        - name: mermaid
          class: mermaid
          format: !!python/name:pymdownx.superfences.fence_mermaid
  - pymdownx.highlight:
      anchor_linenums: true
  - pymdownx.tabbed:            # (6)!
      alternate_style: true
  - pymdownx.tasklist:
      custom_checkbox: true
  - tables
  - footnotes
  - attr_list
  - pymdownx.emoji:
      emoji_index: !!python/name:material.extensions.emoji.twemoji
      emoji_generator: !!python/name:material.extensions.emoji.to_svg
```

1. Renders top-level nav sections as tabs across the header.
2. Adds a copy button to every code block.
3. Enables `(1)!` style numbered annotations inside code blocks.
4. Enables callout boxes: `!!! note`, `!!! warning`, `!!! tip`, etc.
5. Enables fenced code blocks and Mermaid diagrams.
6. Enables `=== "Tab 1"` / `=== "Tab 2"` content tabs.

---

## GitHub Actions workflow

Automatically build and deploy your docs on every push to `main`:

```yaml title=".github/workflows/docs.yml"
name: Deploy docs

on:
  push:
    branches: [main]

permissions:
  contents: write

jobs:
  deploy:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4

      - uses: actions/setup-python@v5
        with:
          python-version: '3.12'

      - run: pip install mkdocs-material  # (1)!

      - run: mkdocs gh-deploy --force     # (2)!
```

1. Installs MkDocs Material and all its dependencies.
2. Builds the site and pushes it to the `gh-pages` branch.

!!! warning "Repository settings required"

    You must enable GitHub Pages in your repository settings and set the
    **Source** to **GitHub Actions**. See the appendix in the course slides
    for step-by-step instructions.

---

## Devcontainer template

For GitHub Codespaces, this `devcontainer.json` pre-installs everything:

```json title=".devcontainer/devcontainer.json"
{
    "name": "DinoSoft Docs",
    "image": "mcr.microsoft.com/devcontainers/python:3.12",
    "postCreateCommand": "pip install mkdocs-material && pip install -e '.[dev]'",
    "forwardPorts": [8000],
    "customizations": {
        "vscode": {
            "extensions": [
                "yzhang.markdown-all-in-one",
                "DavidAnson.vscode-markdownlint"
            ]
        }
    }
}
```

After the Codespace loads, you can immediately run:

=== "Preview docs"

    ```bash
    mkdocs serve
    ```

=== "Run the software"

    ```bash
    python -m dinosoft
    ```

=== "Run the tests"

    ```bash
    python -m pytest tests/ -v
    ```

---

## Checklist for your own project

Use this checklist when setting up documentation for your own software
project:

- [x] Create a `docs/` directory with an `index.md`
- [x] Write a `mkdocs.yml` with Material theme configured
- [x] Add a **Quickstart** — minimal steps to get running
- [x] Add a **Tutorial** — guided learning experience
- [x] Add **How-to Guides** — task-oriented problem solving
- [x] Add an **Explanation** page — concepts and design decisions
- [x] Add an **API Reference** — exhaustive technical details
- [x] Add **Examples** — copy-pasteable single-feature snippets
- [x] Set up CI/CD with GitHub Actions for automatic deployment
- [ ] Add a changelog
- [ ] Add a contributing guide
- [ ] Set up versioning for your docs
