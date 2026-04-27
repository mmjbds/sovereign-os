"""
SOVEREIGN OS - Cognitive Immunity Core Interfaces
Provides the base classes for implementing B-Cell pattern generation and T-Cell routing.
"""

from typing import List, Dict
import math

class Antigen:
    def __init__(self, failure_signature: str, category: str):
        self.signature = failure_signature
        self.category = category

class Antibody:
    def __init__(self, antigen: Antigen, correction_rule: str, strength: float = 1.0):
        self.antigen = antigen
        self.rule = correction_rule
        self.strength = strength

    def decay(self, rate: float):
        """Exponential decay based on time non-activation."""
        self.strength *= math.exp(-rate)

    def reinforce(self, boost: float):
        """Reinforce the antibody if triggered to prevent decay."""
        self.strength += boost

class BCell:
    def __init__(self, extractor_llm):
        self.llm = extractor_llm

    def process_failure(self, task_context: str, failed_output: str) -> Antibody:
        """
        Extracts an Antigen from the failure and proposes an active Antibody correction.
        Implementation specific to application logic.
        """
        raise NotImplementedError("Implement the LLM extraction logic here.")

class TCell:
    def __init__(self, memory_store, threshold: float = 0.3):
        self.memory = memory_store
        self.activation_threshold = threshold

    def scan(self, query: str) -> List[Antibody]:
        """
        Compare query embeddings against the active antibody store.
        Returns active strategies to inject into prompt context if threshold met.
        """
        raise NotImplementedError("Implement vector similarity search here.")
