$ import time

define d = Character("You", color="#64c5ee")
image bg surface = "images/bg surface.png"
image d main = "images/d main.png"

label start:
    "You begin your scuba diving tour. The hum of the boat overhead makes the water ripple. This is going to be a normal day."
    pause
    "...right?"
    pause
    d "This is fine.......but why does the boat sound quieter?"
    pause
    "When you surface, you can see the boat retreating into the distance."
    pause
    "You have been left behind."# Should you wait
    $ location = "surface"
    while True:
        if location == "surface":
            scene bg surface at truecenter with dissolve
            show boat main at truecenter
            show d main_small at center
            "You are on the surface of the water."
            hide boat main with fade
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
                                    pause
                                    "Eventually the boat gets bored and picks you up."
                                    pause 
                                    "I-I-I mean ... a rescue boat eventually comes to your rescue and takes you safely back home."
                                    pause
                                    "Well done, you survived. But that was so boring! You failed as a player! Try diving instead next time."
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
                    "You try and use breaststroke to escape, swimming deeper towards the bottom of the vast ocean."
                    pause
                    "Somehow, through sheer dumb luck, you survive." 
                    pause
                    "You continue with your scuba dive, going deeper."
                    $ location = "twilight"

        if location == 'twilight':
            scene bg twilight
            show d main at truecenter
            "You find yourself in the twilight zone."
            pause
            "Everything seems to be going swimmingly until you see a faint glow in the distance with a small silhouette"
            pause
            #"As the glowing blob "
            "From your brief marine biology class, you know that this is a barbeled dragonfish." # add more info about fish
            pause
            "You also know that it has seen you."
            menu:
                "Swim away":
                    "You try to swim away from the dragonfish, which is now accelerating to 22mph."
                    pause
                    "You die at the hands of its toothy maw." # add fancier language
                    pause
                    "Well done, you were eaten."
                    pause
                    return
                "Fight":
                    if burned == True:
                        "Angered by the death of its mate, it charges towards you."
                        pause
                        "You ready your pole, prepared for its attack."
                        pause
                        "But your injuries are too great, and you are too weak."
                        pause
                        "The dragonfish easily overpowers you. It bites into your neck, and you feel the life draining out of you."
                        pause
                        "Well done, you were tricked by the vents. Not all things that glitter are gold."
                        pause
                        return
                    else:
                        "As it draws closer, you spot a rusty metal pole laying next to some rocks."
                        pause
                        "In a split second decision, you firmly grab the pole (obviously with gloves on so there is no risk of tetanus) and swing it at the head of the barbeled dragonfish."
                        pause
                        "It stays there, dazed for a second, before trying to attack you."
                        pause
                        "Not wanting to die, you decide as a last ditch attempt to impale the dragonfish's skull."
                        pause
                        "You slowly retreat as blood leaks from its skull, contaminating the clear water."
                        pause
                        "You survived... barely."
                        pause
                        "Injured, you descend deeper."
                        $ location = "midnight"

            if location == "midnight":
                "You find yourself in the midnight zone."
                pause
                "You grab a torch, and looking out across the landscape, you see a series of hydrothermal vents."
                pause
                "It's dark out here. You feel the darkness closing in around you. But you're in too deep now. There's no way home."
                pause
                "If you ride the water of the vents, you could potentially reach the surface."
                pause
                menu:
                    "Ride the vents":
                        "As you drift close, dazed, you feel a growing warmth around your body."
                        menu:
                            "Go back":
                                "You ignore it, your mind still thinking about what you could have done."
                                pause
                                "You take one last glance. Something in the back of your mind tells you that it could have been your passageway to freedom. You push the voice down."
                                pause
                                "You get the nagging feeling that you just missed the big picture."
                                pause
                                "And now you will die here."
                                $ location = "abyss"
                            "Swim towards the vents":
                                "Dazed by emotions, you swim towards what you consider to be your passage to freedom, your beacons of hope, your tunnel to the life that you never had!"
                                pause
                                d "finally..."
                                pause
                                "As you draw closer to the vents, you feel your body warming up. You have been cold for so long!"
                                pause
                                "You smile at the warmth that forms a blanket around you, sheltering you."
                                pause
                                "You rise on the plumes of superheated water. You reach your hand out, letting yourself be carried by its momentum."
                                pause
                                "..."
                                pause
                                d "no..."
                                pause
                                d "no, no, no, No, NO!!!"
                                pause
                                "Your body writhes in pain as burns cover your body, torturing you and stripping away all of your energy."
                                pause
                                $ burned = True
                                $ location = "sunlit" #might have to change this as you don't want the diver to be healed
                    "Continue":
                        "You ignore it, your mind still thinking about what you could have done."
                        pause
                        "You take one last glance. Something in the back of your mind tells you that it could have been your passageway to freedom. You push the voice down."
                        pause
                        "You get the nagging feeling that you just missed the big picture."
                        pause
                        "And now you will die here."
                        $ location = "abyss"
                        