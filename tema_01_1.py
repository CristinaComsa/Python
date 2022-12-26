# Exercitiu 1
# variabila = un loc din memorie care stocheaza valori care ii sunt atribuite

# Exercitiu 2 - declara si initializeaza variabile
produse = 'gogosari' #str
pret = 2 #int
cantitate = 4.600 #float
prospetime = True #bool
print(produse)
print(pret)
print(cantitate)
print(prospetime)
print()

# Exercitiu 3 -utilizare functia type
print(type(produse))
print(type(pret))
print(type(cantitate))
print(type(prospetime))
print(f'Am mers la piata si am cumparat {produse}{type(produse)} la pretul de {pret}{type(pret)} lei, '
      f'am cumparat {cantitate}{type(cantitate)} kg '
      f'si am intrebat vanzatorul daca sunt proaspeti, el spunand : {prospetime}{type(prospetime)}! ')
print()

# Exercitiu 4 -round float
cantitate = round(cantitate)
print(cantitate)
print(type(cantitate))
print()

# Exercitiu 5 -propozitii cu variabilele / modificari de tip
print(f'Am facut o zacusca nemaipomenita din {produse}!')
print(f'Am cumparat gogosarii la pretul de {pret} lei.')
print(f'A fost necesar sa cumpar {cantitate} kg.')
print(f'Au fost cei mai proaspeti! {prospetime}')
print()
produse = bool(produse)
print(type(produse))
pret = float(pret)
print(type(pret))
cantitate = int(cantitate)
print(type(cantitate))
prospetime = str(prospetime)
print(type(prospetime))
print()

# Exercitiu 6 -citeste de la tastatura, lungimea numelui
nume = input('Introduceti numele dvs: ')
prenume = input('Introduceti prenumele dvs: ')
print(f'Numele, {nume + " " +  prenume}, are  {len(nume + prenume)} caractere.')
print()

# Exercitiu 7 -citeste de la tastatura lung/lat => aria dreptunghiului
lungime = int(input('Introduceti lungimea dreptunghiului: '))
latime = int(input('Introduceti latimea dreptunghiului: '))
aria_dreptunghiului = latime * lungime
print(f'Aria dreptunghiului este {aria_dreptunghiului}.')
print()

# Exercitiu 8 - se da textul...de cate ori apare cuv 'the'
txt = 'Coral is either the stupidest animal or the smartest rock'
print(txt.count(' the '))
print()

# Exercitiu 9 -acelasi text , cuv 'the' -de cate ori + printare
txt_1 = 'Coral is either the stupidest animal or the smartest rock'
txt_1 = txt_1.count('the')
print(f'Cuvantul "the" apare de {txt_1} ori.')
print()

# Exercitiu 10 - folosim assert sa verificam daca e format doar din numere
txt = 'Coral is either the stupidest animal or the smartest rock'
#assert txt.isdigit(), 'txt nu contine numere'
print()

# Exercitiu 1 - optional
opt_1 = input('Introduceti un string de dimensiune impara: ')
print(f'Caracterul din mijloc este {opt_1[int(len(opt_1)/2)]}')
print()

# Exercitiu 2 - optional, verific cu assert daca un string e polidrom
opt_2 = 'cojoc'
assert opt_2 == opt_2[::-1]
opt_2_1 = input('Introduceti un string polidrom: ')
assert opt_2_1 == opt_2_1[::-1], 'cuvantul nu este polidrom'
print()

# Exercitiu 3 - optional, sa se salveze 2 variabile de la tastatura
x, y = input('Introduceti un string din doua cuvinte: ').split()
print(x)
print(y)
print()

# Exercitiu 4 - optional # alabala portocala
opt_4 = input('Citeste un string de la tastatura: ')
primul_car = opt_4[0]
print(primul_car)
ultimul_car = opt_4[-1]
print(ultimul_car)
opt_4_1 = opt_4.replace(primul_car, primul_car.upper())
print(primul_car + opt_4_1 + ultimul_car)
print()

# Exercitiu 5 - optional
user = input('Introduceti userul dvs: ')
parola = input('Introduceti parola dvs: ')
parola = len(parola) * '*'
print(f'Parola pentru userul {user} este {parola} si are {len(parola)} caractere.')










