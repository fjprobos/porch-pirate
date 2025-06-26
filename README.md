# Porch Pirate

Porch Pirate is a small platform game built with the [Arcade](https://api.arcade.academy/) library. It features enemies powered by an A* path finding algorithm and optional voice commands for the player.

## Quick start

1. **Install [uv](https://github.com/astral-sh/uv)** (optional)
   ```bash
   # Linux/macOS
   pip install uv
   ```
   ```powershell
   # Windows
   pip install uv
   ```

2. **Create a virtual environment (recommended)**
   ```bash
   uv venv .venv
   source .venv/bin/activate  # use `.venv\Scripts\activate` on Windows
   ```

3. **Install the dependencies**
   ```bash
   uv pip install -r requirements.txt
   ```
   The game also depends on a `DataStructures` package providing a `PriorityQueue` class. If this package is not available on your system, obtain it from the Berkeley "AI Pacman" project or provide an equivalent implementation.

4. **Run the game**
   ```bash
   python src/game.py start easy
   ```
   Replace `easy` with `medium` or `hard` to try different difficulties.

Use the arrow keys to move and jump. When a microphone is available you can also control the player with voice commands (`jump`, `right`, `left`, `stop`).
