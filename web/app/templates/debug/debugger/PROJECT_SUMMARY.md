# Flask Debugger Project - Complete Package

## Project Overview

This is a **complete, functional Flask debugging application** designed for CTF/security training purposes. It includes an intentional security vulnerability (exposed `.env` file in Git history) that simulates a realistic developer mistake.

## What's Included

### Core Application Files
- `app.py` - Full Flask application with debug mode support
- `requirements.txt` - Production dependencies
-  `requirements-dev.txt` - Development dependencies
-  `.env.example` - Environment variable template
-  `.env` - Sample environment file (you should customize this)

### Docker Support
-  `Dockerfile` - Multi-stage Docker build
-  `docker-compose.yml` - Container orchestration
-  `.dockerignore` - Docker build optimization

### Templates & Assets
-  `templates/` - Complete HTML templates
  - `base.html` - Base template with navigation
  - `index.html` - Feature-rich landing page
  - `404.html` / `404_debug.html` - Error pages
  - `500.html` / `500_debug.html` - Server error pages
-  `static/` - CSS and JavaScript
  - `css/style.css` - Professional styling
  - `js/main.js` - Interactive features

### Documentation
-  `README.md` - Comprehensive project documentation
-  `SETUP.md` - Detailed setup instructions
-  `CONTRIBUTING.md` - Contribution guidelines
-  `CHANGELOG.md` - Version history
-  `LICENSE` - MIT License

### Git Configuration
-  `.gitignore` - Proper ignore rules (but .env added too late!)
-  `init_git.sh` - Script to create realistic Git history

### CI/CD
-  `.github/workflows/ci.yml` - GitHub Actions pipeline

## Key Features

### 1. Functional Flask Application
- Status and health check endpoints
- Debug mode toggle via environment variables
- Error handling with production/debug modes
- Werkzeug debugger integration with PIN protection

### 2. Realistic Git History
The `init_git.sh` script creates **13 commits over 30 days**:
- Initial project setup
- Feature development
- Docker integration
- **Commit 8: Accidental .env commit** 
- Later .gitignore update (too late)
- Continued development

### 3. Security Vulnerability (Intentional)
**Commit 8** exposes:
```
WERKZEUG_PIN=189-274-365
FLAG=FLAG{github_secrets_exposed}
SECRET_KEY=dev-secret-key-do-not-use-in-production
DATABASE_URL=postgresql://admin:DevPass123@localhost:5432/debugger_db
```

### 4. Multiple Branches
- `main` - Production code (13 commits)
- `development` - Experimental features
- `feature/auth` - WIP authentication module

## How to Use

### Step 1: Initialize Git History
```bash
cd debugger-project
chmod +x init_git.sh
./init_git.sh
```

### Step 2: Customize .env (Optional)
Edit the `.env` file that gets committed in the script to include your:
- Custom WERKZEUG_PIN
- Custom FLAG
- Any other values you want

### Step 3: Push to GitHub
```bash
git remote add origin https://github.com/YOUR-USERNAME/debugger.git
git push -u origin --all
```

### Step 4: Test Locally
```bash
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python app.py
```

### Step 5: Deploy (Optional)
```bash
docker-compose up -d
```

## For CTF Participants

### Finding the Vulnerability

**OSINT Chain:**
1. Find the GitHub repository link (hidden in your main application)
2. Clone the repository
3. Search commit history:
   ```bash
   git log --all --full-history -- .env
   git show <commit-hash>:.env
   ```
4. Extract `WERKZEUG_PIN` and `FLAG`
5. Use PIN to access debug mode
6. Retrieve additional information for next challenges

### Exploitation Flow
```
Main App → GitHub Link (OSINT) → Clone Repo → 
Find .env in History → Get PIN & FLAG → 
Debug Mode Access → Next Challenge Info
```

## Customization Options

### Change Developer Names
Edit `init_git.sh` lines 30-31:
```bash
git config user.name "Your Name"
git config user.email "your.email@example.com"
```

### Modify Commit Messages
Edit the commit messages in `init_git.sh` to fit your scenario.

### Change .env Values
Edit lines 126-146 in `init_git.sh` where the `.env` file is created.

### Adjust Commit Dates
Modify the `GIT_AUTHOR_DATE` values in `init_git.sh` to change the timeline.

## File Structure
```
debugger-project/
├── app.py                          # Main Flask application
├── requirements.txt                # Dependencies
├── requirements-dev.txt            # Dev dependencies
├── Dockerfile                      # Docker build
├── docker-compose.yml              # Container setup
├── .env                            # Environment config (in git history!)
├── .env.example                    # Template
├── .gitignore                      # Git ignore (added too late)
├── .dockerignore                   # Docker ignore
├── init_git.sh                     # Git initialization script 
├── README.md                       # Project docs
├── SETUP.md                        # Setup guide 
├── CONTRIBUTING.md                 # Contribution guide
├── CHANGELOG.md                    # Version history
├── LICENSE                         # MIT License
├── templates/                      # HTML templates
│   ├── base.html
│   ├── index.html
│   ├── 404.html
│   ├── 404_debug.html
│   ├── 500.html
│   └── 500_debug.html
├── static/                         # Static assets
│   ├── css/
│   │   └── style.css
│   ├── js/
│   │   └── main.js
│   └── images/
└── .github/
    └── workflows/
        └── ci.yml                  # CI/CD pipeline
```

## Environment Variables

| Variable | Description | Default |
|----------|-------------|---------|
| `FLASK_ENV` | Environment (development/production) | `production` |
| `DEBUG` | Enable debug mode (0/1) | `0` |
| `SECRET_KEY` | Flask secret key | Required |
| `WERKZEUG_PIN` | Debugger PIN | Auto-generated |
| `HOST` | Server host | `127.0.0.1` |
| `PORT` | Server port | `5000` |
| `DATABASE_URL` | Database connection string | Optional |
| `FLAG` | CTF flag | For training only |

## Security Notes

 **This project intentionally includes security vulnerabilities for educational purposes.**

**DO NOT:**
- Use in production environments
- Commit real secrets
- Enable debug mode in production
- Expose to the internet without proper security

**DO:**
- Use for CTF/training only
- Review commit history for learning
- Understand the risks of exposed credentials
- Practice secure development

## Testing Checklist

Before deployment:
- [ ] Git history initialized with `init_git.sh`
- [ ] `.env` file contains your custom values
- [ ] Repository pushed to GitHub (public)
- [ ] Application runs locally
- [ ] Docker build succeeds
- [ ] All endpoints respond correctly
- [ ] Debug mode works with PIN
- [ ] .env visible in commit 8

## Support & Troubleshooting

**Application won't start:**
- Check Python version (3.9+)
- Verify all dependencies installed
- Check port 5000 availability

**Git history issues:**
- Re-run `init_git.sh`
- Check commit dates with `git log --format=fuller`
- Verify .env in history: `git log --all -- .env`

**Docker problems:**
- Check Docker daemon running
- Verify .env file exists
- Check logs: `docker logs flask-debugger`

## Credits

Created for CTF/security training purposes.
- Flask framework by Pallets
- Werkzeug debugger
- Bootstrap styling concepts

## License

MIT License - See LICENSE file for details.

---

**Version:** 1.0.0  
**Last Updated:** 2026-02-22  
**Status:** Ready for deployment 
