---
name: new-scenario
description: "Design and create a new game scenario/level"
---

# Create New Scenario

Design a new level/scenario for the game.

Before creating, review the existing map structure:
- Read `src/map.json` to understand the Tiled map format (layers, tilesets, grid size)
- Review `src/game.py` to understand how maps are loaded and which layers are expected:
  - `Platforms` - collidable walls/ground
  - `Packages` - collectible items
  - `Background` - decoration tiles
  - `Goal` - level end trigger
- Check available tiles in `assets/images/`

When designing a new scenario:
1. Ask the user about theme, difficulty, and desired layout
2. Define enemy placements (types, positions, patrol boundaries)
3. Define package/collectible locations
4. Ensure the level is completable (path from start to goal exists)
5. Consider A* pathfinding implications — avoid layouts where enemies get stuck

Output the scenario as a new map.json or as modifications to the existing one, depending on user preference.
