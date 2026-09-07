# Python Module 06: Modules, Packages & Imports

Welcome to **Python Module 06** of the 42 Tokyo Python curriculum. This module delves into Python's module and packaging system, exploring namespace resolution, relative vs. absolute imports, package hierarchies, and circular dependencies through an alchemical theme.

## 🎯 Objectives

- Understand Python's import mechanics (`import`, `from ... import ...`, `as` aliases).
- Create package structures using directories and `__init__.py` files.
- Differentiate between absolute and relative imports (`.`, `..`).
- Control namespace exports via `__all__`.
- Diagnose, manage, and prevent circular dependency issues (`ft_kaboom`).
- Build layered multi-tier packages (`alchemy`, `alchemy.grimoire`, `alchemy.transmutation`).

---

## 📁 Package & Directory Structure

```text
python_module06/
├── elements.py
├── ft_alembic_0.py ... ft_alembic_5.py
├── ft_distillation_0.py, ft_distillation_1.py
├── ft_kaboom_0.py, ft_kaboom_1.py
├── ft_transmutation_0.py ... ft_transmutation_2.py
└── alchemy/
    ├── __init__.py
    ├── elements.py
    ├── potions.py
    ├── grimoire/
    │   ├── __init__.py
    │   ├── dark_spellbook.py
    │   ├── dark_validator.py
    │   ├── light_spellbook.py
    │   └── light_validator.py
    └── transmutation/
        ├── __init__.py
        └── recipes.py
```

---

## 🧪 Exercise Series

| Series              | Files                                             | Focus                                                                         |
| :------------------ | :------------------------------------------------ | :---------------------------------------------------------------------------- |
| **Alembic**         | `ft_alembic_0.py` – `ft_alembic_5.py`             | Exploring different import syntaxes, module attributes, and namespace scopes. |
| **Distillation**    | `ft_distillation_0.py` – `ft_distillation_1.py`   | Granular symbol imports and module renaming/aliasing.                         |
| **Kaboom**          | `ft_kaboom_0.py` – `ft_kaboom_1.py`               | Observing circular imports and techniques to avoid them.                      |
| **Transmutation**   | `ft_transmutation_0.py` – `ft_transmutation_2.py` | Package-level imports and accessing submodules across packages.               |
| **Alchemy Package** | `alchemy/` package tree                           | Structured library with modular subpackages (`grimoire`, `transmutation`).    |

---

## 🚀 How to Run

Execute the runner scripts from the module root directory:

```bash
python ft_alembic_0.py
python ft_kaboom_0.py
python ft_transmutation_0.py
```
