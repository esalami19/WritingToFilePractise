#open function you use to read and write
with open ("animals.txt","w") as animals_file:
    animals = "Giraffe \nElephant \nPenguin"

    animals_file.write(animals)

