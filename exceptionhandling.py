print("\nHit e to enter the game")
hit= input("\nHit e to go to space: ")
if hit=="e":
    print("\nSpaceship has started")
    while(True):
        landspaceship= input("\nHit s to land the spaceship or Hit c to continue: ")
        if(landspaceship=="s" or landspaceship==" s " or landspaceship==" s"):
           break
        elif(landspaceship=="c" or landspaceship== " c " or landspaceship==" c"):
         try: #executing try except block
           user_guess=int(input(("\nGuess the amount of fuel in litres: ")))
           guess=56
           if(user_guess==guess):
            print("\nSpaceship is hovering")
            break
         except Exception as e: #returns the Exception error as e
           print("\nThe error in your input is:",e)


        

