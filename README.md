# MiniMart Inventory (OOP Assignment 1)

Author: shahad salim AL-abri
Course: Object-Oriented Programming with Python, University of Nizwa

## How to run

Requires Python 3.10+ (standard library only, no third-party packages).

    python main.py

Optional tests (bonus):

    pip install pytest
    pytest

## Files

- `product.py` - the `Product` class (properties, validation, factories, counter)
- `inventory.py` - the `Inventory` class (dictionary keyed by SKU)
- `main.py` - demonstration script that prints the inventory report
- `test_product.py` - pytest tests for validation and class tools

## Design decisions

- **Validation lives in property setters.** `__init__` assigns through
  `self.price = price`, so the same checks run when the object is created and
  when it is changed later. An invalid `Product` can never exist.
- **`bool` is rejected** for price and quantity, because `True` is technically
  an `int` in Python but is not a sensible price or quantity.
- **The product counter increases at the end of `__init__`**, so a product that
  fails validation is not counted.
- **`Inventory` stores products in a dictionary keyed by SKU** for fast lookup.
  `add` raises `ValueError` for a duplicate SKU, `find` returns `None` when the
  SKU is missing, and `remove` raises `KeyError` when the SKU is missing.
- **SKU validation uses a regular expression** (three letters followed by three
  digits) with `fullmatch`, so extra characters are rejected.
- **Per-instance data is created in `__init__`.** Only constants and the
  product counter are class attributes.

## AI assistance

I used an AI assistant to help with this assignment. I reviewed the code and
I can explain how each part works.
