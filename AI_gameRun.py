from AI_hand import *
from AI_code import *
amount = False

# Player count check
while amount != True:
    spelers_aantal = int(input(f"\nAantal spelers (2 t/m 10): "))
    if spelers_aantal < 2 or spelers_aantal > 10:
        amount = False
        print("kan maar met 2 t/m 10 mensen. kies opnieuw.")
    else:
        amount = True
speel_uno(spelers_aantal)