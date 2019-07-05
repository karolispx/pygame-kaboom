# Config class
class Config:
    # Initialize obstacle
    def __init__(self):
        # Default variables tp be reused when game is restarted
        self.DEFAULT_VARIABLES = {
            'SCORE': 0,
            'LEVEL': 1,
            'MAX_OBSTACLES': 6,
            'MIN_OBSTACLE_VELOCITY': 6,
            'MAX_OBSTACLE_VELOCITY': 12,
        }

        # Define variables
        self.GAME_OVER = False
        self.GAME_STARTED = False
        self.GAME_RUNNING = True

        self.WINDOW_CAPTION = "Kaboom Game by Karolis Pliauskys"
        self.WINDOW_WIDTH = 1000
        self.WINDOW_HEIGHT = 800
        self.WINDOW_BACKGROUND = (232, 232, 232)
        self.AUDIO_VOLUME = 0.5
        self.GAME_TICKER = 20
        self.HEADING_COLOR = (50, 50, 50)
        self.TEXT_COLOR = (236, 55, 0)

        self.PLAYER_COLOR = (73, 142, 212)
        self.PLAYER_RADIUS = 20
        self.PLAYER_VELOCITY = 20
        self.PLAYER_DEFAULT_POSITION_X = int(self.WINDOW_WIDTH / 2)
        self.PLAYER_DEFAULT_POSITION_Y = int(self.WINDOW_HEIGHT - 50)

        self.OBSTACLES = []
        self.GAME_DIFFICULTY_MULTIPLIER = 6
        self.SCORE = self.DEFAULT_VARIABLES['SCORE']
        self.LEVEL = self.DEFAULT_VARIABLES['LEVEL']
        self.MAX_OBSTACLES = self.DEFAULT_VARIABLES['MAX_OBSTACLES']
        self.MIN_OBSTACLE_VELOCITY = self.DEFAULT_VARIABLES['MIN_OBSTACLE_VELOCITY']
        self.MAX_OBSTACLE_VELOCITY = self.DEFAULT_VARIABLES['MAX_OBSTACLE_VELOCITY']


    # Reset default values
    def resetDefaultValues(self):
        self.SCORE = self.DEFAULT_VARIABLES['SCORE']
        self.LEVEL = self.DEFAULT_VARIABLES['LEVEL']
        self.MAX_OBSTACLES = self.DEFAULT_VARIABLES['MAX_OBSTACLES']
        self.MIN_OBSTACLE_VELOCITY = self.DEFAULT_VARIABLES['MIN_OBSTACLE_VELOCITY']
        self.MAX_OBSTACLE_VELOCITY = self.DEFAULT_VARIABLES['MAX_OBSTACLE_VELOCITY']
        self.OBSTACLES = []

        self.GAME_OVER = False
        self.GAME_STARTED = True