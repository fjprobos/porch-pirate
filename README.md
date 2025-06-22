# Porch Pirate

Porch Pirate is a small platform game built with the [Arcade](https://api.arcade.academy/) library. It features enemies powered by an A* path finding algorithm and optional voice commands for the player.

## Quick start

1. **Create a virtual environment (recommended)**
   ```bash
   python3 -m venv .venv
   source .venv/bin/activate
   ```

2. **Install the dependencies**
   ```bash
   pip install -r requirements.txt
   ```
   The game also depends on a `DataStructures` package providing a `PriorityQueue` class. If this package is not available on your system, obtain it from the Berkeley "AI Pacman" project or provide an equivalent implementation.

3. **Run the game**
   ```bash
   python src/game.py start easy
   ```
   Replace `easy` with `medium` or `hard` to try different difficulties.

Use the arrow keys to move and jump. When a microphone is available you can also control the player with voice commands (`jump`, `right`, `left`, `stop`).
