#!/usr/bin/env python3
"""
Benchmark e Test Performance per Binary Prime Engine
===================================================

Script per testare e confrontare le performance del motore primi.
"""

import time
import statistics
from typing import List, Dict, Any
from binary_prime_engine_pro import BinaryPrimeEngine, prime_engine_context

def benchmark_prime_generation(start: int, count: int, config: Dict[str, Any] = None) -> Dict[str, float]:
    """Benchmark della generazione di primi."""
    results = {}
    
    with prime_engine_context(config) as engine:
        start_time = time.time()
        primes = []
        
        for i, (_, prime, _) in enumerate(engine.generate_primes(start, count)):
            primes.append(prime)
        
        total_time = time.time() - start_time
        
        results = {
            'total_time': total_time,
            'primes_per_second': count / total_time if total_time > 0 else 0,
            'avg_prime': statistics.mean(primes),
            'max_prime': max(primes),
            'cache_hits': engine.stats.cache_hits,
            'cache_efficiency': engine.stats.cache_hits / count if count > 0 else 0
        }
    
    return results

def compare_configurations():
    """Confronta diverse configurazioni del motore."""
    test_cases = [
        {'name': 'Default', 'config': {}},
        {'name': 'Large Cache', 'config': {'cache_size': 50000}},
        {'name': 'Small Cache', 'config': {'cache_size': 1000}},
        {'name': 'No Cache', 'config': {'cache_size': 0}},
    ]
    
    print("BENCHMARK CONFIGURAZIONI")
    print("=" * 60)
    print(f"{'Config':<15} {'Time(s)':<10} {'P/s':<10} {'Cache%':<10}")
    print("-" * 60)
    
    for case in test_cases:
        results = benchmark_prime_generation(1000, 100, case['config'])
        print(f"{case['name']:<15} "
              f"{results['total_time']:<10.3f} "
              f"{results['primes_per_second']:<10.1f} "
              f"{results['cache_efficiency']*100:<10.1f}")

def performance_profile():
    """Profiling dettagliato delle performance."""
    ranges = [
        (1, 100),
        (1000, 100),
        (10000, 100),
        (100000, 50)
    ]
    
    print("\nPROFILE PERFORMANCE PER RANGE")
    print("=" * 60)
    print(f"{'Range':<15} {'Count':<8} {'Time(s)':<10} {'P/s':<10} {'Avg Prime':<12}")
    print("-" * 60)
    
    for start, count in ranges:
        results = benchmark_prime_generation(start, count)
        print(f"{start}-{start+count:<8} "
              f"{count:<8} "
              f"{results['total_time']:<10.3f} "
              f"{results['primes_per_second']:<10.1f} "
              f"{results['avg_prime']:<12.0f}")

if __name__ == "__main__":
    print("BINARY PRIME ENGINE - BENCHMARK SUITE")
    print("=" * 60)
    
    compare_configurations()
    performance_profile()
    
    print("\nBenchmark completato!")
