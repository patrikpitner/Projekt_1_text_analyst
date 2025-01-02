"""
projekt_1.py: první projekt do Engeto Online Python Akademie

author: Patrik Pitner
email: patrikpitner@seznam.cz
"""

#texty

TEXTS = ['''
Situated about 10 miles west of Kemmerer,
Fossil Butte is a ruggedly impressive
topographic feature that rises sharply
some 1000 feet above Twin Creek Valley
to an elevation of more than 7500 feet
above sea level. The butte is located just
north of US 30N and the Union Pacific Railroad,
which traverse the valley. ''',
'''At the base of Fossil Butte are the bright
red, purple, yellow and gray beds of the Wasatch
Formation. Eroded portions of these horizontal
beds slope gradually upward from the valley floor
and steepen abruptly. Overlying them and extending
to the top of the butte are the much steeper
buff-to-white beds of the Green River Formation,
which are about 300 feet thick.''',
'''The monument contains 8198 acres and protects
a portion of the largest deposit of freshwater fish
fossils in the world. The richest fossil fish deposits
are found in multiple limestone layers, which lie some
100 feet below the top of the butte. The fossils
represent several varieties of perch, as well as
other freshwater genera and herring similar to those
in modern oceans. Other fish such as paddlefish,
garpike and stingray are also present.'''
]

#tabulka - uživatel a heslo

uzivatel={
    "bob" : "123",
    "ann" : "pass123",
    "mike" : "password123",
    "liz" : "pass123",
}

#zadani jmena a hesla

jmeno = input("username:")
heslo = input("password:")
print(40 * "-")

#podminka na uzivatele a heslo

if jmeno in uzivatel and uzivatel[jmeno] == heslo:
    print("Welcome to the app", jmeno +".")
else:
    print("Unregistered user, terminating the program.")
    raise Exception("The program has ended.")

#vyber textu

print("We have 3 texts to be analyzed.")
print(40 * "-")
vyber = int(input("Enter a number btw. 1 and 3 to select:"))
print(40 * "-")
if vyber < 1 or vyber > len(TEXTS):
    print("Wrong number, terminating the program.")
    raise Exception("The program has ended.") 
#počet slov

vyber_textu = TEXTS[vyber-1]
interpunkce = ".,!?;:'\"()[]{}<>_=-+*/\\|^&$#@~`"
vyber_textu = vyber_textu.strip()
slova = vyber_textu.split()
ocistena_slova = []
for slovo in slova:
    ciste_slovo = slovo.strip(interpunkce)
    if ciste_slovo.isalpha():
        ocistena_slova.append(ciste_slovo)
pocet_slov = len(ocistena_slova)
print("There are", pocet_slov, "words in the selected text.")

#počet slov začínajících velkým písmenem

slova_velka_pismena = []
for slovo in slova:
    if slovo.istitle():
        slova_velka_pismena.append(slovo)
pocet_slov_velke_pismeno = len(slova_velka_pismena)
print("There are", pocet_slov_velke_pismeno, "titlecase words.")

#počet slov napsaných velkými písmeny

slova_velkymi_pismeny = []
for slovo in slova:
    if slovo.isupper():
        slova_velkymi_pismeny.append(slovo)
pocet_slov_velkymi_pismeny = len(slova_velkymi_pismeny)
print("There are", pocet_slov_velkymi_pismeny, "uppercase words.")

#počet slov psaných malými písmeny

slova_mala_pismena = []
for slovo in slova:
    if slovo.islower():
        slova_mala_pismena.append(slovo)
pocet_slov_male_pismeno = len(slova_mala_pismena)
print("There are", pocet_slov_male_pismeno, "lowercase words.")

#počet číslic

cisla = []
for cislo in slova:
    if cislo.isnumeric():
        cisla.append(cislo)
pocet_cisel= len(cisla)
print("There are", pocet_cisel, "numeric strings.")

#suma všech čísel

cisla_float = []
for cislo in cisla:
    cisla_float.append(float(cislo))
suma_cisel = sum(cisla_float)
print("The sum of all the numbers:", suma_cisel)
print(40 * "-")

# graf
delky_slov = {}
for slovo in slova:
    slovo = slovo.strip(interpunkce)
    delka = len(slovo) 
    if delka in delky_slov:
        delky_slov[delka] += 1
    else:
        delky_slov[delka] = 1
print("LEN|  OCCURENCES  |NR.")
print("----------------------------------------")
for delka, pocet in sorted(delky_slov.items()):
    print(f"{delka:3}| {'*' * pocet:<12} |{pocet}")