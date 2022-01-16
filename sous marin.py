if __name__ == '__main__':
    f = open("day 2.txt", "r")

    data = f.read().split('\n')
    dataInt = []

    for l in data:
        line = l.split(" ")
        tabline = [line[0], int(line[1])]
        dataInt.append(tabline)

    print(data)
    print(dataInt)
# avance = position horizontale

    profondeur = 0
    avance = 0
    aim = 0

    # Partie 1
   # for i in dataInt:
   #     if i[0] == "forward":
   #         avance = avance + i[1]
   #     if i[0] == "down":
   #         profondeur = profondeur + i[1]
   #     if i[0] == "up":
   #         profondeur = profondeur - i[1]

    #resultat_1 = avance * profondeur

    #print(resultat_1)

##Partie 2, multiplier position horizontal finale par profondeur finale
    #On met 1 entre crochet pour les calculs car cela correspond à la valeur, i[0] correspond au mouvement.

    for i in dataInt:
        if i [0] == "down":
            aim = aim + i[1]
        if i [0] == "up":
            aim = aim - i[1]
        if i [0] == "forward":
            avance = avance + i[1]
            profondeur = profondeur + aim * i[1]

        resultat_2 = avance * profondeur

    print(resultat_2)



