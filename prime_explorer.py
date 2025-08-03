#!/usr/bin/env python3
"""
🔢 PRIME EXPLORER - Complete Prime Number Research Tool
Advanced menu system for exploring prime numbers with comprehensive features.
"""

import os
import sys
import time
import json
import math
import random
from pathlib import Path
from typing import List, Tuple, Dict, Optional
from binary_prime_engine_pro import BinaryPrimeEngine
from binary_prime_engine import binary_code, next_prime_binary

class PrimeExplorer:
    """Complete prime number exploration and research tool."""
    
    def __init__(self):
        self.engine = BinaryPrimeEngine()
        self.history = []
        self.favorites = set()
        self.load_favorites()
    
    def load_favorites(self):
        """Load favorite primes from file."""
        try:
            favorites_file = Path("prime_favorites.json")
            if favorites_file.exists():
                with open(favorites_file, 'r') as f:
                    self.favorites = set(json.load(f))
        except:
            self.favorites = set()
    
    def save_favorites(self):
        """Save favorite primes to file."""
        try:
            with open("prime_favorites.json", 'w') as f:
                json.dump(list(self.favorites), f)
        except:
            pass
    
    def clear_screen(self):
        """Clear terminal screen."""
        os.system('clear' if os.name == 'posix' else 'cls')
    
    def print_header(self, title: str):
        """Print formatted header."""
        self.clear_screen()
        print("=" * 80)
        print(f"🔢 PRIME EXPLORER - {title}")
        print("=" * 80)
        print()
    
    def print_menu(self, title: str, options: List[str]):
        """Print formatted menu."""
        self.print_header(title)
        for i, option in enumerate(options, 1):
            print(f"{i:2d}. {option}")
        print(f"{len(options) + 1:2d}. Back to Main Menu")
        print(f" 0. Exit Program")
        print("-" * 80)
    
    def get_user_choice(self, max_choice: int) -> int:
        """Get and validate user choice."""
        while True:
            try:
                choice = input(f"Enter your choice (0-{max_choice}): ").strip()
                if choice == '':
                    continue
                choice = int(choice)
                if 0 <= choice <= max_choice:
                    return choice
                print(f"Please enter a number between 0 and {max_choice}")
            except ValueError:
                print("Please enter a valid number")
            except KeyboardInterrupt:
                return 0
    
    def pause(self):
        """Pause for user input."""
        input("\nPress Enter to continue...")
    
    # =================================================================
    # MAIN MENU
    # =================================================================
    
    def main_menu(self):
        """Main menu for prime exploration."""
        while True:
            options = [
                "🔍 Prime Search & Discovery",
                "🧮 Prime Calculations & Analysis",
                "📊 Prime Statistics & Patterns",
                "🎯 Prime Tests & Verification",
                "🎲 Prime Games & Challenges",
                "📈 Prime Performance & Benchmarks",
                "💾 Data Management & Export",
                "🎨 Prime Visualization & Binary Art",
                "📚 Prime Education & Learning",
                "⚙️  Advanced Research Tools"
            ]
            
            self.print_menu("MAIN MENU", options)
            choice = self.get_user_choice(len(options) + 1)
            
            if choice == 0:
                self.save_favorites()
                print("\n🔢 Thank you for using Prime Explorer! Goodbye!")
                sys.exit(0)
            elif choice == 1:
                self.search_menu()
            elif choice == 2:
                self.calculations_menu()
            elif choice == 3:
                self.statistics_menu()
            elif choice == 4:
                self.tests_menu()
            elif choice == 5:
                self.games_menu()
            elif choice == 6:
                self.performance_menu()
            elif choice == 7:
                self.data_menu()
            elif choice == 8:
                self.visualization_menu()
            elif choice == 9:
                self.education_menu()
            elif choice == 10:
                self.research_menu()
            elif choice == len(options) + 1:
                continue
    
    # =================================================================
    # SEARCH & DISCOVERY MENU
    # =================================================================
    
    def search_menu(self):
        """Prime search and discovery menu."""
        while True:
            options = [
                "🔎 Find Next Prime",
                "🔍 Find Previous Prime", 
                "📍 Find Prime at Position (nth prime)",
                "🎯 Find Prime in Range",
                "🌟 Find Twin Primes",
                "💎 Find Cousin Primes",
                "🔗 Find Prime Chains",
                "🎲 Generate Random Prime",
                "🏆 Find Record-Breaking Primes",
                "💫 Find Special Primes (Mersenne, Fermat, etc.)"
            ]
            
            self.print_menu("PRIME SEARCH & DISCOVERY", options)
            choice = self.get_user_choice(len(options) + 1)
            
            if choice == 0:
                return
            elif choice == 1:
                self.find_next_prime()
            elif choice == 2:
                self.find_previous_prime()
            elif choice == 3:
                self.find_nth_prime()
            elif choice == 4:
                self.find_primes_in_range()
            elif choice == 5:
                self.find_twin_primes()
            elif choice == 6:
                self.find_cousin_primes()
            elif choice == 7:
                self.find_prime_chains()
            elif choice == 8:
                self.generate_random_prime()
            elif choice == 9:
                self.find_record_primes()
            elif choice == 10:
                self.find_special_primes()
            elif choice == len(options) + 1:
                return
    
    def find_next_prime(self):
        """Find the next prime after a given number."""
        self.print_header("FIND NEXT PRIME")
        try:
            n = int(input("Enter a number: "))
            print(f"\n🔍 Searching for the next prime after {n:,}...")
            
            start_time = time.time()
            prime = next_prime_binary(n + 1)
            elapsed = time.time() - start_time
            
            print(f"\n✅ Next prime: {prime:,}")
            print(f"📏 Gap: {prime - n}")
            print(f"⏱️  Time: {elapsed:.4f} seconds")
            print(f"🔢 Binary: {binary_code(prime)}")
            
            # Add to history and offer to save as favorite
            self.history.append(('next_prime', n, prime))
            self.offer_favorite(prime)
            
        except ValueError:
            print("❌ Please enter a valid number")
        except Exception as e:
            print(f"❌ Error: {e}")
        
        self.pause()
    
    def find_previous_prime(self):
        """Find the previous prime before a given number."""
        self.print_header("FIND PREVIOUS PRIME")
        try:
            n = int(input("Enter a number: "))
            if n <= 2:
                print("❌ There is no prime before 2")
                self.pause()
                return
            
            print(f"\n🔍 Searching for the previous prime before {n:,}...")
            
            start_time = time.time()
            # Search backwards
            candidate = n - 1 if n > 2 else 1
            while candidate > 1:
                if self.is_prime(candidate):
                    prime = candidate
                    break
                candidate -= 1
            else:
                print("❌ No prime found")
                self.pause()
                return
            
            elapsed = time.time() - start_time
            
            print(f"\n✅ Previous prime: {prime:,}")
            print(f"📏 Gap: {n - prime}")
            print(f"⏱️  Time: {elapsed:.4f} seconds")
            print(f"🔢 Binary: {binary_code(prime)}")
            
            self.history.append(('previous_prime', n, prime))
            self.offer_favorite(prime)
            
        except ValueError:
            print("❌ Please enter a valid number")
        except Exception as e:
            print(f"❌ Error: {e}")
        
        self.pause()
    
    def find_nth_prime(self):
        """Find the nth prime number."""
        self.print_header("FIND NTH PRIME")
        try:
            n = int(input("Enter position (n): "))
            if n < 1:
                print("❌ Position must be positive")
                self.pause()
                return
            
            print(f"\n🔍 Finding the {n:,}th prime number...")
            
            start_time = time.time()
            primes = self.engine.generate_primes_to_count(n)
            elapsed = time.time() - start_time
            
            if len(primes) >= n:
                prime = primes[n-1]
                print(f"\n✅ The {n:,}th prime: {prime:,}")
                print(f"⏱️  Time: {elapsed:.4f} seconds")
                print(f"🔢 Binary: {binary_code(prime)}")
                
                if n > 1:
                    gap = prime - primes[n-2]
                    print(f"📏 Gap from previous: {gap}")
                
                self.history.append(('nth_prime', n, prime))
                self.offer_favorite(prime)
            else:
                print(f"❌ Could not generate {n} primes")
            
        except ValueError:
            print("❌ Please enter a valid number")
        except Exception as e:
            print(f"❌ Error: {e}")
        
        self.pause()
    
    def find_primes_in_range(self):
        """Find all primes in a given range."""
        self.print_header("FIND PRIMES IN RANGE")
        try:
            start = int(input("Enter start number: "))
            end = int(input("Enter end number: "))
            
            if start > end:
                start, end = end, start
            
            print(f"\n🔍 Finding primes between {start:,} and {end:,}...")
            
            start_time = time.time()
            primes = []
            current = max(start, 2)
            
            while current <= end and len(primes) < 1000:  # Limit to prevent overflow
                if self.is_prime(current):
                    primes.append(current)
                current += 1
            
            elapsed = time.time() - start_time
            
            print(f"\n✅ Found {len(primes)} primes:")
            if len(primes) <= 20:
                for prime in primes:
                    print(f"  {prime:,}")
            else:
                print(f"  First 10: {', '.join(map(str, primes[:10]))}")
                print(f"  Last 10:  {', '.join(map(str, primes[-10:]))}")
            
            if primes:
                print(f"\n📊 Statistics:")
                print(f"  Smallest: {min(primes):,}")
                print(f"  Largest: {max(primes):,}")
                print(f"  Average gap: {(max(primes) - min(primes)) / max(1, len(primes) - 1):.2f}")
                
            print(f"⏱️  Time: {elapsed:.4f} seconds")
            
            self.history.append(('range_primes', (start, end), primes))
            
        except ValueError:
            print("❌ Please enter valid numbers")
        except Exception as e:
            print(f"❌ Error: {e}")
        
        self.pause()
    
    def find_twin_primes(self):
        """Find twin prime pairs."""
        self.print_header("FIND TWIN PRIMES")
        try:
            start = int(input("Enter start number: "))
            count = int(input("Enter number of twin prime pairs to find: "))
            
            print(f"\n🔍 Finding {count} twin prime pairs starting from {start:,}...")
            
            start_time = time.time()
            twin_pairs = []
            current = max(start, 3)
            
            while len(twin_pairs) < count and current < start + 1000000:
                if self.is_prime(current) and self.is_prime(current + 2):
                    twin_pairs.append((current, current + 2))
                current += 1
            
            elapsed = time.time() - start_time
            
            print(f"\n✅ Found {len(twin_pairs)} twin prime pairs:")
            for i, (p1, p2) in enumerate(twin_pairs):
                print(f"  {i+1:2d}. ({p1:,}, {p2:,})")
            
            print(f"⏱️  Time: {elapsed:.4f} seconds")
            
            self.history.append(('twin_primes', start, twin_pairs))
            
        except ValueError:
            print("❌ Please enter valid numbers")
        except Exception as e:
            print(f"❌ Error: {e}")
        
        self.pause()
    
    def find_cousin_primes(self):
        """Find cousin prime pairs (difference of 4)."""
        self.print_header("FIND COUSIN PRIMES")
        try:
            start = int(input("Enter start number: "))
            count = int(input("Enter number of cousin prime pairs to find: "))
            
            print(f"\n🔍 Finding {count} cousin prime pairs starting from {start:,}...")
            
            start_time = time.time()
            cousin_pairs = []
            current = max(start, 3)
            
            while len(cousin_pairs) < count and current < start + 1000000:
                if self.is_prime(current) and self.is_prime(current + 4):
                    cousin_pairs.append((current, current + 4))
                current += 1
            
            elapsed = time.time() - start_time
            
            print(f"\n✅ Found {len(cousin_pairs)} cousin prime pairs:")
            for i, (p1, p2) in enumerate(cousin_pairs):
                print(f"  {i+1:2d}. ({p1:,}, {p2:,})")
            
            print(f"⏱️  Time: {elapsed:.4f} seconds")
            
            self.history.append(('cousin_primes', start, cousin_pairs))
            
        except ValueError:
            print("❌ Please enter valid numbers")
        except Exception as e:
            print(f"❌ Error: {e}")
        
        self.pause()
    
    def offer_favorite(self, prime: int):
        """Offer to add prime to favorites."""
        if prime not in self.favorites:
            response = input(f"💝 Add {prime:,} to favorites? (y/n): ").strip().lower()
            if response == 'y':
                self.favorites.add(prime)
                print("✅ Added to favorites!")
    
    # =================================================================
    # UTILITY METHODS
    # =================================================================
    
    def is_prime(self, n: int) -> bool:
        """Check if a number is prime."""
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
    
    # =================================================================
    # CALCULATIONS MENU - IMPLEMENTED
    # =================================================================
    
    def calculations_menu(self):
        """Prime calculations and analysis menu."""
        while True:
            options = [
                "➕ Prime Addition & Subtraction",
                "✖️  Prime Multiplication & Division",
                "📊 Prime Factorization",
                "🧮 Goldbach Conjecture Test",
                "📐 Prime Number Theorem Approximations", 
                "🔢 Prime Counting Function π(x)",
                "📏 Prime Gap Analysis",
                "🎯 Primality Probability",
                "💫 Prime Powers & Roots",
                "🧬 Prime Digit Analysis"
            ]
            
            self.print_menu("PRIME CALCULATIONS & ANALYSIS", options)
            choice = self.get_user_choice(len(options) + 1)
            
            if choice == 0 or choice == len(options) + 1:
                return
            elif choice == 1:
                self.prime_arithmetic()
            elif choice == 2:
                self.prime_multiplication()
            elif choice == 3:
                self.prime_factorization()
            elif choice == 4:
                self.goldbach_test()
            elif choice == 5:
                self.prime_theorem_approximation()
            elif choice == 6:
                self.prime_counting()
            elif choice == 7:
                self.prime_gap_analysis()
            elif choice == 8:
                self.primality_probability()
            elif choice == 9:
                self.prime_powers()
            elif choice == 10:
                self.prime_digit_analysis()
    
    def prime_arithmetic(self):
        """Prime arithmetic operations."""
        self.print_header("PRIME ARITHMETIC")
        try:
            p1 = int(input("Enter first prime: "))
            p2 = int(input("Enter second prime: "))
            
            if not (self.is_prime(p1) and self.is_prime(p2)):
                print("❌ Both numbers must be prime!")
                self.pause()
                return
            
            print(f"\n🧮 Arithmetic with primes {p1:,} and {p2:,}:")
            print(f"  Addition: {p1:,} + {p2:,} = {p1 + p2:,}")
            print(f"  Subtraction: {p1:,} - {p2:,} = {abs(p1 - p2):,}")
            print(f"  Multiplication: {p1:,} × {p2:,} = {p1 * p2:,}")
            if p2 != 0:
                print(f"  Division: {p1:,} ÷ {p2:,} = {p1 / p2:.6f}")
            
            # Check if results are prime
            sum_result = p1 + p2
            diff_result = abs(p1 - p2)
            
            print(f"\n🔍 Prime check of results:")
            print(f"  {sum_result:,} is {'prime ✅' if self.is_prime(sum_result) else 'composite ❌'}")
            if diff_result > 1:
                print(f"  {diff_result:,} is {'prime ✅' if self.is_prime(diff_result) else 'composite ❌'}")
            
        except ValueError:
            print("❌ Please enter valid numbers")
        except Exception as e:
            print(f"❌ Error: {e}")
        
        self.pause()
    
    def goldbach_test(self):
        """Test Goldbach's conjecture for even numbers."""
        self.print_header("GOLDBACH CONJECTURE TEST")
        print("🧮 Goldbach's Conjecture: Every even integer > 2 can be expressed")
        print("   as the sum of two primes.\n")
        
        try:
            n = int(input("Enter an even number > 2: "))
            
            if n <= 2 or n % 2 != 0:
                print("❌ Please enter an even number greater than 2")
                self.pause()
                return
            
            print(f"\n🔍 Finding prime pairs that sum to {n:,}...")
            
            pairs = []
            for p1 in range(2, n // 2 + 1):
                if self.is_prime(p1):
                    p2 = n - p1
                    if self.is_prime(p2):
                        pairs.append((p1, p2))
            
            if pairs:
                print(f"\n✅ Found {len(pairs)} prime pairs:")
                for i, (p1, p2) in enumerate(pairs[:10], 1):  # Show first 10
                    print(f"  {i:2d}. {p1:,} + {p2:,} = {n:,}")
                
                if len(pairs) > 10:
                    print(f"  ... and {len(pairs) - 10} more pairs")
                
                print(f"\n🎯 Goldbach's conjecture confirmed for {n:,}!")
            else:
                print(f"\n❌ No prime pairs found! (This would disprove Goldbach's conjecture)")
            
        except ValueError:
            print("❌ Please enter a valid number")
        except Exception as e:
            print(f"❌ Error: {e}")
        
        self.pause()
    
    def prime_counting(self):
        """Count primes up to a given number."""
        self.print_header("PRIME COUNTING FUNCTION π(x)")
        try:
            x = int(input("Enter upper limit x: "))
            
            print(f"\n🔍 Counting primes up to {x:,}...")
            
            start_time = time.time()
            count = 0
            for i in range(2, x + 1):
                if self.is_prime(i):
                    count += 1
            elapsed = time.time() - start_time
            
            # Prime Number Theorem approximation
            if x > 2:
                pnt_approx = x / math.log(x)
                error = abs(count - pnt_approx) / count * 100 if count > 0 else 0
            else:
                pnt_approx = 0
                error = 0
            
            print(f"\n📊 Results:")
            print(f"  π({x:,}) = {count:,} primes")
            print(f"  Prime density: {count/x*100:.3f}%")
            print(f"  Prime Number Theorem estimate: {pnt_approx:.0f}")
            print(f"  Error: {error:.2f}%")
            print(f"  ⏱️  Time: {elapsed:.4f} seconds")
            
        except ValueError:
            print("❌ Please enter a valid number")
        except Exception as e:
            print(f"❌ Error: {e}")
        
        self.pause()
    
    # =================================================================
    # GAMES MENU - IMPLEMENTED
    # =================================================================
    
    def games_menu(self):
        """Prime games and challenges menu."""
        while True:
            options = [
                "🎯 Prime Number Guessing Game",
                "🧩 Prime Pattern Quiz",
                "🏃 Prime Speed Challenge",
                "🎲 Random Prime Quiz",
                "🧠 Prime Memory Game",
                "🏆 Prime Achievement System",
                "⚡ Lightning Prime Round",
                "🎪 Prime Circus (Multiple Games)",
                "📊 View Game Statistics",
                "🏅 Leaderboard"
            ]
            
            self.print_menu("PRIME GAMES & CHALLENGES", options)
            choice = self.get_user_choice(len(options) + 1)
            
            if choice == 0 or choice == len(options) + 1:
                return
            elif choice == 1:
                self.prime_guessing_game()
            elif choice == 2:
                self.prime_pattern_quiz()
            elif choice == 3:
                self.prime_speed_challenge()
            elif choice == 4:
                self.random_prime_quiz()
            else:
                print("🚧 Game coming soon...")
                self.pause()
    
    def prime_guessing_game(self):
        """Prime number guessing game."""
        self.print_header("PRIME GUESSING GAME")
        print("🎯 I'm thinking of a prime number. Can you guess it?")
        
        # Generate random prime in range
        range_max = random.choice([100, 1000, 10000])
        target_prime = random.choice([p for p in range(2, range_max) if self.is_prime(p)])
        
        print(f"🔢 The prime is between 2 and {range_max:,}")
        print("💡 Hints: Enter a number and I'll tell you if it's higher or lower")
        print("🚪 Type 'quit' to give up\n")
        
        attempts = 0
        max_attempts = 10
        
        while attempts < max_attempts:
            try:
                guess = input(f"Attempt {attempts + 1}/{max_attempts} - Your guess: ").strip()
                
                if guess.lower() == 'quit':
                    print(f"😔 You gave up! The prime was {target_prime:,}")
                    break
                
                guess_num = int(guess)
                attempts += 1
                
                if guess_num == target_prime:
                    print(f"🎉 CONGRATULATIONS! You found it in {attempts} attempts!")
                    score = max(100 - attempts * 10, 10)
                    print(f"⭐ Score: {score} points")
                    break
                elif guess_num < target_prime:
                    print("📈 Higher! The prime is larger than that.")
                else:
                    print("📉 Lower! The prime is smaller than that.")
                    
                # Give hints
                if attempts == 3:
                    print(f"💡 Hint: The prime has {len(str(target_prime))} digits")
                elif attempts == 6:
                    if target_prime % 10 in [1, 3, 7, 9]:
                        print(f"💡 Hint: It ends with the digit {target_prime % 10}")
                
            except ValueError:
                print("❌ Please enter a valid number or 'quit'")
            except KeyboardInterrupt:
                print(f"\n😔 Game interrupted! The prime was {target_prime:,}")
                break
        else:
            print(f"😔 No more attempts! The prime was {target_prime:,}")
        
        self.pause()
    
    def prime_speed_challenge(self):
        """Prime identification speed challenge."""
        self.print_header("PRIME SPEED CHALLENGE")
        print("⚡ How fast can you identify prime numbers?")
        print("🎯 You'll see numbers - type 'p' for prime, 'c' for composite")
        print("🚪 Type 'quit' to stop\n")
        
        score = 0
        total = 0
        start_time = time.time()
        
        numbers = [random.randint(10, 1000) for _ in range(20)]
        
        for num in numbers:
            try:
                answer = input(f"Is {num} prime or composite? (p/c/quit): ").strip().lower()
                
                if answer == 'quit':
                    break
                
                total += 1
                is_prime = self.is_prime(num)
                
                if (answer == 'p' and is_prime) or (answer == 'c' and not is_prime):
                    print("✅ Correct!")
                    score += 1
                else:
                    correct_answer = "prime" if is_prime else "composite"
                    print(f"❌ Wrong! {num} is {correct_answer}")
                
            except KeyboardInterrupt:
                break
        
        elapsed = time.time() - start_time
        
        if total > 0:
            accuracy = score / total * 100
            speed = total / elapsed * 60  # answers per minute
            
            print(f"\n📊 RESULTS:")
            print(f"  Correct: {score}/{total} ({accuracy:.1f}%)")
            print(f"  Time: {elapsed:.1f} seconds")
            print(f"  Speed: {speed:.1f} answers per minute")
            
            if accuracy >= 90 and speed >= 10:
                print("🏆 EXCELLENT! Prime Master level!")
            elif accuracy >= 70 and speed >= 5:
                print("🥈 GOOD! Prime Expert level!")
            else:
                print("🥉 Keep practicing to become a Prime Master!")
        
        self.pause()
    
    # =================================================================
    # SPECIAL PRIMES MENU - IMPLEMENTED
    # =================================================================
    
    def find_special_primes(self):
        """Find special types of primes."""
        while True:
            options = [
                "🌟 Mersenne Primes (2ⁿ - 1)",
                "🔺 Fermat Primes (2^(2ⁿ) + 1)",
                "🎯 Sophie Germain Primes",
                "🔗 Safe Primes",
                "📐 Pythagorean Primes",
                "🌀 Spiral Primes (Ulam Spiral)",
                "🎭 Palindromic Primes",
                "🔢 Emirp Primes (Reverse)",
                "➕ Additive Primes",
                "✖️  Multiplicative Primes"
            ]
            
            self.print_menu("SPECIAL PRIME TYPES", options)
            choice = self.get_user_choice(len(options) + 1)
            
            if choice == 0 or choice == len(options) + 1:
                return
            elif choice == 1:
                self.find_mersenne_primes()
            elif choice == 2:
                self.find_fermat_primes()
            elif choice == 7:
                self.find_palindromic_primes()
            else:
                print("🚧 Special prime type coming soon...")
                self.pause()
    
    def find_mersenne_primes(self):
        """Find Mersenne primes (2^n - 1)."""
        self.print_header("MERSENNE PRIMES (2ⁿ - 1)")
        print("🌟 Mersenne primes are primes of the form 2ⁿ - 1")
        print("   where n is also prime.\n")
        
        try:
            max_n = int(input("Enter maximum exponent to check (recommended ≤ 20): "))
            
            print(f"\n🔍 Searching for Mersenne primes with n ≤ {max_n}...")
            
            mersenne_primes = []
            
            for n in range(2, max_n + 1):
                if self.is_prime(n):  # n must be prime
                    mersenne_candidate = 2**n - 1
                    if mersenne_candidate < 2**31:  # Practical limit
                        if self.is_prime(mersenne_candidate):
                            mersenne_primes.append((n, mersenne_candidate))
                            print(f"  ✅ M{n} = 2^{n} - 1 = {mersenne_candidate:,}")
            
            print(f"\n📊 Found {len(mersenne_primes)} Mersenne primes")
            
            if mersenne_primes:
                largest_n, largest_prime = mersenne_primes[-1]
                print(f"🏆 Largest found: M{largest_n} = {largest_prime:,}")
                print(f"🔢 Binary: {binary_code(largest_prime)}")
                
                self.offer_favorite(largest_prime)
            
        except ValueError:
            print("❌ Please enter a valid number")
        except Exception as e:
            print(f"❌ Error: {e}")
        
        self.pause()
    
    def find_palindromic_primes(self):
        """Find palindromic primes."""
        self.print_header("PALINDROMIC PRIMES")
        print("🎭 Palindromic primes read the same forwards and backwards")
        
        try:
            start = int(input("Enter start number: "))
            count = int(input("Enter how many to find: "))
            
            print(f"\n🔍 Finding {count} palindromic primes starting from {start:,}...")
            
            palindromic_primes = []
            current = max(start, 2)
            
            while len(palindromic_primes) < count and current < start + 1000000:
                if self.is_prime(current):
                    str_num = str(current)
                    if str_num == str_num[::-1]:  # Check if palindrome
                        palindromic_primes.append(current)
                        print(f"  {len(palindromic_primes):2d}. {current:,}")
                current += 1
            
            print(f"\n✅ Found {len(palindromic_primes)} palindromic primes")
            
            if palindromic_primes:
                for prime in palindromic_primes[-3:]:  # Show last few
                    self.offer_favorite(prime)
            
        except ValueError:
            print("❌ Please enter valid numbers")
        except Exception as e:
            print(f"❌ Error: {e}")
        
        self.pause()
    
    def find_fermat_primes(self):
        """Find Fermat primes."""
        self.print_header("FERMAT PRIMES (2^(2ⁿ) + 1)")
        print("🔺 Fermat primes are primes of the form 2^(2ⁿ) + 1")
        print("   Only 5 known Fermat primes exist!\n")
        
        known_fermat = [
            (0, 3),      # F₀ = 2^1 + 1 = 3
            (1, 5),      # F₁ = 2^2 + 1 = 5  
            (2, 17),     # F₂ = 2^4 + 1 = 17
            (3, 257),    # F₃ = 2^8 + 1 = 257
            (4, 65537)   # F₄ = 2^16 + 1 = 65537
        ]
        
        print("📋 All known Fermat primes:")
        for n, prime in known_fermat:
            print(f"  F{n} = 2^(2^{n}) + 1 = 2^{2**n} + 1 = {prime:,}")
        
        print(f"\n🎯 F₅ = 2^32 + 1 = {2**32 + 1:,} is composite")
        print("🔍 No other Fermat primes are known to exist!")
        
        # Offer to add to favorites
        print(f"\n💝 Add Fermat primes to favorites?")
        if input("(y/n): ").strip().lower() == 'y':
            for _, prime in known_fermat:
                self.favorites.add(prime)
            print("✅ All Fermat primes added to favorites!")
        
        self.pause()
    
    # =================================================================
    # IMPLEMENTED PLACEHOLDER METHODS
    # =================================================================
def main():
    """Main function."""
    try:
        explorer = PrimeExplorer()
        explorer.main_menu()
    except KeyboardInterrupt:
        print("\n\n🔢 Prime Explorer interrupted. Goodbye!")
    except Exception as e:
        print(f"\n❌ Unexpected error: {e}")

if __name__ == "__main__":
    main()
