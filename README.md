# Pygame Kaboom!

---

![](assets/images/game-preview.gif)

---

***This is my second `Python` project and my first `Pygame` project ever. There's probably many better ways to do things, use this at your own risk! I built it as I wanted to learn more about Python and I wanted to make something interesting with it. There's a lot of room for improvement.***

This game should be a good starting point for anyone looking to start creating games using `Pygame Library`. I've tried to include as much of the functionality as I could, and I've seperated everything out into appropriate Classes/Functions so it would be easy for anyone to pull out any code that might be useful.

Find out more about `Pygame Library` here: https://www.pygame.org/news.

---

## Introduction

The purpose of the game is to avoid as many of the obstacles as possible. Score is incremented by 1 everytime an obstacle leaves the screen. There's currently **5** levels:

- **Level 1** - score is less than or equal to 100.
- **Level 2** - score is more than 100 and less than or equal to 200.
- **Level 3** - score is more than 200 and less than or equal to 300.
- **Level 4** - score is more than 300 and less than or equal to 400.
- **Level 5** - score is greater than 400 (good luck!).

Everytime the level increases, the obstacles become quicker and the amount of them that can appear on the screen at any given time increases, for example, if you're on **Level 1** - there will be 6 obstacles on the screen at any given time, if you're on **Level 5** - there will be 30 obstacles on the screen at any given time.

---

## Application's Structure:

- **assets** - folder for assets such as images, fonts, audio files.
- **assets/audio** - folder for audio files.
- **assets/designs** - folder for Adobe Illustrator files that can be used to update screen background images.
- **assets/fonts** - folder for fonts.
- **assets/images** - folder for images.
- **`config.py`** - contains configuration functions and variables, the file can be imported into other files easily to get access to those functions and variables.
- **`main.py`** - main file of the application, contains the main game functionality/loop etc.
- **`obstacle.py`** - contains functionality for obstacles.
- **`player.py`** - contains functionality for player.

---

## Run It Locally
1. `pip install pygame`
2. Clone this repository.
3. Open the folder in your terminal.
4. Run `python main.py`.

---

## Resources Borrowed from the WEB
**Background Image** - https://pixabay.com/photos/textile-jute-brown-fabric-texture-2918844/
Used to create background images that are visible in the game, they were incldued  in Adobe Illustrator designs.

**Segoe UI Symbol Font** - https://www.wfonts.com/font/segoe-ui-symbol
The font is used for all texts that are rendered in game (the score/level while in game and the 'game over' details). This font was selected specifically to be able to use HTML symbols (i.e. https://www.htmlsymbols.xyz/star-symbols) in the text.

**Gameover Audio File** - https://freesound.org/people/Prof.Mudkip/sounds/386862/

**Gameplay Audio File** - https://freesound.org/people/zagi2/sounds/270648/

**Theme Audio File** - https://freesound.org/people/zagi2/sounds/231579/

Pygame was unable to load the original `.wav` files due to the encoding, so https://audio.online-convert.com/convert-to-ogg was used to convert them to `.ogg` format.

---

## Would Be Nice To Have
1. Better collision detection.
2. Executable.
3. Some nice sprites for player/obstacles.
