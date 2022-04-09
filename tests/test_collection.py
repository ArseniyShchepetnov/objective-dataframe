"""Tests for columns collections."""
from dataclasses import dataclass

from dataframe.base.collection import Column, ColumnsCollection


def test_properties():
    """Test properties after column collection creation."""

    @dataclass
    class TestColumns(ColumnsCollection):
        """Test collection."""
        column_1: Column = Column("col_a", "int64")
        column_2: Column = Column("col_b", "float64")

    collection = TestColumns()

    assert set(collection.names) == {"col_a", "col_b"}

    dtypes = collection.dtypes
    assert dtypes["col_a"] == "int64"
    assert dtypes["col_b"] == "float64"
