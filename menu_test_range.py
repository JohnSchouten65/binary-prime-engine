#!/usr/bin/env python3
"""
Menu Interattivo per Test Range - Binary Prime Engine
=====================================================
Menu completo per testare il motore in range specifici con varie opzioni.
"""

import time
import sys
import os
from pathlib import Path
from binary_prime_engine import next_prime_binary, binary_code

class PrimeTestMenu:
    def __init__(self):
        self.results = []
        
    def clear_screen(self):
        """Pulisce lo schermo."""
        os.system('clear' if os.name == 'posix' else 'cls')
    
    def print_header(self):
        """Stampa l'header del menu."""
        print("=" * 70)
        print("🔬 BINARY PRIME ENGINE - MENU TEST RANGE")
        print("=" * 70)
        print("Motore testato e affidabile fino a 1 trilione!")
        print()
    
    def print_menu(self):
        """Stampa il menu principale."""
        print("📋 OPZIONI DISPONIBILI:")
        print()
        print("1️⃣  Test Range Personalizzato")
        print("2️⃣  Test Range Predefiniti")
        print("3️⃣  Test Performance Specifico")
        print("4️⃣  Test Validazione Completa")
        print("5️⃣  Generazione Continua con Controlli")
        print("6️⃣  Benchmark Velocità")
        print("7️⃣  Visualizza Ultimi Risultati")
        print("8️⃣  Test Numeri Giganti (Miliardi+)")
        print("9️⃣  Export Risultati")
        print("0️⃣  Esci")
        print()
    
    def get_input(self, prompt, input_type=str, default=None):
        """Input sicuro con gestione errori."""
        while True:
            try:
                if default is not None:
                    user_input = input(f"{prompt} [{default}]: ").strip()
                    if not user_input:
                        return default
                else:
                    user_input = input(f"{prompt}: ").strip()
                
                if input_type == int:
                    return int(user_input)
                elif input_type == float:
                    return float(user_input)
                else:
                    return user_input
                    
            except ValueError:
                print("❌ Input non valido, riprova.")
            except KeyboardInterrupt:
                print("\n🚫 Operazione annullata.")
                return None
    
    def test_custom_range(self):
        """Test range personalizzato."""
        self.clear_screen()
        self.print_header()
        print("1️⃣  TEST RANGE PERSONALIZZATO")
        print("=" * 40)
        
        start = self.get_input("Numero di partenza", int, 1)
        if start is None:
            return
            
        count = self.get_input("Quanti primi generare", int, 10)
        if count is None:
            return
            
        show_binary = self.get_input("Mostrare codici binari? (s/n)", str, "s").lower() == 's'
        show_gaps = self.get_input("Mostrare gap tra primi? (s/n)", str, "s").lower() == 's'
        
        print(f"\n🚀 Generando {count} primi da {start:,}...")
        print("-" * 60)
        
        total_time = 0
        n = start
        last_prime = None
        
        for i in range(count):
            start_time = time.time()
            p = next_prime_binary(n)
            elapsed = time.time() - start_time
            total_time += elapsed
            
            # Calcola gap
            gap = p - last_prime if last_prime else 0
            
            # Formato output
            output = f"p{i+1:2d} = {p:>12,}"
            
            if show_gaps:
                output += f" | gap = {gap:>3d}"
            
            if show_binary:
                bin_code = binary_code(p, 16)
                output += f" | bin: {bin_code}"
            
            output += f" | {elapsed*1000:>6.2f}ms"
            
            print(output)
            
            last_prime = p
            n = p + 1
        
        avg_time = total_time / count
        print("-" * 60)
        print(f"✅ Completato! Tempo totale: {total_time:.3f}s")
        print(f"⏱️  Tempo medio per primo: {avg_time*1000:.2f}ms")
        
        # Salva risultati
        self.results.append({
            'tipo': 'Range Personalizzato',
            'start': start,
            'count': count,
            'tempo_totale': total_time,
            'tempo_medio': avg_time
        })
        
        input("\n📝 Premi INVIO per continuare...")
    
    def test_predefined_ranges(self):
        """Test range predefiniti."""
        self.clear_screen()
        self.print_header()
        print("2️⃣  TEST RANGE PREDEFINITI")
        print("=" * 40)
        
        ranges = [
            ("Piccoli (1-1K)", 1, 1000),
            ("Medi (1K-10K)", 1000, 10000),
            ("Grandi (10K-100K)", 10000, 100000),
            ("Molto Grandi (100K-1M)", 100000, 1000000),
            ("Enormi (1M-10M)", 1000000, 10000000),
        ]
        
        print("Scegli un range:")
        for i, (desc, start, end) in enumerate(ranges, 1):
            print(f"{i}. {desc} ({start:,} - {end:,})")
        
        choice = self.get_input("Scelta (1-5)", int)
        if choice is None or choice < 1 or choice > 5:
            return
        
        desc, start, end = ranges[choice - 1]
        sample_size = self.get_input("Numeri da testare nel range", int, 20)
        
        print(f"\n🔍 Testando range {desc}...")
        print(f"📊 Campionando {sample_size} numeri tra {start:,} e {end:,}")
        print("-" * 60)
        
        # Genera numeri da testare
        if sample_size >= (end - start):
            test_numbers = list(range(start, end + 1))
        else:
            step = (end - start) // sample_size
            test_numbers = list(range(start, end, step))[:sample_size]
        
        total_time = 0
        errors = 0
        
        for i, n in enumerate(test_numbers):
            start_time = time.time()
            try:
                p = next_prime_binary(n)
                elapsed = time.time() - start_time
                total_time += elapsed
                
                print(f"{i+1:3d}. Da {n:>10,} → {p:>10,} in {elapsed*1000:>6.2f}ms")
                
            except Exception as e:
                errors += 1
                print(f"{i+1:3d}. ❌ Errore da {n:,}: {e}")
        
        avg_time = total_time / len(test_numbers) if test_numbers else 0
        
        print("-" * 60)
        print(f"✅ Range {desc} completato!")
        print(f"📊 Testati: {len(test_numbers)} numeri")
        print(f"❌ Errori: {errors}")
        print(f"⏱️  Tempo totale: {total_time:.3f}s")
        print(f"⏱️  Tempo medio: {avg_time*1000:.2f}ms")
        
        input("\n📝 Premi INVIO per continuare...")
    
    def test_performance_specific(self):
        """Test performance su numeri specifici."""
        self.clear_screen()
        self.print_header()
        print("3️⃣  TEST PERFORMANCE SPECIFICO")
        print("=" * 40)
        
        big_numbers = [
            1000, 10000, 100000, 1000000,
            10000000, 100000000, 1000000000
        ]
        
        print("Numeri di test predefiniti:")
        for i, num in enumerate(big_numbers, 1):
            print(f"{i}. {num:,}")
        print("8. Numero personalizzato")
        
        choice = self.get_input("Scelta (1-8)", int)
        if choice is None:
            return
        
        if choice == 8:
            test_num = self.get_input("Inserisci numero", int)
            if test_num is None:
                return
            test_numbers = [test_num]
        elif 1 <= choice <= 7:
            test_numbers = [big_numbers[choice - 1]]
        else:
            return
        
        repeat = self.get_input("Quante volte ripetere il test", int, 3)
        
        print(f"\n🎯 Test performance su {test_numbers[0]:,}")
        print(f"🔄 Ripetizioni: {repeat}")
        print("-" * 60)
        
        times = []
        for test_num in test_numbers:
            for i in range(repeat):
                start_time = time.time()
                p = next_prime_binary(test_num)
                elapsed = time.time() - start_time
                times.append(elapsed)
                
                print(f"Run {i+1}: {test_num:,} → {p:,} in {elapsed*1000:.3f}ms")
        
        avg_time = sum(times) / len(times)
        min_time = min(times)
        max_time = max(times)
        
        print("-" * 60)
        print(f"📊 STATISTICHE PERFORMANCE:")
        print(f"   Tempo medio: {avg_time*1000:.3f}ms")
        print(f"   Tempo minimo: {min_time*1000:.3f}ms")
        print(f"   Tempo massimo: {max_time*1000:.3f}ms")
        
        input("\n📝 Premi INVIO per continuare...")
    
    def test_giant_numbers(self):
        """Test numeri giganti."""
        self.clear_screen()
        self.print_header()
        print("8️⃣  TEST NUMERI GIGANTI (MILIARDI+)")
        print("=" * 40)
        
        giant_numbers = [
            ("1 Miliardo", 1_000_000_000),
            ("10 Miliardi", 10_000_000_000),
            ("100 Miliardi", 100_000_000_000),
            ("1 Trilione", 1_000_000_000_000),
            ("10 Trilioni", 10_000_000_000_000),
        ]
        
        print("⚠️  ATTENZIONE: I numeri molto grandi possono richiedere tempo!")
        print("\nScegli un numero gigante:")
        for i, (desc, num) in enumerate(giant_numbers, 1):
            print(f"{i}. {desc} ({num:,})")
        print("6. Numero personalizzato")
        
        choice = self.get_input("Scelta (1-6)", int)
        if choice is None:
            return
        
        if choice == 6:
            test_num = self.get_input("Inserisci numero gigante", int)
            if test_num is None:
                return
            desc = f"Personalizzato ({test_num:,})"
        elif 1 <= choice <= 5:
            desc, test_num = giant_numbers[choice - 1]
        else:
            return
        
        print(f"\n🚀 Testando {desc}...")
        print("⏳ Questo potrebbe richiedere tempo...")
        
        try:
            start_time = time.time()
            p = next_prime_binary(test_num)
            elapsed = time.time() - start_time
            
            print(f"✅ SUCCESSO!")
            print(f"   Numero di partenza: {test_num:,}")
            print(f"   Primo trovato: {p:,}")
            print(f"   Tempo impiegato: {elapsed:.3f} secondi")
            
            if elapsed < 0.1:
                print("🚀 VELOCISSIMO!")
            elif elapsed < 1:
                print("⚡ Molto veloce!")
            elif elapsed < 10:
                print("👍 Buona performance")
            else:
                print("🐌 Lento ma funzionante")
                
        except KeyboardInterrupt:
            print("\n🚫 Test interrotto dall'utente")
        except Exception as e:
            print(f"\n❌ Errore: {e}")
        
        input("\n📝 Premi INVIO per continuare...")
    
    def show_results(self):
        """Mostra gli ultimi risultati."""
        self.clear_screen()
        self.print_header()
        print("7️⃣  ULTIMI RISULTATI")
        print("=" * 40)
        
        if not self.results:
            print("📭 Nessun risultato salvato ancora.")
            print("Esegui alcuni test per vedere i risultati qui!")
        else:
            print(f"📊 Risultati degli ultimi {len(self.results)} test:")
            print()
            for i, result in enumerate(self.results, 1):
                print(f"{i}. {result['tipo']}")
                print(f"   Start: {result.get('start', 'N/A')}")
                print(f"   Count: {result.get('count', 'N/A')}")
                print(f"   Tempo totale: {result.get('tempo_totale', 0):.3f}s")
                print(f"   Tempo medio: {result.get('tempo_medio', 0)*1000:.2f}ms")
                print()
        
        input("📝 Premi INVIO per continuare...")
    
    def run(self):
        """Esegue il menu principale."""
        while True:
            self.clear_screen()
            self.print_header()
            self.print_menu()
            
            choice = self.get_input("Scegli un'opzione (0-9)", str, "0")
            
            if choice == "1":
                self.test_custom_range()
            elif choice == "2":
                self.test_predefined_ranges()
            elif choice == "3":
                self.test_performance_specific()
            elif choice == "4":
                print("🔄 Avviando test validazione completa...")
                os.system(f'"{sys.executable}" test_prime_validation.py 10000')
                input("\n📝 Premi INVIO per continuare...")
            elif choice == "5":
                print("🔄 Avviando motore continuo...")
                from binary_prime_engine import infinite_prime_engine
                try:
                    start = self.get_input("Numero di partenza", int, 1)
                    infinite_prime_engine(start)
                except KeyboardInterrupt:
                    print("\n🚫 Generazione interrotta")
                input("\n📝 Premi INVIO per continuare...")
            elif choice == "6":
                print("🔄 Avviando benchmark...")
                os.system(f'"{sys.executable}" benchmark.py')
                input("\n📝 Premi INVIO per continuare...")
            elif choice == "7":
                self.show_results()
            elif choice == "8":
                self.test_giant_numbers()
            elif choice == "9":
                print("💾 Export risultati non ancora implementato")
                input("📝 Premi INVIO per continuare...")
            elif choice == "0":
                print("\n👋 Arrivederci!")
                break
            else:
                print("❌ Scelta non valida!")
                time.sleep(1)

def main():
    """Funzione principale."""
    try:
        menu = PrimeTestMenu()
        menu.run()
    except KeyboardInterrupt:
        print("\n\n🚫 Menu interrotto dall'utente. Arrivederci!")
    except Exception as e:
        print(f"\n❌ Errore nel menu: {e}")

if __name__ == "__main__":
    main()
