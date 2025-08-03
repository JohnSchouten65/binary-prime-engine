#!/usr/bin/env python3
"""
Test rapido per mostrare alcuni primi con i loro gap.
"""

from binary_prime_engine import next_prime_binary, binary_code

def show_primes_with_gaps(start=1, count=20):
    """Mostra i primi numeri primi con gap e codici binari."""
    print(f"=== PRIMI CON GAP E CODICI BINARI (da {start}, {count} primi) ===\n")
    
    n = start
    last_prime = None
    
    for i in range(count):
        p = next_prime_binary(n)
        
        if last_prime is None:
            gap = 0
        else:
            gap = p - last_prime
            
        bin_code = binary_code(p, 12)  # 12 bit per compattezza
        
        print(f"p{i+1:2d} = {p:4d} | gap = {gap:2d} | bin: {bin_code}")
        
        last_prime = p
        n = p + 1

if __name__ == "__main__":
    show_primes_with_gaps(1, 30)
    print("\n" + "="*50)
    print("Test con numeri più grandi:")
    show_primes_with_gaps(1000, 10)
