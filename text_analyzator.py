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


# vytvorenie uzivatelov a overenie pristupovych udajov

uzivatelia = {}
oddelovac = '=' * 40
mena_uzivatelov = 'bob', 'ann', 'mike', 'liz'
uzivatelia = uzivatelia.fromkeys(mena_uzivatelov)

uzivatelia['bob'] = '123'
uzivatelia['ann'] = 'pass123'
uzivatelia['mike'] = 'password123'
uzivatelia['liz'] = 'pass123'

print('Ahoj. Vítaj v aplikácii. Prihlás sa. ')

username = input('Uživatelské meno: ')
password = input('Heslo: ')

if uzivatelia.get(username) == password:
    print('Si prihlásený!')
    print(oddelovac)

else:
    print('Pokračuješ ako neregistrovaný užívateľ!')
    print(oddelovac)




# vyber konkrétneho textu a tlač analyzovaného textu

vyber = int(input('K dispozícii máme 3 texty, ktorú máme zanalyzovať? '))
print(oddelovac)

vybrany_text = TEXTS[vyber - 1]
print('Analyzujeme text:') 
print(vybrany_text)
print(oddelovac)


text_cistenie = vybrany_text.strip(' ., ')
text = text_cistenie.split()



# analýza slov

pocet_slov = len(text)


titlecase = 0
uppercase = 0
lowercase = 0
numeric = 0
suma = 0

while text:
    slovo = text.pop()
    if slovo.istitle():
        titlecase = titlecase + 1
    elif slovo.isupper():
        uppercase = uppercase + 1
    elif slovo.islower():
        lowercase = lowercase + 1
    elif slovo.isnumeric():
        numeric = numeric + 1
        suma = suma + int(slovo)
            

print(f"Vo vybranom texte je: {pocet_slov} slov.")
print(f"Vo vybranom texte je: {titlecase} slov s veľkým začiatočným písmenom.")
print(f"Vo vybranom texte je: {uppercase} slov s veľkým písmom.")
print(f"Vo vybranom texte je: {lowercase} slov s malým písmom.")
print(f"Vo vybranom texte je: {numeric} čísiel.")
print(oddelovac)
print(f"Suma všetkých čísiel v texte je: {suma} ")
print(oddelovac)



# druha faza zadania

vyb_text_dva = TEXTS[vyber - 1]
text_cistenie_dva = vyb_text_dva.strip(' ., ')
text_druha_faza = text_cistenie_dva.split()


pocty = {}
pocty_tu = dict.items(pocty)

for dlzka in text_druha_faza:
    pocet = len(dlzka)
    pocty[pocet] = pocty.get(pocet, 0) + 1
   

for i, j in pocty_tu:
    print(j, '*' * int(i), i)

