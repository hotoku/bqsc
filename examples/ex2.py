import bqsc
import pandas as pd

import json

schema_json = "./examples/schema.json"


with open(schema_json) as fp:
    MyTable = bqsc.load(fp, "MyTable")
table = MyTable()

table.col_str = [1, 2, 3]
table.col_int = [0, 1, 2]
table.col_float = [1.1, 1.2, 1.3]


df = bqsc.dataframe(table)
with open(schema_json) as fp:
    df.to_gbq(
        "table_name",
        project_id="project_id",
        table_schema=json.load(fp)
    )
