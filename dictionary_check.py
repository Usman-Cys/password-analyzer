import re
from typing import List, Dict, Optional

class DictionaryCheck:
    """Detects patterns and common passwords."""

    LEET_MAP = {
        '4': 'a', '@': 'a', '8': 'b', '(': 'c', '<': 'c', '3': 'e',
        '1': 'i', '!': 'i', '0': 'o', '5': 's', '$': 's', '7': 't', '+': 't'
    }

    KEYBOARD_WALKS = ["qwertyuiop", "asdfghjkl", "zxcvbnm", "1234567890"]

    def __init__(self, common_passwords_file: Optional[str] = None):
        self.common_passwords = set()
        if common_passwords_file:
            try:
                with open(common_passwords_file, 'r') as f:
                    self.common_passwords = {line.strip().lower() for line in f}
            except FileNotFoundError:
                pass

    def de_leet(self, password: str) -> str:
        """Converts leetspeak to standard English."""
        res = password.lower()
        for leet, char in self.LEET_MAP.items():
            res = res.replace(leet, char)
        return res

    def check_patterns(self, password: str) -> List[str]:
        """Detects repeats, sequences, and walks."""
        findings = []
        pw_lower = password.lower()

        # Repeats (aaa, 111)
        if re.search(r'(.)\1\1', password):
            findings.append("Repeated characters detected.")

        # Sequences (abc, 123)
        for i in range(len(pw_lower) - 2):
            chunk = pw_lower[i:i+3]
            if chunk in "abcdefghijklmnopqrstuvwxyz" or chunk in "0123456789":
                findings.append(f"Sequential pattern detected: '{chunk}'")
                break

        # Keyboard walks
        for walk in self.KEYBOARD_WALKS:
            for i in range(len(pw_lower) - 2):
                if pw_lower[i:i+3] in walk:
                    findings.append("Keyboard walk detected.")
                    return findings

        return findings

    def is_common(self, password: str) -> bool:
        """Checks if password exists in common list or is a leet variation."""
        pw_lower = password.lower()
        de_leeted = self.de_leet(pw_lower)
        return pw_lower in self.common_passwords or de_leeted in self.common_passwords
