"""Start menu view for Porch Pirate."""

import arcade
from arcade.gui import (
    UIAnchorLayout,
    UIBoxLayout,
    UIDropdown,
    UIFlatButton,
    UILabel,
    UIOnChangeEvent,
    UIOnClickEvent,
    UIView,
)

from scenarios import SCENARIOS, DIFFICULTIES


class StartMenuView(UIView):
    """Main menu shown when the game launches."""

    def __init__(self):
        super().__init__()
        self.selected_difficulty = DIFFICULTIES[0]
        self.selected_scenario = SCENARIOS[0]
        self._build_ui()

    def _build_ui(self):
        root = UIAnchorLayout()

        vbox = UIBoxLayout(space_between=20)

        title_label = UILabel(
            text="Porch Pirate",
            font_size=36,
            bold=True,
            text_color=arcade.color.WHITE,
        )
        vbox.add(title_label)

        # Scenario selector
        vbox.add(UILabel(text="Scenario:", font_size=14, text_color=arcade.color.WHITE))

        scenario_names = [s["name"] for s in SCENARIOS]
        self.scenario_dropdown = UIDropdown(
            default=scenario_names[0],
            options=scenario_names,
            width=200,
            height=35,
        )

        @self.scenario_dropdown.event("on_change")
        def on_scenario_change(event: UIOnChangeEvent):
            for s in SCENARIOS:
                if s["name"] == event.new_value:
                    self.selected_scenario = s
                    break

        vbox.add(self.scenario_dropdown)

        # Difficulty selector
        vbox.add(UILabel(text="Difficulty:", font_size=14, text_color=arcade.color.WHITE))

        self.difficulty_dropdown = UIDropdown(
            default=DIFFICULTIES[0],
            options=DIFFICULTIES,
            width=200,
            height=35,
        )

        @self.difficulty_dropdown.event("on_change")
        def on_difficulty_change(event: UIOnChangeEvent):
            self.selected_difficulty = event.new_value

        vbox.add(self.difficulty_dropdown)

        # Start button
        start_button = UIFlatButton(text="Start Game", width=200, height=50)

        @start_button.event("on_click")
        def on_start_click(event: UIOnClickEvent):
            self._launch_game()

        vbox.add(start_button)

        root.add(vbox, anchor_x="center", anchor_y="center")
        self.add_widget(root)

    def _launch_game(self):
        from game import GameView, SpeechRecognizerThread

        game_view = GameView()
        game_view.level = self.selected_difficulty
        game_view.map_file = self.selected_scenario["map_file"]
        game_view.setup()
        self.window.show_view(game_view)

        thread = SpeechRecognizerThread(1, game_view)
        thread.start()

    def on_show_view(self):
        super().on_show_view()
        arcade.set_background_color(arcade.color.DARK_SLATE_GRAY)
