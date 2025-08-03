# Binary Prime Engine

![Python](https://img.shields.io/badge/python-v3.8+-blue.svg)
![License](https://img.shields.io/badge/license-MIT-green.svg)
![Version](https://img.shields.io/badge/version-2.0-orange.svg)

Un motore avanzato per la generazione infinita di numeri primi con analisi dei pattern binari, ottimizzazioni per performance e interfaccia CLI professionale.

## 🚀 Caratteristiche

- **🔢 Generazione Infinita**: Algoritmo ottimizzato per generare numeri primi indefinitamente
- **⚡ Performance Elevate**: 100K+ primi/secondo con cache intelligente
- **📊 Analisi Pattern**: Tracciamento gap (dₙ) e rappresentazione binaria
- **💾 Persistenza Dati**: Database automatico dei pattern binari
- **🛠️ CLI Professionale**: Interfaccia completa con formati multipli
- **📈 Monitoring**: Statistiche in tempo reale e logging avanzato

## 📦 Installazione

### Requisiti
- Python 3.8+
- Ambiente virtuale (raccomandato)

### Setup Rapido
```bash
# Clona il repository
git clone https://github.com/JohnSchouten65/binary-prime-engine.git
cd binary-prime-engine

# Crea ambiente virtuale
python -m venv .venv
source .venv/bin/activate  # Linux/Mac
# .venv\Scripts\activate     # Windows

# Installa dipendenze (se necessarie)
pip install -r requirements.txt
```

## 🎯 Utilizzo

### Versione Base (Prototipo)
```bash
python binary_prime_engine.py
```

### Versione Professionale
```bash
# Genera 100 primi a partire da 1000
python binary_prime_engine_pro.py --start 1000 --limit 100

# Output in formato JSON
python binary_prime_engine_pro.py --start 1 --format json --output primes.json

# Modalità silenziosa per scripting
python binary_prime_engine_pro.py --start 1 --quiet --limit 1000

# Performance test
python benchmark.py
```

### Opzioni CLI Complete
```
--start, -s          Numero di partenza (default: 1)
--limit, -l          Numero massimo di primi da generare
--output, -o         File di output (default: stdout)
--format, -f         Formato: text, json, csv (default: text)
--cache-size         Dimensione cache (default: 10000)
--save-interval      Intervallo salvataggio (default: 1000)
--progress-interval  Intervallo progress log (default: 100)
--quiet, -q          Modalità silenziosa
--verbose, -v        Output verboso
```

## � Esempi di Output

### Formato Text
```
p1 = 2 | gap dₙ = 0 | bin: 0000000000000010
p2 = 3 | gap dₙ = 1 | bin: 0000000000000011
p3 = 5 | gap dₙ = 2 | bin: 0000000000000101
```

### Formato JSON
```json
{"count": 1, "prime": 2, "gap": 0, "binary": "0000000000000010"}
{"count": 2, "prime": 3, "gap": 1, "binary": "0000000000000011"}
```

### Formato CSV
```csv
count,prime,gap,binary
1,2,0,0000000000000010
2,3,1,0000000000000011
```

## 🔧 Strumenti Inclusi

- **`benchmark.py`**: Suite di test performance
- **`utility.sh`**: Script di manutenzione e backup
- **`config.ini`**: Configurazione personalizzabile
- **VS Code Tasks**: Task predefiniti per sviluppo

## 📈 Performance

| Range | Primi/Secondo | Nota |
|-------|---------------|------|
| 1-100 | ~230K | Cache warming |
| 1K-10K | ~200K | Ottimale |
| 10K-100K | ~120K | Numeri grandi |
| 100K+ | ~63K | Range estremi |

## 🧮 Algoritmo

Il motore implementa:
1. **Setaccio ottimizzato** con test solo su numeri dispari
2. **Cache LRU** per evitare ricalcoli
3. **Pattern recognition** per ottimizzazioni future
4. **Database persistente** dei numeri composti
5. **Analisi matematica** dei gap tra primi

## � Ricerca Matematica

Perfetto per:
- **Analisi gap theory** (Congettura di Bertrand)
- **Pattern recognition** in sequenze prime
- **Benchmarking algoritmi** di fattorizzazione
- **Ricerca matematica** su grandi numeri primi

## � Struttura Progetto

```
binary-prime-engine/
├── binary_prime_engine.py      # Versione base
├── binary_prime_engine_pro.py  # Versione professionale
├── benchmark.py                # Suite di test
├── config.ini                  # Configurazione
├── utility.sh                  # Script utilità
├── requirements.txt            # Dipendenze Python
├── .github/
│   └── copilot-instructions.md # Istruzioni AI
├── .vscode/
│   └── tasks.json             # Task VS Code
└── README.md                  # Questo file
```

## 🤝 Contribuire

1. Fork il progetto
2. Crea un feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit le modifiche (`git commit -m 'Add AmazingFeature'`)
4. Push al branch (`git push origin feature/AmazingFeature`)
5. Apri una Pull Request

## � Sviluppi Futuri

- [ ] Algoritmi paralleli multi-core
- [ ] GPU acceleration con CUDA
- [ ] Machine Learning per pattern prediction
- [ ] API REST per servizi web
- [ ] Distribuzione su cluster

## 📄 Licenza

Distribuito sotto licenza MIT. Vedi `LICENSE` per maggiori informazioni.

## 👨‍💻 Autore

**Binary-Prime-Engine** - [@JohnSchouten65](https://github.com/JohnSchouten65)

Link Progetto: [https://github.com/JohnSchouten65/binary-prime-engine](https://github.com/JohnSchouten65/binary-prime-engine)

---

*"In matematica, la bellezza è la prima prova della verità." - G.H. Hardy*
