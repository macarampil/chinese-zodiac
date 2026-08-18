#nakatagalog po ang ibang statements po kasi buwan ng wika ngayon :)
def chinese_zodiacs():
    basta = "oo" 
    while basta == "oo":
        year = int(input("Ilagay ang iyong taon ng kapanganakan: "))
        if year < 1900:
            print("\nHindi wastong taon, dapat ay mas maaga sa 1900\n")
        elif year % 12 == 0:
            print("\nYour Chinese zodiac sign is Monkey")
            print("Lucky Colors: White, blue, and gold.") 
            print("Lucky Flowers: Chrysanthemum and allium.\n")
        elif year % 12 == 1:
            print("\nYour Chinese zodiac sign is Rooster")
            print("Lucky Colors: Gold, brown, and yellow.") 
            print("Lucky Flowers: Gladiolus and cockscomb.\n")  
        elif year % 12 == 2:
            print("\nYour Chinese zodiac sign is Dog")
            print("Lucky Colors: Red, green, and purple.") 
            print("Lucky Flowers: Rose and carnation.\n")
        elif year % 12 == 3:
            print("\nYour Chinese zodiac sign is Pig")
            print("Lucky Colors: Yellow, gray, and brown.") 
            print("Lucky Flowers: Hydrangea and lily.\n")   
        elif year % 12 == 4:
            print("\nYour Chinese zodiac sign is Rat")
            print("Lucky Colors: Blue, gold, and green.") 
            print("Lucky Flowers: Lily and African violet.\n")
        elif year % 12 == 5:
            print("\nYour Chinese zodiac sign is Ox")
            print("Lucky Colors: White, yellow, and green.") 
            print("Lucky Flowers: Lily and carnation.\n")
        elif year % 12 == 6:
            print("\nYour Chinese zodiac sign is Tiger")
            print("Lucky Colors: Blue, gray, and orange.") 
            print("Lucky Flowers: Cineraria and rose.\n")
        elif year % 12 == 7:
            print("\nYour Chinese zodiac sign is Rabbit")
            print("Lucky Colors: Red, pink, and purple.") 
            print("Lucky Flowers: Jasmine and lily.\n")
        elif year % 12 == 8:
            print("\nYour Chinese zodiac sign is Dragon")
            print("Lucky Colors: Gold, silver, and gray.") 
            print("Lucky Flowers: Bleeding heart and delphinium.\n")
        elif year % 12 == 9:
            print("\nYour Chinese zodiac sign is Snake")
            print("Lucky Colors: Black, red, and yellow.") 
            print("Lucky Flowers: Orchid and sunflower.\n")
        elif year % 12 == 10:
            print("\nYour Chinese zodiac sign is Horse")
            print("Lucky Colors: Yellow, brown, and purple.") 
            print("Lucky Flowers: Carnation and geranium.\n")
        elif year % 12 == 11:
            print("\nYour Chinese zodiac sign is Sheep")
            print("Lucky Colors: Green, red, and purple.") 
            print("Lucky Flowers: Carnation and rose.\n")
        basta = input("Gusto mo bang subukan muli? (oo/hindi): ")
        if basta == "oo":
           continue
        else:
            print("Maraming salamat sa paggamit ng programa!!")
            break

chinese_zodiacs()