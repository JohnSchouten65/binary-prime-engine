#!/usr/bin/env python3
"""
Test estremo per numeri molto grandi.
"""

import time
from binary_prime_engine import next_prime_binary

def test_extreme_numbers():
    """Testa numeri estremamente grandi."""
    print("=== TEST NUMERI ESTREMAMENTE GRANDI ===\n")
    
    extreme_numbers = [
        10_000_000,    # 10 milioni
        50_000_000,    # 50 milioni  
        100_000_000,   # 100 milioni
        1_000_000_000, # 1 miliardo
    ]
    
    for n in extreme_numbers:
        print(f"Testing from {n:,}:")
        
        try:
            start_time = time.time()
            prime = next_prime_binary(n)
            elapsed = time.time() - start_time
            
            print(f"  ✅ Primo trovato: {prime:,}")
            print(f"  ⏱️  Tempo: {elapsed:.3f} secondi")
            
            # Se impiega più di 10 secondi, fermati
            if elapsed > 10:
                print(f"  ⚠️  TROPPO LENTO per uso pratico")
                break
                
        except KeyboardInterrupt:
            print(f"  ❌ Interrotto dall'utente")
            break
        except Exception as e:
            print(f"  ❌ ERRORE: {e}")
            break
        
        print()

def theoretical_limits():
    """Analizza i limiti teorici."""
    print("=== ANALISI LIMITI TEORICI ===\n")
    
    print("📊 COMPLESSITÀ ALGORITMO:")
    print("  • Test di primalità: O(√n)")
    print("  • Per ogni numero testato: ~√n operazioni")
    print()
    
    print("⏱️  TEMPI STIMATI:")
    numbers = [1_000, 10_000, 100_000, 1_000_000, 10_000_000, 100_000_000]
    
    for n in numbers:
        sqrt_n = int(n**0.5)
        # Stima operazioni: circa √n/2 divisioni per numero primo
        ops = sqrt_n // 2
        # Stima tempo: assumendo ~1 operazione per microsecondo
        time_estimate = ops / 1_000_000  # secondi
        
        print(f"  {n:>12,}: ~{sqrt_n:>6,} ops -> ~{time_estimate:.4f}s")
    
    print()
    print("🚧 LIMITI PRATICI:")
    print("  • ✅ Affidabile: fino a 10 milioni (< 1s)")
    print("  • ⚠️  Lento: 10-100 milioni (1-10s)")  
    print("  • ❌ Impraticabile: > 100 milioni (> 10s)")
    print()
    
    print("💡 PER NUMERI PIÙ GRANDI:")
    print("  • Miller-Rabin (test probabilistico)")
    print("  • Sieve of Eratosthenes (pre-calcolo)")
    print("  • Librerie specializzate (sympy, gmpy2)")

if __name__ == "__main__":
    theoretical_limits()
    print("\n" + "="*60)
    test_extreme_numbers()
