
set -e

echo "======================================"
echo "Flask Debugger - Git Initialization"
echo "======================================"
echo ""

if [ -d ".git" ]; then
    echo "Git repository already exists!"
    read -p "Do you want to reinitialize? This will delete existing history (y/N): " -n 1 -r
    echo
    if [[ $REPLY =~ ^[Yy]$ ]]; then
        rm -rf .git
        echo "✓ Removed existing .git directory"
    else
        echo "Aborted."
        exit 1
    fi
fi

echo "Initializing Git repository..."
git init
echo "✓ Git initialized"
echo ""

echo "Configuring Git user..."
git config user.name "Max Developer"
git config user.email "max.developer@techcorp.com"
echo "✓ Git user configured"
echo ""

create_commit() {
    local message="$1"
    local days_ago="$2"
    local date=$(date -d "$days_ago days ago" +"%Y-%m-%d %H:%M:%S")
    
    git add .
    GIT_AUTHOR_DATE="$date" GIT_COMMITTER_DATE="$date" git commit -m "$message"
    echo "✓ Created commit: $message"
}



