from __future__ import annotations

import math
import unittest

from core.cognitive_immunity.immunity_core import Antibody, Antigen


class AntibodyLifecycleTests(unittest.TestCase):
    def test_decay_matches_released_equation(self) -> None:
        antibody = Antibody(Antigen("fixture", "test"), "stop", strength=0.8)
        antibody.decay(0.25)
        self.assertTrue(math.isclose(antibody.strength, 0.8 * math.exp(-0.25), rel_tol=1e-12))

    def test_reinforcement_adds_public_boost(self) -> None:
        antibody = Antibody(Antigen("fixture", "test"), "stop", strength=0.5)
        antibody.reinforce(0.1)
        self.assertTrue(math.isclose(antibody.strength, 0.6, rel_tol=1e-12))


if __name__ == "__main__":
    unittest.main()
