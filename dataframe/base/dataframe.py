"""Objective dataframe wrapper."""
from typing import Generic, TypeVar

import pandas as pd

from dataframe.base.collection import ColumnsCollection

ColumnsType = TypeVar("ColumnsType",  # pylint: disable=invalid-name
                      bound=ColumnsCollection)


class ObjectiveDataFrame(Generic[ColumnsType]):
    """Objective datafrmae wrapper around `pandas.DataFrame`"""

    def __init__(self,
                 data: pd.DataFrame,
                 columns: ColumnsType):

        self._columns = columns
        self._data: pd.DataFrame = None
        self.set_data(data)

    @property
    def data(self) -> pd.DataFrame:
        """Get dataframe."""
        return self._data

    @property
    def columns(self) -> ColumnsType:
        """Get columns collection."""
        return self._columns

    @property
    def c(self) -> ColumnsType:  # pylint: disable=invalid-name
        """Get columns collection shortcut."""
        return self._columns

    def set_data(self, data: pd.DataFrame):
        """Set data to the wrapper."""
        data = self._set_dtypes(data)
        self.validate_columns(data)
        self.validate(data)
        self._data = data

    def validate(self, data: pd.DataFrame):
        """DataFrame data validation."""

    def validate_columns(self, data: pd.DataFrame):
        """DataFrame data validation with columns."""
        for column in self.c.column_fields():
            column.validate(data[column.name])

    def _set_dtypes(self, data: pd.DataFrame) -> pd.DataFrame:
        """Set columns data types."""
        return data.astype(self.c.dtypes)
