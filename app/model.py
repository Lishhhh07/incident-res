import math
import random

from .reports import BASE, TRAIN, sequences


class EventLM:
    """Two-event log-linear language model with a next-token objective."""

    def __init__(self, vocabulary):
        self.events = sorted(vocabulary)
        self.weights = {}

    def distribution(self, history):
        features = self.features(history)
        scores = [sum(self.weights.get((f, e), 0.0) for f in features) for e in self.events]
        peak = max(scores)
        values = [math.exp(score - peak) for score in scores]
        total = sum(values)
        return dict(zip(self.events, (value / total for value in values)))

    @staticmethod
    def features(history):
        prev, last = (["START", "START"] + list(history))[-2:]
        return ["bias", last, prev + "/" + last]

    def fit(self, rows, epochs, seed):
        examples = [(row[:i], row[i]) for row in rows for i in range(1, len(row))]
        rng = random.Random(seed)
        for _ in range(epochs):
            rng.shuffle(examples)
            for history, actual in examples:
                for event, probability in self.distribution(history).items():
                    update = 0.08 * ((event == actual) - probability)
                    for feature in self.features(history):
                        key = feature, event
                        self.weights[key] = self.weights.get(key, 0.0) + update


def train():
    base, local = sequences(BASE), sequences(TRAIN)
    model = EventLM({event for row in base + local for event in row})
    model.fit(base, epochs=20, seed=1)
    model.fit(local, epochs=30, seed=2)
    return model

