# Changelog

Tutte le modifiche importanti al progetto Binary Prime Engine saranno documentate in questo file.

Il formato è basato su [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
e questo progetto aderisce al [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [2.0.0] - 2025-08-03

### Added
- **Versione Professionale** (`binary_prime_engine_pro.py`) per uso reale
- **Cache LRU intelligente** per ottimizzazioni performance
- **Interfaccia CLI completa** con argparse
- **Formati output multipli**: text, JSON, CSV
- **Statistiche dettagliate** e monitoring in tempo reale
- **Database persistente** con metadati estesi
- **Gestione interruzioni** sicura con salvataggio dati
- **Suite di benchmark** per test performance
- **Script utility** per manutenzione
- **Configurazione personalizzabile** via config.ini
- **Task VS Code** predefiniti
- **Logging professionale** con rotazione file
- **Documentazione completa** per GitHub

### Changed
- **Algoritmo migliorato**: rimosso filtro binario troppo restrittivo
- **Performance**: da ~1K a ~230K primi/secondo
- **Gestione errori**: robusta con recovery automatico
- **Struttura progetto**: organizzata per uso professionale

### Fixed
- **Bug cache**: gestione corretta cache size 0
- **Generazione primi**: ora include tutti i primi (3, 7, 11, etc.)
- **Memory leaks**: gestione memoria ottimizzata

## [1.0.0] - 2025-08-03

### Added
- **Versione base** del Binary Prime Engine
- **Generazione infinita** di numeri primi
- **Pattern binari** per ottimizzazione
- **Gap tracking** (dₙ) tra primi consecutivi
- **Database semplice** dei codici binari
- **Interfaccia interattiva** base

### Features Base
- Algoritmo setaccio ottimizzato
- Rappresentazione binaria a 16 bit
- Salvataggio automatico database
- Controllo interruzione Ctrl+C

## [Unreleased]

### Planned
- [ ] Algoritmi paralleli multi-core
- [ ] GPU acceleration con CUDA
- [ ] Machine Learning per pattern prediction
- [ ] API REST per servizi web
- [ ] Distribuzione cluster per numeri enormi
- [ ] Interfaccia web moderna
- [ ] Plugin per analisi matematiche avanzate
