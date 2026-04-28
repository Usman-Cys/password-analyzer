import math
import string
from typing import Set

class EntropyEngine:
    """Core engine for calculating password entropy."""

    @staticmethod
    def calculate_entropy(password: str) -> float:
        """Calculates Shannon entropy in bits based on the character pool size.
        
        Security Note: Entropy measures the unpredictability of a password. 
        Formula: E = L * log2(R), where L is length and R is pool size.

        Args:
            password: The plain text password.

        Returns:
            Entropy in bits.
        """
        if not password:
            return 0.0

        length = len(password)
        pool_size = 0
        
        # Determine the character pool size
        if any(c in string.ascii_lowercase for c in password):
            pool_size += 26
        if any(c in string.ascii_uppercase for c in password):
            pool_size += 26
        if any(c in string.digits for c in password):
            pool_size += 10
        if any(c in string.punctuation for c in password):
            pool_size += len(string.punctuation)
        # Check for unicode/other chars if not in standard pools
        remaining_chars = [c for c in password if c not in (string.ascii_letters + string.digits + string.punctuation)]
        if remaining_chars:
            pool_size += 100 # Estimated size for extended chars

        if pool_size == 0:
            return 0.0

        entropy = length * math.log2(pool_size)
        return round(entropy, 2)
