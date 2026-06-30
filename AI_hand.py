import random
import time
from collections import Counter

# AI logica
def kies_kaart(hand, bovenste, huidige_kleur):
    speelbare = [k for k in hand if speelbaar(k, bovenste, huidige_kleur)]

    if not speelbare:
        return None

    # 1. Pestkaarten
    pest = ["+2", "Skip", "Reverse", "Wild +4"]
    for kaart in speelbare:
        if kaart[1] in pest:
            return kaart

    # 2. Hoogste nummer
    nummers = [k for k in speelbare if k[1].isdigit()]
    if nummers:
        return max(nummers, key=lambda x: int(x[1]))

    # 3. Meeste kleur
    kleuren = [k[0] for k in hand if k[0] != "Zwart"]
    if kleuren:
        meest = Counter(kleuren).most_common(1)[0][0]
        for k in speelbare:
            if k[0] == meest:
                return k

    return speelbare[0]

# Check speelbaar
def speelbaar(kaart, bovenste, huidige_kleur):
    kleur, waarde = kaart
    return (
        kleur == huidige_kleur or
        waarde == bovenste[1] or
        kleur == "Zwart"
    )

# Kleur keuze
def kies_kleur(hand):
    kleuren = [k[0] for k in hand if k[0] != "Zwart"]
    if not kleuren:
        return random.choice(["Rood", "Geel", "Groen", "Blauw"])
    return Counter(kleuren).most_common(1)[0][0]

# Eindscore
def score_hand(hand):
    score = 0
    for _, waarde in hand:
        if waarde.isdigit():
            score += int(waarde)
        elif waarde in ["Skip", "Reverse", "+2"]:
            score += 20
        else:
            score += 50
    return score
