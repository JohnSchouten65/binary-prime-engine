#!/usr/bin/env python3
"""
Binary Prime Engine - Professional Version for Real-World Use
==========================================================

Advanced prime number generation engine featuring:
- Performance optimizations
- Efficient memory management  
- Professional CLI interface
- Logging and monitoring
- Flexible configuration
"""

import json
import time
import logging
import argparse
import signal
import sys
from pathlib import Path
from typing import Iterator, Optional, Set, Tuple, Dict, Any
from dataclasses import dataclass, asdict
from contextlib import contextmanager
import threading
from collections import deque
import math

# Logging configuration
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('prime_engine.log'),
        logging.StreamHandler()
    ]
)
logger = logging.getLogger(__name__)

@dataclass
class PrimeStats:
    """Statistics for the prime generation engine."""
    total_primes: int = 0
    total_candidates: int = 0
    total_time: float = 0.0
    avg_gap: float = 0.0
    max_gap: int = 0
    min_gap: int = float('inf')
    primes_per_second: float = 0.0
    cache_hits: int = 0
    cache_size: int = 0

class PrimeCache:
    """LRU cache to optimize prime number searches."""
    
    def __init__(self, max_size: int = 10000):
        self.max_size = max_size
        self.cache: Dict[int, bool] = {}
        self.access_order = deque()
        self.lock = threading.RLock()
    
    def get(self, n: int) -> Optional[bool]:
        """Retrieve from cache if the number is prime."""
        with self.lock:
            if n in self.cache:
                # Move to end (most recent)
                self.access_order.remove(n)
                self.access_order.append(n)
                return self.cache[n]
            return None
    
    def put(self, n: int, is_prime: bool):
        """Add to cache."""
        # If cache is disabled, do nothing
        if self.max_size == 0:
            return
            
        with self.lock:
            if n in self.cache:
                self.access_order.remove(n)
            elif len(self.cache) >= self.max_size:
                # Remove least recently used
                if self.access_order:  # Check that it's not empty
                    oldest = self.access_order.popleft()
                    del self.cache[oldest]
            
            self.cache[n] = is_prime
            self.access_order.append(n)
    
    def size(self) -> int:
        return len(self.cache)

class BinaryPrimeEngine:
    """Binary engine for prime generation - Professional Version."""
    
    def __init__(self, config: Dict[str, Any] = None):
        self.config = config or {}
        self.db_file = Path(self.config.get('db_file', 'binary_codes.json'))
        self.cache = PrimeCache(self.config.get('cache_size', 10000))
        self.stats = PrimeStats()
        self.code_db: Set[str] = set()
        self.running = True
        self.save_interval = self.config.get('save_interval', 1000)
        self.progress_interval = self.config.get('progress_interval', 100)
        
        # Load existing database
        self._load_database()
        
        # Setup signal handlers for clean interruption
        signal.signal(signal.SIGINT, self._signal_handler)
        signal.signal(signal.SIGTERM, self._signal_handler)
    
    def _load_database(self):
        """Load the binary codes database."""
        try:
            if self.db_file.exists():
                with open(self.db_file, "r") as f:
                    data = json.load(f)
                    if isinstance(data, list):
                        self.code_db = set(data)
                    else:
                        # Extended format with metadata
                        self.code_db = set(data.get('codes', []))
                        if 'stats' in data:
                            # Restore previous statistics
                            for key, value in data['stats'].items():
                                if hasattr(self.stats, key):
                                    setattr(self.stats, key, value)
                logger.info(f"Database loaded: {len(self.code_db)} codes")
        except Exception as e:
            logger.warning(f"Database loading error: {e}")
            self.code_db = set()
    
    def _save_database(self):
        """Save the binary codes database with metadata."""
        try:
            data = {
                'codes': list(self.code_db),
                'stats': asdict(self.stats),
                'timestamp': time.time(),
                'version': '2.0'
            }
            
            with open(self.db_file, "w") as f:
                json.dump(data, f, indent=2)
            logger.debug(f"Database saved: {len(self.code_db)} codes")
        except Exception as e:
            logger.error(f"Database saving error: {e}")
    
    def _signal_handler(self, signum, frame):
        """Handle clean interruption."""
        logger.info("Interruption received, saving data...")
        self.running = False
        self._save_database()
        self._print_final_stats()
        sys.exit(0)
    
    def binary_code(self, n: int, bits: int = None) -> str:
        """
        Generate optimized adaptive binary code.
        If bits is not specified, automatically calculate required bits.
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
    
    def is_prime_optimized(self, n: int) -> bool:
        """Optimized primality test with cache and binary patterns."""
        if n < 2:
            return False
        if n == 2:
            return True
        if n % 2 == 0:
            return False
        
        # Check cache
        cached = self.cache.get(n)
        if cached is not None:
            self.stats.cache_hits += 1
            return cached
        
        # Improved binary pattern: exclude only obvious multiples
        # All odd numbers are valid candidates
        # Remove overly restrictive 3-bit filter
        
        # Optimized divisibility test
        limit = int(math.sqrt(n)) + 1
        
        # Test small common divisors
        small_primes = [3, 5, 7, 11, 13, 17, 19, 23, 29, 31]
        for p in small_primes:
            if p >= limit:
                break
            if n % p == 0:
                self.cache.put(n, False)
                self.code_db.add(self.binary_code(n))
                return False
        
        # Test remaining divisors (odd only)
        d = 37  # Start after small primes tested
        while d < limit:
            if n % d == 0:
                self.cache.put(n, False)
                self.code_db.add(self.binary_code(n))
                return False
            d += 2
        
        self.cache.put(n, True)
        return True
    
    def next_prime(self, n: int) -> int:
        """Find next prime with optimizations."""
        self.stats.total_candidates += 1
        
        if n < 2:
            return 2
        if n == 2:
            return 3
        if n % 2 == 0:
            n += 1
        
        while not self.is_prime_optimized(n):
            n += 2
            self.stats.total_candidates += 1
        
        return n
    
    def generate_primes(self, start: int = 1, limit: Optional[int] = None) -> Iterator[Tuple[int, int, int]]:
        """Prime generator with statistics."""
        start_time = time.time()
        n = start
        last_prime = None
        count = 0
        
        while self.running and (limit is None or count < limit):
            p = self.next_prime(n)
            count += 1
            
            # Calculate gap
            gap = 0 if last_prime is None else p - last_prime
            
            # Update statistics
            self._update_stats(gap, time.time() - start_time)
            
            yield count, p, gap
            
            # Periodic saving
            if count % self.save_interval == 0:
                self._save_database()
            
            # Progress logging
            if count % self.progress_interval == 0:
                self._log_progress(count, p)
            
            last_prime = p
            n = p + 1
        
        self._save_database()
    
    def generate_primes_to_count(self, target_count: int) -> list:
        """Generate a specific number of primes."""
        primes = []
        for count, prime, gap in self.generate_primes(1, target_count):
            primes.append(prime)
        return primes
    
    def _update_stats(self, gap: int, elapsed: float):
        """Update internal statistics."""
        self.stats.total_primes += 1
        self.stats.total_time = elapsed
        self.stats.cache_size = self.cache.size()
        
        if gap > 0:
            self.stats.max_gap = max(self.stats.max_gap, gap)
            self.stats.min_gap = min(self.stats.min_gap, gap)
            
            # Moving average for gap
            if self.stats.total_primes == 1:
                self.stats.avg_gap = gap
            else:
                alpha = 0.1  # Smoothing factor
                self.stats.avg_gap = (1 - alpha) * self.stats.avg_gap + alpha * gap
        
        if elapsed > 0:
            self.stats.primes_per_second = self.stats.total_primes / elapsed
    
    def _log_progress(self, count: int, prime: int):
        """Periodic progress logging."""
        logger.info(
            f"Progress: {count} primes generated | "
            f"Latest: {prime} | "
            f"Cache: {self.stats.cache_hits}/{self.cache.size()} | "
            f"Speed: {self.stats.primes_per_second:.2f} p/s"
        )
    
    def _print_final_stats(self):
        """Print final statistics."""
        print("\n" + "="*60)
        print("FINAL STATISTICS - BINARY PRIME ENGINE")
        print("="*60)
        print(f"Primes generated:      {self.stats.total_primes:,}")
        print(f"Candidates tested:     {self.stats.total_candidates:,}")
        print(f"Total time:            {self.stats.total_time:.2f}s")
        print(f"Primes per second:     {self.stats.primes_per_second:.2f}")
        print(f"Average gap:           {self.stats.avg_gap:.2f}")
        print(f"Maximum gap:           {self.stats.max_gap}")
        print(f"Minimum gap:           {self.stats.min_gap}")
        print(f"Cache hits:            {self.stats.cache_hits:,}")
        print(f"Cache size:            {self.stats.cache_size:,}")
        print(f"Binary codes saved:    {len(self.code_db):,}")
        print("="*60)

@contextmanager
def prime_engine_context(config: Dict[str, Any] = None):
    """Context manager for the prime engine."""
    engine = BinaryPrimeEngine(config)
    try:
        yield engine
    finally:
        engine._save_database()

def create_cli_parser() -> argparse.ArgumentParser:
    """Create CLI interface parser."""
    parser = argparse.ArgumentParser(
        description="Binary Prime Engine - Professional Prime Number Generator",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Usage examples:
  %(prog)s --start 1000 --limit 100          # 100 primes from 1000
  %(prog)s --start 1 --output primes.txt     # Save output to file
  %(prog)s --start 1 --format json           # JSON format output
  %(prog)s --start 1 --quiet                 # Results only, no progress
        """
    )
    
    parser.add_argument(
        '--start', '-s', type=int, default=1,
        help='Starting number (default: 1)'
    )
    parser.add_argument(
        '--limit', '-l', type=int,
        help='Maximum number of primes to generate'
    )
    parser.add_argument(
        '--output', '-o', type=str,
        help='Output file (default: stdout)'
    )
    parser.add_argument(
        '--format', '-f', choices=['text', 'json', 'csv'], default='text',
        help='Output format (default: text)'
    )
    parser.add_argument(
        '--cache-size', type=int, default=10000,
        help='Cache size (default: 10000)'
    )
    parser.add_argument(
        '--save-interval', type=int, default=1000,
        help='Save interval (default: 1000)'
    )
    parser.add_argument(
        '--progress-interval', type=int, default=100,
        help='Progress log interval (default: 100)'
    )
    parser.add_argument(
        '--quiet', '-q', action='store_true',
        help='Quiet mode (results only)'
    )
    parser.add_argument(
        '--verbose', '-v', action='store_true',
        help='Verbose output'
    )
    
    return parser

def format_output(count: int, prime: int, gap: int, format_type: str, binary_code: str) -> str:
    """Format output according to requested type."""
    if format_type == 'json':
        return json.dumps({
            'count': count,
            'prime': prime,
            'gap': gap,
            'binary': binary_code
        })
    elif format_type == 'csv':
        return f"{count},{prime},{gap},{binary_code}"
    else:  # text
        return f"p{count} = {prime} | gap dₙ = {gap} | bin: {binary_code}"

def main():
    """Main function with advanced CLI interface."""
    parser = create_cli_parser()
    args = parser.parse_args()
    
    # Configure logging
    if args.quiet:
        logging.getLogger().setLevel(logging.ERROR)
    elif args.verbose:
        logging.getLogger().setLevel(logging.DEBUG)
    
    # Engine configuration
    config = {
        'cache_size': args.cache_size,
        'save_interval': args.save_interval,
        'progress_interval': args.progress_interval
    }
    
    # Output file setup
    output_file = None
    if args.output:
        output_file = open(args.output, 'w')
        if args.format == 'csv':
            output_file.write("count,prime,gap,binary\n")
    
    try:
        with prime_engine_context(config) as engine:
            if not args.quiet:
                print("=== Binary Prime Engine PROFESSIONAL ===")
                print(f"Start: {args.start} | Limit: {args.limit or 'infinite'}")
                print(f"Format: {args.format} | Cache: {args.cache_size}")
                print("-" * 50)
            
            for count, prime, gap in engine.generate_primes(args.start, args.limit):
                binary = engine.binary_code(prime)
                output_line = format_output(count, prime, gap, args.format, binary)
                
                if output_file:
                    output_file.write(output_line + "\n")
                    output_file.flush()
                else:
                    print(output_line)
    
    except KeyboardInterrupt:
        logger.info("User interruption")
    finally:
        if output_file:
            output_file.close()

if __name__ == "__main__":
    main()
