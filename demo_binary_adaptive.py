#!/usr/bin/env python3
"""
Demo: Rappresentazione Binaria Adattiva vs Fissa
=================================================
Dimostra il miglioramento nella rappresentazione binaria.
"""

def binary_code_old(n: int, bits: int = 16) -> str:
    """Versione VECCHIA: bits fissi con troncamento."""
    return format(n & ((1 << bits) - 1), f'0{bits}b')

def binary_code_new(n: int, bits: int = None) -> str:
    """Versione NUOVA: bits adattivi."""
    if bits is None:
        if n == 0:
            return "0"
        bits = n.bit_length()
        bits = ((bits + 3) // 4) * 4  # Arrotonda a nibble
        bits = max(bits, 8)
    return format(n, f'0{bits}b')

def demo_comparison():
    """Confronta vecchia vs nuova rappresentazione."""
    print("🔄 CONFRONTO: RAPPRESENTAZIONE BINARIA VECCHIA vs NUOVA")
    print("=" * 70)
    
    test_cases = [
        ("Piccoli", [2, 3, 7, 15]),
        ("Medi", [255, 256, 1023, 1024]),
        ("Grandi", [65535, 65536, 100000]),
        ("Molto Grandi", [1000000, 10000000, 1000000000]),
        ("Primi Reali", [1009, 10007, 100003, 1000003])
    ]
    
    for category, numbers in test_cases:
        print(f"\n📊 {category.upper()}:")
        print(f"{'Numero':>12} | {'Vecchia (16-bit)':^20} | {'Nuova (Adattiva)':^25} | Problema")
        print("-" * 75)
        
        for n in numbers:
            old = binary_code_old(n, 16)
            new = binary_code_new(n)
            
            # Verifica se c'è troncamento
            original_bits = n.bit_length()
            truncated = original_bits > 16
            problem = "🚨 TRONCATO!" if truncated else "✅ OK"
            
            print(f"{n:>12,} | {old} | {new:^25} | {problem}")
    
    print(f"\n{'='*70}")
    print("📈 VANTAGGI RAPPRESENTAZIONE ADATTIVA:")
    print("✅ Nessun troncamento - rappresentazione completa")
    print("✅ Bit ottimizzati automaticamente")
    print("✅ Leggibilità migliorata con nibble (4-bit)")
    print("✅ Compatibilità con numeri di qualsiasi dimensione")
    print("✅ Efficienza per numeri piccoli (minimo 8 bit)")
    
    print(f"\n❌ PROBLEMI VECCHIA VERSIONE:")
    print("❌ Troncamento per numeri > 65,535")
    print("❌ Perdita di informazione")
    print("❌ Codici binari identici per numeri diversi")
    print("❌ Inadatta per numeri grandi")

def demo_practical_example():
    """Esempio pratico con numeri primi grandi."""
    print(f"\n{'='*70}")
    print("🔍 ESEMPIO PRATICO: PRIMI MOLTO GRANDI")
    print("=" * 70)
    
    from binary_prime_engine import next_prime_binary
    
    big_starts = [1000000, 10000000, 100000000]
    
    print(f"{'Start':>12} | {'Primo Trovato':>14} | {'Rappresentazione Binaria'}")
    print("-" * 65)
    
    for start in big_starts:
        prime = next_prime_binary(start)
        binary = binary_code_new(prime)
        print(f"{start:>12,} | {prime:>14,} | {binary}")
    
    print(f"\n💡 NOTA: Con la vecchia versione, tutti questi primi")
    print("   avrebbero avuto solo 16 bit, perdendo informazione!")

if __name__ == "__main__":
    demo_comparison()
    demo_practical_example()
    
    print(f"\n🎯 CONCLUSIONE:")
    print("La rappresentazione binaria ADATTIVA risolve completamente")
    print("il problema del troncamento e migliora l'usabilità!")
