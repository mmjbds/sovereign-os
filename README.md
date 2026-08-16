# SOVEREIGN: Public Interfaces for Self-Evolving Agent Systems

[![License: Apache 2.0](https://img.shields.io/badge/License-Apache_2.0-blue.svg)](LICENSE)

This repository contains minimal public interfaces related to Cognitive Immunity and structured cross-session memory. It is not the complete SOVEREIGN product or a production agent operating system.

## Cognitive Immunity

Cognitive Immunity is a bounded runtime failure-memory approach: a verified failure can create a scoped, reviewable rule that influences later decisions. The objective is to reduce recurrence of previously observed failure classes while keeping the rule attributable, limited, decaying, and reversible.

A simple continuous decay model is:

```text
dB/dt = r - lambda * B
B* = r / lambda
```

Here `B` is retained rule strength, `r` is reinforcement rate, and `lambda` is decay rate. The steady state follows from the stated differential equation. It does not, by itself, prove PAC bounds, general safety, or a guarantee that an error cannot recur.

## Public Files

- `core/cognitive_immunity/immunity_core.py`: minimal public rule and interface structures.
- `core/memory/deerflow_schema.py`: minimal structured memory schema.

The interfaces are suitable for inspection, teaching, adaptation, and public experiments. Production orchestration, exact thresholds and weights, private prompts and data, tuning history, customer systems, and deployment automation are not included.

## Research Route

Cognitive Immunity was presented as a non-archival workshop paper at the 2nd SeT-LLM Workshop at KDD 2026. The reported study evaluates recurrence under a documented score-level protocol; it does not certify production safety.

- Technical paper index: https://mianzhang.org/papers/kdd-2026/
- Research feature: https://mianzhang.org/press/kdd-2026-two-workshop-papers.html
- Claim boundary: [CLAIM_BOUNDARY.md](CLAIM_BOUNDARY.md)

## Community

- Open research community: https://mianzhang.org/community/
- GitHub Discussions: https://github.com/mmjbds/mianzhang.org/discussions

## Citation

Use [CITATION.cff](CITATION.cff). Do not cite this repository as a NeurIPS proceedings publication.

## License

The intentionally released source code is available under Apache-2.0. No rights are granted to private or unreleased implementations merely because a public interface refers to them.
