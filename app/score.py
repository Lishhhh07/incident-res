def summary(results):
    rounds = len(results)
    correct = sum(hit for hit, _, _ in results)
    covered = sum(hit for _, hit, _ in results)
    deployed = sum(count for _, _, count in results)
    efficiency = covered / deployed if deployed else 0
    points = 4 * correct + 4 * covered - (deployed - covered)
    return (f"Predictions: {correct}/{rounds} | Coverage: {covered}/{rounds} | "
            f"Useful dispatches: {covered}/{deployed} ({efficiency:.0%}) | "
            f"Score: {points}/{8 * rounds}")

