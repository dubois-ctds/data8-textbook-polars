# Building a DataFrame from Series in Chapters 1–12

Every place in chapters 01–12 where a DataFrame is built from columns, or a column is added with `with_columns(pl.Series(...))`. Cell numbers are 0-indexed notebook cells (the first cell is cell 0). A later `with_columns` that only renames or computes with `pl.col` is not listed.

Checked against the live notebooks in `chapters/01`–`12` on 2026-11-24 (after the NumPy-array pass and the `make_array` pass). Chapters 3, 4, and 5 have none of these.

`pl.DataFrame().with_columns(pl.Series(...))` does not appear. An empty `pl.DataFrame()` is shown once, and it is not given a column that way.

| # | Chapter | Notebook | Cell | Code | Purpose |
|---|---------|----------|------|------|---------|
| 1 | 1.3.1 | [Literary Characters](chapters/01/3/1/Literary_Characters.ipynb) | 4 | `pl.DataFrame([huck_finn.str.count_matches(...).alias("Jim"), ...])` | One column per name, each a cumulative count. The next line adds Chapter with `with_columns`. |
| 2 | 1.3.1 | [Literary Characters](chapters/01/3/1/Literary_Characters.ipynb) | 4 | `counts.with_columns(pl.Series("Chapter", np.arange(1, 44)))` | Adds the chapter numbers to the frame from row 1. Not an empty `DataFrame()`. |
| 3 | 1.3.1 | [Literary Characters](chapters/01/3/1/Literary_Characters.ipynb) | 7 | `pl.DataFrame([pl.Series("Chapters", little_women_chapters)])` | One column, the text of each chapter. |
| 4 | 1.3.1 | [Literary Characters](chapters/01/3/1/Literary_Characters.ipynb) | 9 | `pl.DataFrame([little_women.str.count_matches(...).alias("Amy"), ...])` | Same cumulative-count frame for Little Women. |
| 5 | 1.3.1 | [Literary Characters](chapters/01/3/1/Literary_Characters.ipynb) | 9 | `counts.with_columns(pl.Series("Chapter", np.arange(1, 48)))` | Adds chapter numbers, same as row 2. |
| 6 | 1.3.2 | [Another Kind of Character](chapters/01/3/2/Another_Kind_Of_Character.ipynb) | 4 | `pl.DataFrame([huck_finn.str.len_chars().alias("Huck Finn Chapter Length"), huck_finn.str.count_matches(".", literal=True).alias("Number of Periods")])` | Two columns: chapter length and period count. The Little Women frame in the same cell is built the same way. |
| 7 | 1.3 | [Plotting the Classics](chapters/01/3/Plotting_the_Classics.ipynb) | 5 | `pl.DataFrame([pl.Series("Chapters", huck_finn_chapters)])` | One column, the text of each chapter. |
| 8 | 6 | [Tables](chapters/06/Tables.ipynb) | 3 | `pl.DataFrame()` | An empty table, shown by itself. No column is added. |
| 9 | 6 | [Tables](chapters/06/Tables.ipynb) | 5 | `pl.DataFrame([pl.Series("Number of petals", make_array(8, 34, 5))])` | A one-column table. |
| 10 | 6 | [Tables](chapters/06/Tables.ipynb) | 7 | `pl.DataFrame([pl.Series("Number of petals", ...), pl.Series("Name", ...)])` | Two columns, passed together in the list. |
| 11 | 6 | [Tables](chapters/06/Tables.ipynb) | 9 | `flowers = pl.DataFrame([pl.Series("Number of petals", ...), pl.Series("Name", ...)])` | Same two columns, stored as `flowers`. |
| 12 | 6 | [Tables](chapters/06/Tables.ipynb) | 9 | `flowers.with_columns(pl.Series("Color", make_array("pink", "yellow", "red")))` | Adds Color to the existing table. |
| 13 | 6.4 | [Example: Sex Ratios](chapters/06/4/Example_Sex_Ratios.ipynb) | 24 | `pl.DataFrame([females.get_column('AGE'), (females.get_column('2019') / males.get_column('2019')).alias('2019 F:M RATIO')])` | Age and the female-to-male ratio, as two columns of a new frame. |
| 14 | 7.1 | [Visualizing Categorical Distributions](chapters/07/1/Visualizing_Categorical_Distributions.ipynb) | 3 | `pl.DataFrame([pl.Series('Flavor', ...), pl.Series('Number of Cartons', ...)])` | The ice cream table used for the bar charts. |
| 15 | 7.2 | [Visualizing Numerical Distributions](chapters/07/2/Visualizing_Numerical_Distributions.ipynb) | 1 | `pl.DataFrame([pl.Series('bin', edges), pl.Series(column + ' count', np.append(counts, 0))])` | Inside `bin_column`: bin edges and counts. |
| 16 | 8.1 | [Applying a Function to a Column](chapters/08/1/Applying_a_Function_to_a_Column.ipynb) | 8 | `pl.DataFrame([pl.Series("Person", ...), pl.Series("Age", ...)])` | The small ages table. |
| 17 | 8.1 | [Applying a Function to a Column](chapters/08/1/Applying_a_Function_to_a_Column.ipynb) | 23 | `pl.DataFrame([parent_averages.alias("Parent Average"), family_heights.get_column("childHeight").alias("Child")])` | Parent average and child height. |
| 18 | 8.2 | [Classifying by One Variable](chapters/08/2/Classifying_by_One_Variable.ipynb) | 3 | `pl.DataFrame([pl.Series("Flavor", ...), pl.Series("Price", ...)])` | The cones table. |
| 19 | 8.2 | [Classifying by One Variable](chapters/08/2/Classifying_by_One_Variable.ipynb) | 12 | `pl.DataFrame([pl.Series("Flavor", ...), pl.Series("Array of All the Prices", ...)])` | One row per flavor, with the list of prices. |
| 20 | 8.2 | [Classifying by One Variable](chapters/08/2/Classifying_by_One_Variable.ipynb) | 12 | `grouped_cones.with_columns(pl.Series("Sum of the Array", make_array(sum(cones_choc), sum(cones_strawb))))` | Adds the sum of each price list. |
| 21 | 8.2 | [Classifying by One Variable](chapters/08/2/Classifying_by_One_Variable.ipynb) | 16 | `grouped_cones.with_columns(pl.Series("Max of the Array", ...))` | Adds the max of each price list. |
| 22 | 8.2 | [Classifying by One Variable](chapters/08/2/Classifying_by_One_Variable.ipynb) | 18 | `grouped_cones.with_columns(pl.Series("Length of the Array", ...))` | Adds the length of each price list. |
| 23 | 8.3 | [Cross-Classifying by More than One Variable](chapters/08/3/Cross-Classifying_by_More_than_One_Variable.ipynb) | 3 | `pl.DataFrame([pl.Series("Flavor", ...), pl.Series("Color", ...), pl.Series("Price", ...)])` | The three-column cones table. |
| 24 | 8.4 | [Joining Tables by Columns](chapters/08/4/Joining_Tables_by_Columns.ipynb) | 3 | `pl.DataFrame([pl.Series("Flavor", ...), pl.Series("Price", ...)])` | Cones. |
| 25 | 8.4 | [Joining Tables by Columns](chapters/08/4/Joining_Tables_by_Columns.ipynb) | 4 | `pl.DataFrame([pl.Series("Kind", ...), pl.Series("Stars", ...)])` | Ratings. |
| 26 | 8.4 | [Joining Tables by Columns](chapters/08/4/Joining_Tables_by_Columns.ipynb) | 13 | `pl.DataFrame([pl.Series("Flavor", ...), pl.Series("Stars", ...)])` | Reviews. |
| 27 | 8.5 | [Bike Sharing in the Bay Area](chapters/08/5/Bike_Sharing_in_the_Bay_Area.ipynb) | 22 | `cities.with_columns(pl.Series("color", make_array("blue", "red", "green", "orange", "purple")))` | Adds a map color to the existing cities table. |
| 28 | 9.2 | [Iteration](chapters/09/2/Iteration.ipynb) | 29 | `pl.DataFrame([pl.Series("Outcome", outcomes)])` | One column of bet outcomes, for the bar chart. `outcomes` is a NumPy array until this point. |
| 29 | 9.3 | [Simulation](chapters/09/3/Simulation.ipynb) | 17 | `pl.DataFrame([pl.Series("Repetition", np.arange(1, num_repetitions + 1)), pl.Series("Number of Heads", heads)])` | Repetition number and heads count. |
| 30 | 9.3 | [Simulation](chapters/09/3/Simulation.ipynb) | 28 | `pl.DataFrame([pl.Series("Repetition", np.arange(1, num_repetitions + 1)), pl.Series("Sum of Two Rolls", moves)])` | Repetition number and the sum of two dice. |
| 31 | 9.5 | [Finding Probabilities](chapters/09/5/Finding_Probabilities.ipynb) | 12 | `pl.DataFrame([pl.Series("Rolls", rolls), pl.Series("Chance of at least one 6", 1 - (5/6)**rolls)])` | Rolls and the chance of at least one 6. `rolls = np.arange(1, 51, 1)`. |
| 32 | 10.1 | [Empirical Distributions](chapters/10/1/Empirical_Distributions.ipynb) | 2 | `pl.DataFrame([pl.Series("Face", np.arange(1, 7, 1))])` | The six faces of a die. |
| 33 | 10.3 | [Empirical Distribution of a Statistic](chapters/10/3/Empirical_Distribution_of_a_Statistic.ipynb) | 24 | `pl.DataFrame([pl.Series("Sample Median", medians)])` | The simulated sample medians. `medians` is a NumPy array until this point. |
| 34 | 10.4 | [Random Sampling in Python](chapters/10/4/Random_Sampling_in_Python.ipynb) | 2 | `pl.DataFrame([pl.Series("Face", faces)])` | The die again. `faces = np.arange(1, 7)` stays a NumPy array for `np.random.choice(faces, 7)`. |
| 35 | 11.2 | [Multiple Categories](chapters/11/2/Multiple_Categories.ipynb) | 4 | `pl.DataFrame([pl.Series("Ethnicity", ...), pl.Series("Eligible", ...), pl.Series("Panels", ...)])` | The jury table. |
| 36 | 11.2 | [Multiple Categories](chapters/11/2/Multiple_Categories.ipynb) | 8 | `jury.with_columns(sample_distribution)` | Adds the random-sample column. `sample_distribution = pl.Series("Random Sample", sample_proportions(...))` on the previous line. |
| 37 | 11.4 | [Error Probabilities](chapters/11/4/Error_Probabilities.ipynb) | 4 | `pl.DataFrame([pl.Series("\|Number of Heads - 1000\|", statistics)])` | One column of simulated statistics. |
| 38 | 10 | [Sampling and Empirical Distributions](chapters/10/Sampling_and_Empirical_Distributions.ipynb) | 2 | `top1.with_columns(pl.Series("Row Index", np.arange(top1.height)))` | Adds a row-index column. `np.arange`, not `range` or eager `pl.int_range`. |
| 39 | 12.1 | [A/B Testing](chapters/12/1/AB_Testing.ipynb) | 36 | `pl.DataFrame([pl.Series("Difference Between Group Means", differences)])` | The simulated differences (a NumPy array) as one column, for the histogram. |
| 40 | 12.3 | [Deflategate](chapters/12/3/Deflategate.ipynb) | 9 | `drop = pl.Series("Pressure Drop", start) - football.get_column("Combined")`, then `football.with_columns(drop)` | `start` is a NumPy array built with `np.ones` and `np.append`; it is wrapped when it joins the frame. |

## Patterns

- **Literal values → `pl.Series("name", make_array(v1, v2, ...))`; an existing NumPy array → `pl.Series("name", array)`.** Chapters 6, 7.1, 8, and 11.2 build tables from values written out by hand, each column a `make_array(...)`, never a Python list. The one exception is Chapter 8.2's `Array of All the Prices`, a column whose cells are lists. Chapters 1.3.1, 9, 10, 11.4, and 12 wrap a NumPy array (`np.arange`, a simulation collection) at the moment it joins a frame. Before that point the array stays NumPy; it is never `.alias`-ed or wrapped early.
- **A new table is `pl.DataFrame([pl.Series(...), ...])`.** Every new table in this list is built that way. A column can be a `pl.Series`, a Series that already has a name, or an expression with `.alias`. Chapter 6 teaches this in order: an empty table, a one-column table, then a two-column table.
- **`with_columns(pl.Series(...))` adds a column to a table that already has rows.** Chapter 1.3.1 uses it for the Chapter column. Chapter 6 uses it for Color. Chapter 8.2 uses it for the sum, max, and length. Chapter 8.5 uses it for the map color. Chapter 11.2 uses it for the sample column. None of these start from `pl.DataFrame()`.
- **`pl.DataFrame().with_columns(pl.Series(...))` is not used.** The empty call in Chapter 6 cell 3 stands alone.
- **An empty table that will grow is given a schema, not `with_columns`.** Chapter 9.4 starts `games` with `pl.DataFrame(schema={...})` and appends rows with `pl.concat`.
- **A one-column frame for a chart is also a list of Series.** The histogram helpers in Chapters 11 and 12 use `pl.DataFrame([pl.Series(xlabel, values)])`, and Chapter 12.1 cell 36 uses `pl.DataFrame([pl.Series("Difference Between Group Means", differences)])`. No chapter builds a DataFrame from a dictionary.
