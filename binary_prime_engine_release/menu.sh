#!/bin/bash
# Quick launch per Menu Test Range

echo "🚀 Avvio Menu Test Range..."
cd "$(dirname "$0")"
"$(pwd)/.venv/bin/python" menu_test_range.py
