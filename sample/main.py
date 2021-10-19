import table_schema as ts

pred = ts.Prediction()
pred.exec_id = "a"

list_str = ["a", "b", "c"]
list_int = [1, 2, 3]
pred.forward_week_num = list_int

pred.product_code = list_int
