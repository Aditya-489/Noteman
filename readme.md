# Noteman

A simple CLI note-taking application built with Python, Click, and PostgreSQL.

## Features

- Create notes
- Fetch notes by ID or title
- List all notes
- Delete notes
- Global CLI command support using `uv`

---

# Requirements

- Python 3.10+
- PostgreSQL
- uv

---

# Clone Project

```bash
git clone <your-repo-url>
cd notesapp
```

---

# PostgreSQL Setup

## Install PostgreSQL (Ubuntu)

```bash
sudo apt update
sudo apt install postgresql postgresql-contrib
```

---

## Start PostgreSQL

```bash
sudo systemctl start postgresql
sudo systemctl enable postgresql
```

---

## Open PostgreSQL Shell

```bash
sudo -u postgres psql
```

---

## Create Database

```sql
CREATE DATABASE notesdb;
```

---
## Create Notes Table

```sql
CREATE TABLE notes (
    id SERIAL PRIMARY KEY,
    title TEXT NOT NULL,
    content TEXT NOT NULL
);
```

---


# Create `.env` File

Create a `.env` file in the project root:

```env
DATABASE_URL=postgresql://notesuser:yourpassword@localhost:5432/notesdb
```

---

# Understanding The Database URL

Format:

```txt
postgresql://USERNAME:PASSWORD@HOST:PORT/DATABASE_NAME
```

Example:

```txt
postgresql://notesuser:yourpassword@localhost:5432/notesdb
```


# What Is Editable Mode?

Editable mode means the installed CLI command directly uses your source code.

So when you change Python files, the CLI updates immediately without reinstalling.

Example:

```bash
uv tool install -e .
```

The `-e` means editable.

---

# Option 1 — Local Development Setup (Recommended)

## Create Virtual Environment

```bash
uv venv
```

---

## Activate Environment

### Linux / Mac

```bash
source .venv/bin/activate
```

---

## Install Project In Editable Mode

```bash
uv pip install -e .
```

---

## Run CLI

```bash
noteman --help
```

---

# Option 2 — Global CLI Installation Using uv

This makes `noteman` available globally from anywhere in the terminal.

## Install Globally In Editable Mode

```bash
uv tool install -e .
```

---

## Verify Installation

```bash
noteman --help
```



# Available Commands

## Create Note

```bash
noteman make "Title" "Content"
```

Example:

```bash
noteman make "Todo" "Buy milk"
```

---

## List All Notes

```bash
noteman get --a
```

---

## Get Note By ID

```bash
noteman get --i 1
```

---

## Get Note By Title

```bash
noteman get --t "Todo"
```

---

## Delete Note By ID

```bash
noteman kick --i 1
```

---

## Delete Note By Title

```bash
noteman kick --t "Todo"
```

---

# Project Structure

```txt
notesapp/
│
├── pyproject.toml
├── .env
│
└── noteman/
    ├── __init__.py
    ├── __main__.py
    ├── cli.py
    ├── db.py
    ├── notes.py
    └── remove.py
```

---

# Tech Stack

- Python
- Click
- PostgreSQL
- Psycopg
- uv

---

