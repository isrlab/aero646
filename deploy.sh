#!/bin/bash

# Quick deployment script for GitHub Pages
# Usage: ./deploy.sh "Your commit message"

# Get commit message from argument or use default
COMMIT_MSG="${1:-Update presentations}"

echo "🚀 Deploying to GitHub Pages..."
echo ""

# Show current status
echo "📊 Current status:"
git status --short
echo ""

# Add all changes
echo "➕ Adding changes..."
git add .

# Commit with message
echo "💾 Committing: $COMMIT_MSG"
git commit -m "$COMMIT_MSG"

# Push to GitHub
echo "⬆️  Pushing to GitHub..."
git push origin main

echo ""
echo "✅ Done! Your site will be updated at:"
echo "   https://isrlab.github.io/aero646/"
echo ""
echo "⏱️  GitHub Pages usually takes 1-2 minutes to rebuild."
