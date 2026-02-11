# Porch Pirate

## Setup
```bash
uv venv .venv && source .venv/bin/activate && uv pip install -r requirements.txt
```

## Run
```bash
python src/game.py start easy    # easy / medium / hard
```

## Project structure
- `src/` - Source code (`game.py` is the entry point)
- `src/AStarSearch.py` - A* pathfinding algorithm for enemy AI
- `src/DataStructures/` - PriorityQueue used by A*
- `src/map.json` - Tiled map definition (100x20 grid)
- `assets/` - Images and sounds

## Code conventions
- Language: English for all code, comments, and commit messages
- Naming: PEP 8 — snake_case for functions/variables, PascalCase for classes
- Linting/formatting: Ruff
- Testing: pytest (tests/ directory at project root)
- Dependencies: pyproject.toml + uv (migrate from requirements.txt)

## Workflow rules
- Always plan before implementing non-trivial changes
- Auto-commit is OK when a task is complete
- Be extra careful with `src/game.py` (main loop) and `src/AStarSearch.py` (pathfinding) — always plan changes to these files

## Notes
- Uses arcade library for 2D game rendering and physics
- Enemies (robot.py, zombie.py) use A* pathfinding with difficulty-dependent behavior
- Voice commands optional (SpeechRecognition + PyAudio)
- No test suite currently exists
