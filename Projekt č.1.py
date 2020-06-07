ODDELOVAC = '================================================================'
print(ODDELOVAC)
print('Vitejte uživateli!')
ODDELOVAC = '================================================================'
print(ODDELOVAC)
databaze = {}
databaze['bob'] = None
databaze['ann'] = None
databaze['mike'] = None
databaze['liz'] = None

databaze['bob'] = '123'
databaze['ann'] = 'pass123'
databaze['mike'] = 'password123'
databaze['liz'] = 'pass123'

while True:
            name = input('Jaké je vaše jmeno:')
            password = input('Jaké je vaše heslo:')
            if databaze.get(name) == password:
                print('Vítejte.')
                break
            else:
                print('Užovatelské jméno nebo heslo je špatně')

ODDELOVAC = '================================================================'
print(ODDELOVAC)

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

part_1 = TEXTS[0]
part_2 = TEXTS[1]
part_3 = TEXTS[2]

print('Níže vyber část textu, kterou budeš chtít zpracovat:')
print(ODDELOVAC)
print(part_1)
print(ODDELOVAC)
print(part_2)
print(ODDELOVAC)
print(part_3)
print(ODDELOVAC)

tvoje_část_textu = int(input('Zadej číslo textu, které budeš chtít zpracovat: '))
print(ODDELOVAC)

text = TEXTS[tvoje_část_textu-1]

dirty_words = text.split()

words = []

while dirty_words:
    word = dirty_words.pop()
    word = word.strip('.,:/;')
    if word: words.append(word)


print('Zde je  ' + str(len(words)) + ' slov z vybraného textu.')
titlecase = 0
lowercase = 0
uppercase = 0
numeric   = 0
counts    = {}
num_sum   = 0
i = 0
while i < len(words):
    if words[i].istitle():
        titlecase = titlecase + 1
    elif words[i].isupper():
        uppercase = uppercase + 1
    elif words[i].islower():
        lowercase = lowercase + 1
    elif words[i].isnumeric():
        numeric = numeric + 1
        num_sum = num_sum + float(words[i])
    l = len(words[i])
    counts[l] = counts.get(l,0) + 1
    i = i + 1
print('There are ' + str(titlecase) + ' titlecase words')
print('There are ' + str(uppercase) + ' uppercase words')
print('There are ' + str(lowercase) + ' lowercase words')
print('There are ' + str(numeric) + ' numeric strings')
print('-' * 40)
# 6. Program zobrazí jednoduchý sloupcový graf, který bude reprezentovat četnost různých délek slov v textu. Například takto:

lengths = sorted(counts)
i= 0
while i < len(lengths):
    length = lengths[i]
    frequency = counts[length]
    if len(str(length)) == 1:
        str_len = ' ' + str(length)
    else:
        str_len = str(length)
    print(str_len, '*' * frequency, frequency)
    i = i + 1
# 7. Spočítá součet všech čísel (ne cifer!) v textu. Výsledkem tohoto součtu v následujícím textu by teby bylo číslo 8500:

print(ODDELOVAC)
print('Součet všech čísel je: ' + str(num_sum))
print(ODDELOVAC)

















