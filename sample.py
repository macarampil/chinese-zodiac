def chinese_zodiacs():
    basta = "oo" 
    while basta == "oo":
        year = int(input("Enter your birth year: "))
        if year > 1900:
            print("invalid year, must be earlier than 1900")
        elif year % 12 == 0:
            print("Your Chinese zodiac sign is Monkey")
            print("Lucky Colors: White, blue, and gold.") 
            print("Lucky Flowers: Chrysanthemum and allium.")
        elif year % 12 == 1:
            print("Your Chinese zodiac sign is Rooster")
            print("Lucky Colors: Gold, brown, and yellow.") 
            print("Lucky Flowers: Gladiolus and cockscomb.")  
        elif year % 12 == 2:
            print("Your Chinese zodiac sign is Dog")
            print("Lucky Colors: Red, green, and purple.") 
            print("Lucky Flowers: Rose and carnation.")
        elif year % 12 == 3:
            print("Your Chinese zodiac sign is Pig")
            print("Lucky Colors: Yellow, gray, and brown.") 
            print("Lucky Flowers: Hydrangea and lily.")   
        elif year % 12 == 4:
            print("Your Chinese zodiac sign is Rat")
            print("Lucky Colors: Blue, gold, and green.") 
            print("Lucky Flowers: Lily and African violet.")
        elif year % 12 == 5:
            print("Your Chinese zodiac sign is Ox")
            print("Lucky Colors: White, yellow, and green.") 
            print("Lucky Flowers: Lily and carnation.")
        elif year % 12 == 6:
            print("Your Chinese zodiac sign is Tiger")
            print("Lucky Colors: Blue, gray, and orange.") 
            print("Lucky Flowers: Cineraria and rose.")
        elif year % 12 == 7:
            print("Your Chinese zodiac sign is Rabbit")
            print("Lucky Colors: Red, pink, and purple.") 
            print("Lucky Flowers: Jasmine and lily.")
        elif year % 12 == 8:
            print("Your Chinese zodiac sign is Dragon")
            print("Lucky Colors: Gold, silver, and gray.") 
            print("Lucky Flowers: Bleeding heart and delphinium.")
        elif year % 12 == 9:
            print("Your Chinese zodiac sign is Snake")
            print("Lucky Colors: Black, red, and yellow.") 
            print("Lucky Flowers: Orchid and sunflower.")
        elif year % 12 == 10:
            print("Your Chinese zodiac sign is Horse")
            print("Lucky Colors: Yellow, brown, and purple.") 
            print("Lucky Flowers: Carnation and geranium.")
        elif year % 12 == 11:
            print("Your Chinese zodiac sign is Sheep")
            print("Lucky Colors: Green, red, and purple.") 
            print("Lucky Flowers: Carnation and rose.")
        basta = input("Do you want to try again? (oo/hindi): ")
        if basta == "oo":
           continue
        else:
            print("Maraming salamat sa paggamit ng programa!!")
            break