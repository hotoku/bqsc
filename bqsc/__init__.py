__version__ = "2.1.1"

from .load import load as load, loads as loads, load_dir as load_dir
from .table import Table as Table, TypeMismatch as TypeMismatch, NotDefinedColumn as NotDefinedColumn
