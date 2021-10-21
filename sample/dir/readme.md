# サンプル


## 手順


#### **1** スキーマjsonから、クラス定義を生成する


```python
import bqsc


globals().update(bqsc.load_dir("./table_schema"))
```


`bqsc.load_dir`に、スキーマjsonが入っているディレクトリを渡すと、各スキーマを表現したクラスを作ってくれる。
そのクラスを、`globals()`に代入して、モジュールに登録する。


#### **2** スキーマjsonから、型アノテーションを生成する


```shell
$ bqsc dir table_scheam > table_schema.pyi
```


`bqsc dir`コマンドに、スキーマjsonが入っているディレクトリを渡すと、型定義を吐き出してくれるので、`.pyi`ファイルとして保存する。


#### **3** 型のサポートを受けながらコードを書く


```python
import table_schema as ts


pred = ts.Prediction()
pred.exec_id = [1, 2, 3]  # => TypeMismatch exception
```


クラスを定義したファイルをインポートして利用する。
列名の補完や、型の間違いをLSPなどが指摘してくれるようになる。
また、型が間違っていると、実行時にエラーになる。
