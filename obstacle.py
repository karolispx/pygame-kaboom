import random

# Obstacle class
class Obstacle:
    # Initialize obstacle
    def __init__(self, config):
        # Initialize config
        self.config = config

        # Define variables
        self.positionX = random.randint(10, (self.config.WINDOW_WIDTH - 10))
        self.positionY = 20
        self.velocity = random.randint(self.config.MIN_OBSTACLE_VELOCITY, self.config.MAX_OBSTACLE_VELOCITY) + 10

        if self.config.LEVEL == 1: self.color = (255, 0, 0)
        elif self.config.LEVEL == 2: self.color = (0, 0, 255)
        elif self.config.LEVEL == 3: self.color = (0, 255, 0)
        elif self.config.LEVEL == 4: self.color = (150, 50, 150)
        else: self.color = (255, 130, 0)

        self.radius = random.randint(10, 20)
    
    # Control obstacle
    def control(self):
        # Set obstacle position
        self.positionY += self.velocity

        # Check if obstacle has left the window
        if self.positionY > self.config.WINDOW_HEIGHT:
            # Create more obstacles based on the difficulty
            obstaclesCreate = self.config.MAX_OBSTACLES - len(self.config.OBSTACLES)

            if obstaclesCreate < 1: obstaclesCreate = 1

            while obstaclesCreate > 0:
                self.config.OBSTACLES.append(Obstacle(self.config))
                obstaclesCreate -= 1

            # Destroy obstacle if outside of the window
            self.config.OBSTACLES.remove(self)
            self.config.SCORE += 1
            del self

            return False
        else:
            return True
