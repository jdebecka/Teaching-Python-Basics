from Model.Animal import Animal
from Animal_Containers.Sharks import Sharks
from Model.Snake import Snake

horn = Animal('Horn Shark', 'Heterodontus', 'francisci', 4.0, 25)
swell = Animal('Swell Shark', 'Cephaloscyllium', 'ventriosum', 3.5, 10)
white = Animal('Great White Shark', 'Carcharadon', 'carcharias', 20.0, 70)
shortfin_mako = Animal('Shortfin Mako', 'Isurus', 'oxyrinchus', 12.0, 30)
longfin_mako = Animal('Longfin Mako', 'Isurus', 'paucus', 14.0, 'Unknown')
lemon = Animal('Lemon Shark', 'Negaprion', 'bevriostris', 11.0, 27)
bull = Animal('Bull Shark', 'Carcharhinus', 'leucas', 11.5, 14)
great_hammer = Animal('Great Hammerhead Shark', 'Sphyrna', 'mokarran', 20.0, 35)
nurse = Animal('Nurse Shark', 'Ginglymostoma', 'cirratum', 14.0, 35)
porbeagle = Animal('Porbeagle Shark', 'Lamna', 'nasus', 6.6, 65)
black_tip = Animal('Blacktip Reef Shark', 'Carcharhinus', 'melanopterus', 5.2, 13)


# create an object of a shark
# TODO: create at least 3 snakes
snake = Snake('Horn Shark', 'Heterodontus', 'francisci', 4.0, 25, True)

# TODO: Create class for clams
# TODO: Create container for clams
# TODO: Call funcs
print(snake.venomous)

# Create list of sharks
sharks = [horn, swell, white, shortfin_mako, longfin_mako, lemon, bull, great_hammer, nurse, porbeagle, black_tip]

sharks_object = Sharks(sharks)

sharks_object.print_all_sharks()
