---
name: play
description: "Set up environment and launch the game"
---

# Play the Game

Launch Porch Pirate with the specified difficulty level.

1. Ensure the virtual environment is active:
```bash
source .venv/bin/activate
```

2. Run the game with the difficulty provided as argument (defaults to `easy`):
```bash
python src/game.py start <difficulty>
```

Valid difficulty levels: `easy`, `medium`, `hard`.

If no argument is provided, ask which difficulty the user wants.
