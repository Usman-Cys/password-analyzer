import pytest
from entropy_engine import EntropyEngine
from dictionary_check import DictionaryCheck

def test_entropy_calculation():
    engine = EntropyEngine()
    # Simple lowercase
    assert engine.calculate_entropy("aaaaa") > 0
    # Complexity increases entropy
    assert engine.calculate_entropy("Ab1!") > engine.calculate_entropy("abcd")

def test_pattern_detection():
    checker = DictionaryCheck()
    assert len(checker.check_patterns("qwerty")) > 0
    assert len(checker.check_patterns("123456")) > 0
    assert len(checker.check_patterns("aaaaa")) > 0

def test_leetspeak_translation():
    checker = DictionaryCheck()
    assert checker.de_leet("p@ssw0rd") == "password"
    assert checker.de_leet("3ntr0py") == "entropy"
