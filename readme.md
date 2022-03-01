# bqsc

Checking types and column names of a data frame with the schema information for BigQuery.

## Probolem and Motivation

see [my story](https://medium.com/@hotoku/checking-types-and-column-names-of-a-data-frame-with-the-schema-information-for-bigquery-84382b2b57ff) in medium.com.

## How it works.

This package offers several functions that dynamically generate a class. An object of the class keeps information of table schema
and checks if the column names and types are valid according to the schema in execution time.
When it detects mistakes, it immediately raises an error and we can know what exactly is the mistake and where it occurs.

## Examples

### Example 1: from a list of dictionaries.
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
```

### Example 2: from a JSON file.
```python
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
```

Both examples raises an error like:

```
Traceback (most recent call last):
  File "/Users/hotoku/projects/hotoku/bqsc/examples/ex2.py", line 13, in <module>
    table.col_str = [1, 2, 3]
  File "/Users/hotoku/projects/hotoku/bqsc/bqsc/table.py", line 36, in __setattr__
    raise TypeMismatch(name, v, self._table_info.column_types[name])
bqsc.table.TypeMismatch: column: col_str, expected: <class 'str'>, given: 1 (<class 'int'>)
```

Note that:
1. it designates exact lines where the mistake exists
2. it shows how it is mistake

## todo:
- [ ] Write example usage with typehints
