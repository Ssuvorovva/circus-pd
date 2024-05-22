# Specifikācija
# - 1pt Spelētāji sāk no lauciņa nr. 1, vispār 100 lauciņu. Ir divi spēlētāji. Vinē tas kurš pirmais sasniedz pēdējo lauciņu
# - 1pt Maksimāli - 30 raundi, ja beidzas raundi - neizšķirts
# - 1pt Viens pēc otra met kauliņu (ar nejauša ciparu ģenerātora palidzību) un iet uz priekšu
# - 1pt Ja trāpa uz lauciņu ar kāpnem:
# -- zilas kāpnes ved uz leju, 16 -> 5, 65 -> 44 , 78 -> 67, 72 -> 61
# -- sarkanas kāpnes ved uz augšu, 13 -> 22, 37 -> 46, 31 -> 50, 85 -> 94 
# - 1pt Katrā raundā tik drukāta informācija kur atrodas spēlētājs, dators un vai ir uzkāpts uz kāpnem

# Koda vertēšanas kritēriji
# - 1pt Kodā izmanto mainīgus, ciklus (for vai while), zarošanu (if)
# - 1pt Kods strādā bez kļūdam
# - 1pt Mainīgo un funkciju nosaukumi atspoguļo izmantošanas būtību, bez saisinājumiem, rakstīti snake_case stilā
# - 1pt Kodam ir jēdzīgi komentāri, pirms "if, for" koda konstrukcijam
# - 1pt Izmaiņas saglabātas versiju vadības sistēmā Git

# Dokumentācija
# Mainīgie - https://www.w3schools.com/python/python_variables.asp
# Operācijas ar mainīgiem - https://www.w3schools.com/python/python_operators.asp
# Mainīgo drukāšana - https://www.w3schools.com/python/python_variables_output.asp
# Nosacījumi, zarošana, if ... else - https://www.w3schools.com/python/python_conditions.asp
# For cikls - https://www.w3schools.com/python/python_for_loops.asp
# Nejauša skaitļa generēšana - https://www.w3schools.com/python/ref_random_randint.asp
# Github Fork (repozitorija kopija) - https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/working-with-forks/fork-a-repo
# Klonēt repozitoriju - hhttps://code.visualstudio.com/docs/sourcecontrol/intro-to-git

import random 

# Sākuma pozīcijas spēlētājiem
player1 = 1
player2 = 1

# Kāpņu definīcijas
blue = {16: 5, 65: 44, 78: 67, 72: 61}
red = {13: 22, 37: 46, 31: 50, 85: 94}

# Maksimālais raundu skaits
max_rounds = 30

# Funkcija kāpņu pārbaudei
def check_ladders(position):
    if position in blue:
        print(f"Player hits a blue ladder at {position}, moves to {blue[position]}")
        return blue[position]

    elif position in red:
        print(f"Player hits a red ladder at {position}, moves to {red[position]}")
        return red[position]

    else:
        return position

# Galvenais spēles cikls
for round in range(1, max_rounds + 1):
    print(f"\nRound {round}")
    
    # Spēlētāja 1 gājiens
    dice = random.randint(1, 6)
    player1 += dice
    print(f"Player 1 rolls a {dice} and moves to {player1}")
    player1 = check_ladders(player1)
    print(f"Player 1 is now on {player1}")
    
    # Pārbauda vai spēlētājs 1 ir uzvarējis
    if player1 >= 100:
        print("Player 1 wins!")
        break
    
    # Spēlētāja 2 gājiens
    dice = random.randint(1, 6)
    player2 += dice
    print(f"Player 2 rolls a {dice} and moves to {player2}")
    player2 = check_ladders(player2)
    print(f"Player 2 is now on {player2}")
    
    # Pārbauda vai spēlētājs 2 ir uzvarējis
    if player2 >= 100:
        print("Player 2 wins!")
        break
else:
    print("Draw!")

