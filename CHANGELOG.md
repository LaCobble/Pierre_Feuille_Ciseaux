# Changelog

All notable changes to this project are documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

### Added

- Portfolio README, MIT license, contribution guide, code of conduct and security policy.
- Continuous integration (byte-compilation and secret scan) and a release workflow.

### Fixed

- The game modes and result windows open again: `main()` now declares the main window `global`. Since the code was moved into `main()` in August 2021, every sub-window failed with `NameError: name 'fenetre' is not defined`.
- README: the entry point is `PFC.py` and the clone URL points to this repository.

## [1.0.0] - 2022-03-17

First tagged version: the game as built for the challenge.

### Added

- Tkinter rock paper scissors with three modes: player vs AI, player vs player, AI vs AI.
- Result windows with a replay prompt.

[Unreleased]: https://github.com/LaCobble/Pierre_Feuille_Ciseaux/compare/v1.0.0...HEAD
[1.0.0]: https://github.com/LaCobble/Pierre_Feuille_Ciseaux/releases/tag/v1.0.0
