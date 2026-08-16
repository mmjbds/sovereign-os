# Contributing to SOVEREIGN Public Interfaces

This repository accepts bounded improvements to the released cognitive-immunity and structured-memory interfaces. It is not a route for requesting or reconstructing the private production system.

## Useful Contributions

- A deterministic failure-rule lifecycle case with expected output.
- A test for scope, decay, reinforcement, review, conflict, or reversal behavior exposed by the public interface.
- A documentation, typing, schema, or portability repair.
- A public-safe comparison or negative result that narrows a claim.

## Before a Pull Request

Run:

```bash
python examples/rule_lifecycle_demo.py --check
python -m unittest discover -s tests
```

Describe the affected public interface, expected behavior, verification command, and limitation. Use synthetic or properly licensed data only.

## Not Accepted

Do not submit production orchestration, exact operational thresholds or weights, private prompts, private failure memory, customer data, deployment automation, credentials, or unreleased research. Reduce a useful idea to a public interface, synthetic fixture, or non-confidential problem statement.

Use the [failure-rule case form](https://github.com/mmjbds/sovereign-os/issues/new?template=failure_rule_case.yml) for scoped public cases and the central [Discussions](https://github.com/mmjbds/mianzhang.org/discussions) for early research questions.
