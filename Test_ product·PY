import pytest

from inventory import Inventory
from product import Product


def make(**overrides):
    args = dict(name="Milk", sku="MLK001", price=1.25, quantity=12)
    args.update(overrides)
    return Product(**args)


def test_negative_price_raises_value_error():
    with pytest.raises(ValueError):
        make(price=-1)


def test_non_number_price_raises_type_error():
    with pytest.raises(TypeError):
        make(price="cheap")


def test_negative_quantity_raises_value_error():
    with pytest.raises(ValueError):
        make(quantity=-3)


def test_float_quantity_raises_type_error():
    with pytest.raises(TypeError):
        make(quantity=2.5)


def test_setter_validates_after_creation():
    p = make()
    with pytest.raises(ValueError):
        p.price = -5


def test_line_value_and_low_stock():
    p = make(price=2.0, quantity=3)
    assert p.line_value == 6.0
    assert p.is_low_stock is True
    assert make(quantity=5).is_low_stock is False


def test_computed_properties_are_read_only():
    p = make()
    with pytest.raises(AttributeError):
        p.line_value = 10
    with pytest.raises(AttributeError):
        p.is_low_stock = True


def test_is_valid_sku():
    assert Product.is_valid_sku("MLK001")
    assert not Product.is_valid_sku("ML001")
    assert not Product.is_valid_sku("MLK0011")
    assert not Product.is_valid_sku("123ABC")
    assert not Product.is_valid_sku(None)


def test_invalid_sku_blocks_creation():
    with pytest.raises(ValueError):
        make(sku="BAD")


def test_from_csv_line():
    p = Product.from_csv_line("Milk,MLK001,1.25,12")
    assert repr(p) == "Product('Milk', 'MLK001', 1.25, 12)"


def test_count_ignores_failed_creations():
    before = Product.count()
    make()
    with pytest.raises(ValueError):
        make(price=-1)
    assert Product.count() == before + 1


def test_inventory_from_lines_and_total():
    inv = Inventory.from_lines(["Milk,MLK001,1.25,12", "Eggs,EGG003,2.40,30"])
    assert len(inv) == 2
    assert inv.total_value() == pytest.approx(87.0)
    assert inv.find("NOPE00") is None
    inv.remove("MLK001")
    assert len(inv) == 1
