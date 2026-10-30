"""Demonstration script for the MiniMart inventory system."""

from inventory import Inventory
from product import Product

SAMPLE = [
    "Milk,MLK001,1.25,12",
    "Bread,BRD002,0.90,3",
    "Eggs,EGG003,2.40,30",
    "Coffee,COF004,7.50,2",
]


def print_report(inventory):
    print("MiniMart Inventory Report")
    print("=" * 52)
    print(f"{'Name':<10}{'SKU':<9}{'Price':>8}{'Qty':>6}{'Line value':>14}")
    print("-" * 52)
    for p in inventory:
        print(
            f"{p.name:<10}{p.sku:<9}{p.price:>8.2f}"
            f"{p.quantity:>6}{p.line_value:>14.2f}"
        )
    print("-" * 52)
    print(f"{'Total inventory value:':<33}{inventory.total_value():>19.2f}")
    print()
    print("Low-stock items:")
    for p in inventory.low_stock_items():
        print(f"  - {p.name} ({p.sku}): only {p.quantity} left")
    print()
    print(f"Products created: {Product.count()}")


def main():
    inventory = Inventory.from_lines(SAMPLE)
    print_report(inventory)


if __name__ == "__main__":
    main()
