import pygame
import random
import time

# Define constants for the screen size
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

# Define colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Define a class for a virtual pet
class VirtualPet:
    def __init__(self, name):
        self.name = name
        self.hunger = 0
        self.boredom = 0
        self.tiredness = 0
        self.dirtiness = 0
        self.age = 0
        self.alive = True
        self.image = pygame.image.load('pet.jpg')
        self.rect = self.image.get_rect()
        self.rect.center = (SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)
        self.font = pygame.font.Font(None, 36)

    def feed(self):
        self.hunger -= random.randint(1, 10)
        self.dirtiness += random.randint(1, 5)
        if self.hunger < 0:
            self.hunger = 0
        self.speak('Yum, thanks for the food!')

    def play(self):
        self.boredom -= random.randint(1, 10)
        self.tiredness += random.randint(1, 5)
        self.dirtiness += random.randint(1, 5)
        if self.boredom < 0:
            self.boredom = 0
        self.speak('That was fun, let\'s play again sometime!')

    def sleep(self):
        self.tiredness -= random.randint(5, 15)
        if self.tiredness < 0:
            self.tiredness = 0
        self.speak('Zzzzz...')

    def clean(self):
        self.dirtiness -= random.randint(5, 10)
        if self.dirtiness < 0:
            self.dirtiness = 0
        self.speak('Ahh, much better now that I\'m clean!')

    def aging(self):
        self.age += 1
        self.hunger += random.randint(1, 5)
        self.boredom += random.randint(1, 5)
        self.tiredness += random.randint(1, 5)
        self.dirtiness += random.randint(1, 5)
        if self.hunger > 100 or self.boredom > 100 or self.tiredness > 100 or self.dirtiness > 100:
            self.alive = False
            self.speak('I\'m sorry, I don\'t feel well...')

    def speak(self, message):
        self.message = self.font.render(message, True, WHITE, BLACK)
        self.message_rect = self.message.get_rect()
        self.message_rect
        
    def draw(self, screen):
        screen.blit(self.image, self.rect)
        if hasattr(self, 'message'):
            screen.blit(self.message, self.message_rect)

    # Initialize Pygame
pygame.init()

  # Set the window title
pygame.display.set_caption('Virtual Pet')

  # Create the window
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

  # Create a virtual pet and give it a name
pet = VirtualPet('Fluffy')

# Main game loop
while pet.alive:
    # Check for user input
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pet.alive = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_f:
                pet.feed()
            elif event.key == pygame.K_p:
                pet.play()
            elif event.key == pygame.K_s:
                pet.sleep()
            elif event.key == pygame.K_c:
                pet.clean()

    # Update the pet's status
    pet.aging()

    # Clear the screen
    screen.fill(BLACK)

    # Draw the pet on the screen
    pet.draw(screen)

    # Display the pet's message (if any)
    # Check if the pet has a message to display
    if hasattr(pet, 'message'):
        # Display the message
        screen.blit(pet.message, pet.message_rect)
        # Reset the message after a short delay
        pygame.time.delay(2000)
        pet.message = None
        pet.message_rect = None

    # Update the display
    pygame.display.flip()

    # Wait for a short time
    pygame.time.delay(100)

# Quit Pygame
pygame.quit()
