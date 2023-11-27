#Choose your own adventure game. Pick a path and see where it leads!

name = input("Type your name: ")
print("Welcome", name, "to this adventure!")

answer = input("You are walking your dog in the forest and are lost. You can choose to go right or left. Which way would you like to go? (left or right) ").lower()

#swamp path
if answer == "left":
    answer = input("You have reached a swamp. You can either walk around the swamp, which makes your journey longer, or you can walk through the unknown terrain. Which do you choose? (around or through) ").lower()
    
    if answer == "through":
        answer = input("A bunch of critters that resemble leaches have attached to your legs and arms. You start to feel feint. Do you try to rip them off or ignore them and keep walking until you can find another solution? (rip or walk) ").lower()
        
        if answer == "rip":
             print("The critters release some sort of toxic compound into your blood stream as they're being ripped off. You die and lose. ")
        
        elif answer == "walk":
                answer = input("You run into a tribe that appears to have been living here for a while. You can either ask them for help with your critter problem or you can keep quiet and run away. Which do you do? (run or help) ").lower()
               
                if answer == "run":
                     print("The tribe sees this as a signal of aggression. They attack and kill you. You lose.")
                
                elif answer == "help":
                     print("The tribe helps remove the critters from your body and escort you out of the forest. Congratulations, you win!" )
                
                else:
                     print("That isn't an option. As you stand around thinking about the right choice, you pass out and die. You lose.")

        else:
             print("That isn't an option. As you stand around thinking about the right choice, you pass out and die. You lose.")
        
    
    elif answer == "around":
            answer = input("You find evidence of a tribe that must be living in the forest. You can either go back to try to find the tribe, or keep walking towards the exit sign. Which do you choose? (back or exit) ").lower()
            
            if answer == "exit":
                 print("Congratulations, you successfully found your way out of the forest and your curiosity didn't kill you. You win.")
            
            elif answer == "back":
                    answer = input("You find the villagers of the tribe. You can either introduce yourself and say hi, or keep walking towards the exit sign. Which do you choose? (hello or exit) ").lower()
            
                    if answer == "exit":
                        print("The villagers got offended that you didn't say hi so they killed you. You lose.")
            
                    elif answer == "hello":
                        print("The villagers are very nice, show you a great time, and eventually help you get home with a gift. Congratulations you win!")
                            
                    else:
                        print("That's not a valid option. The villagers get upset and attack you. You lose.")

            else:
                 print("That's not a valid option. You get attacked by a pack of wolves and get eaten alive. You lose.")

    else: 
        print("That's not a valid option. You get attacked by a bunch of pythons and eaten alive. You lose.")

#bridge path
elif answer == "right":
    answer = input("You have reached an unstable looking bridge. You can either walk around the bridge, which makes your journey longer, or you can walk across the unstable looking bridge. Which do you choose? (around or across) ").lower()
    
    if answer == "across":
        print("The unstable looking bridge was actually unstable, who would have guessed. The bridge collapses and you fall to your death. You lose")
    
    elif answer == "around":
            answer = input("You find evidence of a tribe that must be living in the forest. You can either go back to try to find the tribe, or keep walking towards the exit sign. Which do you choose? (back or exit) ").lower()
            
            if answer == "exit":
                 print("Congratulations, you successfully found your way out of the forest and your curiosity didn't kill you. You win.")
            
            elif answer == "back":
                    answer = input("You have reached a swamp. You can either walk around the swamp, which makes your journey longer, or you can walk through the unknown terrain. Which do you choose? (around or through) ").lower()

                    if answer == "through":
                        answer = input("A bunch of critters that resemble leaches have attached to your legs and arms. You start to feel feint. Do you try to rip them off or ignore them and keep walking until you can find another solution? (rip or walk) ").lower()
        
                        if answer == "rip":
                            print("The critters release some sort of toxic compound into your blood stream as they're being ripped off. You die and lose. ")
                        
                        elif answer == "walk":
                                answer = input("You run into a tribe that appears to have been living here for a while. You can either ask them for help with your critter problem or you can keep quiet and run away. Which do you do? (run or help) ").lower()
               
                                if answer == "run":
                                    print("The tribe sees this as a signal of aggression. They attack and kill you. You lose.")
                
                                elif answer == "help":
                                    print("The tribe helps remove the critters from your body and escort you out of the forest. Congratulations, you win!" )
                
                                else:
                                    print("That isn't an option. As you stand around thinking about the right choice, you pass out and die. You lose.")

                        else:
                             print("That's not an option. As you stand around making a decision, the critters drain your blood and kill you. You lose.")

                    elif answer == "around":
                            answer = input("You find the villagers of the tribe. You can either introduce yourself and say hi, or keep walking towards the exit sign. Which do you choose? (hello or exit) ").lower()
            
                            if answer == "exit":
                                print("Congratulations, you successfully found your way out of the forest and your curiosity didn't kill you. You win.")
            
                            elif answer == "hello":
                                print("The villagers are very nice, show you a great time, and eventually help you get home with a gift. Congratulations you win!")
                            
                            else:
                                 print("That's not a valid option. The villagers get upset and attack you. You lose.")
            else:
                 print("That's not a valid option. You get attacked by a pack of wolves and get eaten alive. You lose.")
                    
    else:
        print("That isn't an option. As you stand around thinking about the right choice, you pass out and die. You lose.")
        

else:
    print("That is not a valid path. A bear has come out of the bushes to eat you! You lose.")
