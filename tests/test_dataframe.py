"""Tests for objective dataframe wrapper class."""
from dataclasses import dataclass

import pandas as pd
from dataframe.base.collection import Column, ColumnsCollection
from dataframe.base.dataframe import ObjectiveDataFrame


def test_init():
    """Test simple columns initialization."""

    data = pd.DataFrame({
        "col_a": [1, 2, 3],
        "col_b": ["0.1", "0.2", "0.3"]
    })

    @dataclass
    class TestColumns(ColumnsCollection):
        """Test collection."""
        column_1: Column = Column("col_a", "int64")
        column_2: Column = Column("col_b", "float64")

    collection = TestColumns()
    odf = ObjectiveDataFrame(data=data, columns=collection)

    odf_dtypes = odf.data.dtypes.astype(str).to_dict()
    columns_dtypes = collection.dtypes

    for name, dtype in odf_dtypes.items():
        assert columns_dtypes[name] == dtype
