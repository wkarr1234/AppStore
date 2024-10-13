
import random

def speel_nummerspel():
    geheim_nummer = random.randint(1, 100)  # Kies een getal tussen 1 en 100
    aantal_pogingen = int(input("Hoeveel keer wil je raden? "))

    for poging in range(aantal_pogingen):
        gok = int(input("Raad een nummer tussen 1 en 100: "))

        if gok < geheim_nummer:
            print("Te laag!")
        elif gok > geheim_nummer:
            print("Te hoog!")
        else:
            print("Gefeliciteerd! Je hebt het juiste nummer geraden.")
            break
    else:
        print(f"Helaas, het juiste nummer was {geheim_nummer}.")

# Verwijder of commentaar deze regel uit om automatisch starten te voorkomen
# if __name__ == "__main__":
#     speel_nummerspel()







