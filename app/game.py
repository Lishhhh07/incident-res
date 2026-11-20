UNITS = {
    "traffic": "patrol", "clearance": "patrol", "medical": "medic",
    "outage": "utility", "repair": "utility", "flood": "works",
    "cleanup": "works", "storm": "works",
}


def choose(prompt, options):
    while True:
        value = input(prompt).strip().lower()
        if value in options:
            return value
        print("Choose one of:", ", ".join(options))


def play(row, model):
    stock = dict.fromkeys(sorted(set(UNITS.values())), 2)
    results = []
    for i, actual in enumerate(row[1:], 1):
        print("\nReport:", " -> ".join(row[:i]))
        ranked = sorted(model.distribution(row[:i]).items(), key=lambda x: -x[1])
        print("Forecast:", ", ".join(f"{event} {p:.0%}" for event, p in ranked[:3]))
        print("Possible events:", ", ".join(model.events))
        prediction = choose("Predict the next event: ", model.events)
        available = [unit for unit, count in stock.items() if count]
        print("Stock:", ", ".join(f"{unit}={count}" for unit, count in stock.items()))
        print("Choose up to two units, or pass to conserve stock.")
        dispatched = []
        for _ in range(2):
            unit = choose("Dispatch (" + "/".join(available + ["pass"]) + "): ", available + ["pass"])
            if unit == "pass":
                break
            dispatched.append(unit)
            stock[unit] -= 1
            available.remove(unit)
        print(f"Observed: {actual}. Scenario requires: {UNITS[actual]}.")
        results.append((prediction == actual, UNITS[actual] in dispatched, len(dispatched)))
    return results

