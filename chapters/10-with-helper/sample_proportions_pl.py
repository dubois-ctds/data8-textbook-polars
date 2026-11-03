import polars as pl


def sample_proportions_pl(sample_size: int, proportions: list[float]) -> list[float]:
    """
    Draw a random sample of `sample_size` items from a distribution
    defined by `proportions` (a list of probabilities summing to 1),
    and return the proportion of each category in the sample.

    Parameters
    ----------
    sample_size : int
        Number of items to draw.
    proportions : list[float]
        Probability of each category. Must sum to 1.

    Returns
    -------
    list[float]
        Observed proportion of each category in the sample.
    """
    n = len(proportions)
    categories = list(range(n))

    # Build a Series of categories weighted by their proportions,
    # then sample with replacement to simulate the multinomial draw.
    # We expand each category proportionally to approximate the distribution.
    weights = pl.Series("weights", proportions)
    cat_series = pl.Series("categories", categories)

    # Sample with replacement using proportions as relative weights
    # by repeating the sampling process via Polars
    sampled = (
        pl.DataFrame({"category": categories, "weight": proportions})
        .sample(n=sample_size, with_replacement=True, shuffle=True)
        # Note: Polars .sample() does not support weighted sampling directly,
        # so we use a workaround below.
    )

    # Workaround: use numpy for weighted sampling, then count with Polars
    import numpy as np

    drawn = np.random.choice(categories, size=sample_size, p=proportions)
    counts = (
        pl.Series("drawn", drawn)
        .value_counts()
        .sort("drawn")
    )

    # Build full result including zero-count categories
    result = []
    count_dict = dict(zip(counts["drawn"].to_list(), counts["count"].to_list()))
    for cat in categories:
        result.append(count_dict.get(cat, 0) / sample_size)

    return result


if __name__ == "__main__":
    proportions = [0.5, 0.3, 0.2]
    sample_size = 1000
    observed = sample_proportions_pl(sample_size, proportions)
    print(observed)
