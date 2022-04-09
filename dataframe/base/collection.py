"""Columns collection base class."""
import dataclasses
from typing import Any, Dict, Generator, List

from dataframe.base.columns import Column


@dataclasses.dataclass
class ColumnsCollection:
    """Columns collection for objective dataframe."""

    def column_fields(self) -> Generator[Column, None, None]:
        """Return generator over columns."""
        for field in dataclasses.fields(self):
            if issubclass(field.type, Column):
                yield getattr(self, field.name)

    @property
    def dtypes(self) -> Dict[str, Any]:
        """Return column types dictionary."""
        return {column.name: column.dtype for column in self.column_fields()}

    @property
    def names(self) -> List[str]:
        """Return column names."""
        return [column.name for column in self.column_fields()]
