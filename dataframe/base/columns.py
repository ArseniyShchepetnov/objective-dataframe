"""Basic column class."""
import pandas as pd


class Column:
    """Base column class."""

    def __init__(self, name: str, dtype: str):

        self._name = name
        self._dtype = dtype

    @property
    def name(self) -> str:
        """Get column name."""
        return self._name

    @property
    def dtype(self) -> str:
        """Get column data type."""
        return self._dtype

    def validate(self, series: pd.Series):
        """Validate column data."""
