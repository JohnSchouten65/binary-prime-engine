#!/bin/bash
# Script per pubblicare Binary Prime Engine su GitHub

set -e

echo "🚀 PUBBLICAZIONE BINARY PRIME ENGINE SU GITHUB"
echo "==============================================="

# Colori
GREEN='\033[0;32m'
BLUE='\033[0;34m'
YELLOW='\033[1;33m'
RED='\033[0;31m'
NC='\033[0m'

print_step() {
    echo -e "${BLUE}[STEP]${NC} $1"
}

print_success() {
    echo -e "${GREEN}[SUCCESS]${NC} $1"
}

print_warning() {
    echo -e "${YELLOW}[WARNING]${NC} $1"
}

print_error() {
    echo -e "${RED}[ERROR]${NC} $1"
}

# Verifica prerequisiti
print_step "Verificando prerequisiti..."

if ! command -v git &> /dev/null; then
    print_error "Git non trovato! Installalo prima di continuare."
    exit 1
fi

if ! command -v gh &> /dev/null; then
    print_warning "GitHub CLI (gh) non trovato. Dovrai creare il repository manualmente."
    MANUAL_REPO=true
else
    print_success "GitHub CLI trovato!"
    MANUAL_REPO=false
fi

# Verifica configurazione Git
print_step "Verificando configurazione Git..."
if [[ -z $(git config user.name) ]] || [[ -z $(git config user.email) ]]; then
    print_warning "Configurazione Git mancante!"
    echo "Configura Git con:"
    echo "  git config --global user.name 'Your Name'"
    echo "  git config --global user.email 'your.email@example.com'"
    
    read -p "Vuoi configurare ora? (y/n): " configure_git
    if [[ $configure_git == "y" ]]; then
        read -p "Nome: " git_name
        read -p "Email: " git_email
        git config --global user.name "$git_name"
        git config --global user.email "$git_email"
        print_success "Configurazione Git completata!"
    fi
fi

# Ottieni informazioni repository
print_step "Configurazione repository..."
read -p "Nome repository (binary-prime-engine): " repo_name
repo_name=${repo_name:-binary-prime-engine}

read -p "Username GitHub: " github_username
if [[ -z $github_username ]]; then
    print_error "Username GitHub richiesto!"
    exit 1
fi

read -p "Descrizione repository: " repo_description
repo_description=${repo_description:-"Advanced infinite prime number generator with binary pattern analysis and high-performance optimizations"}

read -p "Repository pubblico? (y/n): " is_public
if [[ $is_public == "y" ]]; then
    visibility="public"
else
    visibility="private"
fi

# Aggiorna README con info utente
print_step "Aggiornando README con informazioni utente..."
sed -i.bak "s/\[YOUR_USERNAME\]/$github_username/g" README.md
sed -i.bak "s/your_username/$github_username/g" README.md
sed -i.bak "s/\[Your Name\]/$(git config user.name)/g" README.md
rm README.md.bak

# Commit finale
print_step "Commit finale con informazioni aggiornate..."
git add README.md
git commit -m "📝 Update README with user information

- Updated GitHub username: $github_username
- Updated author information
- Ready for GitHub publication"

# Crea repository su GitHub
if [[ $MANUAL_REPO == false ]]; then
    print_step "Creando repository su GitHub..."
    gh repo create $repo_name \
        --description "$repo_description" \
        --$visibility \
        --source=. \
        --push
    
    print_success "Repository creato: https://github.com/$github_username/$repo_name"
else
    print_step "Istruzioni per creazione manuale repository:"
    echo "1. Vai su https://github.com/new"
    echo "2. Nome repository: $repo_name"
    echo "3. Descrizione: $repo_description"
    echo "4. Visibilità: $visibility"
    echo "5. NON inizializzare con README (già presente)"
    echo ""
    echo "Dopo aver creato il repository, esegui:"
    echo "  git remote add origin https://github.com/$github_username/$repo_name.git"
    echo "  git branch -M main"
    echo "  git push -u origin main"
fi

# Crea release tag
print_step "Creando tag per release v2.0.0..."
git tag -a v2.0.0 -m "🎉 Binary Prime Engine v2.0.0

Features:
✨ Professional prime number generator
⚡ High-performance engine (230K+ primes/second)  
🛠️ Complete CLI interface
📊 Multiple output formats (text/JSON/CSV)
🧠 Intelligent LRU cache
📈 Real-time monitoring
🔧 Professional tools suite
📚 Complete documentation

This is the first stable release ready for production use!"

# Push con tags
if [[ $MANUAL_REPO == false ]]; then
    print_step "Pushing tags..."
    git push origin --tags
    
    print_step "Creando GitHub release..."
    gh release create v2.0.0 \
        --title "🚀 Binary Prime Engine v2.0.0" \
        --notes-file CHANGELOG.md \
        --latest
fi

print_success "🎉 PUBBLICAZIONE COMPLETATA!"
echo ""
echo "📁 Repository: https://github.com/$github_username/$repo_name"
echo "🏷️  Release: https://github.com/$github_username/$repo_name/releases/tag/v2.0.0"
echo ""
echo "🔗 Prossimi passi:"
echo "  • Condividi il repository"
echo "  • Aggiungi topic tags su GitHub"
echo "  • Considera l'aggiunta a package registries"
echo "  • Implementa GitHub Actions per CI/CD"
echo ""
echo "📊 Statistiche progetto:"
echo "  • $(find . -name "*.py" | wc -l | tr -d ' ') file Python"
echo "  • $(cat *.py | wc -l | tr -d ' ') linee di codice"
echo "  • $(ls -la | grep -E '^-' | wc -l | tr -d ' ') file totali"
