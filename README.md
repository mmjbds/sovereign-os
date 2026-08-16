# SOVEREIGN: Public Interfaces for Self-Evolving Agent Systems

[![public-ci](https://github.com/mmjbds/sovereign-os/actions/workflows/public-ci.yml/badge.svg)](https://github.com/mmjbds/sovereign-os/actions/workflows/public-ci.yml)
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
- `examples/rule_lifecycle_demo.py`: deterministic decay-and-reinforcement fixture with a machine-readable receipt.

## Quick Start

```bash
python examples/rule_lifecycle_demo.py --check
python -m unittest discover -s tests
```

The demo uses no model, vector database, provider account or private data. It checks the arithmetic of the released `Antibody` interface; it does not implement production extraction, routing, conflict resolution or deployment policy.

The interfaces are suitable for inspection, teaching, adaptation, and public experiments. Production orchestration, exact thresholds and weights, private prompts and data, tuning history, customer systems, and deployment automation are not included.

## Research Route

Cognitive Immunity was presented as a non-archival workshop paper at the 2nd SeT-LLM Workshop at KDD 2026. The reported study evaluates recurrence under a documented score-level protocol; it does not certify production safety.

- Technical paper index: https://mianzhang.org/papers/kdd-2026/
- Research feature: https://mianzhang.org/press/kdd-2026-two-workshop-papers.html
- AI Agent Reliability Lab: https://mianzhang.org/ai-agent-reliability/
- Claim boundary: [CLAIM_BOUNDARY.md](CLAIM_BOUNDARY.md)

## Community

- Open research community: https://mianzhang.org/community/
- Public issue forms: https://github.com/mmjbds/sovereign-os/issues/new/choose
- GitHub Discussions: https://github.com/mmjbds/mianzhang.org/discussions
- Contribution guide: [CONTRIBUTING.md](CONTRIBUTING.md)
- Private security route: [SECURITY.md](SECURITY.md)

## Citation

Use [CITATION.cff](CITATION.cff). Do not cite this repository as a NeurIPS proceedings publication.

## License

The intentionally released source code is available under Apache-2.0. No rights are granted to private or unreleased implementations merely because a public interface refers to them.
