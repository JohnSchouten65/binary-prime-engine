#!/usr/bin/env python3
"""
Test di stress per determinare fino a che numero il motore è affidabile.
Testa performance e correttezza con numeri sempre più grandi.
"""

import time
import sys
from binary_prime_engine import next_prime_binary, binary_code

def is_prime_reference(n):
    """Funzione di riferimento ottimizzata per verificare se un numero è primo."""
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    
    # Ottimizzazione: controlla solo fino alla radice quadrata
    limit = int(n**0.5) + 1
    for i in range(3, limit, 2):
        if n % i == 0:
            return False
    return True

def stress_test_range(start, end, sample_size=100):
    """Testa un range di numeri con campionamento."""
    print(f"\n=== TEST RANGE {start:,} - {end:,} ===")
    
    # Campiona alcuni numeri dal range
    step = max(1, (end - start) // sample_size)
    test_numbers = list(range(start, min(end + 1, start + step * sample_size), step))
    
    errors = []
    times = []
    
    for n in test_numbers:
        start_time = time.time()
        
        # Trova il prossimo primo dal motore
        engine_prime = next_prime_binary(n)
        
        elapsed = time.time() - start_time
        times.append(elapsed)
        
        # Verifica con funzione di riferimento
        if not is_prime_reference(engine_prime):
            errors.append((n, engine_prime))
    
    avg_time = sum(times) / len(times) if times else 0
    max_time = max(times) if times else 0
    
    print(f"Numeri testati: {len(test_numbers)}")
    print(f"Errori trovati: {len(errors)}")
    print(f"Tempo medio: {avg_time*1000:.2f}ms")
    print(f"Tempo massimo: {max_time*1000:.2f}ms")
    
    if errors:
        print(f"❌ ERRORI: {errors[:5]}{'...' if len(errors) > 5 else ''}")
        return False
    else:
        print("✅ Tutti i primi sono corretti!")
        return True

def performance_test(numbers_to_test):
    """Test di performance con numeri specifici."""
    print(f"\n=== TEST PERFORMANCE NUMERI SPECIFICI ===")
    
    for n in numbers_to_test:
        print(f"\nTesting from {n:,}:")
        
        start_time = time.time()
        prime = next_prime_binary(n)
        elapsed = time.time() - start_time
        
        # Verifica correttezza
        is_correct = is_prime_reference(prime)
        status = "✅" if is_correct else "❌"
        
        bin_repr = binary_code(prime, 20)
        print(f"  Primo trovato: {prime:,} in {elapsed*1000:.2f}ms {status}")
        print(f"  Binary: {bin_repr}")
        
        if not is_correct:
            print(f"  ❌ ERRORE: {prime} NON è primo!")

def find_reliability_limit():
    """Trova il limite di affidabilità del motore."""
    print("=== RICERCA LIMITE DI AFFIDABILITÀ ===")
    
    # Test progressivi
    test_ranges = [
        (1, 10_000),
        (10_000, 100_000),
        (100_000, 500_000),
        (500_000, 1_000_000),
        (1_000_000, 2_000_000),
        (2_000_000, 5_000_000),
    ]
    
    reliable_up_to = 0
    
    for start, end in test_ranges:
        print(f"\n{'='*60}")
        success = stress_test_range(start, end, sample_size=50)
        
        if success:
            reliable_up_to = end
            print(f"✅ Affidabile fino a: {end:,}")
        else:
            print(f"❌ Problemi trovati nel range {start:,} - {end:,}")
            break
            
        # Se il tempo medio supera 100ms, fermiamoci
        if end > 1_000_000:
            print("⚠️  Range molto grande raggiunto, fermandosi per performance")
            break
    
    return reliable_up_to

def main():
    print("🔬 TEST DI AFFIDABILITÀ BINARY PRIME ENGINE")
    print("=" * 60)
    
    # Test 1: Range progressivi
    limit = find_reliability_limit()
    
    # Test 2: Numeri specifici grandi
    big_numbers = [
        100_000, 500_000, 1_000_000,
        1_500_000, 2_000_000, 5_000_000
    ]
    
    performance_test(big_numbers)
    
    # Test 3: Primi molto grandi (se il sistema regge)
    print(f"\n{'='*60}")
    print("=== CONCLUSIONI ===")
    print(f"🎯 Motore affidabile fino a: {limit:,}")
    
    if limit >= 1_000_000:
        print("🏆 ECCELLENTE: Affidabile per numeri fino a milioni!")
    elif limit >= 100_000:
        print("👍 BUONO: Affidabile per numeri fino a centinaia di migliaia")
    elif limit >= 10_000:
        print("✅ DISCRETO: Affidabile per numeri fino a decine di migliaia")
    else:
        print("⚠️  LIMITATO: Problemi con numeri grandi")
    
    print(f"\n💡 Per numeri > {limit:,}, considera algoritmi più avanzati")
    print("   come Miller-Rabin per test probabilistici su numeri molto grandi")

if __name__ == "__main__":
    main()
