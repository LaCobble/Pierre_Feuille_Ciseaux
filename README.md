# Rock Paper Scissors (Pierre Feuille Ciseaux)

[![CI](https://github.com/LaCobble/Pierre_Feuille_Ciseaux/actions/workflows/ci.yml/badge.svg)](https://github.com/LaCobble/Pierre_Feuille_Ciseaux/actions/workflows/ci.yml)
![Python](https://img.shields.io/badge/python-3.8%2B-3776AB?logo=python&logoColor=white)
![GUI](https://img.shields.io/badge/GUI-Tkinter-informational)
[![License: MIT](https://img.shields.io/badge/license-MIT-blue.svg)](LICENSE)

Rock paper scissors with a Tkinter interface and three modes (player vs AI, player vs player, AI vs AI), built under a two-hour time limit.

<p align="center">
  <img src="docs/images/1-menu.webp" alt="Rock Paper Scissors main menu">
</p>

## What it does

The main menu offers three modes:

1. **P1 vs IA**: you play against the computer, which picks a random move.
2. **P1 vs P2**: two players take turns on the same computer.
3. **IA vs IA**: two random players face each other.

After each round the game shows the result (win, draw or loss) and asks whether you want to play again. Known issue: in player vs AI mode some win/loss outcomes are inverted (for example rock against paper is shown as a win). The move buttons use the French names: *Pierre* (rock), *Feuille* (paper), *Ciseau* (scissors).

## Screenshots

Captured on Linux (Xvfb) by running the real program and pressing its buttons; window titles are not shown. The fixed window sizes come from the original code.

<table>
  <tr>
    <td width="50%" align="center"><img src="docs/images/1-menu.webp" alt="Main menu with the three modes"></td>
    <td width="50%" align="center"><img src="docs/images/2-p1-vs-ia.webp" alt="Player vs AI: choose rock, paper or scissors"></td>
  </tr>
  <tr>
    <td align="center"><sub>Main menu: the three modes</sub></td>
    <td align="center"><sub>Player vs AI: pick <i>Pierre</i>, <i>Feuille</i> or <i>Ciseau</i></sub></td>
  </tr>
  <tr>
    <td align="center"><img src="docs/images/3-result.webp" alt="Round result with replay prompt"></td>
    <td align="center"><img src="docs/images/4-ia-vs-ia.webp" alt="AI vs AI mode"></td>
  </tr>
  <tr>
    <td align="center"><sub>Round result and replay prompt</sub></td>
    <td align="center"><sub>AI vs AI: press <b>PLAY</b> to watch a round</sub></td>
  </tr>
</table>

## Getting started

### Prerequisites

- Python 3.8 or newer with Tkinter. Tkinter ships with the python.org installers for Windows and macOS; on Debian/Ubuntu install it with `sudo apt install python3-tk`. No other package is needed.

### Run

```bash
git clone https://github.com/LaCobble/Pierre_Feuille_Ciseaux.git
cd Pierre_Feuille_Ciseaux
python PFC.py
```

## Project structure

```text
.
├── PFC.py      # the whole game: main menu, the three modes, result windows
└── README.md
```

## What this project demonstrates

- Building a multi-window desktop GUI with Tkinter (menus, buttons, pop-ups).
- Encoding game rules and a random computer player.
- Delivering a complete, playable program under a strict two-hour constraint.

## Context

A personal challenge from 2021: build a complete game with a graphical interface in under two hours. The code is kept as it was written, as a portfolio piece; only the repository around it (documentation, CI) has been tidied up.

## Contributing

Issues and small pull requests are welcome: see [CONTRIBUTING.md](CONTRIBUTING.md) and the [Code of Conduct](CODE_OF_CONDUCT.md).

## License

[MIT](LICENSE) © LaCobble
