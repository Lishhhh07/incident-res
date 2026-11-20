from thilimarketbasket.mine import frequent_itemsets


def patterns(reports, min_support=0.12):
    """Measure support among adjacent transitions, preserving direction."""
    windows = [[f"from:{a}", f"to:{b}"] for row in reports for a, b in zip(row, row[1:])]
    found = frequent_itemsets(windows, min_support, max_size=2)
    pairs = []
    for items, support in found.items():
        if len(items) == 2:
            source, target = sorted(items)
            pairs.append((source[5:], target[3:], support))
    return sorted(pairs, key=lambda pair: (-pair[2], pair[:2]))

