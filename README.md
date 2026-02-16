# hello-codex

A minimal demonstration project created and managed automatically by Codex.

## What It Does

This repository contains a Python Hello World script that prints:

```text
Hello, I'm Codex
```

Goal: validate an end-to-end agent workflow, from code creation to version control and GitHub publishing.

## Project Structure

```text
hello-codex/
├── main.py
├── README.md
└── .gitignore
```

- `main.py`: main script entry point.
- `README.md`: project documentation.
- `.gitignore`: local secret and cache exclusions.

## Run Locally

Requirements:
- Python 3 installed.

Default command:

```bash
python3 main.py
```

Custom message:

```bash
python3 main.py "Hi from CLI"
```

## What Was Done in This Repository

1. Initialized a local Git repository.
2. Created the base `main.py` script.
3. Added the initial hello-world commit.
4. Published the repository to GitHub (`main` branch).
5. Added basic secret protection with `.gitignore`.

## Security Notes

This repo ignores by default:
- `.github_token`
- `.env` and `.env.*`
- Python cache (`__pycache__/`, `*.pyc`)

Never commit tokens or credentials.

## Recommended Workflow

For future changes:

```bash
git add .
git commit -m "feat: describe your change"
git push
```

Commit style: Conventional Commits (`feat:`, `fix:`, `docs:`, `chore:`).
