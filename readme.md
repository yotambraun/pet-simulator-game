# Pet Simulator






class called VirtualPet, which represents a virtual pet in a game. The VirtualPet class has a number of attributes, such as name, hunger, boredom, tiredness, dirtiness, age, and alive, that store information about the virtual pet.

The VirtualPet class has several methods that can be used to interact with the virtual pet. The feed method decreases the pet's hunger and increases its dirtiness. The play method decreases the pet's boredom and increases its tiredness and dirtiness. The sleep method decreases the pet's tiredness. The clean method decreases the pet's dirtiness. The aging method increases the pet's age, hunger, boredom, tiredness, and dirtiness.

The code also initializes Pygame and sets up a game window. It then creates an instance of the VirtualPet class and gives it the name "Fluffy". The game enters a main loop where it waits for user input and updates the pet's status. The pet can be fed, played with, put to sleep, or cleaned by pressing the corresponding keys on the keyboard. The game also increments the pet's age and updates its hunger, boredom, tiredness, and dirtiness at each iteration of the main loop. If any of these values exceeds 100, the pet is considered to be not alive and the game loop ends.
