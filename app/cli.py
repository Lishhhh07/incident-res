import argparse
import random

from .game import play
from .model import train
from .patterns import patterns
from .reports import DRILLS, TRAIN, sequences


def main():
    parser = argparse.ArgumentParser(description="Incident response training simulator")
    parser.add_argument("command", choices=["hello", "play", "patterns"], nargs="?", default="play")
    parser.add_argument("--scenario", choices=sorted(DRILLS))
    args = parser.parse_args()
    if args.command == "hello":
        print("Ready. Run python -m app.cli play to start.")
    elif args.command == "patterns":
        for source, target, support in patterns(sequences(TRAIN), 0.05):
            print(f"{source} -> {target}: {support:.1%}")
    else:
        name = args.scenario or random.choice(list(DRILLS))
        print("Exercise:", name)
        try:
            results = play(DRILLS[name].split(), train())
        except (EOFError, KeyboardInterrupt):
            print("\nExercise ended.")
            return
        print("Completed rounds:", len(results))


if __name__ == "__main__":
    main()

