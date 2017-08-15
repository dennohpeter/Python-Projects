# Snake Game! written by Dema Abu Adas
# Started on May 26th 

# Modules needed:
import pygame, sys, random, time

checkErrors = pygame.init() #How you initialize pygame
#(x, y) => (tasks completed, failed)

#If there were errors, exit game
if checkErrors[1] > 0:
    print("(!) Had {0} initializing errors, exiting..", format({checkErrors[1]}))
    sys.exit(-1)
else:
    print("(+) PyGame successfully initialized!")

# Play Surface 
playSurface = pygame.display.set_mode((720, 460)) #Function used to set width/height of window, expects 1 argument of a tuple!
pygame.display.set_caption("Snake Game!") #Title of the game window

# Colours:
#Sends (r,g,b) args
red = pygame.Color(255, 0, 0) #Gameover
green = pygame.Color(0, 255, 0) #Snake
black = pygame.Color(0, 0, 0) #Score
white = pygame.Color(255, 255, 255) #Background
brown = pygame.Color(165, 42, 42) #Food

# Frames per second controller
fpsController = pygame.time.Clock()

# Important Variables
snakePos = [100,50] #The head
snakeBody = [[100,50], [90,50], [80,50]] #A LIST OF LISTS! 
foodPos = [random.randrange(1,72) * 10,random.randrange(1,46) * 10]
foodSpawn = True 

direction = 'RIGHT' 
changeto = direction

# Game over function
def gameOver():
    myFont = pygame.font.SysFont('monaco', 72)
    GOsurface = myFont.render('Game over!', True, red)
    GOrect = GOsurface.get_rect()
    GOrect.midtop = ( (360, 15) )
    playSurface.blit(GOsurface, GOrect)
    pygame.display.flip()
    time.sleep(5) #5 second wait
    pygame.quit() # pygame window exit
    sys.exit() # console exit

#Game Main Logic
while True:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			pygame.quit()
			sys.exit()
		elif event.type == pygame.KEYDOWN:
			if event.key == pygame.K_RIGHT or event.key == ord('d'):
				changeto = 'RIGHT'
			if event.key == pygame.K_LEFT or event.key == ord('a'):
				changeto = 'LEFT'
			if event.key == pygame.K_UP or event.key == ord('w'):
				changeto = 'UP'
			if event.key == pygame.K_DOWN or event.key == ord('s'):
				changeto = 'DOWN'
			if event.key == pygame.K_ESCAPE: 
				pygame.event.post(pygame.event.Event(QUIT))

	# validation of direction :-) 
	if changeto == 'RIGHT' and not direction == 'LEFT':
		direction = 'RIGHT'
	if changeto == 'LEFT' and not direction == 'RIGHT':
		direction = 'LEFT'
	if changeto == 'UP' and not direction == 'DOWN':
		direction = 'UP'
	if changeto == 'DOWN' and not direction == 'UP':
		direction = 'DOWN'	

	if direction == 'RIGHT':
		#[x,y]
		snakePos[0] += 10
	if direction == 'LEFT':
		snakePos[0] -= 10
	if direction == 'UP':
		snakePos[1] -= 10
	if direction == 'DOWN':
		snakePos[1] += 10

	# Snake body mechanism
	snakeBody.insert(0, list(snakePos))
	if snakePos[0] == foodPos[0] and snakePos[1] == foodPos[1]:
		foodSpawn = False
	else: 
		snakeBody.pop() 

	if foodSpawn == False: #spawns a new food randomly 
	 	foodPos = [random.randrange(1,72) * 10,random.randrange(1,46) * 10]
	
	foodSpawn = True
	playSurface.fill(white) #This is the part where we actually draw things on our canvas

	for pos in snakeBody:
		#This is to draw our smol snek
		pygame.draw.rect(playSurface, green, pygame.Rect(pos[0], pos[1], 10, 10))

	pygame.draw.rect(playSurface, brown, 
	pygame.Rect(foodPos[0], foodPos[1], 10, 10))

	#checking for the boundaries! 
	if snakePos[0] > 710 or snakePos[0] < 0:
		gameOver()
	if snakePos[1] > 450 or snakePos[1] < 0:
		gameOver()

	# when head hits body! 
	for block in snakeBody[1:]:
		if snakePos[0] == block[0] and snakePos[1] == block[1]:
			gameOver()

	pygame.display.flip()
	fpsController.tick(25)
