import table_schema as ts

pred = ts.Prediction()
pred.exec_id = [1, 2, 3]  # => TypeMismatch exception
