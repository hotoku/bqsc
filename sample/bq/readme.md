# サンプル


## 手順


#### **1** テーブル名から、スキーマを作る


```python
import bqsc


GithubTimeline = bqsc.load_bq(
    "bigquery-public-data",
    "samples",
    "github_timeline"
)
```


`bqsc.load_bq`に、プロジェクト名・データセット名・テーブル名を渡すとテーブルクラスを作成します。


#### **2** テーブル名から、型アノテーションを作成する


```shell
$ bqsc bq bigquery-public-data:samples.github_timeline > table_schema.py
```


`bqsc bq`コマンドに、 `プロジェクト名:データセット名.テーブル名`を渡すと、型アノテーション文字列を表示するので、適当なファイルに保存します。


#### **3** 型のサポートを受けながらコードを書く


```python
from table_schema import GithubTimeline


gt = GithubTimeline()


gt.actor = "actor"
gt.actor_attributes_blog = 1  # raise TypeMismatch
```


クラスを定義したファイルをインポートして利用します。
IDEが、補完や型チェックでサポートしてくれます。
