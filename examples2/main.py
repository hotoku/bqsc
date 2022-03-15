import bqsc

from . import schemas

my_table = schemas.MyTable()
my_table.col_int = [1, 2, 3]
my_table.col_float = [4.0, 5.0, 6.0]
my_table.col_str = ["a", "b", "c"]

df = bqsc.dataframe(my_table)
