import pygame

# Base class for game objects
class CircleShape(pygame.sprite.Sprite):
    def __init__(self, x, y, radius):
        # we will be using this later
        if hasattr(self, "containers"):
            super().__init__(self.containers)
        else:
            super().__init__()

        self.position = pygame.Vector2(x, y)
        self.velocity = pygame.Vector2(0, 0)
        self.radius = radius
    

    def draw(self, screen):
        # sub-classes must override
        
        pass

    def update(self, dt):
        # sub-classes must override
        pass

    def collision_with(self,another_circle):
        x = self.position.distance_to(another_circle.position)
        if (self.radius + another_circle.radius) > x:
            return True
        else:
            return False

