---
name: new-enemy
description: "Design and implement a new enemy type"
---

# Create New Enemy

Design and implement a new enemy type for the game.

Before creating, review the existing enemy architecture:
- `src/enemy.py` - Base `Enemy` class (extends arcade.AnimatedWalkingSprite)
- `src/robot.py` - Robot subclass (no gravity, boundary patrol or A* tracking)
- `src/zombie.py` - Zombie subclass (has gravity, can jump)
- `src/AStarSearch.py` - Pathfinding system used by enemies
- `src/game.py` - How enemies are instantiated and added to sprite lists

When creating a new enemy:
1. Ask the user about the enemy concept (behavior, appearance, special abilities)
2. Create a new file `src/<enemy_name>.py` following the pattern of robot.py/zombie.py
3. Subclass `Enemy` from enemy.py
4. Implement difficulty-based behavior (easy/medium/hard)
5. Define sprite assets needed (check `assets/images/enemies/` for available sprites)
6. Update `src/game.py` to spawn the new enemy in the level
7. Follow PEP 8 naming conventions

Key design considerations:
- Each difficulty level should feel meaningfully different
- A* pathfinding integration: does the enemy use it? When?
- Physics: does the enemy have gravity? Can it jump/fly?
- Boundaries: patrol area when not tracking the player
