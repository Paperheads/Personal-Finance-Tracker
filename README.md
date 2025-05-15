# Personal Finance Tracker (CLI version)

A simple terminal-based finance tracker built with Python.  
You can add income and expenses, see your current balance, and list/filter/sort all your transactions.

This is just a practice project for learning OOP, file operations, and CLI structure in Python — nothing fancy here.

---

## How to run

```bash
python3 run.py
```

---

## Features

- Add income and expenses (with description + category)
- See your current balance
- View all transactions
- Filter by income or expenses
- Sort by amount or date
- All data saved in `package.json`

---

## Project structure

```
📁 models/          → transaction model + formatter  
📁 services/        → file reading/writing + data filters  
📁 repository/      → user balance and logic  
📄 cli.py           → command-line interface  
📄 run.py           → entry point  
📄 package.json     → data storage (JSON format)  
```

---

## Example usage

```
1 - Add income  
2 - Add expense  
3 - Show balance  
4 - Show all transactions  
5 - Show only income  
6 - Show only expenses  
7 - Sort by amount  
8 - Sort by date  
9 - Exit  
```

---

## Note

This is just a practice project — built to play with Python OOP, basic architecture, and data persistence
