fish = input("FISH kiriting: ") 
parts = fish.split()  

familiya = parts[0]
ism_sharif = ' '.join(parts[1:])

natija = f"{ism_sharif}, {familiya}"
print(natija)
