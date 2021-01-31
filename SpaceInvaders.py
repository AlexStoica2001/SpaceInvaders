'''
Space Invaders

short game description: The purpose of the game is to achieve a score as good as possible to climb the leaderboard!
rules of the game: You can have only one bullet on the screen and as you shoot more invaders their speed will increase.

screen resolution: 1280x720
cheat code to kill all enemies without scoring them (you need to press those buttons in order):   =[]=
cheat code to increase your score by 100 (you need to press those buttons in order):   =lol
boss key to open/close the boss image: esc  (attention: this key should not be used for other purposes!)

images provided by: https://www.kenney.nl and my personal archive
'''

from tkinter import Tk, Canvas, PhotoImage, Entry, Button, Label
from random import randint as rand
from time import sleep

def createWindow(weight, height): #creating the main window
    window = Tk()
    window.title("Space Invaders")

    wscreen = window.winfo_screenwidth() #setting the sizes of the window according the screen
    hscreen = window.winfo_screenheight()
    x = wscreen / 2 - width / 2
    y = hscreen / 2 - height / 2

    window.geometry('%dx%d+%d+%d' % (width, height, x, y)) #sizing the the window

    return window

def setBackground(): #here we set the stars from the background
    colors = ["white", "#fefefe", "#dfdfdf", "cyan", "red", "medium blue"] #possible colors of the stars from background

    for i in range(500): #creating 500 stars
        x = rand(1, width - 1) #choosing randomly x coordinate of the star
        y = rand(1, height - 1) #choosing randomly y coordinate of the star
        size = rand(2, 5) #choosing randomly size of the star
        index = rand(0, len(colors) - 1) #choosing randomly the color of the star

        star = canvas.create_oval(x, y, x + size, y + size)          #creating a star on each canvas at the same position with the same color
        star2 = authentication.create_oval(x, y, x + size, y + size) #in this way when a canvas is swapped with another no difference will be seen
        star3 = leaderboard.create_oval(x, y, x + size, y + size)
        star4 = customization.create_oval(x, y, x + size, y + size)
        star5 = pause.create_oval(x, y, x + size, y + size)
        star6 = saveLoadCanvas.create_oval(x, y, x + size, y + size)

        canvas.itemconfig(star, fill = colors[index]) #putting in place the star on each of the canvases
        authentication.itemconfig(star2, fill = colors[index])
        leaderboard.itemconfig(star3, fill = colors[index])
        customization.itemconfig(star4, fill = colors[index])
        pause.itemconfig(star5, fill = colors[index])
        saveLoadCanvas.itemconfig(star6, fill = colors[index])

def enterName(): #this functions prompts when the user enters their name and wants to start playing
    global nameEntered
    nameEntered = True

def mainMenu(): #setting the main menu's appearance
    entry = Entry(window, highlightbackground = "black")  # this is the box where the user types their name

    authentication.create_text(width / 2, 150, text = "Please enter your name", fill = "white", font = ("Arial Bold", 30)) #setting the text before entering the name
    authentication.create_window(width / 2, 190, window = entry) #setting the box where the player's name should be introduced

    enterNameButton = Button(text = "Enter the game", highlightbackground = "black", command = enterName, width = 15) #setting start game button
    authentication.create_window(width / 2, 220, window = enterNameButton) #placing the button

    loadGameButton = Button(text = "Load Game", highlightbackground = "black", command = loadFromMainMenu, width = 15) #setting load game button
    authentication.create_window(width / 2, 250, window = loadGameButton) #placing the button

    showLeaderboardButton = Button(text = "Show Leaderboard", highlightbackground = "black", command = showLeaderboard, width = 15) #setting show leaderboard button
    authentication.create_window(width / 2, 280, window = showLeaderboardButton) #placing the button

    customizeKeysButton = Button(text = "Customize controls", highlightbackground = "black", command = customizeKeys, width = 15    ) #setting customize keys button
    authentication.create_window(width / 2, 310, window = customizeKeysButton) #placing the button

    authentication.pack() #this command makes the screen display the main menu
    authentication.focus_set()  # focusing on the main menu screen

    global nameEntered, name
    nameEntered = False
    name = "DefaultName"
    while not nameEntered:  # here we record the name typed until the user presses one of the buttons from the main menu
        name = entry.get()

        sleep(0.0001)
        window.update()

    authentication.pack_forget()  # closing main menu screen
    window.update()  # refreshing

def setGoBackToMainMenu(): #this function prompts when the user wants to go back to the main menu
    global goBackToMainMenu
    goBackToMainMenu = True

def processKey(event): #this function displays and converts into string the key pressed by the user
    global newKey
    customization.itemconfig(chosenKeyText, text = "You chose: " + str(event.keysym), fill = "white") #here the key is displayed on the canvas
    newKey = "<" + str(event.keysym) + ">" #here the key is converted into a specific type of string in order to be used for customization

def changeLeftKey(): #this function changes the key that moves left the spaceship
    global leftKey
    leftKey = newKey

def changeRightKey(): #this function changes the key that moves right the spaceship
    global rightKey
    rightKey = newKey

def changeFireKey(): #this function changes the key that makes the spaceship fire
    global fireKey
    fireKey = newKey

def customizeKeys(): #this functions prompts the screen where the key customizations are done
    global leftKey, rightKey, fireKey

    authentication.pack_forget() #hiding the old canvas from the main menu

    customization.pack() #showing the new canvas for the customization screen
    customization.focus_set() #this is to ensure we process every key pressed on this canvas and not on others

    customization.create_text(width / 3, 150, text = "Choose a key by pressing it!", fill = "white", anchor = "nw", font = ("Arial Bold", 30)) #informative text for the user
    global chosenKeyText
    chosenKeyText = customization.create_text(width / 3, 200, text = "You chose: ", fill = "white", anchor = "nw", font = ("Arial Bold", 30)) #informative text for the user that shows the last key pressed
    aux = Entry(window, bg = "black", fg = "black", borderwidth = 0, highlightthickness = 0,highlightbackground = "black") #this entry is made to capture the last key pressed and is hidden from the user's view
    customization.create_window(width - 100, height - 100, window = aux) #the entry seems to be placed on the screen but is fully black as the background so it is hidden
    aux.focus_set() #focusing on the entry in order to register every key pressed without clicking on the specific entry because is hidden

    changeLeftButton = Button(text = "Change Left Key", highlightbackground = "black", command = changeLeftKey, width = 15) #this button changes left key when pressed
    changeRightButton = Button(text = "Change Right Key", highlightbackground = "black", command = changeRightKey, width = 15) #this button changes right key when pressed
    changeFireButton = Button(text = "Change Fire Key", highlightbackground = "black", command = changeFireKey, width = 15) #this button changes fire key when pressed
    customization.create_window(width / 2, 270, window = changeLeftButton) #placing buttons on the screen
    customization.create_window(width / 2, 300, window = changeRightButton)
    customization.create_window(width / 2, 330, window = changeFireButton)

    currentLeft = customization.create_text(width / 3, 390, text = "Current left key: " + str(leftKey), fill = "white", anchor = "nw", font = ("Arial Bold", 30)) #displaying current keys chosen by the use for left, right and fire
    currentRight = customization.create_text(width / 3, 430, text = "Current right key: " + str(rightKey), fill = "white", anchor = "nw", font = ("Arial Bold", 30))
    currentFire = customization.create_text(width / 3, 470, text = "Current fire key: " + str(fireKey), fill = "white", anchor = "nw", font = ("Arial Bold", 30))

    global newKey, goBackToMainMenu
    goBackToMainMenu = False
    newKey = None
    backButton = Button(text = "Go to Main Menu", highlightbackground = "black", command = setGoBackToMainMenu) #this button is made to let the user go back to main menu when pressed
    customization.create_window(100, 40, window = backButton) #button is placed here
    while not goBackToMainMenu: #this loop waits for the user until they want to go back to main menu
        aux.bind('<Key>', processKey) #here is registered the last key pressed
        customization.itemconfig(currentLeft, text = "Current left key: " + str(leftKey)) #here are updated the key mappings on the screen so that the user can see their current choices
        customization.itemconfig(currentRight, text = "Current right key: " + str(rightKey))
        customization.itemconfig(currentFire, text = "Current fire key: " + str(fireKey))

        sleep(0.0001) #this has the purpose to let the screen be updated almost instantly
        window.update() #refresh the window to see the changes

    customization.pack_forget() #we hide the customize key canvas

    authentication.pack() #here we return to the main menu
    authentication.focus_set() #this is to ensure we process every key pressed on this canvas and not on others
    window.update() #refresh the window to see the new canvas

def showLeaderboard(): #this functions outputs the leaderboard on screen
    authentication.pack_forget() #hiding the past canvas

    players = [] #here will be stored the players with their score in format (score, player_name)

    try:
        with open("leaderboard.txt", "r") as file: #opening the leaderboard file
            for line in file:
                elements = line.rstrip("\n").split(separator) #parsing the input
                players.append((int(elements[1]), elements[0])) #storing each player
    except:
        pass

    players.sort(reverse = True) #sorting the players after their score so that the best score will be the first

    leaderboard.create_text(width / 2, 50, text = "Hall of Fame", fill = "yellow", font = ("Arial Bold", 60)) #informations for the user
    leaderboard.create_text(width / 2, 100, text="Displaying best score for each of the top 10 players", fill="white", font=("Arial Bold", 20))

    seenPlayers = set() #this set helps us to output only the best score of each player
    index = 0
    for element in players:
        score, name = element
        if name in seenPlayers: #here we ensure that we did not output this player before with a higher score
            continue
        seenPlayers.add(name) #marking that we will output this player
        leaderboard.create_text(width / 3 + 50, index * 40 + 140, text = str(index + 1) + ". " + str(name) + " -> " + str(score) + " points", anchor = "nw", fill = "white", font=("Arial Bold", 30)) #printing the player with their score
        index += 1
        if index == 10: #ensuring we print only top 10 players
            break

    global goBackToMainMenu
    goBackToMainMenu = False
    backButton = Button(text = "Go to Main Menu", highlightbackground = "black", command = setGoBackToMainMenu) #setting the go back to main menu button
    leaderboard.create_window(100, 40, window = backButton) #placing the button on screen

    leaderboard.pack() #showing the leaderboard canvas on screen
    leaderboard.focus_set() #focusing on it in order to ensure that every key pressed will be registered in this canvas
    window.update() #refreshing the screen
    while not goBackToMainMenu: #we remain in this screen until the user prompts us to go back to main menu by pressing the button
        sleep(0.0001)
        window.update()

    leaderboard.pack_forget() #hiding the canvas of the leaderboard

    authentication.pack() #showing the old canvas of the main menu
    authentication.focus_set() #focusing on it
    window.update() #refreshing the screen

def addToLeaderboard(name, score): #here we add a player with their score into the leaderboard
    with open("leaderboard.txt", "a") as file:
        file.write(str(name) + separator + str(score) + "\n") #we add the player into the file in the format NAMEseparatorSCORE\n

def goLeft(event): #this function is prompted by a button and moves the spaceship to left
    pos = canvas.coords(player) #getting the current position of the spaceship
    if pos[0] > 10: #ensuring that we are not out of bounds
        canvas.move(player, -10, 0)  #moving the ship to left

def goRight(event): #this function is prompted by a button and moves the spaceship to left
    pos = canvas.coords(player) #getting the current position of the spaceship
    if pos[0] < width - 40:  #ensuring that we are not out of bounds
        canvas.move(player, 10, 0) #moving the ship to right

def fire(event): #this function is prompted by a button and makes the ship to land a bullet
    global activeBullet, bullet
    if not activeBullet: #ensuring that we do not have more than 1 bullet on the screen, this is one of the basic rules of the game
        pos = canvas.coords(player) #getting the position of the spaceship
        bullet = canvas.create_oval(pos[0] + 10, height - 70, pos[0] + 20, height - 60, fill = "yellow") #creating the bullet
        activeBullet = True #marking that a bullet was fired

def addEnemies(numberOfEnemies, enemies): #this function adds random enemies in the space
    for index in range(numberOfEnemies):
        x = rand(200, width - 200) #choosing random x coordinate of the enemy
        y = rand(60, 200) #choosing random y coordinate of the enemy
        enemies.append(canvas.create_image(x, y, anchor = "nw", image = invaderImage)) #creating the enemy and storing it to the list of enemies

def moveEnemies(speed, enemies): #this function moves all the enemies according to the game rule: enemies go to right as much as possible, then go 1 step down, the to left as much as possible and this process is repeated
    for enemy in enemies:
        canvas.move(enemy, speed[0], 0) #here we move the enemy to left or right according to their specific stage (left or right), with a fixed speed
    for enemy in enemies:
        pos = canvas.coords(enemy)
        if pos[0] < 10 or pos[0] > width - 40: #here we check if one if the enemies will be out of bounds when doing the next left/right movement
            for enemy2 in enemies:
                canvas.move(enemy2, 0, speed[1]) #since they can't move anymore left/right they will go one step down
            speed[0] *= -1 #after they are getting one step down they will move in the opposite direction on oX axis (example: if before they were moving to left, now will be moving to right)
            break #we want to stop the for because since we moved the enemies one step down we don't want to move them one more, but to move left/right

def moveTest(speed, enemies): #this function is just for testing purposes
    for enemy in enemies:
        canvas.move(enemy, 0, 1)

def isCollision(a, b, limit): #checking if 2 items collided
    distance = (a[0] - b[0]) ** 2 + (a[1] - b[1]) ** 2 #calculating the Euclidean distance between those two items
    if distance < limit: #if the distance is lower than a specific limit (chosen by testing) then those 2 items are colliding
        return True
    return False

def checkCollision(enemies, target, distance): #checking if a specific target is colliding with one or more of the enemies, the collision being resulted from distance between them being lower than a specific one
    for enemy in enemies:
        if isCollision(canvas.coords(enemy), canvas.coords(target), distance):
            if distance != 700: #this distance is specific to the bullet enemy comparison
                canvas.itemconfig(enemy, state = "hidden") #here we delete an enemy from the screen that was hit by a bullet
                enemies.remove(enemy) #we remove the enemy from the list as he died
            return True
    return False

def maxHeight(elements): #this functions gives the maximum Y coordinate from a list of items on the screen
    maxValue = 0 #here the max Y will be stored
    for element in elements:
        pos = canvas.coords(element) #getting coordinates of the item
        maxValue = max(maxValue, pos[1]) #updating maxium
    return maxValue

def exitGame(): #this function closes the game and adds the score to the leaderboard before closing
    addToLeaderboard(name, score) #here we add the score
    window.destroy() #here we close the game

def saveGame(): #saving a game
    with open("saves.txt", "a") as file: #opening the file with all the game saves
        toprint = gameName + separator + str(score) + separator +str(speed[0]) + separator + str(speed[1]) #the format of the save is NAME + SCORE + SPEEDonX + SPEEDonY + for each player(CoordinateX + CoordinateY) where "+" is replaced by a separator
        for enemy in enemies:
            x, y = canvas.coords(enemy)
            toprint = toprint + separator + str(x) + separator + str(y) #saving the coordinate of each enemy
        toprint = toprint + "\n"
        file.write(toprint) #putting the save into the file

def deleteOldEnemies(): #deleting all enemies
    for enemy in enemies:
        canvas.delete(enemy) #removing enemies from the screen
    enemies.clear() #removing the enemies from the list

def putEnemies(positions): #placing enemies at the positions specified into the given list
    global numberOfEnemies
    numberOfEnemies = len(positions) #getting the number of new enemies
    deleteOldEnemies() #deleting old enemies
    for index in range(0, len(positions), 2): #we go through this list with step +2 because enemy coordinates are stored like this: [x1, y1, x2, y2, x3, y3, ...]
        enemies.append(canvas.create_image(positions[index], positions[index + 1], anchor = "nw", image = invaderImage)) #placing the enemies on screen

def loadGame(): #this function loads a specific save
    loadedGames = {}  # every element will have the form {gamename : [score, speed[0], speed[1], x1, y1, x2, y2, ....] } where xi and yi are coordinates of the enemies
    try: #we use try except block because it is possible that we don't have any save yet, so the file is not created and the game should not crash
        with open("saves.txt", "r") as file: #opening the saves file to read from it
            for line in file:
                line = line.rstrip("\n").split(separator) #parsing the line
                newElement = []
                newElement.append(int(line[1])) #here we save the score
                for index in range(2, len(line)): #here we save the speeds and coordinates
                    newElement.append(float(line[index]))
                loadedGames[line[0]] = newElement #placing the save to its name location into the dictionary

        thisGame = loadedGames[gameName] #here we ensure that er pick the last saved game with the name stored in "gameName"

        global score, speed, enemies
        score = thisGame[0] #placing the old score
        speed[0] = thisGame[1] #placing the old speeds
        speed[1] = thisGame[2]

        putEnemies(thisGame[3:]) #placing the old enemies
        window.update() #refreshing the window
    except:
        pass #nothing happens here

def loadFromMainMenu(): #this function is called when load game button from main menu is pressed
    authentication.pack_forget() #hiding main menu
    saveLoadGame(False) #opening the actual load game window, False is to let the program know that we do not want the Save Game option on the screen

    authentication.pack() #showing again main menu
    authentication.focus_set() #focusing on main menu so that every key registered will we on that screen
    window.update() #refreshing screen

def loadFromPause(): #this function is called when save/load game button from pause menu is pressed
    pause.pack_forget() #hiding pause menu
    saveLoadGame(True) #opening the actual load game window, True is to let the program know that we do want the Save Game option on the screen

    pause.pack() #showing the pause menu again
    pause.focus_set() #focusing on pause menu so that every key registered will we on that screen
    window.update() #refreshing screen

def saveLoadGame(canSave): #this is the actual save/load menu
    saveLoadCanvas.pack() #showing the menu
    saveLoadCanvas.focus_set() #focusing on the menu so that every key registered will we on that screen

    global goBackToMainMenu
    goBackToMainMenu = False
    backButton = Button(text = "Go back", highlightbackground = "black", command = setGoBackToMainMenu) #this button prompts the iser back to the old menu
    saveLoadCanvas.create_window(100, 40, window = backButton) #placing the button on the screen

    saveLoadCanvas.create_text(width / 2, 40, text = "Type the save's name", fill = "white", font = ("Arial Bold", 30)) #information for the user
    searchBar = Entry(window, highlightbackground = "black") #the box where the user will type the name of the save
    saveLoadCanvas.create_window(width / 2, 70, window = searchBar) #placing it on the screen

    loadButton = Button(text = "Load Game", highlightbackground = "black", command = loadGame, width = 10) # #this button will load the game with the name typed by the user
    saveLoadCanvas.create_window(width / 2, 130, window = loadButton) #placing the button
    saveLoadCanvas.create_text(width / 2, 160, text = "After loading just return to the game and start playing", fill = "white", font = ("Arial Bold", 20)) #information for the user

    if canSave: #this ensure that we don't have the save game option when this window is opened from the main menu of the game because we do not have anything to save at that moment
        saveButton = Button(text = "Save Game", highlightbackground = "black", command = saveGame, width = 10) #save game button
        saveLoadCanvas.create_window(width / 2, 100, window = saveButton) #placing the button


    saveLoadCanvas.create_text(width / 2, 250, text = "Saved games: ", fill = "white", font = ("Arial Bold", 30)) #information for the user
    while not goBackToMainMenu: #we remain into this window until the user wants to go back to the old menu
        global gameName
        gameName = searchBar.get() #getting the game name typed by the user

        loadedGames = {}  # every element will have the form {gamename : [score, speed[0], speed[1], x1, y1, x2, y2, ....] } where xi and yi are coordinates of the invaders
        try: #we use try except block because it is possible that we don't have any save yet, so the file is not created and the game should not crash
            with open("saves.txt", "r") as file: #loading the old saves from the file
                for index, line in enumerate(file):
                    line = line.rstrip("\n").split(separator) #parsing the input
                    newElement = []
                    for index in range(1, len(line)):
                        newElement.append(float(line[index])) #saving this save's data
                    loadedGames[line[0]] = newElement
        except:
            pass

        for index, saveName in enumerate(loadedGames.keys()): #printing to the screen every save made
            saveLoadCanvas.create_text(width / 2, 295 + index * 35, text = saveName, fill = "white", font = ("Arial", 25))

        sleep(0.0001)
        window.update() #refreshing screen

    saveLoadCanvas.pack_forget() #hiding the save/load menu

def changePause(event = None): #this function change the state of the game from paused to not paused and vice versa
    global isPaused
    isPaused = not isPaused

def pauseScreen(): #this function prompts the pause menu
    canvas.pack_forget() #hiding the game screen
    pause.pack() #showing the pause screen
    pause.focus_set() #focusing on this menu so that every key is registered here

    pause.create_text(width / 2, 200, text = "Game Paused", fill = "white", font = ("Arial Bold", 50)) #information for the user

    unpauseButton = Button(text = "Return to game", highlightbackground = "black", command = changePause, width = 19) #return to game button
    pause.create_window(width / 2, 270, window = unpauseButton) #placing the button
    saveGameButton = Button(text = "Save & Load Game", highlightbackground = "black", width  = 19, command = loadFromPause) #save/load game button
    pause.create_window(width / 2, 300, window = saveGameButton) #placing the button
    quitGameButton = Button(text = "Quit Game and Save Score", highlightbackground = "black", width = 19, command = exitGame) #exit and save score button
    pause.create_window(width / 2, 330, window = quitGameButton) #placing the button

    while isPaused: #this while keeps the user in game pause until they press a button
        sleep(0.0001)
        window.update()

    pause.pack_forget() #closing the pause window
    canvas.pack() #opening the game window
    canvas.focus_set() #focusing on it so that the key pressed are registered there
    window.update() #refreshing the window

def saveLastKey(event): #this function saves the last 4 keys pressed for checking if a cheat code was introduced
    last4Keys.append(str(event.keysym)) #saving the key
    if len(last4Keys) > 4: #if we have more than 4 keys we remove the least recently key
        last4Keys.pop(0)

def cheatCode():
    if last4Keys == ["equal", "bracketleft", "bracketright", "equal"]: #cheat code for killing all enemies without scoring their death
        last4Keys.clear() #deleting last keys because otherwise this cheat code will be run at infinity

        global numberOfEnemies
        numberOfEnemies = 0
        deleteOldEnemies() #deleting enemies
        window.update() #refreshing the window

        sleep(1) #a pause for the game to refresh the board of enemies

    if last4Keys == ["equal", "l", "o", "l"]: #cheat code for adding +100 to your score
        global score
        score += 100
        last4Keys.clear() #deleting last keys because otherwise this cheat code will be run at infinity

def bossKey(event, oldCanvas): #this function makes the "working" image appear when boss key is pressed
    if gameActive: #this if ensures that if the game is running and the boss key is pressed the game progress won't be lsot
        changePause()

    global bossKeyActive
    if bossKeyActive: #if the boss key is active and user presses the same key then the boss image should be closed and the game should be resumed
        bossKeyActive = False #deactivating the boss key
        bossScreen.pack_forget() #closing the game
        if oldCanvas != canvas: #if old screen was not the game we return to it
            oldCanvas.pack() #showing the old screen
        else: #otherwise we return to the pause menu
            pause.pack() #showing the pause screen
    else:
        oldCanvas.pack_forget() #hiding the old screen
        bossKeyActive = True #activating the boss key
        bossScreen.pack() #showing the boss screen
    window.update() #refreshing the screen

width = 1280 #setting the sizes of the screen
height = 720

separator = "$#$" #separator characters for saving games and scores

newKey = None #new key for changing the controls

leftKey = "<Left>" #defautl keys for moving left, right and fire
rightKey = "<Right>"
fireKey = "<space>"

gameName = "DefaultGameName" #default name if the user doesn't introduce their name
nameEntered = False

defaultNumberOfEnemies = 10 #constant number of enemies from the screen
numberOfEnemies = 0 #current number of enemies
enemies = [] #list of all enemies from the screen
speed = [1, 10] #initial speeds of the enemies
score = 0 #score of the player

last4Keys = [] #last 4 keys pressed
bossKeyActive = False
gameActive = False

window = createWindow(width, height) #creating the main window

invaderImage = PhotoImage(file = "invader.gif") #loading the images used thorough the program
playerImage = PhotoImage(file = "player2.gif")
bossImage = PhotoImage(file = "bossScreen2.gif")

canvas = Canvas(window, bg = "black", width = width, height = height) #creating all canvases needed for every screen of the game
authentication = Canvas(window, bg = "black", width = width, height = height)
leaderboard = Canvas(window, bg = "black", width = width, height = height)
customization = Canvas(window, bg = "black", width = width, height = height)
pause = Canvas(window, bg = "black", width = width, height = height)
saveLoadCanvas = Canvas(window, bg = "black", width = width, height = height)

setBackground() #setting the background for each of the canvases so that it would be the same

bossScreen = Label(window, image = bossImage) #creating the boss screen when the button will be pressed
canvas.bind("<Escape>", lambda event: bossKey(event, canvas)) #binding the escape button as the boss key for every of the canvases
authentication.bind("<Escape>", lambda event: bossKey(event, authentication))
leaderboard.bind("<Escape>", lambda event: bossKey(event, leaderboard))
customization.bind("<Escape>", lambda event: bossKey(event, customization))
pause.bind("<Escape>", lambda event: bossKey(event, pause))
saveLoadCanvas.bind("<Escape>", lambda event: bossKey(event, saveLoadCanvas))

mainMenu() #prompting the main menu

#now we will open the actual game screen
canvas.pack() #displaying the actual game
canvas.focus_set() #focusing on the game screen so that every key pressed will be registered here

player = canvas.create_image(width / 2, height - 50, anchor = "nw", image = playerImage) #creating the spaceship

canvas.bind(leftKey, goLeft) #binding the move left key of the ship
canvas.bind(rightKey, goRight) #binding the move right key of the ship
activeBullet = False
bullet = None
canvas.bind(fireKey, fire) #binding the fire key of the ship
canvas.bind("<Key>", saveLastKey) #registering the last key pressed

txt = "Score: " + str(score)
scoreText = canvas.create_text(width / 2, 20, fill = "white", font = ("Times 20 italic bold", 30), text = txt) #displaying the score on the screen

isPaused = False
pauseImage = PhotoImage(file = "pause.gif") #importing the image for the pause button
pauseButton = Button(image = pauseImage, highlightbackground = "black", bg = "black", fg = "black", bd = 0, command = changePause) #creating the pause button
canvas.create_window(width - 50, 30, window = pauseButton) #placing the pause button

while True: #the actual game loop
    gameActive = True

    if(isPaused): #if the pause button is pressed then the pause screen should be displayed
        gameActive = False
        pauseScreen()

    cheatCode() #checking if the last 4 keys pressed are cheat codes

    if numberOfEnemies == 0: #if we do not have enemies on the screen we should generate and display them
        addEnemies(defaultNumberOfEnemies, enemies)
        numberOfEnemies = defaultNumberOfEnemies

    moveEnemies(speed, enemies) #move the enemies according to the game rules

    if checkCollision(enemies, player, 700) or maxHeight(enemies) >= height - 30: #if the spaceship hits one of the enemies or one of the enemies reaches the ground then the game is lost
        addToLeaderboard(name, score) #adding to the leaderboard the score since the game is over
        gameOver = canvas.create_text(width / 2, 300, text = "Game Over", fill = "white", font = ("Arial Bold", 60))  #information for the user
        saveMessageEnd = canvas.create_text(width / 2, 370, text = "You score has been saved", fill = "white", font = ("Arial Bold", 40)) #information for the user
        break #game is over

    if activeBullet and checkCollision(enemies, bullet, 300): #is a bullet hits an enemy
        canvas.itemconfig(bullet, state = 'hidden') #delete the bullet from the screen
        activeBullet = False

        addEnemies(1, enemies) #add another random enemy
        if speed[0] < 0: #as the enemies are killed the game must be harder, so the speed of enemies increases
            speed[0] -= 0.3
        else:
            speed[0] += 0.3
        score += 10 #adding the killed enemy to the score

    if activeBullet: #if the bullet is still active and it didn't hit anything then it should move normally
        canvas.move(bullet, 0, -10) #bullet is moved
        pos = canvas.coords(bullet) #new position of the bullet
        if pos[3] <= 0: #ensuring the bullet if not out of bounds
            activeBullet = False

    txt = "Score: " + str(score)
    canvas.itemconfigure(scoreText, text = txt) #updating the new score on the screen

    sleep(0.015)
    window.update() #refreshing the screen

window.mainloop()
