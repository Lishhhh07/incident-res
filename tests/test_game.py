import subprocess
import sys
import unittest

from app.model import train
from app.patterns import patterns
from app.reports import DRILLS, TRAIN, BASE
from app.score import summary


class TrainingTests(unittest.TestCase):
    def test_patterns_preserve_order(self):
        self.assertEqual(patterns([["a", "b", "a"], ["a", "b"]], 0.5),
                         [("a", "b", 2 / 3)])

    def test_forecast(self):
        probs = train().distribution(["storm", "outage"])
        self.assertAlmostEqual(sum(probs.values()), 1)
        self.assertEqual(max(probs, key=probs.get), "repair")

    def test_holdout(self):
        self.assertTrue(set(DRILLS.values()).isdisjoint(BASE + TRAIN))

    def test_score(self):
        self.assertIn("Score: 7/8", summary([(True, True, 2)]))
        self.assertIn("Score: 0/8", summary([(False, False, 0)]))

    def test_complete_drill(self):
        result = subprocess.run([sys.executable, "-m", "app.cli", "play", "--scenario", "underpass"],
                                input="flood\nworks\npass\noutage\nutility\npass\nrepair\nutility\npass\n",
                                capture_output=True, text=True, check=True)
        self.assertIn("Score: 24/24", result.stdout)

