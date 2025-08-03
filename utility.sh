#!/bin/bash
# Script di utilità per Binary Prime Engine

set -e

# Colori per output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
NC='\033[0m' # No Color

echo -e "${BLUE}=== Binary Prime Engine - Utility Script ===${NC}"

# Funzione per stampare con colori
print_status() {
    echo -e "${GREEN}[INFO]${NC} $1"
}

print_warning() {
    echo -e "${YELLOW}[WARNING]${NC} $1"
}

print_error() {
    echo -e "${RED}[ERROR]${NC} $1"
}

# Verifica Python
check_python() {
    print_status "Verificando Python..."
    if command -v python3 &> /dev/null; then
        python3 --version
    else
        print_error "Python3 non trovato!"
        exit 1
    fi
}

# Installa dipendenze
install_deps() {
    print_status "Installando dipendenze..."
    pip3 install --upgrade pip
    # Aggiungi qui eventuali dipendenze future
    print_status "Dipendenze installate!"
}

# Esegue benchmark
run_benchmark() {
    print_status "Eseguendo benchmark..."
    python3 benchmark.py
}

# Pulisce file temporanei
cleanup() {
    print_status "Pulizia file temporanei..."
    rm -f *.pyc
    rm -rf __pycache__
    rm -f prime_engine*.log
    print_status "Pulizia completata!"
}

# Backup database
backup_db() {
    print_status "Backup database..."
    timestamp=$(date +"%Y%m%d_%H%M%S")
    if [ -f "binary_codes.json" ]; then
        cp binary_codes.json "backup_binary_codes_${timestamp}.json"
        print_status "Backup salvato: backup_binary_codes_${timestamp}.json"
    fi
    if [ -f "binary_codes_pro.json" ]; then
        cp binary_codes_pro.json "backup_binary_codes_pro_${timestamp}.json"
        print_status "Backup salvato: backup_binary_codes_pro_${timestamp}.json"
    fi
}

# Mostra statistiche
show_stats() {
    print_status "Statistiche database:"
    if [ -f "binary_codes.json" ]; then
        size=$(wc -c < binary_codes.json)
        print_status "binary_codes.json: ${size} bytes"
    fi
    if [ -f "binary_codes_pro.json" ]; then
        size=$(wc -c < binary_codes_pro.json)
        print_status "binary_codes_pro.json: ${size} bytes"
    fi
    if [ -f "prime_engine.log" ]; then
        lines=$(wc -l < prime_engine.log)
        print_status "prime_engine.log: ${lines} linee"
    fi
}

# Menu principale
show_menu() {
    echo
    echo -e "${BLUE}Seleziona un'opzione:${NC}"
    echo "1) Verifica Python"
    echo "2) Installa dipendenze"
    echo "3) Esegui benchmark"
    echo "4) Backup database"
    echo "5) Mostra statistiche"
    echo "6) Pulizia file temporanei"
    echo "7) Esci"
    echo
}

# Loop principale
while true; do
    show_menu
    read -p "Scelta [1-7]: " choice
    
    case $choice in
        1) check_python ;;
        2) install_deps ;;
        3) run_benchmark ;;
        4) backup_db ;;
        5) show_stats ;;
        6) cleanup ;;
        7) print_status "Arrivederci!"; exit 0 ;;
        *) print_error "Opzione non valida!" ;;
    esac
    
    echo
    read -p "Premi ENTER per continuare..."
done
