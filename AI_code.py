import random
import time
from AI_hand import *

# Deck maken
def maak_deck():
    deck = []
    kleuren = ["Rood", "Geel", "Groen", "Blauw"]

    for kleur in kleuren:
        deck.append((kleur, "0"))
        for i in range(1, 10):
            deck.extend([(kleur, str(i)), (kleur, str(i))])
        for actie in ["Skip", "Reverse", "+2"]:
            deck.extend([(kleur, actie), (kleur, actie)])

    for _ in range(4):
        deck.append(("Zwart", "Wild"))
        deck.append(("Zwart", "Wild +4"))

    return deck

# Trek kaarten
def trek(deck, aantal):
    kaarten = []
    for _ in range(aantal):
        if deck:
            kaarten.append(deck.pop())
    return kaarten

# Game
def speel_uno(spelers_aantal):
    spelers = [[] for _ in range(spelers_aantal)]

    deck = maak_deck()
    random.shuffle(deck)

    # Uitdelen
    for _ in range(7):
        for s in spelers:
            s.append(deck.pop())

    bovenste = deck.pop()
    huidige_kleur = bovenste[0] if bovenste[0] != "Zwart" else random.choice(["Rood","Geel","Groen","Blauw"])

    richting = 1
    speler_index = 0

    print(f"\nStartkaart: {bovenste}, kleur: {huidige_kleur}\n")

    while True:
        time.sleep(0.25)
        speler = spelers[speler_index]
        print(f"Speler {speler_index+1} ({len(speler)} kaarten)")

        kaart = kies_kaart(speler, bovenste, huidige_kleur)

        if kaart:
            speler.remove(kaart)
            bovenste = kaart

            if kaart[0] == "Zwart":
                huidige_kleur = kies_kleur(speler)
            else:
                huidige_kleur = kaart[0]

            print(f"Speelt: {kaart} -> kleur wordt {huidige_kleur}")

            # Pestkaarten
            if kaart[1] == "Skip":
                speler_index = (speler_index + richting) % spelers_aantal
                print("Volgende speler wordt overgeslagen!")

            elif kaart[1] == "Reverse":
                richting *= -1
                print("Richting omgedraaid!")

            elif kaart[1] == "+2":
                volgende = (speler_index + richting) % spelers_aantal
                spelers[volgende].extend(trek(deck, 2))
                speler_index = volgende
                print("Volgende speler trekt 2 kaarten!")

            elif kaart[1] == "Wild +4":
                volgende = (speler_index + richting) % spelers_aantal
                spelers[volgende].extend(trek(deck, 4))
                speler_index = volgende
                print("Volgende speler trekt 4 kaarten!")

        else:
            if deck:
                getrokken = deck.pop()
                speler.append(getrokken)
                print(f"Trekt: {getrokken}")
            else:
                print("Deck leeg!")
                deck = maak_deck()
                random.shuffle(deck)

        print(f"Bovenste kaart: {bovenste}, kleur: {huidige_kleur}\n")

        # Win check
        if len(speler) == 0:
            print(f"🎉 Speler {speler_index+1} wint!\n")
            break

        speler_index = (speler_index + richting) % spelers_aantal

    # Scores
    print("Scores:")
    scores = []
    for i, s in enumerate(spelers):
        sc = score_hand(s)
        scores.append(sc)
        print(f"Speler {i+1}: {sc}")

    if len(speler) == 0:
        print(f"\n🏆 Eindwinnaar: Speler {speler_index+1}")