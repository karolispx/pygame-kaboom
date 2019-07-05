# Player class
class Player:
    def __init__(self, config):
        # Initialize config
        self.config = config

        # Define variables
        self.color = self.config.PLAYER_COLOR
        self.radius = self.config.PLAYER_RADIUS
        self.velocity = self.config.PLAYER_VELOCITY
        self.positionX = self.config.PLAYER_DEFAULT_POSITION_X
        self.positionY = self.config.PLAYER_DEFAULT_POSITION_Y


    # Reset player position
    def resetPlayerPosition(self):
        self.positionX = self.config.PLAYER_DEFAULT_POSITION_X
        self.positionY = self.config.PLAYER_DEFAULT_POSITION_Y


    # Player control
    def control(self, pygame, keys):
        # Update player's location
        if keys[pygame.K_a] and self.positionX > self.radius: self.positionX -= self.velocity 
        if keys[pygame.K_d] and self.positionX < (self.config.WINDOW_WIDTH - self.radius): self.positionX += self.velocity
        if keys[pygame.K_w] and self.positionY > self.radius: self.positionY -= self.velocity
        if keys[pygame.K_s] and self.positionY < (self.config.WINDOW_HEIGHT - self.radius): self.positionY += self.velocity

        # Ensure player stays within the window
        if self.positionX < self.radius: self.positionX = self.radius
        if self.positionX > (self.config.WINDOW_WIDTH - self.radius): self.positionX = self.config.WINDOW_WIDTH - self.radius
        if self.positionY < self.radius: self.positionY = self.radius
        if self.positionY > (self.config.WINDOW_HEIGHT - self.radius): self.positionY = self.config.WINDOW_HEIGHT - self.radius


    # Detect collisions
    # TODO: Adjust collision detection - it's not very accurate
    def detectCollisions(self):
        # Get center position of player
        playerPositionX = self.positionX + int(self.radius / 2)
        playerPositionY = self.positionY + int(self.radius / 2)

        for obstacle in self.config.OBSTACLES:
            # Get center position of each obstacle
            obstaclePositionX = obstacle.positionX + int(obstacle.radius / 2)
            obstaclePositionY = obstacle.positionY + int(obstacle.radius / 2)

            # Check if player and any of the obstacles overlap/collide
            if (obstaclePositionX < (playerPositionX + self.radius) and obstaclePositionX > (playerPositionX - self.radius)) and (obstaclePositionY < (playerPositionY + self.radius) and obstaclePositionY > (playerPositionY - self.radius)):
                return True
        return False


    # Adjust difficulty
    def adjustDifficulty(self):
        if self.config.SCORE <= 100: self.config.LEVEL = 1
        elif self.config.SCORE > 100 and self.config.SCORE <= 200: self.config.LEVEL = 2
        elif self.config.SCORE > 200 and self.config.SCORE <= 300: self.config.LEVEL = 3
        elif self.config.SCORE > 300 and self.config.SCORE <= 400: self.config.LEVEL = 4
        else: self.config.LEVEL = 5

        self.config.MAX_OBSTACLES = self.config.LEVEL * self.config.GAME_DIFFICULTY_MULTIPLIER
        self.config.MIN_OBSTACLE_VELOCITY = self.config.LEVEL * self.config.GAME_DIFFICULTY_MULTIPLIER
        self.config.MAX_OBSTACLE_VELOCITY = (self.config.LEVEL + 1) * self.config.GAME_DIFFICULTY_MULTIPLIER