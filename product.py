"""Product class for the MiniMart inventory system."""

import re


class Product:
    """A single product stocked by MiniMart."""

    LOW_STOCK_THRESHOLD = 5
    _SKU_PATTERN = re.compile(r"[A-Za-z]{3}[0-9]{3}")
    _count = 0  # class attribute: shared counter of created products

    def __init__(self, name, sku, price, quantity):
        if not isinstance(name, str) or not name.strip():
            raise ValueError("name must be a non-empty string")
        if not self.is_valid_sku(sku):
            raise ValueError(
                f"invalid SKU {sku!r}: expected 3 letters + 3 digits"
            )
        self.name = name.strip()
        self.sku = sku
        # These go through the property setters, so validation runs here.
        self.price = price
        self.quantity = quantity
        # Count only after everything is valid, so failed objects aren't counted.
        Product._count += 1

    # ---------- properties ----------
    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, value):
        # bool is a subclass of int, so reject it explicitly.
        if isinstance(value, bool) or not isinstance(value, (int, float)):
            raise TypeError("price must be a number")
        if value < 0:
            raise ValueError("price cannot be negative")
        self._price = value

    @property
    def quantity(self):
        return self._quantity

    @quantity.setter
    def quantity(self, value):
        if isinstance(value, bool) or not isinstance(value, int):
            raise TypeError("quantity must be an integer")
        if value < 0:
            raise ValueError("quantity cannot be negative")
        self._quantity = value

    @property
    def line_value(self):
        """Read-only: price x quantity."""
        return self.price * self.quantity

    @property
    def is_low_stock(self):
        """Read-only: True when quantity is below the threshold (5)."""
        return self.quantity < self.LOW_STOCK_THRESHOLD

    # ---------- class tools ----------
    @classmethod
    def from_csv_line(cls, line):
        """Build a Product from a line like 'Milk,MLK001,1.25,12'."""
        parts = [part.strip() for part in line.split(",")]
        if len(parts) != 4:
            raise ValueError(f"expected 4 comma-separated fields, got {line!r}")
        name, sku, price, quantity = parts
        return cls(name, sku, float(price), int(quantity))

    @staticmethod
    def is_valid_sku(sku):
        """True only for three letters followed by three digits (e.g. MLK001)."""
        return isinstance(sku, str) and bool(Product._SKU_PATTERN.fullmatch(sku))

    @classmethod
    def count(cls):
        """How many Product objects have been created."""
        return Product._count

    # ---------- dunder ----------
    def __repr__(self):
        return (
            f"Product({self.name!r}, {self.sku!r}, "
            f"{self.price!r}, {self.quantity!r})"
        )
