import random
import json
from datetime import datetime



def kies_woord(moeilijkheidsgraad):

    with open("woorden.txt", "r") as bestand:
        woorden = bestand.read().splitlines()


    if moeilijkheidsgraad == 'makkelijk':
        woorden = [woord for woord in woorden if len(woord) <= 5]
    elif moeilijkheidsgraad == 'gemiddeld':
        woorden = [woord for woord in woorden if 6 <= len(woord) <= 8]
    else:
        woorden = [woord for woord in woorden if len(woord) > 8]

    return random.choice(woorden)



def speel_galgje():
    naam = input("Wat is je naam? ")
    moeilijkheidsgraad = input("Kies een moeilijkheidsgraad (makkelijk, gemiddeld, moeilijk): ").lower()
    woord = kies_woord(moeilijkheidsgraad)


    if moeilijkheidsgraad == 'makkelijk':
        aantal_pogingen = 6  # Makkelijk: 6 kansen
    elif moeilijkheidsgraad == 'gemiddeld':
        aantal_pogingen = 10  # Gemiddeld: 10 kansen
    else:
        aantal_pogingen = 20  # Moeilijk: 20 kansen

    geraden_letters = []
    foutieve_gokken = []

    print(f"Welkom {naam}! Je hebt {aantal_pogingen} pogingen om het woord te raden.")


    while aantal_pogingen > 0:

        weergave_woord = ''.join([letter if letter in geraden_letters else '_' for letter in woord])
        print(f"Status van het woord: {weergave_woord}")


        gok = input("Raad een letter: ").lower()

        if gok in geraden_letters or gok in foutieve_gokken:
            print("Je hebt deze letter al geraden, probeer een andere.")
            continue

        if gok in woord:
            print(f"Goed zo! De letter {gok} zit in het woord.")
            geraden_letters.append(gok)
        else:
            print(f"Helaas! De letter {gok} zit niet in het woord.")
            foutieve_gokken.append(gok)
            aantal_pogingen -= 1


        if all(letter in geraden_letters for letter in woord):
            print(f"Gefeliciteerd {naam}, je hebt het woord {woord} geraden!")
            sla_score_op(naam, woord, True, 6 - aantal_pogingen)
            break

        print(f"Je hebt nog {aantal_pogingen} pogingen over.")


    if aantal_pogingen == 0:
        print(f"Helaas, je hebt geen pogingen meer. Het woord was {woord}.")
        sla_score_op(naam, woord, False, 6)



def sla_score_op(naam, woord, geraden, pogingen):
    score = {
        "naam": naam,
        "woord": woord,
        "geraden": geraden,
        "pogingen": pogingen,
        "datum": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    }

    try:
        with open("score.json", "r") as bestand:
            scores = json.load(bestand)
    except FileNotFoundError:
        scores = []

    scores.append(score)

    with open("score.json", "w") as bestand:
        json.dump(scores, bestand, indent=4)
    print("Score is opgeslagen!")


# Start het spel
if __name__ == "__main__":
    speel_galgje()


