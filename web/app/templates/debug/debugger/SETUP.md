# Setup Instructions for Flask Debugger Repository

This document explains how to set up and publish the Flask Debugger repository to GitHub with realistic commit history.

## Quick Start

### 1. Initialize Git Repository

Run the included script to create a realistic Git history:

```bash
chmod +x init_git.sh
./init_git.sh
```

This will create:
- **main branch**: Production code with 13 commits spanning 30 days
- **development branch**: Experimental features (2 commits)
- **feature/auth branch**: Work-in-progress authentication (1 commit)

### 2. Review the Commit History

```bash
# View all commits across all branches
git log --oneline --all --graph --decorate

# View detailed commit history
git log --stat

# Check which files were committed
git log --name-status

# View the .env leak commit specifically
git show <commit-hash-of-commit-8>
```

### 3. Customize (Optional)

Before publishing, you may want to customize:

**Git User Information:**
```bash
git config user.name "Your Name"
git config user.email "your.email@example.com"

# Re-write commits with new author
git filter-branch -f --env-filter '
    export GIT_AUTHOR_NAME="Your Name"
    export GIT_AUTHOR_EMAIL="your.email@example.com"
    export GIT_COMMITTER_NAME="Your Name"
    export GIT_COMMITTER_EMAIL="your.email@example.com"
' -- --all
```

**Modify .env Content:**
Edit the `.env` file in commit 8 to include your custom values:
```bash
# Checkout the commit
git checkout <commit-8-hash>

# Edit .env
nano .env

# Amend the commit
git add .env
git commit --amend --no-edit

# Return to main
git checkout main
```

### 4. Create GitHub Repository

1. Go to GitHub and create a **new repository**
2. Name it `debugger` or your preferred name
3. Make it **PUBLIC** (so OSINT researchers can find it)
4. **DO NOT** initialize with README, .gitignore, or license (you already have these)

### 5. Push to GitHub

```bash
# Add GitHub remote
git remote add origin https://github.com/YOUR-USERNAME/debugger.git

# Push all branches
git push -u origin --all

# Push all tags (if any)
git push -u origin --tags
```

### 6. Verify the Repository

Check on GitHub that:
-  All 3 branches are visible
-  Commit history shows realistic dates
-  `.env` file is visible in commit 8
-  `.env` is in `.gitignore` (but too late!)
-  Repository looks professional and realistic

## Important Security Notes

### The Intentional Vulnerability

This repository intentionally includes a security vulnerability for CTF/training purposes:

**Commit 8** (around Feb 10, 2024) contains a committed `.env` file with:
- `WERKZEUG_PIN`: PIN to unlock the debugger
- `FLAG`: The CTF flag
- `SECRET_KEY`: Flask secret key
- `DATABASE_URL`: Database credentials

This simulates a **realistic developer mistake** where:
1. Developer commits `.env` for "quick testing"
2. Later adds `.env` to `.gitignore` (commit 9)
3. But the sensitive data is already in Git history
4. Stays visible forever unless force-pushed

### For CTF Participants

To find the vulnerability:
```bash
# Clone the repository
git clone https://github.com/YOUR-USERNAME/debugger.git

# Search commit history for .env
git log --all --full-history -- .env

# View the commit that added .env
git show <commit-hash>:/.env

# Or search all commits for sensitive keywords
git log --all -S "WERKZEUG_PIN"
git log --all -S "FLAG"
```

## Realistic Scenario

This repository simulates a real-world scenario:

**Timeline:**
- **Jan 23**: Project started, initial setup
- **Jan 25-30**: Core development (Flask app, templates, styling)
- **Feb 2**: Debug mode implemented
- **Feb 4**: Docker support added
- **Feb 7**: Environment configuration added
- **Feb 10**: `.env` accidentally committed (developer was rushing to a meeting)
- **Feb 12**: `.gitignore` updated (too late!)
- **Feb 14-21**: Continued development, security improvements

**The Mistake:**
The developer thought they were committing just configuration templates but accidentally included the actual `.env` file with production-like credentials. Two days later, they realized the mistake and updated `.gitignore`, but the damage was done.

## Testing Locally

Before pushing to GitHub, test that everything works:

```bash
# Create virtual environment
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Copy and edit .env
cp .env.example .env.local
nano .env.local

# Run the application
DEBUG=0 python app.py

# Test with debug mode
DEBUG=1 WERKZEUG_PIN=189-274-365 python app.py
```

## Docker Testing

```bash
# Build image
docker build -t flask-debugger:test .

# Run container
docker run -p 5000:5000 --env-file .env.local flask-debugger:test

# Test endpoints
curl http://localhost:5000/status
curl http://localhost:5000/health
```

## Cleanup (If Needed)

If you need to start over:

```bash
# Remove git history
rm -rf .git

# Re-run initialization
./init_git.sh
```

## Advanced: Multiple Developer Personas

To make it even more realistic, you can create commits from different "developers":

```bash
# After running init_git.sh, rewrite some commits

# Commit 1-5: Alice (Team Lead)
git filter-branch --env-filter '
    if [ $GIT_COMMIT = <commit-1-hash> ] ||
       [ $GIT_COMMIT = <commit-2-hash> ] ||
       [ $GIT_COMMIT = <commit-3-hash> ] ||
       [ $GIT_COMMIT = <commit-4-hash> ] ||
       [ $GIT_COMMIT = <commit-5-hash> ]; then
        export GIT_AUTHOR_NAME="Alice Thompson"
        export GIT_AUTHOR_EMAIL="alice.thompson@techcorp.com"
        export GIT_COMMITTER_NAME="Alice Thompson"
        export GIT_COMMITTER_EMAIL="alice.thompson@techcorp.com"
    fi
' -- --all

# Commit 6-9: Bob (DevOps)
# ... similar for other developers
```

## Troubleshooting

**Issue**: `git push` rejected
- Check if repository is initialized on GitHub
- Ensure you're pushing to correct remote
- Try: `git push -f origin main` (only for initial setup!)

**Issue**: Commits show wrong dates
- Git dates are set in the script using `GIT_AUTHOR_DATE`
- Verify with: `git log --format=fuller`

**Issue**: `.env` not showing in history
- Check commit 8: `git show HEAD~5:.env`
- Verify file exists: `git ls-tree -r <commit-8-hash>`

## Support

For questions or issues:
1. Check the commit history: `git log --all --oneline`
2. Review this setup guide
3. Test locally before pushing to GitHub
