import bqsc
import pandas as pd

schema = [
    {
        "name": "col_str",
        "type": "string"
    },
    {
        "name": "col_int",
        "type": "int64"
    },
    {
        "name": "col_float",
        "type": "float64"
    }
]

MyTable = bqsc.from_schema(schema, "MyTable")
table = MyTable()

table.col_str = [1, 2, 3]
table.col_int = [0, 1, 2]
table.col_float = [1.1, 1.2, 1.3]


df = bqsc.dataframe(table)
df.to_gbq(
    "table_name",
    project_id="project_id",
    table_schema=schema
)
