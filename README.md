# Learn Beyond Beginner Python

A concise collection of Python learning modules focused on intermediate topics: typing, functional patterns, recursion, and object-oriented design. This repository is intended as a hands-on learning reference — small, focused scripts you can read, run, and modify.

## Quick overview

- Purpose: Practical examples and short demonstrations to help you move beyond beginner material.
- Scope: Short, self-contained Python files. No external dependencies by default.

## Prerequisites

- Python 3.8+ recommended (3.10+ for the newest typing features).
- Optional: virtual environment for experimenting.

## Project layout (top-level files)

- `README.md` — This file.
- `python-typing.py` — Examples of type hints, generics, and typing patterns.
- `higher-order-functions.py` — Decorators, composition, and passing functions.
- `recursion.py` — Recursive examples, memoization patterns.
- `classes_tutorial.py` — OOP basics and patterns.
- `dataclass_tutorial.py` — Using `@dataclass` for concise data models.
- `class_v_dataclass.py` — Short comparisons and when to use each approach.
- `arg_checker.py` — Small utilities for validating arguments.
- `main.py` — Simple driver that demonstrates selected examples.
- `pydantic-start.py` — Starter Pydantic examples showing basic model creation and validation (optional dependency).
- `pydantic_2.py` — Additional Pydantic examples; check file headers for compatibility notes.
- `pydantic_dataclass.py` — Examples combining dataclasses and Pydantic validation.
- (Local artefacts) `.venv/`, `.mypy_cache/`, `__pycache__/` — Local environment and cache directories; typically excluded from commits.

## Getting started

1. Clone or open the repository.
2. (Optional) Create and activate a virtual environment:
   - Unix / macOS:
     ```bash
     python -m venv .venv
     source .venv/bin/activate
     ```
   - Windows (PowerShell):
     ```powershell
     python -m venv .venv
     .\.venv\Scripts\Activate.ps1
     ```

3. Run an example:
   ```bash
   python classes_tutorial.py
   ```

## Usage notes

- Files are intended to be readable and runnable as scripts. Open a file to see short demos and example output.
- Import functions into an interactive session to experiment:
  ```bash
  python -i python-typing.py
  # or
  python
  >>> from higher_order_functions import some_demo
  >>> some_demo()
  ```

## Tips for learning

- Read the code, run it, then change small parts to see effects.
- Use an editor with type-checking (mypy, Pyright) to explore typing examples.
- Step through examples with a debugger (`python -m pdb`) to follow control flow.

Happy learning — use this repository as a sandbox to practice and explore Python concepts beyond the beginner level.