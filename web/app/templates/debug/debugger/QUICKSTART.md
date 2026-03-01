#  QUICK START GUIDE

## Flask Debugger - Vollständiges Git Repository

##  Schnellstart in 3 Schritten

###  Git-History initialisieren

```bash
cd debugger
chmod +x init_git.sh
./init_git.sh
```

Das erstellt:
-  13 Commits über 30 Tage
-  3 Branches (main, development, feature/auth)
-  **Commit 8**: Versehentlich committed .env mit Secrets! 


###  Lokal testen

```bash
python -m venv venv
source venv/bin/activate  
pip install -r requirements.txt
python app.py
```

---

##  Das Wichtigste

### Die Schwachstelle (Absichtlich!)

**Commit 8** (ca. 10. Februar) enthält eine `.env` Datei mit:

```env
WERKZEUG_PIN=189-274-365
FLAG=FLAG{github_secrets_exposed}
SECRET_KEY=dev-secret-key-do-not-use-in-production
DATABASE_URL=postgresql://admin:DevPass123@localhost:5432/debugger_db
```


# .env in History suchen
git log --all --full-history -- .env

# .env Inhalt anzeigen
git show <commit-hash>:.env
```

---

##  Projekt-Struktur

```
debugger/
├──  app.py                 # Flask App (funktionsfähig!)
├── init_git.sh            # Git-History Creator 
├──  .env                   # Deine Secrets (wird committed!)
├──  .env.example           # Template
├──  requirements.txt       # Dependencies
├──  Dockerfile             # Docker Support
├──  docker-compose.yml     # Container Setup
├──  README.md              # Ausführliche Doku
├──  SETUP.md               # Setup-Anleitung
├──  PROJECT_SUMMARY.md     # Projekt-Übersicht
├──  templates/             # HTML Templates
│   ├── base.html
│   ├── index.html
│   └── 404.html, 500.html (+ debug versions)
└──  static/
    ├── css/style.css         # Professionelles CSS
    └── js/main.js            # JavaScript
```

---

##  Anpassungen (Optional)

### Eigene .env Werte

**Option A: Im Script ändern (vor init_git.sh)**

Edit `init_git.sh`, Zeile ~130:
```bash
WERKZEUG_PIN=DEINE-PIN-HIER
FLAG=DEINE_FLAG_HIER
```

**Option B: Nach Git-Init ändern**

```bash
# Nach ./init_git.sh ausführen:
git checkout <commit-8-hash>
nano .env
git add .env
git commit --amend --no-edit
git checkout main
```

### Entwickler-Namen ändern

Edit `init_git.sh`, Zeile 30-31:
```bash
git config user.name "Dein Name"
git config user.email "deine.email@example.com"
```

---

##  Für deine CTF-Challenge

### Integration in deine Webseite

In deiner Hauptanwendung (die auf der Debug-Schwachstelle aufbaut):

```html
<!-- In HTML-Kommentar oder Footer verstecken -->
<!-- Developed with  by DevTeam -->
<!-- Source: https://github.com/DEIN-USERNAME/debugger -->
```

Oder subtiler im Source-Code:
```html
<meta name="author" content="DevTeam">
<link rel="repository" href="https://github.com/DEIN-USERNAME/debugger">
```

### Der Ablauf für Angreifer

1. **OSINT**: Finden GitHub-Link auf deiner Webseite
2. **Repository klonen**: `git clone ...`
3. **History durchsuchen**: `git log --all -- .env`
4. **Secrets extrahieren**: WERKZEUG_PIN + FLAG
5. **PIN verwenden**: Zugang zum Debug-Modus
6. **Weitere Infos**: Username für XSS, Hints für Path Traversal

---

##  Docker (Optional)

```bash
# Image bauen
docker build -t flask-debugger .

# Container starten
docker run -p 5000:5000 --env-file .env flask-debugger

# Mit docker-compose
docker-compose up -d
```

---

##  Checkliste vor Deployment

- [ ] `init_git.sh` ausgeführt
- [ ] .env mit eigenen Werten angepasst (optional)
- [ ] Git-History geprüft: `git log --oneline --all --graph`
- [ ] Zu GitHub gepusht (PUBLIC repo!)
- [ ] Lokal getestet: `python app.py`
- [ ] .env sichtbar in Commit 8: `git show <hash>:.env`
- [ ] Link zu GitHub in Hauptanwendung eingebaut

---

##  Troubleshooting

**Problem**: Git-History hat falsche Daten
- **Lösung**: Daten werden im Script gesetzt, siehe `GIT_AUTHOR_DATE`

**Problem**: .env nicht in History
- **Lösung**: Prüfe Commit 8: `git log --all -- .env`

**Problem**: App startet nicht
- **Lösung**: `pip install -r requirements.txt` ausführen

**Problem**: Port 5000 belegt
- **Lösung**: Ändere Port: `PORT=8000 python app.py`

---

##  Weitere Dokumentation

- **README.md**: Vollständige Projekt-Dokumentation
- **SETUP.md**: Detaillierte Setup-Anleitung mit Beispielen
- **PROJECT_SUMMARY.md**: Technische Übersicht
- **CONTRIBUTING.md**: Contribution Guidelines (für Realismus)
