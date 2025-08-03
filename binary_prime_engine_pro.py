#!/usr/bin/env python3
"""
Binary Prime Engine - Versione Professionale per Uso Reale
========================================================

Motore avanzato per generazione di numeri primi con:
- Ottimizzazioni per performance
- Gestione memoria efficiente  
- Interfaccia CLI professionale
- Logging e monitoring
- Configurazione flessibile
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

# Configurazione logging
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
    """Statistiche del motore di generazione primi."""
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
    """Cache LRU per ottimizzare la ricerca di primi."""
    
    def __init__(self, max_size: int = 10000):
        self.max_size = max_size
        self.cache: Dict[int, bool] = {}
        self.access_order = deque()
        self.lock = threading.RLock()
    
    def get(self, n: int) -> Optional[bool]:
        """Recupera dal cache se il numero è primo."""
        with self.lock:
            if n in self.cache:
                # Sposta in coda (più recente)
                self.access_order.remove(n)
                self.access_order.append(n)
                return self.cache[n]
            return None
    
    def put(self, n: int, is_prime: bool):
        """Aggiunge al cache."""
        # Se cache disabilitato, non fare nulla
        if self.max_size == 0:
            return
            
        with self.lock:
            if n in self.cache:
                self.access_order.remove(n)
            elif len(self.cache) >= self.max_size:
                # Rimuovi il meno usato
                if self.access_order:  # Controlla che non sia vuoto
                    oldest = self.access_order.popleft()
                    del self.cache[oldest]
            
            self.cache[n] = is_prime
            self.access_order.append(n)
    
    def size(self) -> int:
        return len(self.cache)

class BinaryPrimeEngine:
    """Motore binario per generazione primi - Versione Professionale."""
    
    def __init__(self, config: Dict[str, Any] = None):
        self.config = config or {}
        self.db_file = Path(self.config.get('db_file', 'binary_codes.json'))
        self.cache = PrimeCache(self.config.get('cache_size', 10000))
        self.stats = PrimeStats()
        self.code_db: Set[str] = set()
        self.running = True
        self.save_interval = self.config.get('save_interval', 1000)
        self.progress_interval = self.config.get('progress_interval', 100)
        
        # Carica database esistente
        self._load_database()
        
        # Setup signal handlers per interruzione pulita
        signal.signal(signal.SIGINT, self._signal_handler)
        signal.signal(signal.SIGTERM, self._signal_handler)
    
    def _load_database(self):
        """Carica il database dei codici binari."""
        try:
            if self.db_file.exists():
                with open(self.db_file, "r") as f:
                    data = json.load(f)
                    if isinstance(data, list):
                        self.code_db = set(data)
                    else:
                        # Formato esteso con metadati
                        self.code_db = set(data.get('codes', []))
                        if 'stats' in data:
                            # Ripristina statistiche precedenti
                            for key, value in data['stats'].items():
                                if hasattr(self.stats, key):
                                    setattr(self.stats, key, value)
                logger.info(f"Database caricato: {len(self.code_db)} codici")
        except Exception as e:
            logger.warning(f"Errore caricamento database: {e}")
            self.code_db = set()
    
    def _save_database(self):
        """Salva il database dei codici binari con metadati."""
        try:
            data = {
                'codes': list(self.code_db),
                'stats': asdict(self.stats),
                'timestamp': time.time(),
                'version': '2.0'
            }
            
            with open(self.db_file, "w") as f:
                json.dump(data, f, indent=2)
            logger.debug(f"Database salvato: {len(self.code_db)} codici")
        except Exception as e:
            logger.error(f"Errore salvataggio database: {e}")
    
    def _signal_handler(self, signum, frame):
        """Gestisce interruzione pulita."""
        logger.info("Interruzione ricevuta, salvando dati...")
        self.running = False
        self._save_database()
        self._print_final_stats()
        sys.exit(0)
    
    def binary_code(self, n: int, bits: int = 16) -> str:
        """Genera codice binario compatto ottimizzato."""
        return format(n & ((1 << bits) - 1), f'0{bits}b')
    
    def is_prime_optimized(self, n: int) -> bool:
        """Test di primalità ottimizzato con cache e pattern binari."""
        if n < 2:
            return False
        if n == 2:
            return True
        if n % 2 == 0:
            return False
        
        # Controlla cache
        cached = self.cache.get(n)
        if cached is not None:
            self.stats.cache_hits += 1
            return cached
        
        # Pattern binario migliorato: escludi solo multipli ovvi
        # Tutti i numeri dispari sono candidati validi
        # Rimuoviamo il filtro troppo restrittivo sui 3 bit
        
        # Test divisibilità ottimizzato
        limit = int(math.sqrt(n)) + 1
        
        # Test divisori piccoli comuni
        small_primes = [3, 5, 7, 11, 13, 17, 19, 23, 29, 31]
        for p in small_primes:
            if p >= limit:
                break
            if n % p == 0:
                self.cache.put(n, False)
                self.code_db.add(self.binary_code(n))
                return False
        
        # Test divisori restanti (solo dispari)
        d = 37  # Inizia dopo i primi piccoli testati
        while d < limit:
            if n % d == 0:
                self.cache.put(n, False)
                self.code_db.add(self.binary_code(n))
                return False
            d += 2
        
        self.cache.put(n, True)
        return True
    
    def next_prime(self, n: int) -> int:
        """Trova il prossimo primo con ottimizzazioni."""
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
        """Generatore di primi con statistiche."""
        start_time = time.time()
        n = start
        last_prime = None
        count = 0
        
        while self.running and (limit is None or count < limit):
            p = self.next_prime(n)
            count += 1
            
            # Calcola gap
            gap = 0 if last_prime is None else p - last_prime
            
            # Aggiorna statistiche
            self._update_stats(gap, time.time() - start_time)
            
            yield count, p, gap
            
            # Salvataggio periodico
            if count % self.save_interval == 0:
                self._save_database()
            
            # Progress logging
            if count % self.progress_interval == 0:
                self._log_progress(count, p)
            
            last_prime = p
            n = p + 1
        
        self._save_database()
    
    def _update_stats(self, gap: int, elapsed: float):
        """Aggiorna statistiche interne."""
        self.stats.total_primes += 1
        self.stats.total_time = elapsed
        self.stats.cache_size = self.cache.size()
        
        if gap > 0:
            self.stats.max_gap = max(self.stats.max_gap, gap)
            self.stats.min_gap = min(self.stats.min_gap, gap)
            
            # Media mobile per gap
            if self.stats.total_primes == 1:
                self.stats.avg_gap = gap
            else:
                alpha = 0.1  # Fattore di smoothing
                self.stats.avg_gap = (1 - alpha) * self.stats.avg_gap + alpha * gap
        
        if elapsed > 0:
            self.stats.primes_per_second = self.stats.total_primes / elapsed
    
    def _log_progress(self, count: int, prime: int):
        """Log periodico del progresso."""
        logger.info(
            f"Progress: {count} primi generati | "
            f"Ultimo: {prime} | "
            f"Cache: {self.stats.cache_hits}/{self.cache.size()} | "
            f"Speed: {self.stats.primes_per_second:.2f} p/s"
        )
    
    def _print_final_stats(self):
        """Stampa statistiche finali."""
        print("\n" + "="*60)
        print("STATISTICHE FINALI - BINARY PRIME ENGINE")
        print("="*60)
        print(f"Primi generati:        {self.stats.total_primes:,}")
        print(f"Candidati testati:     {self.stats.total_candidates:,}")
        print(f"Tempo totale:          {self.stats.total_time:.2f}s")
        print(f"Primi per secondo:     {self.stats.primes_per_second:.2f}")
        print(f"Gap medio:             {self.stats.avg_gap:.2f}")
        print(f"Gap massimo:           {self.stats.max_gap}")
        print(f"Gap minimo:            {self.stats.min_gap}")
        print(f"Cache hits:            {self.stats.cache_hits:,}")
        print(f"Cache size:            {self.stats.cache_size:,}")
        print(f"Codici binari salvati: {len(self.code_db):,}")
        print("="*60)

@contextmanager
def prime_engine_context(config: Dict[str, Any] = None):
    """Context manager per il motore primi."""
    engine = BinaryPrimeEngine(config)
    try:
        yield engine
    finally:
        engine._save_database()

def create_cli_parser() -> argparse.ArgumentParser:
    """Crea parser per interfaccia CLI."""
    parser = argparse.ArgumentParser(
        description="Binary Prime Engine - Generatore Professionale di Numeri Primi",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Esempi d'uso:
  %(prog)s --start 1000 --limit 100          # 100 primi da 1000
  %(prog)s --start 1 --output primes.txt     # Salva output su file
  %(prog)s --start 1 --format json           # Output in formato JSON
  %(prog)s --start 1 --quiet                 # Solo risultati, no progress
        """
    )
    
    parser.add_argument(
        '--start', '-s', type=int, default=1,
        help='Numero di partenza (default: 1)'
    )
    parser.add_argument(
        '--limit', '-l', type=int,
        help='Numero massimo di primi da generare'
    )
    parser.add_argument(
        '--output', '-o', type=str,
        help='File di output (default: stdout)'
    )
    parser.add_argument(
        '--format', '-f', choices=['text', 'json', 'csv'], default='text',
        help='Formato di output (default: text)'
    )
    parser.add_argument(
        '--cache-size', type=int, default=10000,
        help='Dimensione cache (default: 10000)'
    )
    parser.add_argument(
        '--save-interval', type=int, default=1000,
        help='Intervallo di salvataggio (default: 1000)'
    )
    parser.add_argument(
        '--progress-interval', type=int, default=100,
        help='Intervallo progress log (default: 100)'
    )
    parser.add_argument(
        '--quiet', '-q', action='store_true',
        help='Modalità silenziosa (solo risultati)'
    )
    parser.add_argument(
        '--verbose', '-v', action='store_true',
        help='Output verboso'
    )
    
    return parser

def format_output(count: int, prime: int, gap: int, format_type: str, binary_code: str) -> str:
    """Formatta l'output secondo il tipo richiesto."""
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
    """Funzione principale con interfaccia CLI avanzata."""
    parser = create_cli_parser()
    args = parser.parse_args()
    
    # Configura logging
    if args.quiet:
        logging.getLogger().setLevel(logging.ERROR)
    elif args.verbose:
        logging.getLogger().setLevel(logging.DEBUG)
    
    # Configurazione motore
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
                print("=== Binary Prime Engine PROFESSIONALE ===")
                print(f"Start: {args.start} | Limit: {args.limit or 'infinito'}")
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
        logger.info("Interruzione utente")
    finally:
        if output_file:
            output_file.close()

if __name__ == "__main__":
    main()
