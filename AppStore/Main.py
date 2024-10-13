from Galgje import speel_galgje
from Nummerspel import speel_nummerspel


def main_menu():
    while True:
        print("\nWelkom bij de SpelletjesParadijs!")
        print("1. Nummerspel")
        print("2. Galgje")
        print("3. Stoppen")

        keuze = input("Kies een spel (1-3): ")

        if keuze == '1':
            speel_nummerspel()
        elif keuze == '2':
            speel_galgje()
        elif keuze == '3':
            print("Bedankt voor het spelen!")
            break
        else:
            print("Ongeldige keuze, probeer opnieuw.")

if __name__ == "__main__":
    main_menu()


