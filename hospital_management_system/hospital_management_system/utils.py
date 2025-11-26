# utils.py
"""
Utility functions (e.g., ID generator, validation).
"""

import random

def generate_id(prefix):
    """
    Generate unique IDs like:
    PAT123, DOC456, APT789
    using prefix + random number.
    """
    return f"{prefix}{random.randint(100, 999)}"
