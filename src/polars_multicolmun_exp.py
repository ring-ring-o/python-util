import polars as pl

df = pl.DataFrame(
    {
        "name": ["foo", "bar", "piyo", "fuga"],
        "value": ["1", "value2", "3", "4"],
        "enable": [True, False, False, False],
    }
)
print("原型")
print(df)

updated = df.with_columns(
    pl.when(pl.col("name") == "piyo")
    .then(pl.lit(True))
    .otherwise(pl.lit(False))
    .alias("enable")
)
print(f"""
条件に当てはまる行を条件分岐に使ったカラムとは別のカラムに対して値の更新.
指定した行のみTrueに変更
{updated}
""")


updated = df.with_columns(
    pl.when(pl.col("name") == "bar")
    .then(pl.lit("2"))
    .otherwise(pl.col("value"))
    .alias("value")
)
print(f"""
条件に当てはまる行を条件分岐に使ったカラムとは別のカラムに対して値の更新.
指定した行以外は変更しない.
{updated}
""")
