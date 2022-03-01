# bqsc

Checking types and column names of a data frame with the schema information for BigQuery.

## Probolem and Motivation

see [my story](https://medium.com/@hotoku/checking-types-and-column-names-of-a-data-frame-with-the-schema-information-for-bigquery-84382b2b57ff) in medium.com.

## How it works.

This package offers several functions that dynamically generate a class. An object of the class keeps information of table schema
and checks if the column names and types are valid according to the schema in execution time.
When it detects mistakes, it immediately raises an error and we can know what exactly is the mistake and where it occurs.

## Example 1: from a list of dictionaries.
`from_schema` function generates cheker

```python
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

MyTable = bqsc.from_schema(schema, "MyTable") # the 2nd argument is name of the generted class.
table = MyTable()

table.col_str = ["a", "b", "c"]
table.col_int = [0, 1, 2]
table.col_float = [1.1, 1.2, 1.3]

df = bqsc.dataframe(table)
df.to_gbq(
    "table_name",
    project_id="project_id",
    table_schema=schema
)
```

## Example 2: from a JSON file.
```
import bqsc
import pandas as pd

import json

schema_json = "./examples/schema.json"

with open(schema_json) as fp:
    MyTable = bqsc.load(fp, "MyTable")
table = MyTable()

table.col_str = ["a", "b", "c"]
table.col_int = [0, 1, 2]
table.col_float = [1.1, 1.2, 1.3]

df = bqsc.dataframe(table)
with open(schema_json) as fp:
    df.to_gbq(
        "table_name",
        project_id="project_id",
        table_schema=json.load(fp)
    )
```

## todo:
- [ ] Write example usage with typehints
