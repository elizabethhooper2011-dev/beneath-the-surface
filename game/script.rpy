# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.


$ import time

define d = Character("Diver", color="#64c5ee")


# # The game starts here.

# label start:

#     # Show a background. This uses a placeholder by default, but you can
#     # add a file (named either "bg room.png" or "bg room.jpg") to the
#     # images directory to show it.

#     scene bg room

#     # This shows a character sprite. A placeholder is used, but you can
#     # replace it by adding a file named "diver happy.png" to the images
#     # directory.

#     show diver happy

#     # These display lines of dialogue.

#     d "You've created a new Ren'Py game."

#     d "Once you add a story, pictures, and music, you can release it to the world!"
#     # This ends the game.

#     return

label start:
    "You begin your scuba diving tour. The hum of the boat overhead makes the water ripple. This is going to be a normal day."
    pause
    "...right?"
    pause
    while True:
        if location == "surface":
            menu:
                "Dive":
                    $ location = 'sunlit'
                "Wait":
                    "You wait for a little while."    
                    menu:
                        "Dive":
                            $ location = "sunlit"
                        "Wait":
                            "You wait for a while."
                            menu:
                                "Dive":
                                    $ location = "sunlit"
                                "Wait":
                                    "You wait for hours."
                                    pause
                                    "Eventually the boat gets bored and picks you up."
                                    pause #gap 0.5
                                    "I-I-I mean ... a rescue boat eventually comes to your rescue and takes you safely back home."
                                    pause
                                    "Boring Ending"
                                    pause
                                    return

        if location == 'sunlit':
            "You find yourself in the sunlit zone."
            pause
            "You contemplate your options."
            menu: 
                "Surface":
                    "You (not so calmly) resurface, for some reason."
                    $ location = "surface"
                "Backstroke":
                    "You try and use backstroke to escape."
                    pause
                    "But you don't realise that you are heading towards a series of sharp rocks."
                    pause
                    "You pierce your oxygen tank."
                    pause
                    "Your chest feels tight as you reflect on your idiocy."
                    pause
                    "Well done, you drowned."
                    pause
                    return
                "Breaststroke":
                    "Somehow, through sheer dumb luck, you survive."
                    pause
                    $ location = "twilight"