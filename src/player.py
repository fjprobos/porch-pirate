import arcade
import os

# Get the absolute path to the assets directory
ASSETS_PATH = os.path.join(os.path.dirname(os.path.dirname(__file__)), "assets")
PLAYER_MOVE_SPEED = 5


class Player(arcade.AnimatedWalkingSprite):
    """An player sprite with basic walking movement"""

    def __init__(self, pos_x: int, pos_y: int) -> None:
        super().__init__(center_x=pos_x, center_y=pos_y)

        # Where are the player images stored
        texture_path = ASSETS_PATH + "/" + "images" + "/" + "players"

        # Set up the appropriate textures
        walking_texture_path = [
            texture_path + "/" + "character_maleAdventurer_walk0.png",
            texture_path + "/" + "character_maleAdventurer_walk1.png",
            texture_path + "/" + "character_maleAdventurer_walk2.png",
            texture_path + "/" + "character_maleAdventurer_walk3.png",
            texture_path + "/" + "character_maleAdventurer_walk4.png",
            texture_path + "/" + "character_maleAdventurer_walk5.png",
            texture_path + "/" + "character_maleAdventurer_walk6.png",
            texture_path + "/" + "character_maleAdventurer_walk7.png"
        ]
        standing_texture_path = texture_path + "/" + "character_maleAdventurer_hold.png"

        # Load them all now
        base_textures = [
            arcade.load_texture(texture)
            for texture in walking_texture_path
        ]

        self.walk_left_textures = [
            texture.flip_horizontally()
            for texture in base_textures
        ]

        self.walk_right_textures = base_textures

        base_standing_texture = arcade.load_texture(standing_texture_path)
        self.stand_left_textures = [base_standing_texture.flip_horizontally()]
        self.stand_right_textures = [base_standing_texture]

        # Set the initial texture
        self.texture = self.stand_left_textures[0]