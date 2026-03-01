
define d = Character("You", color="#64c5ee")
define e = Character("?", color="#b30000")
image bg surface = "images/bg surface.png"
image d main = "images/d main.png"

label start:

    "You begin your scuba diving tour. The hum of the boat overhead makes the water ripple. This is going to be a normal day."
    

    "...right?"

    d "This is fine.......but why does the boat sound quieter?"
    
    scene bg surface at truecenter with dissolve
    show boat main at truecenter with fade
    show d main_small at center 


    "When you surface, you can see the boat retreating into the distance."
    hide boat main with fade
    "You have been left behind."# Should you wait
    $ location = "surface"
    $ burned = False
    $ end = False
    while end == False:
        if location == "surface":
            "You are on the surface of the water."
            scene bg surface at truecenter with dissolve
            show d main_small at center 
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
                                    
                                    
                                    "Eventually the boat gets bored and picks you up."
                                     
                                    "I-I-I mean ... a rescue boat eventually comes to your rescue and takes you safely back home."
                                    
                                    "Well done, you survived. But that was so boring! You failed as a player! Try diving instead next time."
                                    
                                    $ end = True

        if location == 'sunlit':
            scene bg sunlit
            show d main at truecenter
            "You find yourself in the sunlit zone."
            
            "You contemplate your options."
            menu: 
                "Surface":
                    "You (not so calmly) resurface, for some reason."
                    $ location = "surface"
                "Backstroke":
                    "You try and use backstroke to escape."
                    
                    "But you don't realise that you are heading towards a series of sharp rocks."
                    
                    "You pierce your oxygen tank."
                    scene black
                    "Your chest feels tight as you reflect on your idiocy."
                    
                    "Well done, you drowned."
                    
                    $ end = True
                "Breaststroke":
                    "You try and use breaststroke to escape, swimming deeper towards the bottom of the vast ocean."
                    
                    "Somehow, through sheer dumb luck, you survive." 
                    
                    "You continue with your scuba dive, going deeper."
                    $ location = "twilight"

        if location == 'twilight':
            scene bg twilight
            show d main at truecenter
            "You find yourself in the twilight zone."
            
            "Everything seems to be going swimmingly until you see a faint glow in the distance with a small silhouette"
            
            #"As the glowing blob "
            "From your brief marine biology class, you know that this is a barbeled dragonfish." # add more info about fish
            show f main at right
            
            "You also know that it has seen you."
            menu:
                "Swim away":
                    "You try to swim away from the dragonfish, which is now accelerating to 22mph."
                    scene black
                    "You die at the hands of its toothy maw." # add fancier language
                    
                    "Well done, you were eaten."
                    
                    $ end = True
                "Fight":
                    if burned == True:
                        "Angered by the death of its mate, it charges towards you."
                        
                        "You ready your pole, prepared for its attack."
                        
                        "But your injuries are too great, and you are too weak."
                        
                        "The dragonfish easily overpowers you. It bites into your neck, and you feel the life draining out of you."
                        
                        "Well done, you were tricked by the vents. Not all things that glitter are gold."
                        
                        $ end = True
                    else:
                        "As it draws closer, you spot a rusty metal pole laying next to some rocks."
                        
                        "In a split second decision, you firmly grab the pole (obviously with gloves on so there is no risk of tetanus) and swing it at the head of the barbeled dragonfish."
                        
                        "It stays there, dazed for a second, before trying to attack you."
                        
                        "Not wanting to die, you decide as a last ditch attempt to impale the dragonfish's skull."
                        
                        hide f
                        "You slowly retreat as blood leaks from its skull, contaminating the clear water."
                        
                        "You survived... barely."
                        
                        "Injured, you descend deeper."
                        $ location = "midnight"

            if location == "midnight":
                "You find yourself in the midnight zone."
                scene bg vents
                
                "You grab a torch, and looking out across the landscape, you see a series of hydrothermal vents."
                
                "It's dark out here. You feel the darkness closing in around you. But you're in too deep now. There's no way home."
                
                "If you ride the water of the vents, you could potentially reach the surface."
                
                menu:
                    "Ride the vents":
                        "As you drift close, dazed, you feel a growing warmth around your body."
                        menu:
                            "Go back":
                                "You ignore it, your mind still thinking about what you could have done."
                                
                                "You take one last glance. Something in the back of your mind tells you that it could have been your passageway to freedom. You push the voice down."
                                
                                "You get the nagging feeling that you just missed the big picture."
                                
                                "And now you will die here."
                                $ location = "abyss"
                            "Swim towards the vents":
                                "Dazed by emotions, you swim towards what you consider to be your passage to freedom, your beacons of hope, your tunnel to the life that you never had!"
                                
                                d "finally..."
                                
                                "As you draw closer to the vents, you feel your body warming up. You have been cold for so long!"
                                
                                "You smile at the warmth that forms a blanket around you, sheltering you."
                                
                                "You rise on the plumes of superheated water. You reach your hand out, letting yourself be carried by its momentum."
                                
                                pause
                                
                                d "no..."
                                
                                d "no, no, no, No, NO!!!"
                                
                                "Your body writhes in pain as burns cover your body, torturing you and stripping away all of your energy."
                                
                                $ burned = True
                                $ location = "sunlit" #might have to change this as you don't want the diver to be healed
                    "Stay":
                        "You decide to take a rest."
                        
                        d "I'm... so tired..."
                        
                        d "..."
                        
                        "Unfortunately for you, hours pass."
                        
                        "You panic but look around, trying to keep yourself busy."
                        
                        d "Why is it getting hard to breathe?"
                        
                        "You look behind you at the pressure gauge for your oxygen tank."#oxygen is low
                        
                        "It is dangerously low."
                        
                        d "Oh no..."
                        
                        d "I need to get out of here!"
                        
                        "You desperately try to escape your death by grabbing hold of a sperm whale."
                        
                        "The water gets brighter as you and the sperm whale ascend from the midnight zone."
                        "\n\nYou feel hopeful but cautious as you watch your oxygen levels deplete further."
                        
                        d "Maybe, just maybe I can make it out alive."
                        
                        d "I am so close!"
                        
                        "You hear a rumbling..."
                        
                        "Confused, you look around, realising that you are in a cave."
                        ##rocks fall and block your exit (the whale escapes though, you just fall off (dies fron lack of oxygen)) # not finished
                    "Proceed":
                        "You ignore it, your mind still thinking about what you could have done."
                        
                        "You take one last glance. Something in the back of your mind tells you that it could have been your passageway to freedom. You push the voice down."
                        
                        "You get the nagging feeling that you just missed the big picture."
                        
                        "And now you will die here."
                        $ location = "abyss"

            if location == "abyss": # go over the ai sounding bit
                "You find yourself in the abyss."
                
                "You are in the deepest part of the ocean. The pressure is crushing; the darkness is suffocating."
                
                "You feel a trememdous loneliness as you contemplate your fate."
                
                "As your tired feet drag across the ocean floor, you notice a symbol carved into the rock."
                
                menu:
                    "Inspect":
                        show p main at left
                        "You realise that the symbol is a huge pentagram scrawled across the ocean floor. Tremors shake the ground. Your vision blurs."
                        
                        "You hear a voice calling out to you. It is a deep, guttural voice, that seems to be coming from the very depths of the earth."
                        
                        e "hear me..."
                        
                        e "free me..."
                        
                        e "join me..."
                        
                        menu:
                            "Touch the pentagram":
                                "You reach out and touch the pentagram. You feel a surge of energy coursing through your body."
                                
                            "Run away":
                                e "Do you think you can escape my power? Your mortal mind will break like a twig."
                                menu:
                                    "Touch the pentagram":
                                        "You reach out and touch the pentagram. You feel a surge of energy coursing through your body."
                                        
                        define e = Character("Entity", color="#b30000")
                        show bg cthulu
                        "Standing before you is a primordial cthonic monstrosity, an eldritch being of cosmic power and horror."
                        e "You have unbound me from my chains."
                        e "But to be my disciple, I demand a sacrifice of you."
                        menu:
                            "Sacrifice yourself":
                                "You feel your mortal essence being sapped away by the cosmic entity that stands before you."
                                e "Your soul will bring me power."
                                scene black
                                "For eternity you feel nothing but a profound loneliness."
                                "Well done, you sacrificed your soul to a demonic entity."
                                $ end = True
                            "Sacrifice the world":
                                "The being flicks a tentacle, and under your feet a gaping breach opens."
                                scene bg earth
                                show d main with fade
                                "From the moment you enter the breach, you begin falling."
                                
                                "And falling."
                                
                                "And falling."
                                
                                "You fall through the earth, with nothing to do, except wait for the quickly approaching core to burn you to a crisp."
                                
                                "It takes so long."
                                
                                "Well done, you fell through the earth and died."
                                
                                $ end = True
                            "Sacrifice the barbeled dragonfish":
                                e "A barbeled dragonfish? Sufficient."
                                scene black
                                "Even though you sacrifice the fish, you don't leave. You sleep."
                                "And the day you open your eyes again, you see the being, drinking tea with the fish."
                                e "More sugar?"
                                Character("Barbeled Dragonfish", color="#ffb700") "No thank you, it's sweet enough."
                                "Well done, you trapped yourself in the bottom of the ocean."
                                $ end = True

                    "Ignore":
                        "You ignore the cruel voice, and continue walking."
                        
                        "Anyway, staying focused has kept you alive so far."
                        
                        "You continue walking, until you reach a huge breach in the floor."
                        
                        menu:
                            "Enter":
                                "You feel a strange pull towards the breach. You are drawn to it, as if it is calling out to you."
                                
                            "Resist":
                                "You try to resist the pull, but it is too strong. You are drawn towards the breach, as if it is calling out to you."
                                
                        scene bg earth
                        show d main with fade
                        "From the moment you enter the breach, you begin falling."
                        
                        "And falling."
                        
                        "And falling."
                        
                        "You fall through the earth, with nothing to do, except wait for the quickly approaching core to burn you to a crisp."
                        
                        "It takes so long."
                        
                        "Well done, you fell through the earth and died."
                        
                        $ end = True
    return
