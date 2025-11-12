# FP2425P1 – MNK Game Project

**A Python implementation of the m,n,k board game with human vs computer gameplay.**

This repository contains my solution for **Fundamentos da Programação – Project 1 (2024/25)**.  
All logic is implemented in a single file: `projectoFP.py`.

---

## 🔧 Running the Public Tests

To execute the public tests using **pytest**, place `projectoFP.py` and `test_public.py` in the same folder and run:

```bash
pytest -vv test_public.py

```

## Requirements:

- **Python 3.x

- **pytest (install with pip install pytest)

## 🧠 Project Overview

The project follows the official MNK specification:

- **Board stored as tuples of tuples

- **Player pieces: 1 = black, -1 = white

- **Win condition: k consecutive pieces (horizontal, vertical, diagonal)

- **Computer AI strategies:

- ***easy

- ***normal

- ***difficult

## 🧩 Core Implemented Functions

- **Board structure & validation

- **Position inspection & manipulation

- **Line checking (verifica_k_linhas)

- **End‐game detection (eh_fim_jogo)

- **Manual move input + AI automatic move

- **Full game execution (jogo_mnk)