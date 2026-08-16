from __future__ import annotations

import argparse
import json
import math
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from core.cognitive_immunity.immunity_core import Antibody, Antigen


def run_fixture() -> dict[str, object]:
    antigen = Antigen(
        failure_signature="synthetic:unverified-number-presented-as-fact",
        category="public_fixture",
    )
    antibody = Antibody(
        antigen=antigen,
        correction_rule="Require a public source or return an unresolved state.",
        strength=0.8,
    )
    initial_strength = antibody.strength
    decay_rate = 0.25
    antibody.decay(decay_rate)
    after_decay = antibody.strength
    reinforcement = 0.1
    antibody.reinforce(reinforcement)
    after_reinforcement = antibody.strength
    return {
        "schema": "cognitive_immunity_public_fixture_v1",
        "failure_signature": antigen.signature,
        "category": antigen.category,
        "correction_rule": antibody.rule,
        "initial_strength": initial_strength,
        "decay_rate": decay_rate,
        "after_decay": after_decay,
        "reinforcement": reinforcement,
        "after_reinforcement": after_reinforcement,
        "expected_after_decay": initial_strength * math.exp(-decay_rate),
        "boundary": (
            "Arithmetic fixture only. It does not implement production rule extraction, "
            "similarity routing, policy thresholds, conflict resolution, or safety certification."
        ),
    }


def main() -> int:
    parser = argparse.ArgumentParser(description="Run the public Cognitive Immunity lifecycle fixture")
    parser.add_argument("--check", action="store_true")
    args = parser.parse_args()
    receipt = run_fixture()
    print(json.dumps(receipt, ensure_ascii=True, indent=2))
    if args.check:
        if not math.isclose(receipt["after_decay"], receipt["expected_after_decay"], rel_tol=1e-12):
            return 1
        if receipt["after_reinforcement"] <= receipt["after_decay"]:
            return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
