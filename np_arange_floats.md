# `np.arange(...)` with floats in Chapters 1–12

Every place in chapters 01–12 where `np.arange` is called with at least one float argument (start, stop, or step). Cell numbers are 0-indexed notebook cells (the first cell is cell 0). Integer-only calls such as `np.arange(5)` and `np.arange(1, 7)` are not listed.

| # | Chapter | Notebook | Cell | Code | Purpose |
|---|---------|----------|------|------|---------|
| 1 | 5.2 | [Ranges](chapters/05/2/Ranges.ipynb) | 9 | `np.arange(1.5, -2, -0.5)` | Float start and a negative float step; counts down from 1.5. |
| 2 | 9.3 | [Simulation](chapters/09/3/Simulation.ipynb) | 19 | `np.arange(30.5, 69.6, 1)` | Histogram bins centred on integer head counts. |
| 3 | 9.3 | [Simulation](chapters/09/3/Simulation.ipynb) | 28 | `np.arange(1.5, 12.6, 1)` | Histogram bins centred on the sum of two dice (2 to 12). |
| 4 | 10.1 | [Empirical Distributions](chapters/10/1/Empirical_Distributions.ipynb) | 4 | `np.arange(0.5, 6.6, 1)` | Histogram bins centred on die faces 1 to 6. |
| 5 | 10.3 | [Empirical Distribution of a Statistic](chapters/10/3/Empirical_Distribution_of_a_Statistic.ipynb) | 26 | `np.arange(0.5, 5, 1)` | Histogram bins for simulated medians. |
| 6 | 11.1 | [Assessing a Model](chapters/11/1/Assessing_a_Model.ipynb) | 12 | `np.arange(5.5, 46.6, 1)` | Histogram bins for counts in a random sample. |
| 7 | 11.1 | [Assessing a Model](chapters/11/1/Assessing_a_Model.ipynb) | 15 | `np.arange(5.5, 46.6, 1)` | Same bins, reused when the observed value is added to the plot. |
| 8 | 11.2 | [Multiple Categories](chapters/11/2/Multiple_Categories.ipynb) | 34 | `np.arange(0, 0.2, 0.005)` | Float step; histogram bins for the simulated TVDs. |
| 9 | 12.2 | [Causality](chapters/12/2/Causality.ipynb) | 30 | `np.arange(0, 0.7, 0.1)` | Float step; histogram bins for simulated distances. |

## Patterns

- **Half-integer start (**`x.5`**) with a stop ending in** `.6`**.** Examples are `np.arange(30.5, 69.6, 1)` and `np.arange(5.5, 46.6, 1)`. The `.5` start centres each bin on an integer, and the `.6` stop makes sure the last bin edge is included, because the stop value is exclusive.
- **Fractional step.** Examples are `0.005`, `0.1`, and `-0.5`. These are the cases most at risk of floating-point rounding, so the number of elements can differ from what you expect. `np.linspace` is the safer alternative when you need an exact count.
- **Nearly all of these are histogram** `bins=`**.** The one exception is `05/2/Ranges.ipynb`, which uses a float `np.arange` to explain how ranges work.
