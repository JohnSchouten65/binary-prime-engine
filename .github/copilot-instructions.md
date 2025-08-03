<!-- Use this file to provide workspace-specific custom instructions to Copilot. For more details, visit https://code.visualstudio.com/docs/copilot/copilot-customization#_use-a-githubcopilotinstructionsmd-file -->

# Binary Prime Engine Project

This is a Python project that implements an infinite binary prime engine with advanced pattern analysis and gap tracking.

## Key Features
- Binary pattern analysis for prime number generation
- Gap tracking between consecutive primes (dₙ)
- Compact binary representation of numbers
- Persistent storage of binary codes for known composite numbers
- Optimized prime checking using binary patterns

## Code Style Guidelines
- Use Italian comments for domain-specific functions
- Follow PEP 8 conventions for Python code
- Maintain mathematical precision in prime calculations
- Use descriptive variable names for mathematical concepts (p for primes, d for gaps)

## Mathematical Context
- pₙ represents the nth prime number
- dₙ represents the gap between consecutive primes
- Binary patterns focus on last 3 bits: 001 or 101 for potential primes
- Only check odd divisors for efficiency
