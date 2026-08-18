# Nakatagalog po ang ibang statements kasi Buwan ng Wika ngayon :)
zodiacSigns = [
    {
        "name": "Rat (鼠 / Shǔ)",
        "color": "Blue, gold, and green",
        "flower": "Lily and African violet"
    },
    {
        "name": "Ox (牛 / Niú)",
        "color": "White, yellow, and green",
        "flower": "Lily and carnation"
    },
    {
        "name": "Tiger (虎 / Hǔ)",
        "color": "Blue, gray, and orange",
        "flower": "Cineraria and rose"
    },
    {
        "name": "Rabbit (兔 / Tù)",
        "color": "Red, pink, and purple",
        "flower": "Jasmine and lily"
    },
    {
        "name": "Dragon (龙 / Lóng)",
        "color": "Gold, silver, and gray",
        "flower": "Bleeding heart and delphinium"
    },
    {
        "name": "Snake (蛇 / Shé)",
        "color": "Black, red, and yellow",
        "flower": "Orchid and sunflower"
    },
    {
        "name": "Horse (马 / Mǎ)",
        "color": "Yellow, brown, and purple",
        "flower": "Carnation and geranium"
    },
    {
        "name": "Goat (羊 / Yáng)",
        "color": "Green, red, and purple",
        "flower": "Carnation and rose"
    },
    {
        "name": "Monkey (猴 / Hóu)",
        "color": "White, blue, and gold",
        "flower": "Chrysanthemum and allium"
    },
    {
        "name": "Rooster (鸡 / Jī)",
        "color": "Gold, brown, and yellow",
        "flower": "Gladiolus and cockscomb"
    },
    {
        "name": "Dog (狗 / Gǒu)",
        "color": "Red, green, and purple",
        "flower": "Rose and carnation"
    },
    {
        "name": "Pig (猪 / Zhū)",
        "color": "Yellow, gray, and brown",
        "flower": "Hydrangea and lily"
    }
]
sagot = "oo"
while sagot == "oo":

    year = int(input("Ilagay ang iyong taon ng kapanganakan: "))

    if year < 1900:
        print("\nHindi wastong taon. Dapat ay 1900 o mas bago.\n")
        sagot = input("Gusto mo bang subukan muli? (oo/hindi): ")
        if sagot.lower() == "oo":
                continue
        else:
                 break
      

    # Kinukuha ang zodiac sign gamit ang 12-year cycle
    sign = (year - 1900) % 12
    zodiac = zodiacSigns[sign]

    print("\nYour Chinese zodiac sign is:", zodiac["name"])
    print("Lucky Colors:", zodiac["color"])
    print("Lucky Flowers:", zodiac["flower"])
    print()

    sagot = input("Gusto mo bang subukan muli? (oo/hindi): ")
    if sagot.lower() == "oo":
        continue
    else:
        break
    
print("Maraming salamat sa paggamit ng programa!!")