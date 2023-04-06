# This Function runs the actual game two parameters are needed frames per second "speed" and high score 
def runGame(fps, HighScore):
    #Import Modules 
    import random
    import pygame


    pygame.init()

    #Colors RGB Used
    white = (255, 255, 255)
    black = (0,0,0)
    green = (0,255,0)
    red = (255, 0, 0)
    grey = (128,128,128)
    orange = (255, 165, 0)
    yellow =(255, 255, 0)
    blue = (0, 0, 200)
    pink = (255,192,203)
    brown = (150,75,0)

    #constants 
    WIDTH = 255
    HEIGHT = 300
    lives = 3

    #Game Varibles
    score = 0
    scoreCounter = 0
    obstacle_speed = 2
    
    #Positioning 
    player_x = 120
    player_y = 150
    y_change = 0
    x_change = 0
    PlayerWidth = 20
    item1= 59
    item2=110
    item3=158
    item4 = 110
    obstacles = [300, 450, 600, 800]
    obstacles2 = [300, 450, 600, 300]

    #Boolean Varibles for Jumping and sliding 
    active = True
    jumping = False
    sliding = False
    running = True

    #Scene Creation 
    screen = pygame.display.set_mode([WIDTH, HEIGHT])
    pygame.display.set_caption("Runner Game")
    background = black
    font = pygame.font.Font('freesansbold.ttf', 18)
    
    #Timing and Limits 
    timer = pygame.time.Clock()
    seconds = 0
    seconds1 = 0
    seconds2 = 0

    #This simulates running the game 
    while running:
        
        if active: #Adds counter to get score seconds 
            scoreCounter += 1

        if scoreCounter == fps: #Adds one to score every second
            score += 1
            scoreCounter = 0
            
        if score >= HighScore: #Keeps track of high score 
                HighScore = score

        #Ticks through the fps and background
        timer.tick(fps) 
        screen.fill(background)
        
        if not active: #Stops player from jumping and sliding
            if score >= HighScore:
                HighScore = score
                jumping = False
                sliding = False

        #Creates Grass and Slidewalk on the left side
        Grass_Left = pygame.draw.rect(screen, green, [0, 0, 25, HEIGHT])
        SideWalk_Left = pygame.draw.rect(screen, grey, [25, 0, 25, HEIGHT])

        #Creates the Lanes for running 
        White1 = pygame.draw.rect(screen, white, [50, 0, 5, HEIGHT])
        Lane1 = pygame.draw.rect(screen, yellow, [100, 0, 5, HEIGHT])
        Lane2 = pygame.draw.rect(screen, yellow, [150, 0, 5, HEIGHT])
        White2 = pygame.draw.rect(screen, white, [200, 0, 5, HEIGHT])

        #Creates Grass and Slidewalk on the right side
        SideWalk_Right = pygame.draw.rect(screen, grey, [205, 0, 25, HEIGHT])
        Grass_Right = pygame.draw.rect(screen, green, [230, 0, 25, HEIGHT])

        #Creates the player "Green"
        player = pygame.draw.rect(screen, green, [player_x, player_y, PlayerWidth, PlayerWidth])

        #Creates the obstacles 
        obstacle0 = pygame.draw.rect(screen, blue, [item1,obstacles[0], 40, 20]) ### Police Car 
        obstacle1 = pygame.draw.rect(screen, red, [item2,obstacles[1], 35, 20]) ### Helicopter (SLIDING AVOIDS THIS)
        obstacle2 = pygame.draw.rect(screen, yellow, [item3,obstacles[2], 35, 20]) ### Blockage (JUMPING AVOIDS THIS)
        extraLives = pygame.draw.rect(screen, pink, [item4,obstacles[3], 10, 10]) ### Extra Life Heart 

        # Creates the buildings on the sides "Not Obstacles"
        buildings1 = pygame.draw.rect(screen, brown, [225,obstacles2[0], 30, 50])
        buildings2 = pygame.draw.rect(screen, brown, [225,obstacles2[1], 30, 50])
        buildings3 = pygame.draw.rect(screen, brown, [0,obstacles2[2], 30, 50])
        buildings4 = pygame.draw.rect(screen, brown, [0,obstacles2[3], 30, 50])

        heartst= ""
        for i in range(lives):
            heartst += '\4'
        score_text = font.render(f'Lives: {heartst}  Score: {score} ', True, white, blue) #Shows Lives and Score
        screen.blit(score_text, (50, 0))
        score_text = font.render(f'HIGH SCORE: {HighScore} ', True, white,blue) #Shows High Score
        screen.blit(score_text, (55, 253))
        quit_text = font.render("  QUIT ", True, white,blue) #Shows Quit Buttons and allows it to be selected
        screen.blit(quit_text, (142, 270))
        instruction_text = font.render(f' RESTART  ', True, white,blue) #Shows Restart button which allows selection
        screen.blit(instruction_text, (55, 270))

        if jumping == True: #Makes the Player Bigger when jumping
            PlayerWidth = 30
        if sliding == True: #Makes the Player Smaller when Sliding
            PlayerWidth = 10
        if jumping == False and sliding == False: #Keeps player regular size.
            PlayerWidth = 20
            
        for event in pygame.event.get(): #Gets Mouse Positioning for buttons 
            mouse = pygame.mouse.get_pos()
        
            if event.type == pygame.QUIT: #Used if the player quits 
                running == False
                
            if event.type == pygame.MOUSEBUTTONDOWN: #Checks if the restart button is selected "Resets Lives and High Score"
                if mouse[0] > 50 and mouse[0] < 100:
                    if mouse[1] < 300 and 100 < mouse[1]:
                        playAgain(fps, HighScore)
                        
              
                if mouse[0] > 150 and mouse[0] < 200: # Checks if the quit button is selected "Returns to main menu"
                    if mouse[1] < 300 and 100 < mouse[1]:
                        exit_to_menu(HighScore)

            if mouse[0] > 50 and mouse[0] < 100: #Highlights the Restart button is mouse positioning is over it 
                if mouse[1] < 300 and 100 < mouse[1]:
                    instruction_text = font.render(f' RESTART  ', True, red, blue)
                    screen.blit(instruction_text, (55, 270))
                    
            if mouse[0] > 150 and mouse[0] < 200: #Highlights the Quit button is mouse positioning is over it 
                if mouse[1] < 300 and 100 < mouse[1]:
                    quit_text = font.render("  QUIT ", True, red, blue)
                    screen.blit(quit_text, (142, 270))

            if event.type == pygame.KEYDOWN: #Checks if a key is pressed 
                if event.key == pygame.K_UP: #Allows the User to jump with a time limit
                    jumping = True
                    seconds1 = 0 #Time Limit Set
                if event.key == pygame.K_RIGHT: #Moves the player to the right ONLY if active
                    if active:
                        x_change = 1
                if event.key == pygame.K_LEFT: #Moves the player to the left ONLY if active
                    if active:
                        x_change = -1
                if event.key == pygame.K_DOWN: #Allows the User to Slide with a time limit
                    seconds1 = 0 #Time Limit Set
                    sliding = True 
            if event.type == pygame.KEYUP: #When the button is released 
                if event.key == pygame.K_RIGHT: #Stops movement 
                    x_change = 0
                if event.key == pygame.K_UP: #Stops movement 
                    jumping = False
                if event.key == pygame.K_LEFT: #Stops movement 
                    x_change = 0
                if event.key == pygame.K_DOWN: #Stops movement 
                    sliding = False
                
                
        for i in range(len(obstacles)):
            if active:
                #Counts 1/100 seconds for following time limits 
                seconds += 1
                seconds1 += 1
            #Randomly generates Obstacles and Hearts with time limits 1 second
                if seconds1 > 100:
                    jumping = False
                    sliding = False
                    seconds1 = 0
                obstacles[i] += obstacle_speed
                if obstacles[i] > 300:
                    obstacles[i] = random.randint(-500,-100)
                    if i == 3:
                        obstacles[i] = random.randint(-10000,-1000)
                    randLane = {59, 110,158}
                    if i == 0:
                        item1 = random.choice(tuple(randLane))
                    if i == 1:
                        item2 = random.choice(tuple(randLane))
                    if i == 2:
                        item3 = random.choice(tuple(randLane))
                    item4 = random.choice(tuple(randLane))

                # Randomly Generates Buildings 
                obstacles2[i] += obstacle_speed
                if obstacles2[i] > 300:
                    obstacles2[i] = random.randint(-125,-20)

                #Using time limits checks for collition Player can only be hit once every 1 second
                if seconds > 100:     
                    if player.colliderect(obstacle0) or player.colliderect(obstacle1) or player.colliderect(obstacle2) or player.colliderect(extraLives):
                        seconds = 0
                        if player.colliderect(extraLives) and not sliding and not jumping :
                            lives += 1
                        if player.colliderect(obstacle0):
                            lives -= 1
                        if player.colliderect(obstacle1) and not sliding:
                            lives -= 1
                        if player.colliderect(obstacle2) and not jumping:
                            lives -= 1
                        if lives == 0:
                           active = False


            #Checks for X and Y player changes 
            if 0 <= player_x <= 430:
                player_x += x_change
                
            if player_x < 55:
                player_x = 55
                
            if player_x > 180:
                player_x = 180

            if 200 >= player_y:
                player_y -= y_change

            if player_y < 0:
                y_change = 0
                
            
        pygame.display.flip() 
    pygame.quit() 

'''#Play Again Function 
def playAgain(fps, HighScore):
    runGame(fps, HighScore)

# Exit Function
def exit_to_menu(HighScore):
    import JAFN_Menu
    JAFN_Menu.mainMenu(HighScore)

#Displays Start Menu "This is in a seprate JAFN_Menu Module"
def startMenu():
    import JAFN_Menu
    JAFN_Menu.mainMenu(0)

#Runs the upper function ONLY if this module is run 
if __name__ == "__main__":
    startMenu()'''
