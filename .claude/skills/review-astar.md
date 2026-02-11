---
name: review-astar
description: "Review A* pathfinding and enemy AI for correctness and performance"
---

# Review A* Pathfinding

Perform a thorough review of the pathfinding system and enemy AI.

Files to analyze:
- `src/AStarSearch.py` - A* algorithm, Graph class, GameBarriers
- `src/DataStructures/AbstractDataStructures.py` - PriorityQueue
- `src/enemy.py` - Base enemy with path following
- `src/robot.py` - Robot AI per difficulty level
- `src/zombie.py` - Zombie AI per difficulty level

Review for:
1. **Correctness** - Does A* produce optimal paths? Are heuristics admissible?
2. **Performance** - Iteration limits, unnecessary recalculations, data structure efficiency
3. **Edge cases** - What happens when no path exists? When player is unreachable?
4. **Difficulty balance** - Are easy/medium/hard behaviors meaningfully different?

Provide a summary with specific findings and actionable suggestions.
