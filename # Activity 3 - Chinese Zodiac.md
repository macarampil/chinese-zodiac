# Activity 3 - Chinese Zodiac

## Description

This program determines the Chinese Zodiac sign based on the user's birth year.

## Requirements

- The baseline year is 1900.
- The birth year must not be earlier than 1900.
- The program uses a 12-year repeating zodiac cycle.
- Only the birth year is considered.

## Chinese Zodiac Signs

1. Rat (鼠 / Shǔ)
2. Ox (牛 / Niú)
3. Tiger (虎 / Hǔ)
4. Rabbit (兔 / Tù)
5. Dragon (龙 / Lóng)
6. Snake (蛇 / Shé)
7. Horse (马 / Mǎ)
8. Goat (羊 / Yáng)
9. Monkey (猴 / Hóu)
10. Rooster (鸡 / Jī)
11. Dog (狗 / Gǒu)
12. Pig (猪 / Zhū)

## Code

#nakatagalog po ang ibang statements po kasi buwan ng wika ngayon :)
def chinese_zodiacs():
    sagot = "oo" 
    while sagot == "oo":
        # Ito po ay humihingi ang taon ng kapanganakan ng user
        year = int(input("Ilagay ang iyong taon ng kapanganakan: "))
        # Tinutukoy ang Chinese zodiac sign gamit ang remainder ng taon kapag hinati sa 12
        if year < 1900:
            print("\nHindi wastong taon, dapat ay mas maaga sa 1900.\n")
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
        sagot = input("Gusto mo bang subukan muli? (oo/hindi): ")
        if sagot == "oo":
           continue
        else:
            print("Maraming salamat sa paggamit ng programa!!")
            break

chinese_zodiacs()


Screenshot of the program's output:
#kapag ang taon na inilagay ay mas maaga pa sa 1900
![alt text](<Screenshot 2026-08-18 105616-1.png>)
#kapag wasto ang taong inilagay
![alt text](<Screenshot 2026-08-18 105644.png>)
