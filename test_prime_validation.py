#!/usr/bin/env python3
"""
Test di validazione per verificare che il motore generi solo numeri primi corretti.
"""

import sys
from binary_prime_engine import next_prime_binary

def is_prime_reference(n):
    """Funzione di riferimento per verificare se un numero è primo."""
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    
    for i in range(3, int(n**0.5) + 1, 2):
        if n % i == 0:
            return False
    return True

def test_prime_engine(limit=1000):
    """Testa il motore fino al limite specificato."""
    print(f"=== TEST VALIDAZIONE PRIMI FINO A {limit} ===\n")
    
    n = 1
    count = 0
    false_positives = []
    missed_primes = []
    
    # Genera tutti i primi dal motore
    engine_primes = []
    while True:
        p = next_prime_binary(n)
        if p > limit:
            break
        engine_primes.append(p)
        n = p + 1
        count += 1
    
    print(f"Primi generati dal motore: {count}")
    print(f"Primi: {engine_primes[:20]}{'...' if len(engine_primes) > 20 else ''}\n")
    
    # Verifica ogni primo generato
    for p in engine_primes:
        if not is_prime_reference(p):
            false_positives.append(p)
    
    # Trova tutti i primi di riferimento
    reference_primes = [n for n in range(2, limit + 1) if is_prime_reference(n)]
    
    # Verifica se abbiamo perso dei primi
    for p in reference_primes:
        if p not in engine_primes:
            missed_primes.append(p)
    
    # Risultati
    print("=== RISULTATI TEST ===")
    print(f"✅ Primi corretti generati: {len(engine_primes) - len(false_positives)}")
    print(f"❌ Falsi positivi: {len(false_positives)}")
    if false_positives:
        print(f"   Numeri NON primi generati: {false_positives}")
    
    print(f"❌ Primi mancanti: {len(missed_primes)}")
    if missed_primes:
        print(f"   Primi non trovati: {missed_primes}")
    
    print(f"📊 Riferimento (totale primi fino a {limit}): {len(reference_primes)}")
    
    # Test specifici per i primi piccoli
    print("\n=== TEST PRIMI PICCOLI ===")
    small_primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47]
    for i, expected in enumerate(small_primes):
        if i < len(engine_primes):
            generated = engine_primes[i]
            status = "✅" if generated == expected else "❌"
            print(f"p{i+1}: generato={generated}, atteso={expected} {status}")
        else:
            print(f"p{i+1}: mancante, atteso={expected} ❌")
    
    return len(false_positives) == 0 and len(missed_primes) == 0

if __name__ == "__main__":
    # Test con limite personalizzabile
    limit = int(sys.argv[1]) if len(sys.argv) > 1 else 1000
    
    success = test_prime_engine(limit)
    
    print(f"\n{'='*50}")
    if success:
        print("🎉 SUCCESSO: Il motore genera SOLO numeri primi corretti!")
    else:
        print("⚠️  ATTENZIONE: Trovati errori nella generazione!")
    print(f"{'='*50}")
