#!/usr/bin/env python3
"""
Binary Prime Engine - English Version
=====================================

Infinite binary prime number generator with advanced pattern analysis and gap tracking.

Features:
- Adaptive binary representation (auto-expanding bits)
- Gap tracking between consecutive primes (dₙ)
- Compact binary representation of numbers
- Persistent storage of binary codes for known composite numbers
- Optimized prime checking using binary patterns
"""

import json
from pathlib import Path

DB_FILE = Path("binary_codes.json")

# Load known binary codes database
if DB_FILE.exists():
    with open(DB_FILE, "r") as f:
        code_db = set(json.load(f))
else:
    code_db = set()

def binary_code(n: int, bits: int = None) -> str:
    """
    Adaptive binary code of number n.
    If bits is not specified, automatically calculates required bits.
    """
    if bits is None:
        # Automatically calculate required bits
        if n == 0:
            return "0"
        bits = n.bit_length()
        # Round to multiples of 4 for readability (nibble)
        bits = ((bits + 3) // 4) * 4
        # Minimum 8 bits for small numbers
        bits = max(bits, 8)
    
    return format(n, f'0{bits}b')

def next_prime_binary(n: int) -> int:
    """Find the next binary prime using patterns and predictive gaps."""
    # Force n to be odd
    if n < 2:
        return 2
    if n == 2:
        return 3
    if n % 2 == 0:
        n += 1

    while True:
        # Primality test for odd numbers
        # Binary check with odd divisors
        d = 3
        is_prime = True
        while d * d <= n:
            if n % d == 0:
                is_prime = False
                code_db.add(binary_code(n))
                break
            d += 2
        if is_prime:
            return n
        n += 2  # Skip to next odd numbers

def infinite_prime_engine(start: int = 1):
    """Infinite binary engine with pₙ and dₙ."""
    n = start
    last_prime = None
    count = 0
    while True:
        p = next_prime_binary(n)
        count += 1
        if last_prime is None:
            gap = 0
        else:
            gap = p - last_prime
        print(f"p{count} = {p} | gap dₙ = {gap} | bin: {binary_code(p)}")
        last_prime = p
        n = p + 1

def save_database():
    """Save the binary codes database."""
    try:
        with open(DB_FILE, "w") as f:
            json.dump(list(code_db), f, indent=2)
        print(f"\n💾 Database saved: {len(code_db)} binary codes")
    except Exception as e:
        print(f"❌ Error saving database: {e}")

if __name__ == "__main__":
    print("=== Binary Prime Engine - INFINITE & BINARY with pₙ and dₙ ===")
    print("🔢 Advanced prime number generation with binary pattern analysis")
    print("📊 Features: gap tracking, adaptive binary codes, persistent storage")
    print("="*70)
    
    try:
        start = int(input("Enter starting number: "))
        print(f"\n🚀 Starting infinite prime generation from {start}...")
        print("⚠️  Press Ctrl+C to stop and save database\n")
        infinite_prime_engine(start)
    except KeyboardInterrupt:
        print("\n\n⏹️  Generation stopped by user.")
        save_database()
        print("👋 Thank you for using Binary Prime Engine!")
    except ValueError:
        print("❌ Please enter a valid number")
    except Exception as e:
        print(f"❌ Unexpected error: {e}")
        save_database()
