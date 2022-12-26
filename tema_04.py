print('Exercitiu 1')
"""
# 1.Având lista:
# mașini = ['Audi', 'Volvo', 'BMW', 'Mercedes', 'Aston Martin', 'Lăstun',
# 'Fiat', 'Trabant', 'Opel']
# Folosește un for că să iterezi prin toată lista și să afișezi;
# ● ‘Mașina mea preferată este x’.
# ● Fă același lucru cu un for each.
# ● Fă același lucru cu un while.
# """
masini = ['Audi', 'Volvo', 'BMW', 'Mercedes', 'Aston Martin', 'Lăstun', 'Fiat', 'Trabant', 'Opel']
for x in range(len(masini)): # for
    x = masini[x]
    print(f"masina mea preferata este {x}")
print()
for masina in masini: # for each
    print(f"masina mea preferata este {masina}")
print()
x = 0
while x < len(masini): # atata timp cat x este mai mic decat lungimea listei
    masina = masini[x] # variabila masina ia valoarea fiecarui index x
    x += 1 # incrementam pe x pentru fiecare index din lista
    print(f"masina mea preferata este {masina}")

print()
print('Exercitiu 2')
"""
2. Aceeași listă:
Folosește un for else
În for
- Modifică elementele din listă astfel încât să fie scrie cu majuscule,
exceptând primul și ultimul.
În else:
- Printează lista.
"""
masini = ['Audi', 'Volvo', 'BMW', 'Mercedes', 'Aston Martin', 'Lăstun', 'Fiat', 'Trabant', 'Opel']
for i in range(1,len(masini)-1):
    masini[i] = masini[i].upper()
else:
    print(masini)
print()
print('Exercitiu 3')
"""
3.Aceeași listă:
Vine un cumpărător care dorește să cumpere un Mercedes.
Itereaza prin ea prin modalitatea aleasă de tine.
Dacă mașina e mercedes:
Printează ‘am găsit mașina dorită de dvs’
Ieși din ciclu folosind un cuvânt cheie care face acest lucru
Altfel:
Printează ‘Am găsit mașina X. Mai căutam‘
"""
masini = ['Audi', 'Volvo', 'BMW', 'Mercedes', 'Aston Martin', 'Lăstun', 'Fiat', 'Trabant', 'Opel']
for i in masini:
    if i == 'Mercedes':
        print(f'Am gasit masina dorita de dvs: {i}')
        break
    else:
        print(f"Am gasit masina {i}. Mai cautam")
print()
print('Exercitiu 4')
"""
4.Aceași listă;
Vine un cumpărător bogat dar indecis. Îi vom prezenta toate mașinile cu
excepția Trabant și Lăstun.
- Dacă mașina e Trabant sau Lăstun:
Folosește un cuvânt cheie care să dea skip la ce urmează (nu trebuie
else).
- Printează S-ar putea să vă placă mașina x.
"""
masini = ['Audi', 'Volvo', 'BMW', 'Mercedes', 'Aston Martin', 'Lastun', 'Fiat', 'Trabant', 'Opel']
for i in masini:
    if i == 'Trabant':
        continue
    if i == 'Lastun':
        continue
    print(f'S-ar putea sa va placa masina {i}.')
print()
print('Exercitiu 5')
"""
5. Modernizează parcul de mașini:
● Crează o listă goală, masini_vechi.
● Itereaza prin mașini.
● Când găsesti Lăstun sau Trabant:
- Salvează aceste mașini în masini_vechi.
- Suprascrie-le cu ‘Tesla’ (în lista inițială de mașini).
● Printează Modele vechi: x.
● Modele noi: x.
"""
masini = ['Audi', 'Volvo', 'BMW', 'Mercedes', 'Aston Martin', 'Lastun', 'Fiat', 'Trabant', 'Opel']
masini_vechi = []
for i in range(len(masini)):
    if masini[i] == 'Lastun' or masini[i]== 'Trabant':
        masini_vechi.append(masini[i])
        masini[i] = 'Tesla'
print(f"Modele vechi {masini_vechi}")
print(f"Modele noi {masini}")
print()
print('Exercitiu 6')
"""
6. Având dict:
pret_masini = {
'Dacia': 6800,
'Lăstun': 500,
'Opel': 1100,
'Audi': 19000,
'BMW': 23000
}
Vine un client cu un buget de 15000 euro.
● Prezintă doar mașinile care se încadrează în acest buget.
● Itereaza prin dict.items() și accesează mașina și prețul.
● Printează Pentru un buget de sub 15000 euro puteți alege mașină
xLastun
● Iterează prin listă.
"""
pret_masini = {
'Dacia': 6800,
'Lastun': 500,
'Opel': 1100,
'Audi': 19000,
'BMW': 23000
}
for k,v in pret_masini.items():
    if v < 15000 :
        print(f"Pentru bugetul dvs de sub 15000 euro puteti alege masina {k} cu pretul {v} euro.")
for k, v in pret_masini.items():
    print(f"In showroom avem masina {k} la pretul {v} euro.")
for k, v in pret_masini.items():
    if v < 15000 and k == 'Lastun':
        print(f"Pentru bugetul de sub 15000 de euro puteti alege masina {k} la pretul {v} euro.")
print()
print('Exercitiu 7')
"""
7. Având lista:
numere = numere = [5, 7, 3, 9, 3, 3, 1, 0, -4, 3]
● Iterează prin ea.
● Afișează de câte ori apare 3 (nu ai voie să folosești count).
"""
numere = [5, 7, 3, 9, 3, 3, 1, 0, -4, 3]
contor = 0
for i in numere:
    if i == 3:
        contor += 1
print(f"Cifra 3 apare de {contor} ori.")
print()
print('Exercitiu 8')
"""
8. Aceeași listă:
● Iterează prin ea
● Calculează și afișează suma numerelor (nu ai voie să folosești sum).
"""
numere = [5, 7, 3, 9, 3, 3, 1, 0, -4, 3]
suma = 0
for i in numere:
    suma += i
print(f"suma numerelor este: {suma}")
print()
print('Exercitiu 9')
"""
9. Aceeași listă:
● Iterează prin ea.
● Afișază cel mai mare număr (nu ai voie să folosești max).
"""
numere = [5, 7, 3, 9, 3, 3, 1, 0, -4, 3]
highest_value = 0
for i in range(len(numere)):
    if i > highest_value:
        highest_value = i
print(f"maximul din lista este {highest_value}")
print()
print('Exercitiu 10')
"""
10. Aceeași listă:
● Iterează prin ea.
● Dacă numărul e pozitiv, înlocuieste-l cu valoarea lui negativă.
Ex: dacă e 3, să devină -3
● Afișază noua listă.
"""
numere = [5, 7, 3, 9, 3, 3, 1, 0, -4, 3]
numere_negative = []
for i in range(len(numere)):
    if numere[i] > 0:
        numere_negative = -abs(numere[i]) # abs converteste numere pozitive in negative, -abs numere poz in negative
        print(numere_negative, end=" ")
print()
print('Exercitiu optional 1')
"""
1.
alte_numere = [-5, 7, 2, 9, 12, 3, 1, -6, -4, 3]
numere_pare = []
numere_impare = []
numere_pozitive = []
numere_negative = []
Itereaza prin listă alte_numere
Populează corect celelalte liste
Afișeaza cele 4 liste la final
"""
alte_numere = [-5, 7, 2, 9, 12, 3, 1, -6, -4, 3]
numere_pare = []
numere_impare = []
numere_pozitive = []
numere_negative = []
for numar in alte_numere:
    if numar % 2 == 0:
        numere_pare.append(numar)
    if numar % 2 != 0:
        numere_impare.append(numar)
    if numar > 0:
        numere_pozitive.append(numar)
    if numar < 0:
        numere_negative.append(numar)
print(f"numerele pare: {numere_pare}")
print(f"numerele impare: {numere_impare}")
print(f"numerele pozitive: {numere_pozitive}")
print(f"numerele negative: {numere_negative}")
print()
print('Exercitiu optional 2')
"""
2. Aceeași listă:
Ordonează crescător lista fară să folosești sort (Bubble sort)
"""
alte_numere = [-5, 7, 2, 9, 12, 3, 1, -6, -4, 3]
for i in range(len(alte_numere)):
    for j in range(0, len(alte_numere) - i -1):
        if alte_numere[j] > alte_numere[j + 1]:
            alte_numere[j], alte_numere[j + 1] = alte_numere[j + 1], alte_numere[j]
print('Lista sortata crescator prin Bubble sort:')
print(alte_numere)

print()
print('Exercitiu optional 3')
"""
3. Ghicitoare de număr:
numar_secret = Generați un număr random între 1 și 30
Numar_ghicit = None
Folosind un while
User alege un număr
Programul îi spune:
● Nr secret e mai mare
● Nr secret e mai mic
● Felicitări! Ai ghicit!
"""
import random
numar_secret = random.randint(1, 30)
while True:
    numar_ghicit = int(input('Guess the secret number (hint: between 1 and 30): '))
    if numar_ghicit < numar_secret:
        print('The secret number is higher!')
    elif numar_ghicit > numar_secret:
        print('The secret number is lower!')
    else:
        print('Congratulation! You guessed it!')
        break
print()
print('Exercitiu optional 4')
"""
4. Alege un număr de la tastatură
Ex: 7
Scrie un program care să genereze în consolă următoarea piramidă
1
22
333
4444
55555
666666
7777777
"""
numar = int(input('Pick a number: '))
for i in range(1, numar + 1):
    for j in range(i):
        print(i, end="")
    print()

print()
print('Exercitiu optional 5')
"""
5.tastatura_telefon = [
[1, 2, 3],
[4, 5, 6],
[7, 8, 9],
[0]
]
Iterează prin listă 2d
Printează ‘Cifra curentă este x’
"""
tastatura_telefon = [
[1, 2, 3],
[4, 5, 6],
[7, 8, 9],
[0]
]
for i in range(len(tastatura_telefon)):
    for j in range(len(tastatura_telefon[i])):
        print(f'Cifra curenta este: {tastatura_telefon[i][j]}')


