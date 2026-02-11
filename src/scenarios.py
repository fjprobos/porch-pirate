"""Scenario and difficulty definitions for Porch Pirate."""

import os

_SRC_DIR = os.path.dirname(__file__)

SCENARIOS = [
    {
        "name": "Default",
        "map_file": os.path.join(_SRC_DIR, "map.json"),
    },
]

DIFFICULTIES = ["easy", "medium", "hard"]
