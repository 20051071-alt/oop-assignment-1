"""Inventory class for the MiniMart inventory system."""

from product import Product


class Inventory:
    """Stores products in a dictionary keyed by SKU."""

    def __init__(self):
        self._products = {}  # per-instance data, created in __init__

    def add(self, product):
        if not isinstance(product, Product):
            raise TypeError("only Product objects can be added")
        if product.sku in self._products:
            raise ValueError(f"SKU {product.sku} already exists")
        self._products[product.sku] = product

    def remove(self, sku):
        """Remove and return the product; raises KeyError if missing."""
        try:
            return self._products.pop(sku)
        except KeyError:
            raise KeyError(f"no product with SKU {sku!r}") from None

    def find(self, sku):
        """Return the product, or None if the SKU is not stocked."""
        return self._products.get(sku)

    def total_value(self):
        return sum(p.line_value for p in self._products.values())

    def low_stock_items(self):
        return [p for p in self._products.values() if p.is_low_stock]

    @classmethod
    def from_lines(cls, lines):
        """Build a complete Inventory from a list of CSV lines."""
        inventory = cls()
        for line in lines:
            inventory.add(Product.from_csv_line(line))
        return inventory

    def __iter__(self):
        return iter(self._products.values())

    def __len__(self):
        return len(self._products)
