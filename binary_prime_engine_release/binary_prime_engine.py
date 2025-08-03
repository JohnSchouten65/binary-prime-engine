import json
from pathlib import Path

DB_FILE = Path("binary_codes.json")

# Carica database codici binari conosciuti
if DB_FILE.exists():
    with open(DB_FILE, "r") as f:
        code_db = set(json.load(f))
else:
    code_db = set()

def binary_code(n: int, bits: int = None) -> str:
    """
    Codice binario adattivo del numero n.
    Se bits non è specificato, calcola automaticamente i bit necessari.
    """
    if bits is None:
        # Calcola automaticamente i bit necessari
        if n == 0:
            return "0"
        bits = n.bit_length()
        # Arrotonda a multipli di 4 per leggibilità (nibble)
        bits = ((bits + 3) // 4) * 4
        # Minimo 8 bit per numeri piccoli
        bits = max(bits, 8)
    
    return format(n, f'0{bits}b')

def next_prime_binary(n: int) -> int:
    """Trova il prossimo primo binario usando pattern e gap predittivi."""
    # Forza n a essere dispari
    if n < 2:
        return 2
    if n == 2:
        return 3
    if n % 2 == 0:
        n += 1

    while True:
        # Test di primalità per numeri dispari
        # Controllo binario con divisori dispari
        d = 3
        primo = True
        while d * d <= n:
            if n % d == 0:
                primo = False
                code_db.add(binary_code(n))
                break
            d += 2
        if primo:
            return n
        n += 2  # Salta ai prossimi dispari

def infinite_prime_engine(start: int = 1):
    """Motore binario infinito con pₙ e dₙ."""
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

if __name__ == "__main__":
    print("=== Binary Prime Engine INFINITA & BINARIA con pₙ e dₙ ===")
    try:
        start = int(input("Inserisci numero iniziale: "))
        infinite_prime_engine(start)
    except KeyboardInterrupt:
        print("\nInterrotto manualmente.")
