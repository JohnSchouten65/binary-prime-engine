# 🔢 Binary Prime Engine - International Edition

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python 3.8+](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/downloads/)
[![GitHub release](https://img.shields.io/github/v/release/JohnSchouten65/binary-prime-engine)](https://github.com/JohnSchouten65/binary-prime-engine/releases)

**Advanced infinite prime number generator with binary pattern analysis, gap tracking, and professional-grade optimization.**

## 🌟 Features

### Core Engine
- ✅ **Infinite Prime Generation** - Generate unlimited sequences of prime numbers
- ✅ **Binary Pattern Analysis** - Advanced binary representation with adaptive bit allocation
- ✅ **Gap Tracking (dₙ)** - Monitor gaps between consecutive primes
- ✅ **LRU Cache Optimization** - High-performance caching for repeated calculations
- ✅ **Persistent Storage** - Automatic saving of binary codes for composite numbers

### Professional Tools
- ✅ **CLI Interface** - Command-line interface with multiple output formats
- ✅ **Multiple Output Formats** - Text, JSON, CSV export capabilities
- ✅ **Performance Monitoring** - Real-time statistics and benchmarking
- ✅ **Interactive Menu System** - Comprehensive prime exploration tools
- ✅ **Logging & Configuration** - Professional logging and configurable parameters

### Advanced Features
- ✅ **Prime Explorer** - Interactive menu for prime number research
- ✅ **Stress Testing** - Comprehensive validation and reliability testing
- ✅ **Benchmark Suite** - Performance comparison and optimization tools
- ✅ **Educational Tools** - Learning resources and demonstration scripts

## 🚀 Quick Start

### Installation

```bash
# Clone the repository
git clone https://github.com/JohnSchouten65/binary-prime-engine.git
cd binary-prime-engine

# Install dependencies
pip install -r requirements.txt
```

### Basic Usage

```bash
# Generate first 100 primes
python binary_prime_engine_pro_en.py --start 1 --limit 100

# Generate primes starting from 1000
python binary_prime_engine_pro_en.py --start 1000

# Save results to file in JSON format
python binary_prime_engine_pro_en.py --start 1 --limit 50 --format json --output primes.json

# Interactive prime exploration
python prime_explorer.py
```

## 📚 Usage Examples

### Command Line Interface

```bash
# Basic prime generation
python binary_prime_engine_pro_en.py --start 1000 --limit 100

# JSON output with custom cache size
python binary_prime_engine_pro_en.py --start 1 --format json --cache-size 50000

# CSV export for data analysis
python binary_prime_engine_pro_en.py --start 1 --limit 1000 --format csv --output dataset.csv

# Quiet mode for automated scripts
python binary_prime_engine_pro_en.py --start 1 --limit 100 --quiet

# Verbose mode for debugging
python binary_prime_engine_pro_en.py --start 1 --limit 10 --verbose
```

### Python API

```python
from binary_prime_engine_pro_en import BinaryPrimeEngine

# Create engine with custom configuration
config = {'cache_size': 20000, 'save_interval': 500}
engine = BinaryPrimeEngine(config)

# Generate primes with statistics
for count, prime, gap in engine.generate_primes(start=1000, limit=50):
    print(f"Prime #{count}: {prime} (gap: {gap})")
    print(f"Binary: {engine.binary_code(prime)}")
```

## 🔧 Configuration

Create a `config.ini` file to customize engine behavior:

```ini
[engine]
cache_size = 10000
save_interval = 1000
progress_interval = 100
db_file = binary_codes.json

[output]
default_format = text
show_binary = true
show_gaps = true

[performance]
enable_cache = true
auto_save = true
```

## 📊 Performance Benchmarks

| Range | Primes Found | Time (seconds) | Primes/sec |
|-------|--------------|----------------|------------|
| 1-1,000 | 168 | 0.001 | 168,000 |
| 1-10,000 | 1,229 | 0.015 | 81,933 |
| 1-100,000 | 9,592 | 0.156 | 61,487 |
| 1-1,000,000 | 78,498 | 1.847 | 42,505 |

*Benchmarks run on: Intel i7-10700K @ 3.80GHz, 32GB RAM*

## 🎯 Advanced Features

### Prime Explorer Interactive Menu

```bash
python prime_explorer.py
```

Features include:
- **Prime Search & Discovery** - Find next/previous primes, nth prime, ranges
- **Prime Calculations** - Mathematical operations and analysis
- **Pattern Analysis** - Twin primes, cousin primes, prime chains
- **Special Primes** - Mersenne, Fermat, palindromic primes
- **Performance Testing** - Benchmarks and speed comparisons
- **Data Management** - Export, import, favorites system

### Testing & Validation

```bash
# Run comprehensive test suite
python test_prime_validation.py

# Stress testing with large numbers
python stress_test.py

# Binary representation limits testing
python test_bit_limits.py

# Gap analysis and statistics
python test_gaps.py
```

## 🏗️ Architecture

### Core Components

```
binary_prime_engine_pro_en.py    # Main professional engine
binary_prime_engine_en.py        # Basic engine for simple use
prime_explorer.py                # Interactive exploration tool
```

### Testing & Utilities

```
test_prime_validation.py         # Validation and correctness tests
stress_test.py                   # Performance and reliability testing
benchmark.py                     # Performance benchmarking
utility.sh                      # Maintenance and utility scripts
```

### Data & Configuration

```
config.ini                      # Engine configuration
binary_codes.json               # Persistent storage for composites
prime_engine.log                # Runtime logging
```

## 🧮 Mathematical Background

### Binary Pattern Analysis
The engine uses adaptive binary representation that automatically adjusts bit allocation based on number size:

- **Nibble Alignment**: Rounds to multiples of 4 bits for readability
- **Auto-Expansion**: Dynamically increases bits as numbers grow
- **No Truncation**: Preserves complete binary representation

### Gap Tracking (dₙ)
Monitors the gaps between consecutive primes:
- **dₙ = pₙ₊₁ - pₙ** (gap between nth and (n+1)th prime)
- **Statistical Analysis**: Tracks min, max, and average gaps
- **Pattern Recognition**: Identifies unusual gap patterns

### Optimization Strategies
- **Sieve of Odd Numbers**: Only tests odd candidates after 2
- **Early Termination**: Stops divisibility testing at √n
- **Cache Strategy**: LRU cache for frequently tested numbers
- **Binary Storage**: Efficient storage of composite number patterns

## 🔬 Scientific Applications

### Research Use Cases
- **Prime Distribution Studies** - Analyze prime number density and patterns
- **Gap Analysis Research** - Study gaps between consecutive primes
- **Computational Number Theory** - Generate datasets for mathematical research
- **Algorithm Benchmarking** - Test and compare primality algorithms

### Educational Applications
- **Mathematics Education** - Demonstrate prime number properties
- **Computer Science Teaching** - Algorithm optimization examples
- **Binary Number Systems** - Understand binary representation
- **Performance Analysis** - Study algorithmic complexity

## 🛠️ Development

### Building from Source

```bash
# Install development dependencies
pip install -r requirements.txt

# Run tests
python -m pytest tests/

# Generate documentation
python generate_docs.py

# Create distribution package
python setup.py sdist bdist_wheel
```

### Contributing

1. Fork the repository
2. Create a feature branch: `git checkout -b feature-name`
3. Make your changes with tests
4. Run the test suite: `python test_prime_validation.py`
5. Commit your changes: `git commit -am 'Add feature'`
6. Push to the branch: `git push origin feature-name`
7. Submit a pull request

## 📈 Roadmap

### Version 3.0 (Upcoming)
- [ ] **GPU Acceleration** - CUDA support for massive prime generation
- [ ] **Distributed Computing** - Multi-machine prime generation
- [ ] **Advanced Visualizations** - 3D prime distribution plots
- [ ] **Machine Learning** - AI-powered prime pattern prediction

### Version 2.1 (Current)
- [x] **English Internationalization** - Complete English version
- [x] **Enhanced Prime Explorer** - Comprehensive interactive menu
- [x] **Professional CLI** - Advanced command-line interface
- [x] **Performance Optimization** - LRU cache and binary optimizations

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- **Mathematical Foundation**: Based on classical number theory and modern optimization techniques
- **Performance Inspiration**: Influenced by production-grade mathematical libraries
- **Community**: Thanks to the open-source mathematics and Python communities

## 📞 Support

- **Documentation**: See the [Wiki](https://github.com/JohnSchouten65/binary-prime-engine/wiki)
- **Issues**: Report bugs on [GitHub Issues](https://github.com/JohnSchouten65/binary-prime-engine/issues)
- **Discussions**: Join the [GitHub Discussions](https://github.com/JohnSchouten65/binary-prime-engine/discussions)

---

**🔢 Made with ❤️ for the mathematics and computer science communities**

*Generate infinite prime sequences with professional-grade performance and reliability.*
