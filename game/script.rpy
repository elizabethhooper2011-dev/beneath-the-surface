# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.


$ import time

define d = Character("Diver", color="#64c5ee")
image bg surface = "images/bg surface.png"
image d main = "images/d main.png"

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
    $ location = "surface"
    while True:
        if location == "surface":
            scene bg surface at truecenter
            show boat main#:
                #xpos right
                #ypos top
            show d main_small at center
            "You are on the surface of the water."
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
            scene bg sunlit
            show d main at truecenter
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
                    "You continue with your scuba dive, going deeper."
                    $ location = "twilight"

        if location == 'twilight':
            scene bg twilight
            show d main at truecenter
            "You find yourself in the twilight zone."
            pause
            "Everything seems to be going swimmingly until you see a shadowy fish in the distance."
            pause
            "From your brief marine biology class, you know that this is a barbeled dragonfish."
            pause
            "You also know that it has seen you."
            menu:
                "Swim away":
                    "You try to swim away from the dragonfish, which is now accelerating to 22mph."
                    pause
                    "You die at the hands of its toothy maw."
                    pause
                    "Well done, you were eaten."
                    pause
                    return
                "Fight":
                    #"You manage to hold it off with a rusty metal bar."
                    #pause
                    #"You impale it through its head."
                    #pause
                    #"You descend further into the ocean."
                    "As it draws closer, you spot a rusty metal pole laying next to some rocks."
                    pause
                    "in a split second decision, you firmly grab the pole (obviously with gloves on so there is no risk of tetanus) and swing it at the head of the barbeled dragonfish."
                    pause
                    "It stays there, dazed for a second, before trying to attack you."
                    pause
                    "Not wanting to die, you decide as a last ditch attempt to impale the dragonfish's skull."
                    pause
                    "You slowly retreat as blood leaks from its skull, contaminating the clear water."
                    pause
                    "You survived... barely."
                    pause
                    "Limping, you descend deeper."
                    $ location = "midnight"

            # if location == "midnight":
            #     "You find yourself in the midnight zone."
            #     pause
            #     "You grab a torch, and looking out across the landscape, you see a series of hydrothermal vents."
            #     pause
            #     "It's dark out here."
            #     pause
            #     "If you ride the water of the vents, you could potentially reach the surface."
            #     pause
            #     ""