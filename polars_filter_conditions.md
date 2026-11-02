# Combined filters in Chapters 1–12

Every place in chapters 01–12 where one set of rows is kept only if it passes two conditions. Cell numbers are 0-indexed notebook cells (the first cell is cell 0). A single `.filter` with one comparison is not listed. Two `.filter` calls that each answer a different question, as in Chapter 8.2 where chocolate prices and strawberry prices are collected separately, are not listed either.

Checked on the chapter branch for each chapter: `chapter-1-to-polars`, `chapter-3-to-polars`, `chapter-1-to-4-polars` (Chapter 4), `chapter-5-polars` through `chapter-12-polars`, including the Chapter 10 and 11 helper and `datascience` copies. Chapters 1, 3, 4, 5, 9, 10, 11, and 12 have none of these.

| # | Chapter | Notebook | Cell | Code | Purpose |
|---|---------|----------|------|------|---------|
| 1 | 6.2 | [Selecting Rows](chapters/06/2/Selecting_Rows.ipynb) | 21 | `nba.filter(pl.col("POSITION") == "PG").filter(pl.col("SALARY") > 15)` | Point guards whose salary is over 15. The text says to call `filter` repeatedly for multiple features. |
| 2 | 6.2 | [Selecting Rows](chapters/06/2/Selecting_Rows.ipynb) | 36 | `nba.filter(pl.col("TEAM") != "Cleveland Cavaliers")` then `.filter(~(pl.col("SALARY") < 20))` | Players who are not Cavaliers and whose salary is at least 20. `!=` excludes the team. `~` negates `<`. |
| 3 | 6.4 | [Example: Sex Ratios](chapters/06/4/Example_Sex_Ratios.ipynb) | 18 | `us_pop_2019.filter(pl.col('SEX') == 2)` then `.filter(pl.col('AGE') != 999)` | Female rows, then drop the age-999 total. The second condition uses `!=`. |
| 4 | 6.4 | [Example: Sex Ratios](chapters/06/4/Example_Sex_Ratios.ipynb) | 19 | `us_pop_2019.filter(pl.col('SEX') == 1)` then `.filter(pl.col('AGE') != 999)` | The same two steps for male rows. |
| 5 | 7.3 | [Overlaid Graphs](chapters/07/3/Overlaid_Graphs.ipynb) | 8 | `us_pop.filter((pl.col('SEX') == 0) & (pl.col('AGE') < 19))` | Both sexes, ages 0–18, in one `filter`. The two comparisons are joined with `&`. |
| 6 | 8.3 | [Cross-Classifying by More than One Variable](chapters/08/3/Cross-Classifying_by_More_than_One_Variable.ipynb) | 23 | `full_table.filter((pl.col("Year") == "1/1/14 0:00") & (pl.col("Age") != "00 to 17"))` | California adults in 2014. `&` joins the year check and the age check. The age check uses `!=`. |

## Patterns

- **Two `.filter` calls.** Chapter 6 is the only chapter that selects rows this way. Chapter 6.2 teaches it: the second call runs on the rows kept by the first. Chapter 6.4 uses the same shape, with the second result stored under a new name. No notebook writes `&` outside `.filter`, as in `nba.filter(pl.col("POSITION") == "PG") & (pl.col("SALARY") > 15)`. That `&` would apply to the filtered DataFrame, not to the two column comparisons.
- **`&` inside one `.filter`.** Chapters 7.3 and 8.3 do this. Each comparison is in parentheses. There is no `|` joining two conditions. The `|` characters in Chapter 11.4 are part of the column name `|Number of Heads - 1000|`.
- **`~` appears once, and it is not standing in for `!=`.** In Chapter 6.2 cell 36, `~(pl.col("SALARY") < 20)` means "salary is not below 20," which is the same cut as `>= 20`. The same cell uses `!=` for "team is not the Cavaliers." Chapters 6.4 and 8.3 also use `!=` when the condition is "not this value."
